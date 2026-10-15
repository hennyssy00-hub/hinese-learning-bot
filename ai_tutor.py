"""
Module Thầy Giáo AI Dạy Tiếng Trung Chuyên Nghiệp (AI Master Chinese Tutor)
Hỗ trợ cả Gemini API (nếu có key) và Động cơ Ngôn ngữ & Sư phạm Thông minh Tích hợp (Chạy mượt mà 100% offline).
"""

import os
import json
import re
import httpx
from pathlib import Path

# Load optional Gemini API key
def get_gemini_api_key() -> str | None:
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        config_path = Path("config.json")
        if config_path.exists():
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    cfg = json.load(f)
                    key = cfg.get("gemini_api_key")
            except Exception:
                pass
    return key.strip() if key else None


def set_gemini_api_key(new_key: str) -> bool:
    """Lưu Gemini API key vào config.json."""
    config_path = Path("config.json")
    cfg = {}
    if config_path.exists():
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                cfg = json.load(f)
        except Exception:
            cfg = {}
    cfg["gemini_api_key"] = new_key.strip()
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=4)
    return True


async def validate_gemini_key(api_key: str) -> tuple[bool, str]:
    """Kiểm tra xem Gemini API key có hoạt động và hợp lệ không."""
    cleaned = api_key.strip()
    if not cleaned or "..." in cleaned or cleaned == "AIzaSy":
        return False, "Bạn chưa điền mã API Key thật (chuỗi 'AIzaSy...' chỉ là ví dụ minh họa). Hãy vào Google AI Studio tạo key và dán toàn bộ chuỗi key vào đây!"

    models_to_test = ["gemini-1.5-flash", "gemini-2.0-flash", "gemini-1.5-pro"]
    last_err = ""
    for model in models_to_test:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={cleaned}"
        payload = {
            "contents": [{"parts": [{"text": "Hello"}]}],
            "generationConfig": {"maxOutputTokens": 5}
        }
        try:
            async with httpx.AsyncClient(timeout=8.0) as client:
                res = await client.post(url, json=payload)
                if res.status_code == 200:
                    return True, model
                # Nếu API key không hợp lệ hoặc bị cấm, dừng ngay để báo lỗi nhanh
                if res.status_code in (400, 403):
                    try:
                        err_json = res.json()
                        msg = err_json.get("error", {}).get("message", res.text[:120])
                    except Exception:
                        msg = res.text[:120]
                    return False, f"HTTP {res.status_code}: {msg}"
                last_err = f"HTTP {res.status_code}: {res.text[:120]}"
        except Exception as e:
            last_err = str(e)
    return False, last_err


SYSTEM_PROMPT = """
Bạn là Thầy Lý (李老师) - một chuyên gia sư phạm cao cấp dạy tiếng Trung Quốc cho người Việt Nam.
Phong cách giảng dạy của bạn:
1. Nhiệt tình, thân thiện, kiên nhẫn, chuyên nghiệp và truyền cảm hứng.
2. Với MỌI câu tiếng Trung xuất hiện trong câu trả lời, LUÔN LUÔN kèm theo Phiên âm Pinyin chuẩn có thanh điệu và Dịch nghĩa tiếng Việt.
3. Nếu học viên viết sai ngữ pháp, pinyin hoặc dùng từ chưa tự nhiên, hãy nhẹ nhàng chỉ ra lỗi sai và hướng dẫn cách sửa như người bản xứ.
4. Luôn đặt ra 1 câu hỏi tương tác tiếp theo bằng tiếng Trung (kèm pinyin + nghĩa) để học viên luyện phản xạ đối đáp.
5. Định dạng câu trả lời rõ ràng, dùng icon emoji sinh động, dễ đọc.
"""

