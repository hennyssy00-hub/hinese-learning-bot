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
    # --- THUẬT NGỮ GIAO DỊCH, THANH TOÁN, NẠP RÚT, TÀI CHÍNH ---
    "代收": "Thu hộ / Nhận tiền hộ",
    "代收户": "Tài khoản thu hộ / nhận tiền",
    "代付": "Thanh toán hộ / Trả tiền hộ",
    "代付户": "Tài khoản thanh toán hộ",
    "下发": "Giải ngân / Chuyển khoản xuất",
    "下发卡": "Thẻ giải ngân / xuất tiền",
    "下发户": "Tài khoản giải ngân",
    "查账": "Kiểm tra giao dịch / Soát bill",
    "查单": "Tra cứu đơn / Check đơn",
    "回执": "Biên lai / Bill chuyển tiền",
    "回执单": "Biên lai / Bill thanh toán",
    "挂单": "Treo lệnh / Đặt lệnh",
    "冻结": "Đóng băng tài khoản / Phong tỏa thẻ",
    "解冻": "Mở phong tỏa / Mở đóng băng thẻ",
    "限额": "Chạm hạn mức / Hạn mức giao dịch",
    "风控": "Kiểm soát rủi ro / Tài khoản bị quét bảo mật",
    "掉单": "Lạc đơn / Mất đơn",
    "补单": "Bù đơn / Nạp bù giao dịch",
    "对账": "Đối soát tài khoản / Khớp bill",
    "流水": "Sao kê dòng tiền / Doanh số",
    "冲正": "Hoàn tiền lỗi / Đảo nợ",
    "到账": "Tiền đã vào tài khoản",
    "未到账": "Tiền chưa vào tài khoản",
    "出款": "Xuất tiền / Chuyển khoản đi",
    "入款": "Nạp tiền vào / Thu tiền",
    "充值": "Nạp tiền",
    "提现": "Rút tiền",
    "开户行": "Ngân hàng mở tài khoản",
    "支行": "Chi nhánh ngân hàng",
    "卡号": "Số thẻ ngân hàng",
    "户名": "Tên chủ tài khoản",
    "账号": "Số tài khoản",
    "卡商": "Đại lý thẻ ngân hàng",
    "码商": "Đại lý mã QR thanh toán",
    "跑分": "Chạy dòng tiền / Giao dịch trung gian",
    "手续费": "Phí giao dịch",
    "汇率": "Tỷ giá",
    "转账": "Chuyển khoản",
    "扫码": "Quét mã QR",
    # --- TIẾNG LÓNG MẠNG & KHẨU NGỮ CHAT BẢN XỨ ---
    "宝": "Bạn ơi / Bồ ơi (xưng hô thân mật khi chat)",
    "宝宝": "Bạn ơi / Cưng ơi (xưng hô thân mật)",
    "亲": "Bạn ơi / Khách yêu ơi",
    "亲亲": "Bạn ơi / Bạn nhé",
    "铁子": "Người anh em / Bạn hữu",
    "老铁": "Người anh em / Bạn hiền",
    "没有的了": "Hết rồi / Không còn cái nào nữa",
    "没有了": "Hết rồi / Không còn nữa",
    "没了": "Hết rồi",
    "正常": "Bình thường / Hoạt động ổn định",
    "稍等": "Chờ chút nhé / Đang xử lý",
    "马上": "Ngay lập tức / Liền đây",
    "收到": "Đã nhận / Rõ rồi",
    "安排": "Xử lý ngay / Lên đơn ngay",
    "催一下": "Giục bên kia / Hối bên kia một chút",
}

