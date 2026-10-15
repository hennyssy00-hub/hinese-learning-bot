"""
Module Dịch Thuật Song Ngữ Trung - Việt Khẩu Ngữ Đời Thường (Conversational Bilingual Translator PRO MAX)
Tối ưu hóa đặc biệt cho giao tiếp hàng ngày, văn phong nói tự nhiên, không sách vở, không từ ngữ chuyên ngành.
Đầy đủ: Chữ Hán Giản thể + Pinyin chuẩn có thanh điệu + Tiếng Việt khẩu ngữ + Phân tích từ vựng + Biến thể bản xứ.
"""

import os
import re
import html
import time
import httpx
import jieba
from pypinyin import pinyin, Style
from ai_tutor import get_gemini_api_key

# ============================================================
# NGÂN HÀNG KHẨU NGỮ ĐỜI THƯỜNG & TỪ ĐIỂN TỰ NHIÊN
# ============================================================

COMMON_VOCAB = {
    "你好": "Xin chào",
    "谢谢": "Cảm ơn",
    "不客气": "Không có gì / Đừng khách sáo",
    "对不起": "Xin lỗi",
    "没关系": "Không sao cả",
    "再见": "Tạm biệt",
    "今天": "Hôm nay",
    "明天": "Ngày mai",
    "昨天": "Hôm qua",
    "待会儿": "Lát nữa / Tí nữa",
    "一会儿": "Một lát / Lát nữa",
    "太累": "Quá mệt",
    "累死": "Mệt chết đi được",
    "奶茶": "Trà sữa",
    "喝奶茶": "Uống trà sữa",
    "吃饭": "Ăn cơm",
    "吃过": "Đã ăn",
    "上班": "Đi làm",
    "下班": "Tan làm",
    "朋友": "Bạn bè",
    "多少钱": "Bao nhiêu tiền",
    "便宜": "Rẻ",
    "太贵": "Đắt quá",
    "好吃": "Ngon (đồ ăn)",
    "好喝": "Ngon (đồ uống)",
    "漂亮": "Xinh đẹp",
    "帅哥": "Soái ca / Đẹp trai",
    "美女": "Mỹ nữ / Gái xinh",
    "喜欢": "Thích",
    "想你": "Nhớ bạn",
    "爱": "Yêu",
    "放心": "Yên tâm",
    "没事": "Không sao đâu",
    "怎么了": "Sao thế / Có chuyện gì vậy",
    "干嘛": "Làm gì đấy / Chi vậy",
    "去哪儿": "Đi đâu thế",
    "真的吗": "Thật không?",
    "算了吧": "Thôi bỏ đi",
    "无语": "Cạn lời / Bó tay",
    "厉害": "Đỉnh / Lợi hại",
    "晚安": "Chúc ngủ ngon",
    "最近": "Dạo này / Gần đây",
    "怎么样": "Thế nào / Ra sao",
    "有空": "Có rảnh",
    "没空": "Bận / Không rảnh",
    "知道": "Biết",
    "不知道": "Không biết",
    "买单": "Thanh toán / Tính tiền",
    "打包": "Gói mang về",
    "微信": "WeChat",
    "支付宝": "Alipay",
    "加油": "Cố lên!",
    "好久不见": "Lâu rồi không gặp",
    "开玩笑": "Đùa đấy / Nói đùa",
    "随便": "Tùy ý / Sao cũng được",
    "什么": "Cái gì",
    "哪里": "Ở đâu",
    "为什么": "Tại sao",
    "现在": "Bây giờ",
    "回家": "Về nhà",
    "睡觉": "Đi ngủ",
    "开心": "Vui vẻ",
    "难过": "Buồn",
    "着急": "Sốt ruột / Gấp gáp",
    "麻烦": "Phiền phức / Làm phiền",
}