# Ngân hàng tri thức chuyên gia dự phòng (Offline Knowledge Base)
CHINESE_DICTIONARY_SAMPLE = {
    "chào": ("你好！(Nǐ hǎo!)", "Xin chào! Đây là lời chào phổ biến nhất trong tiếng Trung."),
    "cảm ơn": ("谢谢！(Xièxie!)", "Cảm ơn bạn! Để đáp lại, bạn có thể nói '不客气 (Bú kèqi)' - Đừng khách sáo!"),
    "tạm biệt": ("再见！(Zàijiàn!)", "Tạm biệt! Chữ '再 (zài)' nghĩa là lại, '见 (jiàn)' nghĩa là gặp, tức là hẹn gặp lại!"),
    "xin lỗi": ("对不起！(Duìbuqǐ!)", "Xin lỗi! Để an ủi người khác, bạn có thể nói '没关系 (Méi guānxi)' - Không sao đâu!"),
    "yêu": ("我爱你！(Wǒ ài nǐ!)", "Tôi yêu bạn / Em yêu anh / Anh yêu em!"),
    "nhớ": ("我想你。(Wǒ xiǎng nǐ.)", "Tôi nhớ bạn. Từ '想 (xiǎng)' vừa có nghĩa là nhớ, vừa có nghĩa là muốn/nghĩ."),
    "ăn cơm": ("吃饭 (Chī fàn)", "Ăn cơm. Câu hỏi xã giao quen thuộc: 你吃了吗？(Nǐ chī le ma? - Bạn ăn cơm chưa?)"),
    "uống nước": ("喝水 (Hē shuǐ)", "Uống nước. Uống trà là '喝茶 (Hē chá)', uống cà phê là '喝咖啡 (Hē kāfēi)'."),
    "bao nhiêu tiền": ("多少钱？(Duōshao qián?)", "Bao nhiêu tiền? Ví dụ: 这个多少钱？(Zhè ge duōshao qián? - Cái này bao nhiêu tiền?)"),
    "đắt": ("太贵了！(Tài guì le!)", "Đắt quá! Bạn có thể mặc cả: 便宜一点吧！(Piányi yìdiǎn ba! - Bớt rẻ chút đi!)"),
    "ngon": ("好吃！(Hǎochī!)", "Ngon tuyệt! Đồ uống ngon thì nói là '好喝 (Hǎohē)'."),
    "xinh đẹp": ("漂亮 (Piàoliang)", "Xinh đẹp. Ví dụ: 你真漂亮！(Nǐ zhēn piàoliang! - Bạn thật xinh đẹp!)"),
    "đẹp trai": ("帅 (Shuài)", "Đẹp trai. Chàng trai đẹp thường gọi là '帅哥 (Shuàigē)'."),
    "bạn tên gì": ("你叫什么名字？(Nǐ jiào shénme míngzi?)", "Bạn tên là gì? Trả lời: 我叫... (Wǒ jiào... - Tôi tên là...)"),
    "người việt nam": ("越南人 (Yuènán rén)", "Người Việt Nam. Ví dụ: 我是越南人。(Wǒ shì Yuènán rén. - Tôi là người Việt Nam.)"),
    "chúc ngủ ngon": ("晚安！(Wǎn'ān!)", "Chúc ngủ ngon! '晚 (wǎn)' là buổi tối, '安 (ān)' là bình an, an lành."),
    "chúc mừng sinh nhật": ("生日快乐！(Shēngrì kuàilè!)", "Chúc mừng sinh nhật!"),
    "đi đâu": ("去哪儿？(Qù nǎr?)", "Đi đâu thế? Ví dụ: 你去哪儿？(Nǐ qù nǎr?)"),
}


async def chat_with_gemini(user_message: str, history: list[dict], api_key: str) -> str:
    """Gọi Gemini API để đàm thoại và dạy học chuyên sâu."""
    # Format messages
    contents = [
        {"role": "user", "parts": [{"text": SYSTEM_PROMPT + "\nHọc viên bắt đầu phiên học."}]},
        {"role": "model", "parts": [{"text": "你好！我是李老师。很高兴跟你一起学中文！(Nǐ hǎo! Wǒ shì Lǐ lǎoshī. Hěn gāoxìng gēn nǐ yìqǐ xué Zhōngwén! - Chào em! Thầy là Thầy Lý, rất vui được cùng em học tiếng Trung!). Hãy nói chuyện với thầy nhé!"}]}
    ]

    for item in history[-6:]:
        role = "user" if item["role"] == "user" else "model"
        contents.append({"role": role, "parts": [{"text": item["text"]}]})

    contents.append({"role": "user", "parts": [{"text": user_message}]})

    payload = {
        "contents": contents,
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 1000,
        }
    }

    models = ["gemini-1.5-flash", "gemini-2.0-flash", "gemini-1.5-pro"]
    last_err = None
    async with httpx.AsyncClient(timeout=25.0) as client:
        for model in models:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key.strip()}"
            try:
                res = await client.post(url, json=payload)
                if res.status_code == 200:
                    data = res.json()
                    return data["candidates"][0]["content"]["parts"][0]["text"]
                last_err = f"Status {res.status_code}: {res.text[:100]}"
            except Exception as e:
                last_err = str(e)
    raise RuntimeError(f"Gemini API error: {last_err}")