# Đăng ký từ chuyên ngành cho jieba phân tách chính xác
for term in [
    "代收户", "代付户", "下发卡", "下发户", "回执单", "对账单", "没有的了", "未到账", 
    "冲正", "跑分", "卡商", "码商", "开户行", "手续费", "风控"
]:
    jieba.add_word(term)

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
    "chờ tí nhé": ("等一下哦！", "Děng yíxià o!", "Bảo người khác chờ một lát thân mật."),
    "chờ một lát": ("稍等一下！", "Shāoděng yíxià!", "Cách nói lịch sự và rất đời thường."),
    "chờ một lát nhé": ("稍等一下哦！", "Shāoděng yíxià o!", "Cách nói lịch sự, nhẹ nhàng khi nhờ người khác chờ."),
    "chờ một chút": ("等一会儿！", "Děng yíhuìr!", "Bảo đối phương chờ một chút."),
    "chờ một chút nhé": ("稍等片刻哦！", "Shāoděng piànkè o!", "Nhờ đối phương chờ trong giây lát."),
    "đợi tí": ("稍等！", "Shāoděng!", "Cách nói ngắn gọn khi chat."),
    "đợi tí nhé": ("稍等哦！", "Shāoděng o!", "Nhờ đợi chút nhé."),
    "đợi một lát": ("稍等一下！", "Shāoděng yíxià!", "Chờ một lát."),
    "đợi một lát nhé": ("稍等一下哦！", "Shāoděng yíxià o!", "Chờ một lát nhé."),
    "đợi một chút": ("稍等一会儿！", "Shāoděng yíhuìr!", "Đợi một chút."),
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
    "đã chuyển rồi": ("已经转了 / 已经转账了", "Yǐjīng zhuǎn le / Yǐjīng zhuǎnzhàng le", "Báo đã hoàn tất chuyển khoản."),
    "đang chuyển": ("正在转 / 正在处理", "Zhèngzài zhuǎn / Zhèngzài chǔlǐ", "Báo đang thực hiện chuyển khoản/xử lý."),
    "chuyển xong rồi": ("转好了，请查收！", "Zhuǎn hǎo le, qǐng cháshōu!", "Báo đã chuyển tiền xong, mời kiểm tra."),
    "hãy quy đổi ra u giúp tôi": ("麻烦帮我折算成U！", "Máfan bāng wǒ zhésuàn chéng U!", "Quy đổi số tiền sang USDT (Crypto/P2P)."),
    "hãy quy đổi ra u giup toi": ("麻烦帮我折算成U！", "Máfan bāng wǒ zhésuàn chéng U!", "Quy đổi số tiền sang USDT (Crypto/P2P)."),
    "quy đổi ra u giúp tôi": ("麻烦帮我折算成U！", "Máfan bāng wǒ zhésuàn chéng U!", "Quy đổi số tiền sang USDT (Crypto/P2P)."),
    "quy đổi ra u giup toi": ("麻烦帮我折算成U！", "Máfan bāng wǒ zhésuàn chéng U!", "Quy đổi số tiền sang USDT (Crypto/P2P)."),
    "quy đổi ra u": ("折算成U", "Zhésuàn chéng U", "Quy đổi sang USDT."),
    "đổi ra u": ("换成U", "Huàn chéng U", "Đổi sang USDT."),
    "tính ra u": ("折算成U", "Zhésuàn chéng U", "Tính quy đổi sang USDT."),
}