# Ánh xạ câu giao tiếp cửa miệng chuẩn bản xứ (Vietnamese -> Chinese Spoken Idioms)
SPOKEN_IDIOMS = {
    "đi đâu đấy": ("去哪儿呀？", "Qù nǎr ya?", "Câu chào hỏi cửa miệng cực kỳ quen thuộc khi gặp bạn bè."),
    "đi đâu thế": ("去哪儿呢？", "Qù nǎr ne?", "Hỏi thăm nhẹ nhàng, tự nhiên."),
    "làm gì đấy": ("干嘛呢？", "Gàn má ne?", "Khẩu ngữ phổ biến số 1 của giới trẻ Trung Quốc khi chat."),
    "đang làm gì đấy": ("在干嘛呢？", "Zài gàn má ne?", "Dùng khi nhắn tin hỏi thăm xem đối phương đang làm gì."),
    "ăn cơm chưa": ("吃饭了吗？", "Chī fàn le ma?", "Lời chào hỏi văn hóa ấm áp, tương đương 'hello'."),
    "ăn gì chưa": ("吃了没？", "Chī le méi?", "Cách nói ngắn gọn, cực kỳ đời thường của người bản xứ."),
    "uống trà sữa không": ("去喝奶茶吗？", "Qù hē nǎichá ma?", "Câu rủ rê quốc dân của giới trẻ."),
    "uống trà sữa không bạn ơi": ("一起去喝奶茶吧！", "Yìqǐ qù hē nǎichá ba!", "Lời rủ bạn bè đi uống trà sữa."),
    "ngủ ngon nhé": ("晚安哦！", "Wǎn'ān o!", "Chúc ngủ ngon kèm trợ từ '哦' ngọt ngào."),
    "ngủ ngon nha": ("做个好梦！", "Zuò gè hǎo mèng!", "Chúc ngủ ngon và mơ giấc mơ đẹp."),
    "bó tay": ("算了吧，真无语！", "Suàn le ba, zhēn wúyǔ!", "Biểu đạt sự bất lực hoặc cạn lời."),
    "thôi bó tay luôn": ("彻底无语了！", "Chèdǐ wúyǔ le!", "Cạn lời hoàn toàn."),
    "đỉnh thật": ("太牛了！", "Tài niú le!", "Tiếng lóng khen ngợi siêu đỉnh của giới trẻ."),
    "quá đỉnh": ("太绝了！", "Tài jué le!", "Khen ngợi mức độ cao nhất, không gì sánh bằng."),
    "ảo thật đấy": ("太离谱了吧！", "Tài lípǔ le ba!", "Kinh ngạc trước điều gì đó quá ảo hoặc khó tin."),
    "chờ tí": ("等一下！", "Děng yíxià!", "Bảo người khác chờ một lát."),
    "đợi tí": ("稍等一下！", "Shāoděng yíxià!", "Cách nói lịch sự và rất đời thường."),
    "yên tâm đi": ("放心吧！", "Fàngxīn ba!", "Trấn an đối phương đừng lo lắng."),
    "thật không": ("真的假的？", "Zhēn de jiǎ de?", "Thật hay đùa thế? (cực kỳ tự nhiên)."),
    "không sao đâu": ("没事的，别担心！", "Méi shì de, bié dānxīn!", "An ủi đối phương đừng bận tâm."),
    "dạo này thế nào": ("最近怎么样？", "Zuìjìn zěnmeyàng?", "Hỏi thăm tình hình dạo này thế nào."),
    "nhớ bạn quá": ("太想你了！", "Tài xiǎng nǐ le!", "Bày tỏ tình cảm thân mật, gần gũi."),
    "chúc mừng sinh nhật": ("生日快乐！祝你天天开心！", "Shēngrì kuàilè! Zhù nǐ tiāntiān kāixīn!", "Lời chúc sinh nhật vui vẻ mỗi ngày."),
    "tính tiền": ("买单！/ 结账！", "Mǎidān! / Jiézhàng!", "Cách gọi thanh toán chuẩn tại nhà hàng, quán nước."),
    "gói mang về": ("打包！", "Dǎbāo!", "Nói với nhân viên khi muốn mang đồ về."),
    "bao nhiêu tiền một bát": ("多少钱一碗？", "Duōshao qián yì wǎn?", "Hỏi giá đồ ăn tính theo tô/bát."),
    "bớt chút đi": ("便宜一点吧！", "Piányi yìdiǎn ba!", "Câu mặc cả quốc dân khi đi mua sắm."),
}