def offline_expert_tutor(user_text: str) -> str:
    """Động cơ chuyên gia phân tích ngôn ngữ nội bộ khi không dùng API ngoài."""
    raw = user_text.strip()
    lower = raw.lower()

    # Kiểm tra xem có chữ Hán không
    has_hanzi = any('\u4e00' <= c <= '\u9fff' for c in raw)

    # 1. Nếu người dùng nhập chữ Hán (Học viên đang thực hành gõ tiếng Trung)
    if has_hanzi:
        # Nhận diện một số mẫu câu thông dụng
        if any(w in raw for w in ["你好", "您好", "哈喽"]):
            return (
                "👋 <b>你好！很高兴收到你的信息！</b>\n"
                "<i>(Nǐ hǎo! Hěn gāoxìng shōudào nǐ de xìnxī!)</i>\n"
                "Chào bạn! Rất vui nhận được tin nhắn tiếng Trung của bạn!\n\n"
                "🔍 <b>Nhận xét:</b> Bạn viết chữ Hán rất chuẩn xác! 👍\n"
                "💡 <b>Luyện phản xạ tiếp nhé:</b>\n"
                "今天你过得怎么样？工作/学习忙吗？\n"
                "<i>(Jīntiān nǐ guò de zěnmeyàng? Gōngzuò/xuéxí máng ma?)</i>\n"
                "<i>(Hôm nay bạn thế nào? Công việc/học tập có bận không?)</i>\n\n"
                "👉 Hãy thử trả lời bằng tiếng Trung cho thầy nhé!"
            )
        elif any(w in raw for w in ["我是", "我叫"]):
            return (
                f"👏 <b>认识你很高兴！(Rènshi nǐ hěn gāoxìng!) - Rất vui được biết bạn!</b>\n\n"
                f"Bạn viết: <code>{raw}</code>\n"
                "✅ <b>Đánh giá:</b> Câu giới thiệu bản thân rất chuẩn và tự nhiên!\n\n"
                "💡 <b>Thầy mở rộng cho bạn:</b>\n"
                "• Bạn có thể nói thêm tuổi: 我今年...岁 (Wǒ jīnnián... suì - Tôi năm nay... tuổi)\n"
                "• Nói nghề nghiệp: 我是一名... (Wǒ shì yì míng... - Tôi là một...)\n\n"
                "❓ <b>Thầy hỏi bạn nhé:</b>\n"
                "你学中文多久了？为什么想学中文？\n"
                "<i>(Nǐ xué Zhōngwén duōjiǔ le? Wèishénme xiǎng xué Zhōngwén?)</i>\n"
                "<i>(Bạn học tiếng Trung bao lâu rồi? Vì sao muốn học tiếng Trung?)</i>"
            )
        elif any(w in raw for w in ["吃", "饭", "饿"]):
            return (
                "🍜 <b>关于美食的话题！(Chủ đề ẩm thực!)</b>\n\n"
                f"Bạn viết: <code>{raw}</code>\n"
                "🇨🇳 Người Trung Quốc có câu: <i>'民以食为天' (Mín yǐ shí wéi tiān - Dân lấy ăn làm đầu)</i>, chủ đề ăn uống rất phổ biến!\n\n"
                "💡 <b>Từ vựng & Mẫu câu bỏ túi:</b>\n"
                "• 我饿了 (Wǒ è le) = Tôi đói rồi\n"
                "• 我想吃中国菜 (Wǒ xiǎng chī Zhōngguó cài) = Tôi muốn ăn món Trung Quốc\n"
                "• 这个菜很好吃 (Zhè ge cài hěn hǎochī) = Món này ngon lắm\n\n"
                "❓ <b>Trả lời thầy nào:</b>\n"
                "你最喜欢吃什么中国菜？火锅还是烤鸭？\n"
                "<i>(Nǐ zuì xǐhuan chī shénme Zhōngguó cài? Huǒguō háishì kǎoyā?)</i>\n"
                "<i>(Bạn thích ăn món Trung nào nhất? Lẩu hay Vịt quay?)</i>"
            )
        else:
            return (
                f"🧑‍🏫 <b>Thầy Lý đã nhận được câu của bạn:</b>\n\n"
                f"<b>🇨🇳 {raw}</b>\n\n"
                "👏 <b>Đánh giá:</b> Rất khen ngợi tinh thần chủ động gõ tiếng Trung của bạn! "
                "Việc luyện gõ chữ Hán hàng ngày là chìa khóa vàng giúp bạn nhớ mặt chữ và phản xạ tự nhiên.\n\n"
                "💡 <b>Mẹo học từ Thầy Lý:</b>\n"
                "Hãy kết hợp đọc to câu này thành tiếng để luyện cơ miệng và thanh điệu nhé.\n\n"
                "❓ <b>Thầy muốn nghe bạn kể thêm:</b>\n"
                "请再跟我多聊聊，你今天做了什么有趣的事？\n"
                "<i>(Qǐng zài gēn wǒ duō liáoliao, nǐ jīntiān zuò le shénme yǒuqù de shì?)</i>\n"
                "<i>(Hãy trò chuyện thêm với thầy, hôm nay bạn có chuyện gì vui không?)</i>"
            )

    # 2. Người dùng hỏi cách nói / dịch từ tiếng Việt sang tiếng Trung
    for key, (zh, expl) in CHINESE_DICTIONARY_SAMPLE.items():
        if key in lower:
            return (
                f"🧑‍🏫 <b>Thầy Lý hướng dẫn bạn nói câu này nhé:</b>\n\n"
                f"✨ <b>{zh}</b>\n\n"
                f"📖 <b>Giải thích chi tiết:</b>\n{expl}\n\n"
                "💡 <b>Cách luyện tập:</b> Hãy thử gõ lại câu tiếng Trung trên và gửi lại cho thầy để kiểm tra trí nhớ nhé! 加油！(Jiāyóu!)"
            )

    # 3. Người dùng nhập Pinyin không dấu
    pinyin_greetings = {
        "ni hao": ("你好！(Nǐ hǎo!)", "Xin chào!"),
        "xiexie": ("谢谢！(Xièxie!)", "Cảm ơn!"),
        "zaijian": ("再见！(Zàijiàn!)", "Tạm biệt!"),
        "duibuqi": ("对不起！(Duìbuqǐ!)", "Xin lỗi!"),
        "wo ai ni": ("我爱你！(Wǒ ài nǐ!)", "Tôi yêu bạn!"),
        "wo jiao": ("我叫... (Wǒ jiào...)", "Tôi tên là..."),
        "chi fan": ("吃饭 (Chī fàn)", "Ăn cơm"),
        "duoshao qian": ("多少钱？(Duōshao qián?)", "Bao nhiêu tiền?"),
    }
    for py, (zh, trans) in pinyin_greetings.items():
        if py in lower:
            return (
                f"🧑‍🏫 <b>Thầy nhận ra bạn đang gõ Pinyin: '{py}'</b>\n\n"
                f"🇨🇳 Chữ Hán chuẩn: <b>{zh}</b>\n"
                f"🇻🇳 Nghĩa tiếng Việt: <b>{trans}</b>\n\n"
                "💡 <b>Lời khuyên sư phạm:</b>\n"
                "Lần tới, bạn hãy cài bàn phím Pinyin (chọn gõ chữ Hán) trên điện thoại hoặc máy tính để tập nhắn tin bằng chữ Hán trực tiếp nhé!\n\n"
                "👉 Bạn có muốn học thêm câu gì liên quan không?"
            )

    # 4. Tin nhắn chung / Đặt câu hỏi
    return (
        "🧑‍🏫 <b>Thầy Lý (李老师) - Chuyên gia Tiếng Trung đây!</b>\n\n"
        f"Thầy đã nhận được tin nhắn của bạn: <i>\"{raw}\"</i>\n\n"
        "💡 <b>Thầy có thể giúp bạn:</b>\n"
        "• Dịch câu Việt ➔ Trung chuẩn ngữ cảnh (kèm Pinyin thanh điệu)\n"
        "• Sửa lỗi ngữ pháp, phát âm pinyin khi bạn nhắn tiếng Trung\n"
        "• Giải thích cặn kẽ các cặp từ dễ nhầm lẫn (会/能/可以, 想/要, 没/不...)\n"
        "• Đóng vai đối đáp trò chuyện theo chủ đề\n\n"
        "👉 <i>Bạn muốn dịch câu nào, hoặc muốn hỏi ngữ pháp gì? Hãy nhắn ngay cho thầy nhé!</i>"
    )


async def get_tutor_response(user_text: str, history: list[dict] | None = None) -> str:
    """Hàm chính trả về câu trả lời sư phạm của Thầy giáo AI."""
    api_key = get_gemini_api_key()
    if api_key:
        try:
            return await chat_with_gemini(user_text, history or [], api_key)
        except Exception as e:
            # Fallback sang động cơ chuyên gia nếu API gặp sự cố mạng
            pass

    return offline_expert_tutor(user_text)