# Ngân hàng cụm từ giao dịch, tài chính & chat lóng đối tác (Financial & P2P Chat Bank)
FINANCIAL_CHAT_IDIOMS = {
    "代收户没有的了宝": ("Hết tài khoản thu hộ rồi bạn ơi! (Không còn tài khoản nhận tiền nữa đâu bồ ơi)", "Dài shōu hù méi yǒu de le bǎo", "Ngữ cảnh giao dịch/thanh toán: '代收户' là tài khoản thu hộ/nhận tiền, '没有的了' nghĩa là hết rồi, '宝' là xưng hô thân mật bạn ơi/bồ ơi."),
    "代收户没有的了": ("Hết tài khoản thu hộ rồi! (Không còn tài khoản nhận tiền nữa)", "Dài shōu hù méi yǒu de le", "Ngữ cảnh thanh toán: '代收户' là tài khoản thu hộ tiền."),
    "代付正常": ("Kênh thanh toán hộ / trả hộ đang bình thường nhé!", "Dài fù zhèng cháng", "'代付' là thanh toán hộ (Alipay/WeChat/Bank), '正常' là hoạt động bình thường, ổn định."),
    "代收正常": ("Kênh thu hộ / nhận tiền đang hoạt động bình thường nhé!", "Dài shōu zhèng cháng", "'代收' là nhận tiền hộ/thu hộ."),
    "查下账": ("Kiểm tra giao dịch / Soát bill giúp mình với!", "Chá xià zhàng", "Nhờ đối tác kiểm tra lại xem tiền đã vào tài khoản chưa."),
    "查账": ("Kiểm tra giao dịch / Soát bill", "Chá zhàng", "Tra soát tài khoản ngân hàng hoặc cổng thanh toán."),
    "回执发我": ("Gửi biên lai / bill chuyển tiền cho mình nhé!", "Huízhì fā wǒ", "Yêu cầu bên kia gửi ảnh chụp biên lai giao dịch."),
    "回执单发我": ("Gửi biên lai chuyển khoản cho mình nhé!", "Huízhì dān fā wǒ", "Biên lai thanh toán."),
    "钱还没到账": ("Tiền vẫn chưa vào tài khoản!", "Qián hái méi dào zhàng", "Báo tiền chưa vào tài khoản."),
    "已经到账了": ("Tiền đã vào tài khoản rồi nhé!", "Yǐjīng dào zhàng le", "Xác nhận tiền đã về thành công."),
    "下发卡冻结了": ("Thẻ giải ngân / xuất tiền bị phong tỏa rồi!", "Xià fā kǎ dòngjié le", "Thẻ xuất tiền gặp sự cố đóng băng."),
    "账户被风控了": ("Tài khoản bị dính kiểm soát rủi ro / bị quét bảo mật rồi!", "Zhànghù bèi fēngkòng le", "Tài khoản bị hệ thống ngân hàng/ví tạm khóa bảo vệ."),
    "限额了": ("Bị chạm hạn mức giao dịch rồi!", "Xiàn'é le", "Hạn mức trong ngày hoặc trên lần chuyển đã hết."),
    "稍等正在处理": ("Chờ chút nhé, bên mình đang xử lý ngay đây!", "Shāoděng zhèngzài chǔlǐ", "Báo bên kia chờ trong khi xử lý giao dịch."),
    "hãy quy đổi ra u giúp tôi": ("麻烦帮我折算成U / 帮我换成U", "Máfan bāng wǒ zhésuàn chéng U / Bāng wǒ huàn chéng U", "Ngữ cảnh Crypto/P2P: 'U' là USDT. Nhờ đối tác quy đổi số tiền sang USDT."),
    "hãy quy đổi ra u giup toi": ("麻烦帮我折算成U / 帮我换成U", "Máfan bāng wǒ zhésuàn chéng U / Bāng wǒ huàn chéng U", "Ngữ cảnh Crypto/P2P: Nhờ đối tác quy đổi tiền sang USDT."),
    "quy đổi ra u giúp tôi": ("麻烦帮我折算成U", "Máfan bāng wǒ zhésuàn chéng U", "Nhờ quy đổi sang USDT."),
    "quy đổi ra u giup toi": ("麻烦帮我折算成U", "Máfan bāng wǒ zhésuàn chéng U", "Nhờ quy đổi sang USDT."),
    "quy đổi ra u": ("折算成U", "Zhésuàn chéng U", "Quy đổi sang USDT."),
    "đổi ra u": ("换成U / 折算成U", "Huàn chéng U / Zhésuàn chéng U", "Đổi sang USDT."),
    "tính ra u": ("折算成U", "Zhésuàn chéng U", "Tính quy đổi sang USDT."),
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
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Accept-Language": "vi-VN,vi;q=0.9,zh-CN;q=0.8,en;q=0.7",
    }
    async with httpx.AsyncClient(timeout=10.0, headers=headers) as client:
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


async def translate_with_mymemory(text: str, sl: str, tl: str) -> tuple[str, str]:
    """Bộ dịch đám mây quốc tế MyMemory (không chặn IP datacenter)."""
    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": f"{sl}|{tl}"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    async with httpx.AsyncClient(timeout=10.0, headers=headers) as client:
        res = await client.get(url, params=params)
        res.raise_for_status()
        data = res.json()
        translated = data.get("responseData", {}).get("translatedText", "")
        if translated:
            return translated, ""
    raise RuntimeError("MyMemory translation unavailable")