# ============================================================
# CÁC BỘ DỊCH THUẬT (TRANSLATION ENGINES)
# ============================================================

class MicrosoftNeuralTranslator:
    """Bộ dịch Neural / LLM hiện đại của Microsoft Bing - Dịch thoát nghĩa, chuẩn khẩu ngữ đời thường."""

    def __init__(self):
        self.ig = None
        self.iid = None
        self.key = None
        self.token = None
        self.last_fetch = 0
        self._headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "Referer": "https://www.bing.com/translator",
        }

    async def _refresh_token(self):
        try:
            async with httpx.AsyncClient(timeout=10.0, headers=self._headers) as client:
                r = await client.get("https://www.bing.com/translator")
                ig = re.search(r'IG:"([^"]+)"', r.text)
                iid = re.search(r'data-iid="([^"]+)"', r.text)
                params_match = re.search(r'params_AbusePreventionHelper\s*=\s*\[([^\]]+)\]', r.text)
                if ig and params_match:
                    parts = [x.strip().strip('"') for x in params_match.group(1).split(",")]
                    self.ig = ig.group(1)
                    self.iid = iid.group(1) if iid else "translator.5028"
                    self.key = parts[0]
                    self.token = parts[1]
                    self.last_fetch = time.time()
                    return True
        except Exception:
            pass
        return False

    async def translate(self, text: str, from_lang: str, to_lang: str) -> tuple[str, str]:
        if not self.key or time.time() - self.last_fetch > 600:
            await self._refresh_token()
        if not self.key:
            raise RuntimeError("Microsoft Neural Translator unavailable")

        post_url = f"https://www.bing.com/ttranslatev3?isVertical=1&&IG={self.ig}&IID={self.iid}"
        form = {
            "text": text,
            "fromLang": from_lang,
            "to": to_lang,
            "key": self.key,
            "token": self.token
        }
        async with httpx.AsyncClient(timeout=12.0, headers=self._headers) as client:
            res = await client.post(post_url, data=form)
            if res.status_code != 200:
                await self._refresh_token()
                form["key"] = self.key
                form["token"] = self.token
                res = await client.post(post_url, data=form)
                res.raise_for_status()

            data = res.json()
            trans_text = data[0]["translations"][0]["text"]
            pinyin_raw = data[0]["translations"][0].get("transliteration", {}).get("text", "")
            if not pinyin_raw and len(data) > 1:
                pinyin_raw = data[1].get("inputTransliteration", "")
            return trans_text, pinyin_raw


microsoft_translator = MicrosoftNeuralTranslator()


async def translate_with_google(text: str, sl: str, tl: str) -> tuple[str, str]:
    """Bộ dịch dự phòng Google Translate Pro với định dạng chi tiết."""
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": sl,
        "tl": tl,
        "dt": ["t", "rm", "bd"],
        "dj": "1",
        "q": text
    }
    async with httpx.AsyncClient(timeout=10.0) as client:
        res = await client.get(url, params=params)
        res.raise_for_status()
        data = res.json()

    sentences = data.get("sentences", [])
    trans_parts = [s.get("trans", "") for s in sentences if "trans" in s]
    trans_text = "".join(trans_parts).strip()

    pinyin_raw = ""
    for s in sentences:
        if "translit" in s:
            pinyin_raw = s["translit"]
            break
        elif "src_translit" in s:
            pinyin_raw = s["src_translit"]
            break
    return trans_text, pinyin_raw


async def translate_with_gemini_ai(text: str, api_key: str) -> str:
    """Bộ dịch thông minh cao cấp qua Gemini AI với chỉ dẫn sư phạm khẩu ngữ."""
    system_prompt = (
        "Bạn là Chuyên gia Dịch thuật Khẩu ngữ Song ngữ Trung - Việt / Việt - Trung đỉnh cao.\n"
        "Yêu cầu tuyệt đối:\n"
        "1. Dịch chuẩn văn phong NÓI ĐỜI THƯỜNG, tự nhiên, gần gũi, người bản xứ hay dùng.\n"
        "2. Không dùng từ ngữ hàn lâm sách vở, không dịch word-by-word cứng nhắc.\n"
        "3. Nếu là Việt -> Trung: Cung cấp Câu tiếng Trung chuẩn + Pinyin có thanh điệu + Giải thích ngữ cảnh + Biến thể giới trẻ.\n"
        "4. Nếu là Trung -> Việt: Dịch nghĩa tiếng Việt đời thường + Pinyin câu gốc + Bóc tách từ vựng hay.\n"
        "5. Định dạng HTML Telegram rõ ràng, dùng emoji đẹp mắt."
    )
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    payload = {
        "contents": [
            {"role": "user", "parts": [{"text": f"{system_prompt}\n\nHãy dịch câu sau:\n\"{text}\""}]}
        ],
        "generationConfig": {"temperature": 0.4, "maxOutputTokens": 800}
    }
    async with httpx.AsyncClient(timeout=15.0) as client:
        res = await client.post(url, json=payload)
        res.raise_for_status()
        data = res.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]


# ============================================================
# CÁC TIỆN ÍCH NGÔN NGỮ (LANGUAGE UTILITIES)
# ============================================================

def make_accurate_pinyin(hanzi_text: str) -> str:
    """Tạo Pinyin chuẩn 100% có dấu thanh điệu, tự nhiên bằng pypinyin."""
    py_parts = pinyin(hanzi_text, style=Style.TONE)
    tokens = [p[0] for p in py_parts if p[0].strip()]
    raw_pinyin = " ".join(tokens)
    # Viết hoa chữ cái đầu câu cho đẹp
    if raw_pinyin:
        raw_pinyin = raw_pinyin[0].upper() + raw_pinyin[1:]
    return raw_pinyin


def extract_key_vocabulary(hanzi_text: str) -> list[tuple[str, str, str]]:
    """Phân tích các từ vựng nổi bật trong câu Hán tự."""
    words = [w for w in jieba.cut(hanzi_text) if len(w) > 1 and any('\u4e00' <= c <= '\u9fff' for c in w)]
    result = []
    seen = set()
    for w in words:
        if w in seen:
            continue
        seen.add(w)
        py = make_accurate_pinyin(w)
        meaning = COMMON_VOCAB.get(w, "")
        result.append((w, py, meaning))
    return result[:3]


VI_CHARS = set("đĐăĂâÂêÊôÔơƠưƯảẢãÃạẠẳẲẵẴặẶẩẨẫẪậẬẻẺẽẼẹẸểỂễỄệỆỉỈĩĨịỊỏỎõÕọỌổỔỗỖộỘởỞỡỠợỢủỦũŨụỤửỬữỮựỰỷỶỹỸỵỴáàéèíìóòúùýÁÀÉÈÍÌÓÒÚÙÝ")
PINYIN_EXCLUSIVE_TONES = set("āēīōūǖǎǐǒǔǚ")
VI_DISTINCTIVE_WORDS = {
    "không", "khong", "bạn", "ban", "tôi", "toi", "mình", "minh", "ơi", "oi", "cơm", "com",
    "uống", "uong", "trà", "tra", "sữa", "sua", "đi", "di", "làm", "lam", "gì", "gi",
    "ăn", "an", "chưa", "chua", "thế", "the", "sao", "nào", "nao", "quá", "qua", "nhé", "nhe",
    "nhỉ", "nhi", "nha", "đẹp", "dep", "rất", "rat", "muốn", "muon", "được", "duoc", "biết", "biet",
    "tiền", "tien", "đắt", "dat", "rẻ", "re", "ngon", "nấu", "nau", "mệt", "met", "ngủ", "ngu"
}
PINYIN_CLUES = {
    "ni", "hao", "wo", "ta", "men", "hen", "shi", "ma", "ne", "ba", "xie", "xiexie",
    "zaijian", "duibuqi", "meiguanxi", "chifan", "he", "naicha", "duoshao", "qian",
    "xiang", "ai", "pengyou", "jintian", "mingtian", "zuotian", "zenme", "shenme", "weishenme"
}