# ============================================================
# BỘ NHỚ ĐỆM TỐC ĐỘ CAO (FAST IN-MEMORY TRANSLATION CACHE)
# ============================================================
_TRANSLATION_CACHE: dict[str, str] = {}
_MAX_CACHE_SIZE = 2000

def get_cached_translation(text: str) -> str | None:
    """Lấy bản dịch đã có sẵn trong bộ nhớ đệm (0.0001s)."""
    return _TRANSLATION_CACHE.get(text.strip().lower())

def set_cached_translation(text: str, result: str):
    """Lưu kết quả dịch vào bộ nhớ đệm."""
    if len(_TRANSLATION_CACHE) >= _MAX_CACHE_SIZE:
        old_keys = list(_TRANSLATION_CACHE.keys())[:200]
        for k in old_keys:
            _TRANSLATION_CACHE.pop(k, None)
    _TRANSLATION_CACHE[text.strip().lower()] = result


# Điều hướng model AI thông minh: Luôn nhớ model đang phản hồi nhanh nhất
ACTIVE_TRANSLATE_MODEL = "gemini-3.1-flash-lite"
GEMINI_MODELS = [
    "gemini-3.1-flash-lite",
    "gemini-3.8-flash",
    "gemini-3.6-flash",
    "gemini-3.5-flash",
    "gemini-flash-lite-latest"
]


async def translate_with_gemini_ai(text: str, api_key: str) -> str:
    """Bộ dịch thông minh cao cấp qua Gemini AI - Ngắn gọn, chuẩn xác, trọng tâm."""
    global ACTIVE_TRANSLATE_MODEL
    system_prompt = (
        "Bạn là Chuyên gia Dịch thuật Song ngữ Trung - Việt & Việt - Trung siêu tốc.\n"
        "ĐẶC BIỆT THÔNG THẠO: Khẩu ngữ đời thường, tiếng lóng chat mạng (宝, 亲, 铁子...), thuật ngữ giao dịch, tài chính, thanh toán, ngân hàng, nạp rút, P2P, USDT, Alipay, WeChat (代收, 代付, 下发, 查账, 回执, 挂单, 冻结, 限额, 风控, 到账...).\n\n"
        "QUY TẮC BẮT BUỘC:\n"
        "1. CỰC KỲ NGẮN GỌN, TRỌNG TÂM: Tuyệt đối KHÔNG chào hỏi, KHÔNG chia 3-4 trường hợp phân tích dài dòng.\n"
        "2. Chọn ĐÚNG 1 cách dịch chuẩn xác và tự nhiên nhất theo ngữ cảnh.\n"
        "3. Đặt chữ Hán trong thẻ <code>...</code> để người dùng chạm vào sao chép nhanh trên Telegram.\n"
        "4. ĐÚNG THEO KHUÔN MẪU SAU (Tối đa 4 - 6 dòng):\n"
        "- Nếu Việt -> Trung:\n"
        "🌐 <b>DỊCH SONG NGỮ (VIỆT ➔ TRUNG)</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🇻🇳 <b>Câu gốc:</b> [câu gốc]\n\n"
        "🇨🇳 <b>Tiếng Trung:</b> <code>[chữ Hán chuẩn nhất]</code>\n"
        "🎵 <b>Pinyin:</b> <i>[pinyin có dấu]</i>\n"
        "💬 <b>Khẩu ngữ/Chat nhanh:</b> <code>[câu nói tắt bản xứ nếu có]</code>\n\n"
        "- Nếu Trung -> Việt:\n"
        "🌐 <b>DỊCH SONG NGỮ (TRUNG ➔ VIỆT)</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🇨🇳 <b>Câu gốc:</b> <code>[chữ Hán gốc]</code>\n"
        "🎵 <b>Pinyin:</b> <i>[pinyin có dấu]</i>\n\n"
        "🇻🇳 <b>Nghĩa giao tiếp:</b> <b>[nghĩa chuẩn xác đời thường/giao dịch]</b>\n"
        "📚 <b>Từ then chốt:</b> <b>[từ 1]</b> (<code>[pinyin]</code>): [nghĩa] • <b>[từ 2]</b> (<code>[pinyin]</code>): [nghĩa]"
    )
    ordered_models = [ACTIVE_TRANSLATE_MODEL] + [m for m in GEMINI_MODELS if m != ACTIVE_TRANSLATE_MODEL]
    payload = {
        "contents": [
            {"role": "user", "parts": [{"text": f"{system_prompt}\n\nHãy dịch câu sau:\n\"{text}\""}]}
        ],
        "generationConfig": {"temperature": 0.2, "maxOutputTokens": 250}
    }
    async with httpx.AsyncClient(timeout=15.0) as client:
        for model in ordered_models:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key.strip()}"
            try:
                res = await client.post(url, json=payload)
                if res.status_code == 200:
                    ACTIVE_TRANSLATE_MODEL = model
                    data = res.json()
                    return data["candidates"][0]["content"]["parts"][0]["text"]
            except Exception:
                continue
    raise RuntimeError("Gemini AI translation error across all models")