def detect_language(text: str) -> str:
    """
    Phân loại chính xác ngôn ngữ đầu vào:
    - 'zh': Chữ Hán
    - 'vi': Tiếng Việt (có dấu hoặc không dấu)
    - 'pinyin': Phiên âm Pinyin
    """
    # 1. Chứa chữ Hán
    if any('\u4e00' <= c <= '\u9fff' for c in text):
        return "zh"
    # 2. Chứa ký tự độc quyền tiếng Việt
    if any(c in VI_CHARS for c in text):
        return "vi"
    # 3. Chứa dấu thanh điệu độc quyền Pinyin (thanh 1 hoặc thanh 3)
    if any(c in PINYIN_EXCLUSIVE_TONES for c in text.lower()):
        return "pinyin"
    # 4. Kiểm tra từ vựng tiếng Việt đặc trưng
    words = [w.strip(',.!?').lower() for w in text.split()]
    if any(w in VI_DISTINCTIVE_WORDS for w in words):
        return "vi"
    # 5. Kiểm tra từ vựng pinyin điển hình
    if words and any(w in PINYIN_CLUES for w in words):
        return "pinyin"
    return "vi"


# ============================================================
# BỘ XỬ LÝ CHÍNH (MAIN TRANSLATION CONTROLLER)
# ============================================================

async def translate_text(text: str) -> str:
    """
    Xử lý dịch thuật song ngữ Trung - Việt chuyên nghiệp:
    1. Kiểm tra Gemini AI (nếu có key).
    2. Kiểm tra bộ thành ngữ/khẩu ngữ bản xứ có sẵn.
    3. Bộ dịch Microsoft Neural / LLM (chuẩn đời thường, thoát ý).
    4. Dự phòng Google Translate Pro (`dj=1`).
    5. Đính kèm Pinyin chuẩn 100% thanh điệu + Bóc tách từ vựng + Mẹo giao tiếp.
    """
    cleaned_text = text.strip()
    if not cleaned_text:
        return "⚠️ <b>Vui lòng nhập câu bạn muốn dịch!</b>"

    # 1. Thử dùng Gemini AI nếu có key
    gemini_key = get_gemini_api_key()
    if gemini_key:
        try:
            return await translate_with_gemini_ai(cleaned_text, gemini_key)
        except Exception:
            pass

    # 2. Nhận diện ngôn ngữ đầu vào
    lang = detect_language(cleaned_text)

    # 3. Kiểm tra từ điển thành ngữ khẩu ngữ tức thì (Zero-latency Instant Match)
    norm_text = re.sub(r'[!?,.]', '', cleaned_text.lower()).strip()
    if norm_text in SPOKEN_IDIOMS:
        zh, py, note = SPOKEN_IDIOMS[norm_text]
        return (
            "🌐 <b>DỊCH SONG NGỮ CHUẨN KHẨU NGỮ BẢN XỨ</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            f"🇻🇳 <b>Câu gốc:</b> {html.escape(cleaned_text)}\n\n"
            f"🇨🇳 <b>Tiếng Trung (Khẩu ngữ):</b> <code>{zh}</code>\n"
            f"🎵 <b>Pinyin:</b> <i>{py}</i>\n\n"
            f"🗣️ <b>Sắc thái & Gợi ý:</b> {note}\n"
            "💡 <i>Mẹo: Bấm vào dòng chữ Hán để sao chép nhanh và gửi tin nhắn!</i>"
        )

    # 4. Thực hiện dịch qua Động cơ Neural LLM
    try:
        if lang == "zh":
            # Trung -> Việt
            try:
                trans_vi, py_from_engine = await microsoft_translator.translate(cleaned_text, "zh-Hans", "vi")
            except Exception:
                trans_vi, py_from_engine = await translate_with_google(cleaned_text, "zh-CN", "vi")

            # Luôn sinh Pinyin chuẩn bằng pypinyin
            final_pinyin = make_accurate_pinyin(cleaned_text)
            vocab_list = extract_key_vocabulary(cleaned_text)

            res = (
                "🌐 <b>DỊCH THUẬT SONG NGỮ (TRUNG ➔ VIỆT ĐỜI THƯỜNG)</b>\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                f"🇨🇳 <b>Câu gốc:</b> <code>{html.escape(cleaned_text)}</code>\n"
                f"🎵 <b>Pinyin:</b> <i>{final_pinyin}</i>\n\n"
                f"🇻🇳 <b>Nghĩa giao tiếp:</b> <b>{html.escape(trans_vi)}</b>\n"
            )

            if vocab_list:
                res += "\n📚 <b>Bóc tách từ vựng then chốt:</b>\n"
                for word, py, meaning in vocab_list:
                    mean_str = f" - <i>{html.escape(meaning)}</i>" if meaning else ""
                    res += f"• <b>{word}</b> (<code>{py}</code>){mean_str}\n"

            res += (
                "\n💬 <i>Bản dịch theo ngữ cảnh khẩu ngữ hàng ngày, tự nhiên và thân mật!</i>"
            )
            return res

        elif lang == "pinyin":
            # Pinyin -> Cả Hán Tự & Tiếng Việt
            try:
                trans_vi, _ = await microsoft_translator.translate(cleaned_text, "zh-Hans", "vi")
                trans_zh, _ = await microsoft_translator.translate(trans_vi, "vi", "zh-Hans")
            except Exception:
                trans_vi, _ = await translate_with_google(cleaned_text, "zh-CN", "vi")
                trans_zh, _ = await translate_with_google(trans_vi, "vi", "zh-CN")

            final_pinyin = make_accurate_pinyin(trans_zh) if trans_zh else cleaned_text

            return (
                "🌐 <b>DỊCH TỪ PHIÊN ÂM PINYIN SONG NGỮ</b>\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                f"🎵 <b>Pinyin gốc:</b> <i>{html.escape(cleaned_text)}</i>\n\n"
                f"🇨🇳 <b>Chữ Hán:</b> <code>{trans_zh}</code>\n"
                f"🎵 <b>Pinyin chuẩn:</b> <i>{final_pinyin}</i>\n"
                f"🇻🇳 <b>Nghĩa tiếng Việt:</b> <b>{html.escape(trans_vi)}</b>\n\n"
                "💡 <i>Bạn có thể bấm vào chữ Hán để copy nhanh nhé!</i>"
            )

        else:
            # Việt -> Trung
            try:
                trans_zh, py_from_engine = await microsoft_translator.translate(cleaned_text, "vi", "zh-Hans")
            except Exception:
                trans_zh, py_from_engine = await translate_with_google(cleaned_text, "vi", "zh-CN")

            # Tạo Pinyin chuẩn bằng pypinyin
            final_pinyin = make_accurate_pinyin(trans_zh)
            vocab_list = extract_key_vocabulary(trans_zh)

            res = (
                "🌐 <b>DỊCH THUẬT SONG NGỮ (VIỆT ➔ TRUNG KHẨU NGỮ)</b>\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                f"🇻🇳 <b>Câu gốc:</b> {html.escape(cleaned_text)}\n\n"
                f"🇨🇳 <b>Tiếng Trung:</b> <code>{trans_zh}</code>\n"
                f"🎵 <b>Pinyin:</b> <i>{final_pinyin}</i>\n"
            )

            if vocab_list:
                res += "\n📚 <b>Từ vựng nổi bật:</b>\n"
                for word, py, meaning in vocab_list:
                    mean_str = f" - <i>{html.escape(meaning)}</i>" if meaning else ""
                    res += f"• <b>{word}</b> (<code>{py}</code>){mean_str}\n"

            res += (
                "\n🗣️ <b>Giọng điệu:</b> Khẩu ngữ giao tiếp đời thường tự nhiên như người bản xứ.\n"
                "💡 <b>Mẹo:</b> Bấm vào dòng chữ Hán để copy nhanh và gửi ngay cho bạn bè!"
            )
            return res

    except Exception as e:
        return (
            "⚠️ <b>Lỗi kết nối dịch thuật!</b>\n\n"
            "Không thể kết nối đến máy chủ dịch thuật lúc này. Xin vui lòng thử lại sau vài giây!"
        )