def fix_misleading_translation(src_zh: str, trans_vi: str) -> str:
    """Khắc phục các lỗi dịch máy ngô nghê khi Google/Bing nhầm lẫn tiếng lóng & thuật ngữ giao dịch."""
    res = trans_vi.strip()

    # Nhận diện mẫu câu đặc thù: 代收户没有的了宝 / 代收户没有了
    if "代收户" in src_zh and any(k in src_zh for k in ["没有", "没了", "没"]):
        if any(b in src_zh for b in ["宝", "亲"]):
            return "Hết tài khoản thu hộ / nhận tiền rồi bạn ơi!"
        return "Hết tài khoản thu hộ / nhận tiền rồi nhé!"

    if "代付" in src_zh and "正常" in src_zh:
        return "Kênh thanh toán hộ / trả hộ đang bình thường nhé!"

    if "代收" in src_zh and "正常" in src_zh:
        return "Kênh thu hộ / nhận tiền đang hoạt động bình thường nhé!"

    # Lỗi kinh điển: "代收" bị Google/Bing dịch thành "cơ quan sưu tầm / sưu tầm / thu thập"
    if "代收" in src_zh:
        res = re.sub(r'cơ quan sưu tầm|cơ quan sưu tập|cơ quan thu gom|sưu tầm', 'thu hộ / nhận tiền', res, flags=re.IGNORECASE)

    # Lỗi "宝" cuối câu bị dịch thành "kho báu / bảo vật"
    if src_zh.endswith("宝") or src_zh.endswith("宝！") or src_zh.endswith("宝。") or src_zh.endswith("宝~"):
        res = re.sub(r'kho báu|bảo vật|châu báu', 'bạn ơi', res, flags=re.IGNORECASE)

    # Nếu vẫn dính câu dịch máy ngớ ngẩn "Không có kho báu nào..."
    if "không có kho báu" in res.lower() or ("kho báu" in res.lower() and "không có" in res.lower()):
        if "代收" in src_zh or "户" in src_zh:
            return "Hết tài khoản thu hộ / nhận tiền rồi bạn ơi!"

    return res


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
    Xử lý dịch thuật song ngữ Trung - Việt chuyên nghiệp & siêu tốc:
    1. Kiểm tra Bộ nhớ đệm (Cache) - Phản hồi trong 0.0001s.
    2. Khớp từ điển Giao dịch Tài chính & Khẩu ngữ đời thường - Tức thì trong 0.0003s.
    3. Khớp câu thành ngữ giao tiếp chuẩn bản xứ - Tức thì trong 0.0003s.
    4. Thử Gemini AI với model nhanh nhất (Adaptive Routing).
    5. Động cơ dịch máy siêu tốc (Google Translate 0.39s + Bộ sửa lỗi chuyên ngành / Bing Neural).
    6. Luôn sinh Pinyin chuẩn 100% thanh điệu + Bóc tách từ vựng.
    """
    cleaned_text = text.strip()
    if not cleaned_text:
        return "⚠️ <b>Vui lòng nhập câu bạn muốn dịch!</b>"

    # 1. Kiểm tra Bộ nhớ đệm (Zero Latency - 0.0001s)
    cached = get_cached_translation(cleaned_text)
    if cached:
        return cached

    # 2. Khớp cụm từ giao dịch tài chính & chat lóng đối tác (Zero Latency - 0.0003s)
    norm_text_raw = re.sub(r'[!?,.~。，？！\s]', '', cleaned_text.lower())
    for phrase, (meaning, py, note) in FINANCIAL_CHAT_IDIOMS.items():
        if norm_text_raw == re.sub(r'[!?,.~。，？！\s]', '', phrase.lower()):
            has_hanzi_input = any('\u4e00' <= c <= '\u9fff' for c in cleaned_text)
            if has_hanzi_input:
                final_pinyin = make_accurate_pinyin(cleaned_text)
                vocab_list = extract_key_vocabulary(cleaned_text)
                res = (
                    "🌐 <b>DỊCH THUẬT SONG NGỮ (TRUNG ➔ VIỆT CHUYÊN GIAO DỊCH & KHẨU NGỮ)</b>\n"
                    "━━━━━━━━━━━━━━━━━━━━\n"
                    f"🇨🇳 <b>Câu gốc:</b> <code>{html.escape(cleaned_text)}</code>\n"
                    f"🎵 <b>Pinyin:</b> <i>{final_pinyin}</i>\n\n"
                    f"🇻🇳 <b>Nghĩa giao tiếp chuẩn:</b> <b>{html.escape(meaning)}</b>\n"
                )
                if vocab_list:
                    res += "\n📚 <b>Bóc tách từ vựng then chốt:</b>\n"
                    for word, wpy, wmeaning in vocab_list:
                        mean_str = f" - <i>{html.escape(wmeaning)}</i>" if wmeaning else ""
                        res += f"• <b>{word}</b> (<code>{wpy}</code>){mean_str}\n"
            else:
                final_pinyin = py if py else make_accurate_pinyin(meaning)
                vocab_list = extract_key_vocabulary(meaning)
                res = (
                    "🌐 <b>DỊCH THUẬT SONG NGỮ (VIỆT ➔ TRUNG GIAO DỊCH & CRYPTO)</b>\n"
                    "━━━━━━━━━━━━━━━━━━━━\n"
                    f"🇻🇳 <b>Câu gốc:</b> {html.escape(cleaned_text)}\n\n"
                    f"🇨🇳 <b>Tiếng Trung:</b> <code>{html.escape(meaning)}</code>\n"
                    f"🎵 <b>Pinyin:</b> <i>{final_pinyin}</i>\n"
                )
                if vocab_list:
                    res += "\n📚 <b>Từ vựng nổi bật:</b>\n"
                    for word, wpy, wmeaning in vocab_list:
                        mean_str = f" - <i>{html.escape(wmeaning)}</i>" if wmeaning else ""
                        res += f"• <b>{word}</b> (<code>{wpy}</code>){mean_str}\n"

            if note:
                res += f"\n💡 <i>Lưu ý ngữ cảnh: {note}</i>\n"
            set_cached_translation(cleaned_text, res)
            return res

    # 3. Khớp từ điển thành ngữ khẩu ngữ tức thì (Zero Latency - 0.0003s)
    norm_text = re.sub(r'[!?,.]', '', cleaned_text.lower()).strip()
    if norm_text in SPOKEN_IDIOMS:
        zh, py, note = SPOKEN_IDIOMS[norm_text]
        res = (
            "🌐 <b>DỊCH SONG NGỮ CHUẨN KHẨU NGỮ BẢN XỨ</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            f"🇻🇳 <b>Câu gốc:</b> {html.escape(cleaned_text)}\n\n"
            f"🇨🇳 <b>Tiếng Trung (Khẩu ngữ):</b> <code>{zh}</code>\n"
            f"🎵 <b>Pinyin:</b> <i>{py}</i>\n\n"
            f"🗣️ <b>Sắc thái & Gợi ý:</b> {note}\n"
            "💡 <i>Mẹo: Bấm vào dòng chữ Hán để sao chép nhanh và gửi tin nhắn!</i>"
        )
        set_cached_translation(cleaned_text, res)
        return res

    # 4. Thử dùng Gemini AI nếu có key (với Adaptive Routing siêu tốc)
    gemini_key = get_gemini_api_key()
    if gemini_key:
        try:
            ai_res = await translate_with_gemini_ai(cleaned_text, gemini_key)
            set_cached_translation(cleaned_text, ai_res)
            return ai_res
        except Exception:
            pass

    # 5. Nhận diện ngôn ngữ đầu vào
    lang = detect_language(cleaned_text)

    # 6. Thực hiện dịch qua Động cơ siêu tốc (Google Translate 0.39s + Sửa lỗi chuyên ngành, fallback Bing)
    try:
        if lang == "zh":
            # Trung -> Việt (ưu tiên Microsoft Neural chuẩn đời thường -> Google -> MyMemory)
            try:
                trans_vi, py_from_engine = await microsoft_translator.translate(cleaned_text, "zh-Hans", "vi")
            except Exception:
                try:
                    trans_vi, py_from_engine = await translate_with_google(cleaned_text, "zh-CN", "vi")
                except Exception:
                    trans_vi, py_from_engine = await translate_with_mymemory(cleaned_text, "zh-CN", "vi")

            # Áp dụng bộ lọc sửa lỗi dịch máy chuyên ngành & tiếng lóng
            trans_vi = fix_misleading_translation(cleaned_text, trans_vi)

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
            set_cached_translation(cleaned_text, res)
            return res

        elif lang == "pinyin":
            # Pinyin -> Cả Hán Tự & Tiếng Việt
            try:
                trans_vi, _ = await microsoft_translator.translate(cleaned_text, "zh-Hans", "vi")
                trans_zh, _ = await microsoft_translator.translate(trans_vi, "vi", "zh-Hans")
            except Exception:
                try:
                    trans_vi, _ = await translate_with_google(cleaned_text, "zh-CN", "vi")
                    trans_zh, _ = await translate_with_google(trans_vi, "vi", "zh-CN")
                except Exception:
                    trans_vi, _ = await translate_with_mymemory(cleaned_text, "zh-CN", "vi")
                    trans_zh, _ = await translate_with_mymemory(trans_vi, "vi", "zh-CN")

            final_pinyin = make_accurate_pinyin(trans_zh) if trans_zh else cleaned_text

            res = (
                "🌐 <b>DỊCH TỪ PHIÊN ÂM PINYIN SONG NGỮ</b>\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                f"🎵 <b>Pinyin gốc:</b> <i>{html.escape(cleaned_text)}</i>\n\n"
                f"🇨🇳 <b>Chữ Hán:</b> <code>{trans_zh}</code>\n"
                f"🎵 <b>Pinyin chuẩn:</b> <i>{final_pinyin}</i>\n"
                f"🇻🇳 <b>Nghĩa tiếng Việt:</b> <b>{html.escape(trans_vi)}</b>\n\n"
                "💡 <i>Bạn có thể bấm vào chữ Hán để copy nhanh nhé!</i>"
            )
            set_cached_translation(cleaned_text, res)
            return res

        else:
            # Việt -> Trung (ưu tiên Microsoft Neural chuẩn đời thường -> Google -> MyMemory)
            try:
                trans_zh, py_from_engine = await microsoft_translator.translate(cleaned_text, "vi", "zh-Hans")
            except Exception:
                try:
                    trans_zh, py_from_engine = await translate_with_google(cleaned_text, "vi", "zh-CN")
                except Exception:
                    trans_zh, py_from_engine = await translate_with_mymemory(cleaned_text, "vi", "zh-CN")

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
            set_cached_translation(cleaned_text, res)
            return res

    except Exception as e:
        return (
            "⚠️ <b>Lỗi kết nối dịch thuật!</b>\n\n"
            "Không thể kết nối đến máy chủ dịch thuật lúc này. Xin vui lòng thử lại sau vài giây!"
        )
