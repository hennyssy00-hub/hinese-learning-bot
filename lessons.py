"""
Dữ liệu bài học tiếng Trung - Từ cơ bản đến HSK3
Mỗi bài học bao gồm: Chữ Hán, Pinyin, Nghĩa tiếng Việt, Ví dụ
"""

# ============================================================
# LEVEL 0: MẤT GỐC / NHẬP MÔN (Chưa biết gì)
# ============================================================

LEVEL_0_LESSONS = {
    "intro": {
        "title": "📚 Giới thiệu tiếng Trung",
        "content": (
            "🇨🇳 <b>GIỚI THIỆU VỀ TIẾNG TRUNG QUỐC</b>\n\n"
            "Tiếng Trung Quốc (中文 - Zhōngwén) là ngôn ngữ "
            "được sử dụng nhiều nhất thế giới.\n\n"
            "📌 <b>Những điều cơ bản cần biết:</b>\n\n"
            "1️⃣ <b>Chữ Hán (汉字 - Hànzì)</b>\n"
            "   Mỗi chữ là một ký tự riêng biệt, không ghép vần.\n"
            "   Ví dụ: 人 (rén) = người, 大 (dà) = to/lớn\n\n"
            "2️⃣ <b>Pinyin (拼音 - Pīnyīn)</b>\n"
            "   Hệ thống phiên âm Latin giúp đọc chữ Hán.\n"
            "   Ví dụ: nǐ hǎo = xin chào\n\n"
            "3️⃣ <b>Thanh điệu (声调 - Shēngdiào)</b>\n"
            "   Tiếng Trung có 4 thanh + 1 thanh nhẹ:\n"
            "   ā (thanh 1 - ngang)\n"
            "   á (thanh 2 - lên)\n"
            "   ǎ (thanh 3 - xuống rồi lên)\n"
            "   à (thanh 4 - xuống)\n"
            "   a (thanh nhẹ - không dấu)\n\n"
            "4️⃣ <b>Nét viết cơ bản (基本笔画 - Jīběn bǐhuà)</b>\n"
            "   横 héng (ngang) —\n"
            "   竖 shù (sổ) |\n"
            "   撇 piě (phẩy) /\n"
            "   捺 nà (mác) \\\n"
            "   点 diǎn (chấm) .\n"
            "   折 zhé (gấp) ㄥ\n"
        ),
    },
    "tones": {
        "title": "🎵 Thanh điệu tiếng Trung",
        "content": (
            "🎵 <b>BÀI HỌC VỀ THANH ĐIỆU</b>\n\n"
            "Thanh điệu RẤT QUAN TRỌNG trong tiếng Trung!\n"
            "Cùng một âm nhưng khác thanh = khác nghĩa hoàn toàn.\n\n"
            "📌 <b>4 thanh điệu chính:</b>\n\n"
            "1️⃣ <b>Thanh 1 (ˉ) - Âm cao đều</b>\n"
            "   mā (妈) = mẹ\n"
            "   Giọng cao, kéo dài đều\n\n"
            "2️⃣ <b>Thanh 2 (ˊ) - Âm lên</b>\n"
            "   má (麻) = tê, gai\n"
            "   Giọng đi từ thấp lên cao (như hỏi \"hả?\")\n\n"
            "3️⃣ <b>Thanh 3 (ˇ) - Âm xuống rồi lên</b>\n"
            "   mǎ (马) = ngựa\n"
            "   Giọng xuống thấp rồi đi lên\n\n"
            "4️⃣ <b>Thanh 4 (ˋ) - Âm xuống</b>\n"
            "   mà (骂) = chửi, mắng\n"
            "   Giọng từ cao xuống thấp (như ra lệnh)\n\n"
            "5️⃣ <b>Thanh nhẹ (không dấu)</b>\n"
            "   ma (吗) = hả? (trợ từ hỏi)\n"
            "   Đọc nhẹ, ngắn\n\n"
            "💡 <b>Mẹo nhớ:</b>\n"
            "Thanh 1: — (ngang phẳng)\n"
            "Thanh 2: / (đi lên)\n"
            "Thanh 3: ∨ (xuống rồi lên)\n"
            "Thanh 4: \\ (đi xuống)\n"
        ),
    },
    "pinyin_initials": {
        "title": "🔤 Phụ âm đầu (Shēngmǔ)",
        "content": (
            "🔤 <b>PHỤ ÂM ĐẦU - 声母 (Shēngmǔ)</b>\n\n"
            "Tiếng Trung có 23 phụ âm đầu:\n\n"
            "📌 <b>Nhóm 1 - Giống tiếng Việt:</b>\n"
            "b (bō) - như \"b\" trong \"ba\"\n"
            "p (pō) - như \"p\" bật hơi\n"
            "m (mō) - như \"m\" trong \"mẹ\"\n"
            "f (fō) - như \"ph\" trong \"phở\"\n"
            "d (dē) - như \"đ\" trong \"đi\"\n"
            "t (tē) - như \"th\" trong \"thấy\"\n"
            "n (nē) - như \"n\" trong \"nó\"\n"
            "l (lē) - như \"l\" trong \"lá\"\n\n"
            "📌 <b>Nhóm 2 - Cần luyện tập:</b>\n"
            "g (gē) - như \"g\" trong \"gà\"\n"
            "k (kē) - như \"kh\" bật hơi\n"
            "h (hē) - như \"h\" trong \"hà\"\n"
            "j (jī) - uốn lưỡi nhẹ \"ch\"\n"
            "q (qī) - bật hơi mạnh \"ch\"\n"
            "x (xī) - như \"x\" nhẹ\n\n"
            "📌 <b>Nhóm 3 - Đặc biệt:</b>\n"
            "zh (zhī) - uốn lưỡi \"tr\"\n"
            "ch (chī) - uốn lưỡi bật hơi\n"
            "sh (shī) - uốn lưỡi \"s\"\n"
            "r (rī) - uốn lưỡi \"r\"\n"
            "z (zī) - răng \"d/z\"\n"
            "c (cī) - răng bật hơi \"ts\"\n"
            "s (sī) - răng \"x\"\n"
            "y (yī) - như \"d\" nhẹ\n"
            "w (wū) - như \"v/u\"\n"
        ),
    },
    "pinyin_finals": {
        "title": "🔤 Vần (Yùnmǔ)",
        "content": (
            "🔤 <b>VẦN - 韵母 (Yùnmǔ)</b>\n\n"
            "📌 <b>6 nguyên âm đơn:</b>\n"
            "a (啊) - như \"a\" trong \"ba\"\n"
            "o (哦) - như \"o\" trong \"bo\"\n"
            "e (鹅) - như \"ơ\" trong \"bơ\"\n"
            "i (衣) - như \"i\" trong \"bi\"\n"
            "u (乌) - như \"u\" trong \"bu\"\n"
            "ü (鱼) - tròn môi, phát \"uy\"\n\n"
            "📌 <b>Vần phổ biến:</b>\n"
            "ai - như \"ai\" \n"
            "ei - như \"ây\"\n"
            "ao - như \"ao\"\n"
            "ou - như \"âu\"\n"
            "an - như \"an\"\n"
            "en - như \"ân\"\n"
            "ang - như \"ang\"\n"
            "eng - như \"âng\"\n"
            "ong - như \"ung\"\n"
            "ia - như \"ia\"\n"
            "ie - như \"iê\"\n"
            "iu - như \"iu\"\n"
            "ian - như \"iên\"\n"
            "in - như \"in\"\n"
            "iang - như \"iang\"\n"
            "ing - như \"inh\"\n"
            "ua - như \"oa\"\n"
            "uo - như \"uô\"\n"
            "ui - như \"uây\"\n"
            "uan - như \"oan\"\n"
            "un - như \"uân\"\n"
            "uang - như \"oang\"\n"
        ),
    },
    "numbers": {
        "title": "🔢 Số đếm 1-100",
        "content": (
            "🔢 <b>SỐ ĐẾM - 数字 (Shùzì)</b>\n\n"
            "📌 <b>Số 0-10:</b>\n"
            "0 - 零 (líng) - không\n"
            "1 - 一 (yī) - một\n"
            "2 - 二 (èr) - hai\n"
            "3 - 三 (sān) - ba\n"
            "4 - 四 (sì) - bốn\n"
            "5 - 五 (wǔ) - năm\n"
            "6 - 六 (liù) - sáu\n"
            "7 - 七 (qī) - bảy\n"
            "8 - 八 (bā) - tám\n"
            "9 - 九 (jiǔ) - chín\n"
            "10 - 十 (shí) - mười\n\n"
            "📌 <b>Quy tắc ghép số:</b>\n"
            "11 = 十一 (shí yī) = mười một\n"
            "12 = 十二 (shí èr) = mười hai\n"
            "20 = 二十 (èr shí) = hai mươi\n"
            "21 = 二十一 (èr shí yī) = hai mươi mốt\n"
            "99 = 九十九 (jiǔ shí jiǔ) = chín mươi chín\n"
            "100 = 一百 (yì bǎi) = một trăm\n\n"
            "📌 <b>Lưu ý đặc biệt:</b>\n"
            "• 两 (liǎng) dùng khi đếm đồ vật thay cho 二\n"
            "  Ví dụ: 两个人 (liǎng gè rén) = hai người\n"
            "• 二 (èr) dùng trong số thứ tự, toán học\n"
        ),
    },
    "greetings": {
        "title": "👋 Chào hỏi cơ bản",
        "content": (
            "👋 <b>CHÀO HỎI CƠ BẢN - 问候 (Wènhòu)</b>\n\n"
            "📌 <b>Các câu chào thông dụng:</b>\n\n"
            "你好！(Nǐ hǎo!) = Xin chào!\n"
            "您好！(Nín hǎo!) = Xin chào! (lịch sự)\n"
            "你好吗？(Nǐ hǎo ma?) = Bạn khỏe không?\n"
            "我很好。(Wǒ hěn hǎo.) = Tôi rất khỏe.\n"
            "谢谢！(Xièxie!) = Cảm ơn!\n"
            "不客气。(Bú kèqi.) = Không có gì.\n"
            "对不起。(Duìbuqǐ.) = Xin lỗi.\n"
            "没关系。(Méi guānxi.) = Không sao.\n"
            "再见！(Zàijiàn!) = Tạm biệt!\n"
            "早上好！(Zǎoshang hǎo!) = Chào buổi sáng!\n"
            "晚上好！(Wǎnshang hǎo!) = Chào buổi tối!\n"
            "晚安！(Wǎn'ān!) = Chúc ngủ ngon!\n\n"
            "📌 <b>Hội thoại mẫu:</b>\n\n"
            "A: 你好！(Nǐ hǎo!) - Xin chào!\n"
            "B: 你好！你好吗？(Nǐ hǎo! Nǐ hǎo ma?) - Chào! Bạn khỏe không?\n"
            "A: 我很好，谢谢！你呢？\n"
            "   (Wǒ hěn hǎo, xièxie! Nǐ ne?)\n"
            "   Tôi rất khỏe, cảm ơn! Còn bạn?\n"
            "B: 我也很好。(Wǒ yě hěn hǎo.) - Tôi cũng rất khỏe.\n"
        ),
    },
    "self_intro": {
        "title": "🙋 Tự giới thiệu bản thân",
        "content": (
            "🙋 <b>TỰ GIỚI THIỆU - 自我介绍 (Zìwǒ jièshào)</b>\n\n"
            "📌 <b>Từ vựng cần biết:</b>\n"
            "我 (wǒ) = tôi\n"
            "你 (nǐ) = bạn\n"
            "他/她 (tā) = anh ấy / cô ấy\n"
            "叫 (jiào) = gọi là, tên là\n"
            "是 (shì) = là\n"
            "名字 (míngzi) = tên\n"
            "国 (guó) = nước\n"
            "人 (rén) = người\n"
            "越南 (Yuènán) = Việt Nam\n"
            "越南人 (Yuènán rén) = người Việt Nam\n\n"
            "📌 <b>Mẫu câu giới thiệu:</b>\n\n"
            "我叫___。(Wǒ jiào ___.) = Tôi tên là ___.\n"
            "我是越南人。(Wǒ shì Yuènán rén.) = Tôi là người Việt Nam.\n"
            "我是学生。(Wǒ shì xuéshēng.) = Tôi là học sinh/sinh viên.\n"
            "我今年___岁。(Wǒ jīnnián ___ suì.) = Năm nay tôi ___ tuổi.\n"
            "认识你很高兴。(Rènshi nǐ hěn gāoxìng.)\n"
            "   = Rất vui được quen biết bạn.\n\n"
            "📌 <b>Hội thoại mẫu:</b>\n\n"
            "A: 你好！你叫什么名字？\n"
            "   (Nǐ hǎo! Nǐ jiào shénme míngzi?)\n"
            "   Chào! Bạn tên gì?\n\n"
            "B: 我叫小明。你呢？\n"
            "   (Wǒ jiào Xiǎo Míng. Nǐ ne?)\n"
            "   Tôi tên Tiểu Minh. Còn bạn?\n\n"
            "A: 我叫安娜。我是越南人。你是哪国人？\n"
            "   (Wǒ jiào Ānnà. Wǒ shì Yuènán rén. Nǐ shì nǎ guó rén?)\n"
            "   Tôi tên Anna. Tôi là người Việt Nam. Bạn là người nước nào?\n\n"
            "B: 我是中国人。认识你很高兴！\n"
            "   (Wǒ shì Zhōngguó rén. Rènshi nǐ hěn gāoxìng!)\n"
            "   Tôi là người Trung Quốc. Rất vui được quen biết bạn!\n"
        ),
    },
}

# ============================================================
# LEVEL 1: HSK1 (150 từ vựng)
# ============================================================

LEVEL_1_LESSONS = {
    "vocab_family": {
        "title": "👨‍👩‍👧 Gia đình - 家庭",
        "content": (
            "👨‍👩‍👧 <b>GIA ĐÌNH - 家庭 (Jiātíng)</b>\n\n"
            "📌 <b>Từ vựng:</b>\n"
            "爸爸 (bàba) = bố, ba\n"
            "妈妈 (māma) = mẹ, má\n"
            "哥哥 (gēge) = anh trai\n"
            "姐姐 (jiějie) = chị gái\n"
            "弟弟 (dìdi) = em trai\n"
            "妹妹 (mèimei) = em gái\n"
            "儿子 (érzi) = con trai\n"
            "女儿 (nǚ'ér) = con gái\n"
            "丈夫 (zhàngfu) = chồng\n"
            "妻子 (qīzi) = vợ\n"
            "家 (jiā) = nhà, gia đình\n\n"
            "📌 <b>Mẫu câu:</b>\n"
            "我家有五口人。(Wǒ jiā yǒu wǔ kǒu rén.)\n"
            "= Gia đình tôi có năm người.\n\n"
            "我有一个哥哥和一个妹妹。\n"
            "(Wǒ yǒu yí gè gēge hé yí gè mèimei.)\n"
            "= Tôi có một anh trai và một em gái.\n\n"
            "我爸爸是老师。(Wǒ bàba shì lǎoshī.)\n"
            "= Bố tôi là giáo viên.\n\n"
            "📌 <b>Hội thoại:</b>\n"
            "A: 你家有几口人？(Nǐ jiā yǒu jǐ kǒu rén?)\n"
            "   Gia đình bạn có mấy người?\n"
            "B: 我家有四口人，爸爸、妈妈、哥哥和我。\n"
            "   (Wǒ jiā yǒu sì kǒu rén, bàba, māma, gēge hé wǒ.)\n"
            "   Nhà tôi có bốn người: bố, mẹ, anh trai và tôi.\n"
        ),
    },
    "vocab_time": {
        "title": "🕐 Thời gian - 时间",
        "content": (
            "🕐 <b>THỜI GIAN - 时间 (Shíjiān)</b>\n\n"
            "📌 <b>Từ vựng:</b>\n"
            "今天 (jīntiān) = hôm nay\n"
            "明天 (míngtiān) = ngày mai\n"
            "昨天 (zuótiān) = hôm qua\n"
            "现在 (xiànzài) = bây giờ\n"
            "上午 (shàngwǔ) = buổi sáng\n"
            "下午 (xiàwǔ) = buổi chiều\n"
            "晚上 (wǎnshang) = buổi tối\n"
            "年 (nián) = năm\n"
            "月 (yuè) = tháng\n"
            "日/号 (rì/hào) = ngày\n"
            "星期 (xīngqī) = tuần\n"
            "点 (diǎn) = giờ (đồng hồ)\n"
            "分 (fēn) = phút\n"
            "半 (bàn) = nửa, rưỡi\n\n"
            "📌 <b>Các ngày trong tuần:</b>\n"
            "星期一 (xīngqī yī) = Thứ Hai\n"
            "星期二 (xīngqī èr) = Thứ Ba\n"
            "星期三 (xīngqī sān) = Thứ Tư\n"
            "星期四 (xīngqī sì) = Thứ Năm\n"
            "星期五 (xīngqī wǔ) = Thứ Sáu\n"
            "星期六 (xīngqī liù) = Thứ Bảy\n"
            "星期日/天 (xīngqī rì/tiān) = Chủ Nhật\n\n"
            "📌 <b>Hỏi giờ:</b>\n"
            "现在几点？(Xiànzài jǐ diǎn?) = Bây giờ mấy giờ?\n"
            "现在三点半。(Xiànzài sān diǎn bàn.) = Bây giờ 3 giờ rưỡi.\n"
            "现在十点十五分。(Xiànzài shí diǎn shíwǔ fēn.) = Bây giờ 10:15.\n"
        ),
    },
    "vocab_food": {
        "title": "🍜 Đồ ăn & Uống - 饮食",
        "content": (
            "🍜 <b>ĐỒ ĂN & UỐNG - 饮食 (Yǐnshí)</b>\n\n"
            "📌 <b>Đồ ăn:</b>\n"
            "米饭 (mǐfàn) = cơm\n"
            "面条 (miàntiáo) = mì, phở\n"
            "菜 (cài) = rau, món ăn\n"
            "肉 (ròu) = thịt\n"
            "鱼 (yú) = cá\n"
            "鸡蛋 (jīdàn) = trứng gà\n"
            "水果 (shuǐguǒ) = trái cây\n"
            "苹果 (píngguǒ) = quả táo\n\n"
            "📌 <b>Đồ uống:</b>\n"
            "水 (shuǐ) = nước\n"
            "茶 (chá) = trà\n"
            "咖啡 (kāfēi) = cà phê\n"
            "牛奶 (niúnǎi) = sữa bò\n"
            "啤酒 (píjiǔ) = bia\n\n"
            "📌 <b>Mẫu câu gọi món:</b>\n"
            "我要一碗米饭。(Wǒ yào yì wǎn mǐfàn.)\n"
            "= Tôi muốn một bát cơm.\n\n"
            "请给我一杯咖啡。(Qǐng gěi wǒ yì bēi kāfēi.)\n"
            "= Cho tôi một ly cà phê.\n\n"
            "你想吃什么？(Nǐ xiǎng chī shénme?)\n"
            "= Bạn muốn ăn gì?\n\n"
            "我想喝茶。(Wǒ xiǎng hē chá.)\n"
            "= Tôi muốn uống trà.\n\n"
            "多少钱？(Duōshao qián?) = Bao nhiêu tiền?\n"
        ),
    },
    "grammar_shi": {
        "title": "📝 Ngữ pháp: 是 (shì) - là",
        "content": (
            "📝 <b>NGỮ PHÁP: CÂU VỚI 是 (shì)</b>\n\n"
            "是 (shì) = \"là\" - Dùng để giới thiệu, xác nhận.\n\n"
            "📌 <b>Cấu trúc:</b>\n"
            "A + 是 + B (A là B)\n\n"
            "📌 <b>Khẳng định:</b>\n"
            "我是学生。(Wǒ shì xuéshēng.) = Tôi là sinh viên.\n"
            "他是老师。(Tā shì lǎoshī.) = Anh ấy là giáo viên.\n"
            "这是我的书。(Zhè shì wǒ de shū.) = Đây là sách của tôi.\n\n"
            "📌 <b>Phủ định: 不是 (bú shì) = không phải là</b>\n"
            "我不是中国人。(Wǒ bú shì Zhōngguó rén.)\n"
            "= Tôi không phải là người Trung Quốc.\n"
            "她不是医生。(Tā bú shì yīshēng.)\n"
            "= Cô ấy không phải là bác sĩ.\n\n"
            "📌 <b>Nghi vấn (đặt câu hỏi):</b>\n"
            "你是学生吗？(Nǐ shì xuéshēng ma?)\n"
            "= Bạn là sinh viên phải không?\n"
            "他是不是老师？(Tā shì bu shì lǎoshī?)\n"
            "= Anh ấy có phải là giáo viên không?\n\n"
            "⚠️ <b>Lưu ý:</b> KHÔNG dùng 是 với tính từ!\n"
            "❌ 我是高兴 (Sai!)\n"
            "✅ 我很高兴 (Wǒ hěn gāoxìng.) = Tôi rất vui.\n"
        ),
    },
    "grammar_you": {
        "title": "📝 Ngữ pháp: 有 (yǒu) - có",
        "content": (
            "📝 <b>NGỮ PHÁP: CÂU VỚI 有 (yǒu)</b>\n\n"
            "有 (yǒu) = \"có\" - Diễn tả sở hữu hoặc tồn tại.\n\n"
            "📌 <b>Cấu trúc sở hữu:</b>\n"
            "A + 有 + B (A có B)\n\n"
            "我有一本书。(Wǒ yǒu yì běn shū.) = Tôi có một quyển sách.\n"
            "他有两个孩子。(Tā yǒu liǎng gè háizi.) = Anh ấy có hai đứa con.\n"
            "你有手机吗？(Nǐ yǒu shǒujī ma?) = Bạn có điện thoại không?\n\n"
            "📌 <b>Phủ định: 没有 (méi yǒu) = không có</b>\n"
            "我没有钱。(Wǒ méi yǒu qián.) = Tôi không có tiền.\n"
            "他没有女朋友。(Tā méi yǒu nǚ péngyou.) = Anh ấy không có bạn gái.\n\n"
            "📌 <b>Cấu trúc tồn tại:</b>\n"
            "Nơi chốn + 有 + Sự vật\n\n"
            "桌子上有一本书。(Zhuōzi shàng yǒu yì běn shū.)\n"
            "= Trên bàn có một quyển sách.\n"
            "教室里有很多学生。(Jiàoshì lǐ yǒu hěn duō xuéshēng.)\n"
            "= Trong lớp có rất nhiều sinh viên.\n\n"
            "⚠️ <b>Lưu ý:</b>\n"
            "• Phủ định dùng 没有 (KHÔNG dùng 不有)\n"
            "• 有 thường đi với lượng từ: 个、本、杯...\n"
        ),
    },
    "grammar_questions": {
        "title": "📝 Cách đặt câu hỏi",
        "content": (
            "📝 <b>CÁCH ĐẶT CÂU HỎI - 提问 (Tíwèn)</b>\n\n"
            "📌 <b>Cách 1: Thêm 吗 (ma) cuối câu</b>\n"
            "Câu khẳng định + 吗?\n"
            "你是学生吗？(Nǐ shì xuéshēng ma?) = Bạn là SV không?\n"
            "你吃饭了吗？(Nǐ chīfàn le ma?) = Bạn ăn cơm chưa?\n\n"
            "📌 <b>Cách 2: Dùng từ để hỏi</b>\n"
            "什么 (shénme) = cái gì?\n"
            "   你叫什么名字？= Bạn tên gì?\n"
            "谁 (shéi) = ai?\n"
            "   他是谁？= Anh ấy là ai?\n"
            "哪 (nǎ) = nào?\n"
            "   你是哪国人？= Bạn là người nước nào?\n"
            "哪儿/哪里 (nǎr/nǎlǐ) = ở đâu?\n"
            "   你住在哪儿？= Bạn sống ở đâu?\n"
            "几 (jǐ) = mấy? (số nhỏ)\n"
            "   你家有几口人？= Nhà bạn có mấy người?\n"
            "多少 (duōshao) = bao nhiêu?\n"
            "   这个多少钱？= Cái này bao nhiêu tiền?\n"
            "怎么 (zěnme) = thế nào? / làm sao?\n"
            "   这个字怎么读？= Chữ này đọc thế nào?\n"
            "为什么 (wèi shénme) = tại sao?\n"
            "   你为什么学中文？= Bạn tại sao học tiếng Trung?\n\n"
            "📌 <b>Cách 3: A 不 A (khẳng-phủ)</b>\n"
            "你去不去？= Bạn đi không đi? → Bạn có đi không?\n"
            "好不好？= Tốt không? → Được không?\n"
        ),
    },
    "conversation_shopping": {
        "title": "🛒 Giao tiếp: Mua sắm",
        "content": (
            "🛒 <b>GIAO TIẾP MUA SẮM - 购物 (Gòuwù)</b>\n\n"
            "📌 <b>Từ vựng:</b>\n"
            "买 (mǎi) = mua\n"
            "卖 (mài) = bán\n"
            "钱 (qián) = tiền\n"
            "块 (kuài) = đồng (đơn vị tiền)\n"
            "贵 (guì) = đắt\n"
            "便宜 (piányi) = rẻ\n"
            "大 (dà) = to, lớn\n"
            "小 (xiǎo) = nhỏ, bé\n"
            "多 (duō) = nhiều\n"
            "少 (shǎo) = ít\n\n"
            "📌 <b>Hội thoại mẫu:</b>\n\n"
            "🙋 Khách: 你好，这个多少钱？\n"
            "   (Nǐ hǎo, zhège duōshao qián?)\n"
            "   Xin chào, cái này bao nhiêu tiền?\n\n"
            "🧑‍💼 Bán hàng: 这个五十块。\n"
            "   (Zhège wǔshí kuài.)\n"
            "   Cái này năm mươi đồng.\n\n"
            "🙋 Khách: 太贵了！便宜一点儿可以吗？\n"
            "   (Tài guì le! Piányi yìdiǎnr kěyǐ ma?)\n"
            "   Đắt quá! Rẻ hơn một chút được không?\n\n"
            "🧑‍💼 Bán hàng: 四十块吧。\n"
            "   (Sìshí kuài ba.)\n"
            "   Bốn mươi đồng nhé.\n\n"
            "🙋 Khách: 好的，我要这个。\n"
            "   (Hǎo de, wǒ yào zhège.)\n"
            "   Được, tôi lấy cái này.\n"
        ),
    },
    "writing_basic": {
        "title": "✍️ Tập viết chữ Hán cơ bản",
        "content": (
            "✍️ <b>TẬP VIẾT CHỮ HÁN CƠ BẢN</b>\n\n"
            "📌 <b>Quy tắc viết chữ Hán:</b>\n"
            "1. Trên trước, dưới sau (先上后下)\n"
            "2. Trái trước, phải sau (先左后右)\n"
            "3. Ngang trước, sổ sau (先横后竖)\n"
            "4. Phẩy trước, mác sau (先撇后捺)\n"
            "5. Ngoài trước, trong sau (先外后内)\n"
            "6. Đóng khung sau cùng (先进后关)\n"
            "7. Giữa trước, hai bên sau (先中后两边)\n\n"
            "📌 <b>10 chữ Hán đầu tiên cần học:</b>\n\n"
            "一 (yī) = một [1 nét ngang]\n"
            "二 (èr) = hai [2 nét ngang]\n"
            "三 (sān) = ba [3 nét ngang]\n"
            "人 (rén) = người [2 nét: phẩy + mác]\n"
            "大 (dà) = to, lớn [3 nét]\n"
            "小 (xiǎo) = nhỏ, bé [3 nét]\n"
            "口 (kǒu) = miệng [3 nét]\n"
            "日 (rì) = mặt trời, ngày [4 nét]\n"
            "月 (yuè) = mặt trăng, tháng [4 nét]\n"
            "水 (shuǐ) = nước [4 nét]\n\n"
            "💡 <b>Mẹo nhớ chữ Hán:</b>\n"
            "• 人 (rén) = giống người đang bước đi\n"
            "• 大 (dà) = người dang rộng tay = to lớn\n"
            "• 口 (kǒu) = hình cái miệng mở ra\n"
            "• 日 (rì) = hình mặt trời tròn\n"
            "• 月 (yuè) = hình trăng lưỡi liềm\n"
        ),
    },
}

# ============================================================
# LEVEL 2: HSK2 (300 từ vựng)
# ============================================================

LEVEL_2_LESSONS = {
    "vocab_transport": {
        "title": "🚌 Phương tiện giao thông",
        "content": (
            "🚌 <b>PHƯƠNG TIỆN GIAO THÔNG - 交通 (Jiāotōng)</b>\n\n"
            "📌 <b>Từ vựng:</b>\n"
            "公共汽车 (gōnggòng qìchē) = xe buýt\n"
            "出租车 (chūzū chē) = xe taxi\n"
            "地铁 (dìtiě) = tàu điện ngầm\n"
            "飞机 (fēijī) = máy bay\n"
            "火车 (huǒchē) = tàu hỏa\n"
            "自行车 (zìxíngchē) = xe đạp\n"
            "船 (chuán) = thuyền, tàu\n"
            "走路 (zǒulù) = đi bộ\n"
            "开车 (kāichē) = lái xe\n"
            "路 (lù) = đường\n"
            "站 (zhàn) = trạm, ga\n\n"
            "📌 <b>Mẫu câu:</b>\n"
            "你怎么去上班？(Nǐ zěnme qù shàngbān?)\n"
            "= Bạn đi làm bằng gì?\n\n"
            "我坐地铁去上班。(Wǒ zuò dìtiě qù shàngbān.)\n"
            "= Tôi đi tàu điện ngầm đi làm.\n\n"
            "从这儿到机场要多长时间？\n"
            "(Cóng zhèr dào jīchǎng yào duō cháng shíjiān?)\n"
            "= Từ đây đến sân bay mất bao lâu?\n\n"
            "大概一个小时。(Dàgài yí gè xiǎoshí.)\n"
            "= Khoảng một tiếng.\n"
        ),
    },
    "vocab_weather": {
        "title": "🌤 Thời tiết - 天气",
        "content": (
            "🌤 <b>THỜI TIẾT - 天气 (Tiānqì)</b>\n\n"
            "📌 <b>Từ vựng:</b>\n"
            "天气 (tiānqì) = thời tiết\n"
            "热 (rè) = nóng\n"
            "冷 (lěng) = lạnh\n"
            "晴天 (qíngtiān) = trời nắng\n"
            "阴天 (yīntiān) = trời âm u\n"
            "下雨 (xià yǔ) = mưa\n"
            "下雪 (xià xuě) = tuyết rơi\n"
            "风 (fēng) = gió\n"
            "云 (yún) = mây\n"
            "暖和 (nuǎnhuo) = ấm áp\n"
            "凉快 (liángkuai) = mát mẻ\n\n"
            "📌 <b>Mẫu câu:</b>\n"
            "今天天气怎么样？(Jīntiān tiānqì zěnmeyàng?)\n"
            "= Hôm nay thời tiết thế nào?\n\n"
            "今天很热。(Jīntiān hěn rè.) = Hôm nay rất nóng.\n"
            "明天会下雨。(Míngtiān huì xià yǔ.) = Ngày mai sẽ mưa.\n"
            "越南的天气很热。(Yuènán de tiānqì hěn rè.)\n"
            "= Thời tiết Việt Nam rất nóng.\n\n"
            "📌 <b>Hội thoại:</b>\n"
            "A: 明天天气怎么样？\n"
            "   (Míngtiān tiānqì zěnmeyàng?)\n"
            "B: 明天会下雨，你带伞吧。\n"
            "   (Míngtiān huì xià yǔ, nǐ dài sǎn ba.)\n"
            "   Ngày mai sẽ mưa, bạn mang dù đi nhé.\n"
        ),
    },
    "vocab_body_health": {
        "title": "🏥 Sức khỏe & Cơ thể",
        "content": (
            "🏥 <b>SỨC KHỎE & CƠ THỂ - 健康 (Jiànkāng)</b>\n\n"
            "📌 <b>Bộ phận cơ thể:</b>\n"
            "头 (tóu) = đầu\n"
            "眼睛 (yǎnjing) = mắt\n"
            "耳朵 (ěrduo) = tai\n"
            "鼻子 (bízi) = mũi\n"
            "嘴 (zuǐ) = miệng\n"
            "手 (shǒu) = tay\n"
            "脚 (jiǎo) = chân\n"
            "肚子 (dùzi) = bụng\n\n"
            "📌 <b>Từ vựng sức khỏe:</b>\n"
            "病 (bìng) = bệnh\n"
            "疼 (téng) = đau\n"
            "发烧 (fāshāo) = sốt\n"
            "感冒 (gǎnmào) = cảm lạnh\n"
            "药 (yào) = thuốc\n"
            "医院 (yīyuàn) = bệnh viện\n"
            "医生 (yīshēng) = bác sĩ\n\n"
            "📌 <b>Hội thoại ở bệnh viện:</b>\n"
            "🧑‍⚕️ 医生: 你哪儿不舒服？\n"
            "   (Nǐ nǎr bù shūfu?)\n"
            "   Bạn thấy không khỏe ở đâu?\n\n"
            "😷 Bệnh nhân: 我头疼，还有点儿发烧。\n"
            "   (Wǒ tóu téng, hái yǒudiǎnr fāshāo.)\n"
            "   Tôi đau đầu, còn hơi sốt.\n\n"
            "🧑‍⚕️ 医生: 你感冒了，吃点儿药就好了。\n"
            "   (Nǐ gǎnmào le, chī diǎnr yào jiù hǎo le.)\n"
            "   Bạn bị cảm, uống thuốc là khỏi.\n"
        ),
    },
    "grammar_le": {
        "title": "📝 Ngữ pháp: 了 (le) - Quá khứ",
        "content": (
            "📝 <b>NGỮ PHÁP: TRỢ TỪ 了 (le)</b>\n\n"
            "了 (le) dùng để chỉ hành động đã hoàn thành hoặc\n"
            "sự thay đổi trạng thái.\n\n"
            "📌 <b>Cách 1: Hành động đã xong (V + 了)</b>\n"
            "我吃了早饭。(Wǒ chī le zǎofàn.)\n"
            "= Tôi đã ăn sáng rồi.\n\n"
            "他去了北京。(Tā qù le Běijīng.)\n"
            "= Anh ấy đã đi Bắc Kinh.\n\n"
            "我买了一件衣服。(Wǒ mǎi le yí jiàn yīfu.)\n"
            "= Tôi đã mua một bộ quần áo.\n\n"
            "📌 <b>Cách 2: Thay đổi trạng thái (cuối câu)</b>\n"
            "下雨了。(Xià yǔ le.) = Trời mưa rồi.\n"
            "我饿了。(Wǒ è le.) = Tôi đói rồi.\n"
            "春天来了。(Chūntiān lái le.) = Mùa xuân đến rồi.\n\n"
            "📌 <b>Phủ định: 没(有) + V (BỎ 了)</b>\n"
            "我没吃早饭。(Wǒ méi chī zǎofàn.)\n"
            "= Tôi chưa ăn sáng.\n"
            "他没去北京。(Tā méi qù Běijīng.)\n"
            "= Anh ấy chưa đi Bắc Kinh.\n\n"
            "⚠️ <b>Lưu ý quan trọng:</b>\n"
            "• Phủ định dùng 没 + V (KHÔNG có 了)\n"
            "• 不 + V = không muốn/sẽ không\n"
            "• 没 + V = chưa (quá khứ)\n"
        ),
    },
    "grammar_comparison": {
        "title": "📝 Ngữ pháp: So sánh",
        "content": (
            "📝 <b>NGỮ PHÁP SO SÁNH - 比较 (Bǐjiào)</b>\n\n"
            "📌 <b>1. So sánh hơn: A 比 B + Adj</b>\n"
            "比 (bǐ) = hơn, so với\n\n"
            "他比我高。(Tā bǐ wǒ gāo.) = Anh ấy cao hơn tôi.\n"
            "今天比昨天热。(Jīntiān bǐ zuótiān rè.)\n"
            "= Hôm nay nóng hơn hôm qua.\n"
            "苹果比香蕉贵。(Píngguǒ bǐ xiāngjiāo guì.)\n"
            "= Táo đắt hơn chuối.\n\n"
            "📌 <b>2. So sánh bằng: A 跟 B 一样 + Adj</b>\n"
            "跟...一样 (gēn...yíyàng) = giống như, bằng\n\n"
            "他跟我一样高。(Tā gēn wǒ yíyàng gāo.)\n"
            "= Anh ấy cao bằng tôi.\n"
            "这个跟那个一样贵。(Zhège gēn nàge yíyàng guì.)\n"
            "= Cái này đắt bằng cái kia.\n\n"
            "📌 <b>3. So sánh nhất: 最 + Adj</b>\n"
            "最 (zuì) = nhất\n\n"
            "他最高。(Tā zuì gāo.) = Anh ấy cao nhất.\n"
            "这个最便宜。(Zhège zuì piányi.) = Cái này rẻ nhất.\n"
            "我最喜欢吃米饭。(Wǒ zuì xǐhuan chī mǐfàn.)\n"
            "= Tôi thích ăn cơm nhất.\n\n"
            "⚠️ <b>Lưu ý:</b>\n"
            "• 比 KHÔNG đi với 很: ❌ 他比我很高\n"
            "• Có thể thêm mức độ: 他比我高一点儿/得多\n"
        ),
    },
    "grammar_zai": {
        "title": "📝 Ngữ pháp: 在 (zài) - Đang/Ở",
        "content": (
            "📝 <b>NGỮ PHÁP: 在 (zài)</b>\n\n"
            "在 (zài) có 2 nghĩa chính:\n\n"
            "📌 <b>1. 在 = Ở (chỉ vị trí)</b>\n"
            "Cấu trúc: S + 在 + Nơi chốn\n\n"
            "我在家。(Wǒ zài jiā.) = Tôi ở nhà.\n"
            "他在学校。(Tā zài xuéxiào.) = Anh ấy ở trường.\n"
            "书在桌子上。(Shū zài zhuōzi shàng.)\n"
            "= Sách ở trên bàn.\n\n"
            "📌 <b>2. 在 + V = Đang (tiến hành)</b>\n"
            "Cấu trúc: S + 在 + V\n\n"
            "我在吃饭。(Wǒ zài chīfàn.) = Tôi đang ăn cơm.\n"
            "他在看书。(Tā zài kàn shū.) = Anh ấy đang đọc sách.\n"
            "你在做什么？(Nǐ zài zuò shénme?)\n"
            "= Bạn đang làm gì?\n\n"
            "📌 <b>Phương hướng:</b>\n"
            "上 (shàng) = trên\n"
            "下 (xià) = dưới\n"
            "前 (qián) = trước\n"
            "后 (hòu) = sau\n"
            "左 (zuǒ) = trái\n"
            "右 (yòu) = phải\n"
            "里 (lǐ) = trong\n"
            "外 (wài) = ngoài\n"
            "旁边 (pángbiān) = bên cạnh\n"
            "对面 (duìmiàn) = đối diện\n"
        ),
    },
    "conversation_restaurant": {
        "title": "🍽 Giao tiếp: Nhà hàng",
        "content": (
            "🍽 <b>GIAO TIẾP TẠI NHÀ HÀNG - 在餐厅 (Zài cāntīng)</b>\n\n"
            "📌 <b>Từ vựng bổ sung:</b>\n"
            "服务员 (fúwùyuán) = nhân viên phục vụ\n"
            "菜单 (càidān) = thực đơn\n"
            "点菜 (diǎn cài) = gọi món\n"
            "好吃 (hǎo chī) = ngon (đồ ăn)\n"
            "好喝 (hǎo hē) = ngon (đồ uống)\n"
            "辣 (là) = cay\n"
            "甜 (tián) = ngọt\n"
            "咸 (xián) = mặn\n"
            "酸 (suān) = chua\n"
            "买单 (mǎidān) = tính tiền\n\n"
            "📌 <b>Hội thoại mẫu:</b>\n\n"
            "🧑‍🍳 服务员: 欢迎光临！请坐，这是菜单。\n"
            "   (Huānyíng guānglín! Qǐng zuò, zhè shì càidān.)\n"
            "   Chào mừng! Mời ngồi, đây là thực đơn.\n\n"
            "🙋 Khách: 谢谢。请问，有什么推荐的吗？\n"
            "   (Xièxie. Qǐngwèn, yǒu shénme tuījiàn de ma?)\n"
            "   Cảm ơn. Xin hỏi, có gì gợi ý không?\n\n"
            "🧑‍🍳 服务员: 我们的红烧肉很好吃。\n"
            "   (Wǒmen de hóngshāo ròu hěn hǎochī.)\n"
            "   Thịt kho tàu của chúng tôi rất ngon.\n\n"
            "🙋 Khách: 好的，我要一个红烧肉，一碗米饭。\n"
            "   (Hǎo de, wǒ yào yí gè hóngshāo ròu, yì wǎn mǐfàn.)\n"
            "   Vâng, tôi muốn một phần thịt kho, một bát cơm.\n\n"
            "🙋 Khách: 买单！一共多少钱？\n"
            "   (Mǎidān! Yígòng duōshao qián?)\n"
            "   Tính tiền! Tổng cộng bao nhiêu?\n"
        ),
    },
    "conversation_directions": {
        "title": "🗺 Giao tiếp: Hỏi đường",
        "content": (
            "🗺 <b>HỎI ĐƯỜNG - 问路 (Wèn lù)</b>\n\n"
            "📌 <b>Từ vựng:</b>\n"
            "往 (wǎng) = về hướng\n"
            "走 (zǒu) = đi\n"
            "转 (zhuǎn) = rẽ, quẹo\n"
            "到 (dào) = đến\n"
            "远 (yuǎn) = xa\n"
            "近 (jìn) = gần\n"
            "十字路口 (shízì lùkǒu) = ngã tư\n"
            "红绿灯 (hóng lǜ dēng) = đèn giao thông\n\n"
            "📌 <b>Hội thoại mẫu:</b>\n\n"
            "🙋 Bạn: 请问，去火车站怎么走？\n"
            "   (Qǐngwèn, qù huǒchē zhàn zěnme zǒu?)\n"
            "   Xin hỏi, đi ga tàu hỏa đi thế nào?\n\n"
            "👤 Người qua đường: 一直往前走，到十字路口右转。\n"
            "   (Yìzhí wǎng qián zǒu, dào shízì lùkǒu yòu zhuǎn.)\n"
            "   Đi thẳng phía trước, đến ngã tư rẽ phải.\n\n"
            "🙋 Bạn: 远不远？\n"
            "   (Yuǎn bù yuǎn?)\n"
            "   Có xa không?\n\n"
            "👤 Người qua đường: 不远，走路大概十分钟。\n"
            "   (Bù yuǎn, zǒulù dàgài shí fēnzhōng.)\n"
            "   Không xa, đi bộ khoảng 10 phút.\n\n"
            "🙋 Bạn: 谢谢你！(Xièxie nǐ!) = Cảm ơn bạn!\n"
            "👤: 不客气。(Bú kèqi.) = Không có gì.\n"
        ),
    },
}

# ============================================================
# LEVEL 3: HSK3 (600 từ vựng)
# ============================================================

LEVEL_3_LESSONS = {
    "vocab_work": {
        "title": "💼 Công việc & Nghề nghiệp",
        "content": (
            "💼 <b>CÔNG VIỆC - 工作 (Gōngzuò)</b>\n\n"
            "📌 <b>Nghề nghiệp:</b>\n"
            "老师 (lǎoshī) = giáo viên\n"
            "医生 (yīshēng) = bác sĩ\n"
            "律师 (lǜshī) = luật sư\n"
            "工程师 (gōngchéngshī) = kỹ sư\n"
            "经理 (jīnglǐ) = giám đốc, quản lý\n"
            "记者 (jìzhě) = phóng viên\n"
            "演员 (yǎnyuán) = diễn viên\n"
            "司机 (sījī) = tài xế\n"
            "服务员 (fúwùyuán) = nhân viên phục vụ\n"
            "护士 (hùshi) = y tá\n\n"
            "📌 <b>Từ vựng công việc:</b>\n"
            "上班 (shàngbān) = đi làm\n"
            "下班 (xiàbān) = tan làm\n"
            "加班 (jiābān) = tăng ca\n"
            "工资 (gōngzī) = lương\n"
            "请假 (qǐngjià) = xin nghỉ phép\n"
            "面试 (miànshì) = phỏng vấn\n"
            "简历 (jiǎnlì) = CV, sơ yếu lý lịch\n"
            "经验 (jīngyàn) = kinh nghiệm\n\n"
            "📌 <b>Hội thoại:</b>\n"
            "A: 你做什么工作？(Nǐ zuò shénme gōngzuò?)\n"
            "   Bạn làm nghề gì?\n"
            "B: 我是工程师。(Wǒ shì gōngchéngshī.)\n"
            "   Tôi là kỹ sư.\n"
            "A: 你每天几点上班？(Nǐ měitiān jǐ diǎn shàngbān?)\n"
            "   Mỗi ngày bạn mấy giờ đi làm?\n"
            "B: 我八点上班，五点下班。\n"
            "   (Wǒ bā diǎn shàngbān, wǔ diǎn xiàbān.)\n"
            "   Tôi 8 giờ đi làm, 5 giờ tan.\n"
        ),
    },
    "vocab_emotions": {
        "title": "😊 Cảm xúc & Tính cách",
        "content": (
            "😊 <b>CẢM XÚC & TÍNH CÁCH - 情感 (Qínggǎn)</b>\n\n"
            "📌 <b>Cảm xúc:</b>\n"
            "高兴 (gāoxìng) = vui vẻ\n"
            "难过 (nánguò) = buồn\n"
            "生气 (shēngqì) = tức giận\n"
            "害怕 (hàipà) = sợ hãi\n"
            "紧张 (jǐnzhāng) = lo lắng, hồi hộp\n"
            "着急 (zháojí) = sốt ruột, vội vã\n"
            "满意 (mǎnyì) = hài lòng\n"
            "失望 (shīwàng) = thất vọng\n"
            "感动 (gǎndòng) = cảm động\n"
            "无聊 (wúliáo) = chán, nhạt nhẽo\n\n"
            "📌 <b>Tính cách:</b>\n"
            "聪明 (cōngming) = thông minh\n"
            "认真 (rènzhēn) = nghiêm túc, chăm chỉ\n"
            "热情 (rèqíng) = nhiệt tình\n"
            "耐心 (nàixīn) = kiên nhẫn\n"
            "勇敢 (yǒnggǎn) = dũng cảm\n"
            "懒 (lǎn) = lười\n"
            "骄傲 (jiāo'ào) = kiêu ngạo / tự hào\n\n"
            "📌 <b>Mẫu câu:</b>\n"
            "我今天很高兴。(Wǒ jīntiān hěn gāoxìng.)\n"
            "= Hôm nay tôi rất vui.\n"
            "别生气了。(Bié shēngqì le.) = Đừng giận nữa.\n"
            "他是一个很认真的人。\n"
            "(Tā shì yí gè hěn rènzhēn de rén.)\n"
            "= Anh ấy là một người rất nghiêm túc.\n"
        ),
    },
    "vocab_hobbies": {
        "title": "🎨 Sở thích & Giải trí",
        "content": (
            "🎨 <b>SỞ THÍCH - 爱好 (Àihào)</b>\n\n"
            "📌 <b>Từ vựng:</b>\n"
            "看书 (kàn shū) = đọc sách\n"
            "听音乐 (tīng yīnyuè) = nghe nhạc\n"
            "看电影 (kàn diànyǐng) = xem phim\n"
            "唱歌 (chàng gē) = hát\n"
            "跳舞 (tiào wǔ) = nhảy múa\n"
            "画画 (huà huà) = vẽ tranh\n"
            "旅游 (lǚyóu) = du lịch\n"
            "运动 (yùndòng) = thể thao\n"
            "游泳 (yóuyǒng) = bơi lội\n"
            "打篮球 (dǎ lánqiú) = chơi bóng rổ\n"
            "踢足球 (tī zúqiú) = đá bóng\n"
            "爬山 (pá shān) = leo núi\n"
            "上网 (shàng wǎng) = lên mạng\n"
            "玩游戏 (wán yóuxì) = chơi game\n\n"
            "📌 <b>Hội thoại:</b>\n"
            "A: 你有什么爱好？(Nǐ yǒu shénme àihào?)\n"
            "   Bạn có sở thích gì?\n\n"
            "B: 我喜欢看书和听音乐。你呢？\n"
            "   (Wǒ xǐhuan kàn shū hé tīng yīnyuè. Nǐ ne?)\n"
            "   Tôi thích đọc sách và nghe nhạc. Còn bạn?\n\n"
            "A: 我最喜欢旅游。我去过很多地方。\n"
            "   (Wǒ zuì xǐhuan lǚyóu. Wǒ qù guo hěn duō dìfang.)\n"
            "   Tôi thích nhất là du lịch. Tôi đã đi nhiều nơi.\n\n"
            "B: 你去过中国吗？\n"
            "   (Nǐ qù guo Zhōngguó ma?)\n"
            "   Bạn đã đi Trung Quốc chưa?\n"
        ),
    },
    "grammar_ba": {
        "title": "📝 Ngữ pháp: 把 (bǎ) - Câu xử trí",
        "content": (
            "📝 <b>NGỮ PHÁP: CÂU 把 (bǎ)</b>\n\n"
            "Câu 把 dùng khi muốn nhấn mạnh tác động lên đối tượng.\n\n"
            "📌 <b>Cấu trúc:</b>\n"
            "S + 把 + Tân ngữ + V + Kết quả bổ ngữ\n\n"
            "📌 <b>Ví dụ:</b>\n"
            "请把门关上。(Qǐng bǎ mén guān shàng.)\n"
            "= Xin hãy đóng cửa lại.\n\n"
            "我把作业做完了。(Wǒ bǎ zuòyè zuò wán le.)\n"
            "= Tôi đã làm xong bài tập rồi.\n\n"
            "他把那本书看完了。(Tā bǎ nà běn shū kàn wán le.)\n"
            "= Anh ấy đã đọc xong quyển sách đó.\n\n"
            "请把这个字写一遍。(Qǐng bǎ zhège zì xiě yí biàn.)\n"
            "= Xin hãy viết chữ này một lần.\n\n"
            "📌 <b>Phủ định: 没/不 đặt trước 把</b>\n"
            "他没把窗户关上。(Tā méi bǎ chuānghu guān shàng.)\n"
            "= Anh ấy chưa đóng cửa sổ.\n\n"
            "你不要把他的东西弄坏了。\n"
            "(Nǐ bú yào bǎ tā de dōngxi nòng huài le.)\n"
            "= Đừng làm hỏng đồ của anh ấy.\n\n"
            "⚠️ <b>Lưu ý:</b>\n"
            "• Tân ngữ phải xác định (đã biết)\n"
            "• V phải có kết quả bổ ngữ (完、好、上、下...)\n"
            "• Không phải câu nào cũng dùng được 把\n"
        ),
    },
    "grammar_de_complement": {
        "title": "📝 Ngữ pháp: 得 (de) - Bổ ngữ trình độ",
        "content": (
            "📝 <b>NGỮ PHÁP: BỔ NGỮ TRÌNH ĐỘ VỚI 得</b>\n\n"
            "得 (de) dùng để mô tả mức độ / cách thức hành động.\n\n"
            "📌 <b>Cấu trúc:</b>\n"
            "V + 得 + Adj / Mô tả\n\n"
            "📌 <b>Ví dụ:</b>\n"
            "他说得很好。(Tā shuō de hěn hǎo.)\n"
            "= Anh ấy nói rất giỏi.\n\n"
            "她唱得很好听。(Tā chàng de hěn hǎotīng.)\n"
            "= Cô ấy hát rất hay.\n\n"
            "你跑得太快了。(Nǐ pǎo de tài kuài le.)\n"
            "= Bạn chạy nhanh quá.\n\n"
            "我写汉字写得不好。(Wǒ xiě Hànzì xiě de bù hǎo.)\n"
            "= Tôi viết chữ Hán không đẹp.\n\n"
            "📌 <b>Đặt câu hỏi:</b>\n"
            "他中文说得怎么样？\n"
            "(Tā Zhōngwén shuō de zěnmeyàng?)\n"
            "= Tiếng Trung anh ấy nói thế nào?\n\n"
            "你昨天睡得好吗？\n"
            "(Nǐ zuótiān shuì de hǎo ma?)\n"
            "= Hôm qua bạn ngủ có ngon không?\n\n"
            "⚠️ <b>Phân biệt 3 chữ de:</b>\n"
            "• 的 (de) = \"của\" → 我的书 (sách của tôi)\n"
            "• 得 (de) = bổ ngữ → 说得好 (nói giỏi)\n"
            "• 地 (de) = trạng ngữ → 高兴地说 (vui vẻ nói)\n"
        ),
    },
    "grammar_passive": {
        "title": "📝 Ngữ pháp: 被 (bèi) - Bị động",
        "content": (
            "📝 <b>NGỮ PHÁP: CÂU BỊ ĐỘNG VỚI 被 (bèi)</b>\n\n"
            "被 (bèi) dùng để diễn đạt ý \"bị\" hoặc \"được\".\n\n"
            "📌 <b>Cấu trúc:</b>\n"
            "Người chịu + 被 + (Người gây ra) + V + Kết quả\n\n"
            "📌 <b>Ví dụ:</b>\n"
            "我的手机被偷了。(Wǒ de shǒujī bèi tōu le.)\n"
            "= Điện thoại của tôi bị trộm rồi.\n\n"
            "杯子被他打碎了。(Bēizi bèi tā dǎ suì le.)\n"
            "= Cái cốc bị anh ấy đập vỡ rồi.\n\n"
            "他被老师批评了。(Tā bèi lǎoshī pīpíng le.)\n"
            "= Anh ấy bị giáo viên phê bình.\n\n"
            "这本书被翻译成越南语了。\n"
            "(Zhè běn shū bèi fānyì chéng Yuènán yǔ le.)\n"
            "= Quyển sách này đã được dịch sang tiếng Việt.\n\n"
            "📌 <b>Lưu ý:</b>\n"
            "• Thường mang nghĩa tiêu cực (bị)\n"
            "• Cũng có thể mang nghĩa tích cực (được)\n"
            "• V phải có kết quả bổ ngữ\n"
            "• Có thể bỏ người gây ra:\n"
            "  衣服被弄脏了。= Quần áo bị làm bẩn rồi.\n"
        ),
    },
    "conversation_travel": {
        "title": "✈️ Giao tiếp: Du lịch",
        "content": (
            "✈️ <b>GIAO TIẾP DU LỊCH - 旅游 (Lǚyóu)</b>\n\n"
            "📌 <b>Từ vựng:</b>\n"
            "护照 (hùzhào) = hộ chiếu\n"
            "签证 (qiānzhèng) = visa\n"
            "酒店 (jiǔdiàn) = khách sạn\n"
            "预订 (yùdìng) = đặt trước\n"
            "景点 (jǐngdiǎn) = điểm du lịch\n"
            "导游 (dǎoyóu) = hướng dẫn viên\n"
            "地图 (dìtú) = bản đồ\n"
            "照相 (zhào xiàng) = chụp ảnh\n\n"
            "📌 <b>Hội thoại đặt phòng khách sạn:</b>\n\n"
            "🙋 Bạn: 你好，我想预订一个房间。\n"
            "   (Nǐ hǎo, wǒ xiǎng yùdìng yí gè fángjiān.)\n"
            "   Xin chào, tôi muốn đặt một phòng.\n\n"
            "🏨 Lễ tân: 您要住几天？\n"
            "   (Nín yào zhù jǐ tiān?)\n"
            "   Quý khách muốn ở mấy ngày?\n\n"
            "🙋 Bạn: 三天。有双人间吗？\n"
            "   (Sān tiān. Yǒu shuāngrén jiān ma?)\n"
            "   Ba ngày. Có phòng đôi không?\n\n"
            "🏨 Lễ tân: 有的。一天三百块。\n"
            "   (Yǒu de. Yì tiān sān bǎi kuài.)\n"
            "   Có ạ. Một ngày 300 tệ.\n\n"
            "📌 <b>Câu hữu ích khi du lịch:</b>\n"
            "请帮我照一张相。(Qǐng bāng wǒ zhào yì zhāng xiàng.)\n"
            "= Xin chụp giúp tôi một tấm ảnh.\n"
            "这个地方叫什么？(Zhège dìfang jiào shénme?)\n"
            "= Nơi này tên gì?\n"
            "附近有什么好玩的地方？\n"
            "(Fùjìn yǒu shénme hǎo wán de dìfang?)\n"
            "= Gần đây có chỗ nào vui không?\n"
        ),
    },
    "conversation_phone": {
        "title": "📱 Giao tiếp: Điện thoại & Mạng xã hội",
        "content": (
            "📱 <b>ĐIỆN THOẠI & MẠNG XÃ HỘI</b>\n\n"
            "📌 <b>Từ vựng:</b>\n"
            "手机 (shǒujī) = điện thoại di động\n"
            "打电话 (dǎ diànhuà) = gọi điện\n"
            "发短信 (fā duǎnxìn) = gửi tin nhắn\n"
            "微信 (Wēixìn) = WeChat\n"
            "网络 (wǎngluò) = mạng\n"
            "密码 (mìmǎ) = mật khẩu\n"
            "下载 (xiàzǎi) = tải xuống\n"
            "扫码 (sǎo mǎ) = quét mã QR\n"
            "充电 (chōng diàn) = sạc pin\n"
            "没电了 (méi diàn le) = hết pin rồi\n"
            "WiFi (WiFi) = WiFi\n\n"
            "📌 <b>Hội thoại gọi điện:</b>\n\n"
            "📞 Riiing...\n"
            "A: 喂？你好！(Wéi? Nǐ hǎo!) = Alô? Xin chào!\n\n"
            "B: 你好，请问小王在吗？\n"
            "   (Nǐ hǎo, qǐngwèn Xiǎo Wáng zài ma?)\n"
            "   Chào, xin hỏi Tiểu Vương có đó không?\n\n"
            "A: 我就是。你是谁？\n"
            "   (Wǒ jiù shì. Nǐ shì shéi?)\n"
            "   Tôi đây. Bạn là ai?\n\n"
            "B: 我是小李。明天你有空吗？\n"
            "   (Wǒ shì Xiǎo Lǐ. Míngtiān nǐ yǒu kòng ma?)\n"
            "   Tôi là Tiểu Lý. Ngày mai bạn rảnh không?\n\n"
            "📌 <b>Câu hữu ích:</b>\n"
            "WiFi密码是什么？(WiFi mìmǎ shì shénme?)\n"
            "= Mật khẩu WiFi là gì?\n"
            "你的微信号是多少？(Nǐ de Wēixìn hào shì duōshao?)\n"
            "= Số WeChat của bạn là bao nhiêu?\n"
        ),
    },
}


# ============================================================
# BÀI TẬP ÔN LUYỆN (QUIZ)
# ============================================================

QUIZZES = {
    "level_0": [
        {
            "question": "\"Xin chào\" trong tiếng Trung là gì?",
            "options": ["你好 (Nǐ hǎo)", "再见 (Zàijiàn)", "谢谢 (Xièxie)", "对不起 (Duìbuqǐ)"],
            "correct": 0,
            "explanation": "你好 (Nǐ hǎo) = Xin chào! Đây là câu chào phổ biến nhất."
        },
        {
            "question": "Thanh điệu nào đi từ thấp lên cao?",
            "options": ["Thanh 1 (ˉ)", "Thanh 2 (ˊ)", "Thanh 3 (ˇ)", "Thanh 4 (ˋ)"],
            "correct": 1,
            "explanation": "Thanh 2 (ˊ) đi từ thấp lên cao, giống như khi bạn hỏi \"hả?\""
        },
        {
            "question": "妈 (mā) nghĩa là gì?",
            "options": ["Ngựa", "Mẹ", "Chửi", "Tê/Gai"],
            "correct": 1,
            "explanation": "妈 (mā - thanh 1) = mẹ. So sánh: 马 (mǎ - thanh 3) = ngựa"
        },
        {
            "question": "Số 7 trong tiếng Trung viết là gì?",
            "options": ["六 (liù)", "七 (qī)", "八 (bā)", "九 (jiǔ)"],
            "correct": 1,
            "explanation": "七 (qī) = 7. Lưu ý: 六=6, 八=8, 九=9"
        },
        {
            "question": "\"Tạm biệt\" là gì?",
            "options": ["你好 (Nǐ hǎo)", "谢谢 (Xièxie)", "再见 (Zàijiàn)", "对不起 (Duìbuqǐ)"],
            "correct": 2,
            "explanation": "再见 (Zàijiàn) = Tạm biệt! 再 = lại, 见 = gặp → gặp lại"
        },
        {
            "question": "我是越南人。Câu này nghĩa là gì?",
            "options": [
                "Tôi là người Trung Quốc.",
                "Tôi là người Việt Nam.",
                "Tôi là sinh viên.",
                "Tôi là giáo viên."
            ],
            "correct": 1,
            "explanation": "我(tôi) + 是(là) + 越南(Việt Nam) + 人(người) = Tôi là người Việt Nam."
        },
        {
            "question": "Nét cơ bản 横 (héng) là nét gì?",
            "options": ["Nét sổ (|)", "Nét ngang (—)", "Nét phẩy (/)", "Nét chấm (.)"],
            "correct": 1,
            "explanation": "横 (héng) = nét ngang (—), là nét cơ bản đầu tiên cần học."
        },
        {
            "question": "12 trong tiếng Trung viết như thế nào?",
            "options": ["一十二", "十二", "二十", "十十二"],
            "correct": 1,
            "explanation": "十二 (shí èr) = 12. Không cần thêm 一 phía trước."
        },
    ],
    "level_1": [
        {
            "question": "你家有几口人？Câu này hỏi gì?",
            "options": [
                "Nhà bạn ở đâu?",
                "Gia đình bạn có mấy người?",
                "Bạn có bao nhiêu tiền?",
                "Bạn muốn ăn gì?"
            ],
            "correct": 1,
            "explanation": "家(nhà) + 有(có) + 几(mấy) + 口(đơn vị đếm người trong gia đình) + 人(người)"
        },
        {
            "question": "\"Ngày mai\" trong tiếng Trung là gì?",
            "options": ["昨天 (zuótiān)", "今天 (jīntiān)", "明天 (míngtiān)", "后天 (hòutiān)"],
            "correct": 2,
            "explanation": "明天 (míngtiān) = ngày mai. 昨天=hôm qua, 今天=hôm nay, 后天=ngày kia"
        },
        {
            "question": "Phủ định của 有 (yǒu) là gì?",
            "options": ["不有", "没有", "不是", "没是"],
            "correct": 1,
            "explanation": "Phủ định của 有 luôn là 没有 (méi yǒu). KHÔNG BAO GIỜ dùng 不有!"
        },
        {
            "question": "我想喝茶。Nghĩa là gì?",
            "options": [
                "Tôi muốn ăn cơm.",
                "Tôi muốn uống trà.",
                "Tôi muốn mua trà.",
                "Tôi thích uống trà."
            ],
            "correct": 1,
            "explanation": "想(muốn) + 喝(uống) + 茶(trà) = Tôi muốn uống trà."
        },
        {
            "question": "这个多少钱？用来做什么？ Câu hỏi này dùng khi nào?",
            "options": ["Hỏi giờ", "Hỏi đường", "Hỏi giá tiền", "Hỏi tên"],
            "correct": 2,
            "explanation": "多少钱 (duōshao qián) = bao nhiêu tiền? Dùng khi mua sắm, hỏi giá."
        },
        {
            "question": "Đâu KHÔNG phải cách đặt câu hỏi đúng?",
            "options": [
                "你是学生吗？",
                "你是不是学生？",
                "你是学生不？",
                "谁是学生？"
            ],
            "correct": 2,
            "explanation": "Cách đúng: thêm 吗, dùng A不A, hoặc dùng từ để hỏi. \"你是学生不？\" là sai ngữ pháp."
        },
    ],
    "level_2": [
        {
            "question": "他比我高。Nghĩa là gì?",
            "options": [
                "Anh ấy cao bằng tôi.",
                "Anh ấy cao hơn tôi.",
                "Tôi cao hơn anh ấy.",
                "Anh ấy cao nhất."
            ],
            "correct": 1,
            "explanation": "A 比 B + Adj = A hơn B. 他(anh ấy) 比(hơn) 我(tôi) 高(cao)"
        },
        {
            "question": "我吃了早饭。了 trong câu này có nghĩa gì?",
            "options": [
                "Đang ăn",
                "Sẽ ăn",
                "Đã ăn xong",
                "Muốn ăn"
            ],
            "correct": 2,
            "explanation": "V + 了 = hành động đã hoàn thành. 吃了早饭 = đã ăn sáng rồi."
        },
        {
            "question": "Phủ định của 我吃了早饭 là gì?",
            "options": [
                "我不吃了早饭",
                "我没吃早饭",
                "我不吃早饭了",
                "我没吃了早饭"
            ],
            "correct": 1,
            "explanation": "Phủ định quá khứ: 没 + V (bỏ 了). 我没吃早饭 = Tôi chưa ăn sáng."
        },
        {
            "question": "你在做什么？Nghĩa là gì?",
            "options": [
                "Bạn ở đâu?",
                "Bạn đang làm gì?",
                "Bạn muốn làm gì?",
                "Bạn đã làm gì?"
            ],
            "correct": 1,
            "explanation": "在 + V = đang. 你在做什么 = Bạn đang làm gì?"
        },
        {
            "question": "去火车站怎么走？Câu này dùng khi nào?",
            "options": ["Mua vé tàu", "Hỏi đường đến ga tàu", "Gọi taxi", "Đặt phòng khách sạn"],
            "correct": 1,
            "explanation": "去(đi) + 火车站(ga tàu) + 怎么走(đi thế nào) = Đến ga tàu đi thế nào?"
        },
    ],
    "level_3": [
        {
            "question": "请把门关上。Câu 把 này có nghĩa gì?",
            "options": [
                "Xin hãy mở cửa ra.",
                "Xin hãy đóng cửa lại.",
                "Cửa đã đóng rồi.",
                "Đừng đóng cửa."
            ],
            "correct": 1,
            "explanation": "把 + 门(cửa) + 关上(đóng lại) = Hãy đóng cửa lại."
        },
        {
            "question": "他说得很好。得 trong câu này dùng để làm gì?",
            "options": [
                "Chỉ sở hữu (của)",
                "Bổ ngữ trình độ (mức độ)",
                "Trạng ngữ",
                "Chỉ khả năng"
            ],
            "correct": 1,
            "explanation": "V + 得 + Adj = bổ ngữ trình độ. 说得很好 = nói rất giỏi."
        },
        {
            "question": "我的手机被偷了。被 nghĩa là gì?",
            "options": ["Được", "Bị", "Cho", "Với"],
            "correct": 1,
            "explanation": "被 (bèi) = bị (câu bị động). 手机被偷了 = điện thoại bị trộm rồi."
        },
        {
            "question": "Phân biệt 的, 得, 地 - câu nào đúng?",
            "options": [
                "我的书 / 说得好 / 高兴地说",
                "我得书 / 说的好 / 高兴地说",
                "我地书 / 说得好 / 高兴的说",
                "我的书 / 说地好 / 高兴得说"
            ],
            "correct": 0,
            "explanation": "的=sở hữu(我的书), 得=trình độ(说得好), 地=trạng ngữ(高兴地说)"
        },
        {
            "question": "WiFi密码是什么？Câu này hỏi gì?",
            "options": [
                "WiFi có nhanh không?",
                "Mật khẩu WiFi là gì?",
                "Có WiFi không?",
                "WiFi bao nhiêu tiền?"
            ],
            "correct": 1,
            "explanation": "密码(mật khẩu) + 是什么(là gì) = Mật khẩu WiFi là gì?"
        },
    ],
}

# ============================================================
# CẤU TRÚC LỘ TRÌNH HỌC
# ============================================================

CURRICULUM = {
    "level_0": {
        "name": "🌱 Nhập môn (Mất gốc)",
        "description": "Dành cho người chưa biết gì về tiếng Trung. Học phát âm, thanh điệu, pinyin, số đếm, chào hỏi cơ bản.",
        "lessons": LEVEL_0_LESSONS,
        "lesson_order": ["intro", "tones", "pinyin_initials", "pinyin_finals", "numbers", "greetings", "self_intro"],
    },
    "level_1": {
        "name": "📗 HSK1 (Cơ bản)",
        "description": "150 từ vựng, ngữ pháp cơ bản, giao tiếp đơn giản. Chủ đề: gia đình, thời gian, ăn uống, mua sắm.",
        "lessons": LEVEL_1_LESSONS,
        "lesson_order": ["vocab_family", "vocab_time", "vocab_food", "grammar_shi", "grammar_you", "grammar_questions", "conversation_shopping", "writing_basic"],
    },
    "level_2": {
        "name": "📘 HSK2 (Sơ trung cấp)",
        "description": "300 từ vựng, ngữ pháp mở rộng, giao tiếp thực tế. Chủ đề: giao thông, thời tiết, sức khỏe, nhà hàng.",
        "lessons": LEVEL_2_LESSONS,
        "lesson_order": ["vocab_transport", "vocab_weather", "vocab_body_health", "grammar_le", "grammar_comparison", "grammar_zai", "conversation_restaurant", "conversation_directions"],
    },
    "level_3": {
        "name": "📙 HSK3 (Trung cấp)",
        "description": "600 từ vựng, ngữ pháp nâng cao, giao tiếp tự tin. Chủ đề: công việc, cảm xúc, sở thích, du lịch.",
        "lessons": LEVEL_3_LESSONS,
        "lesson_order": ["vocab_work", "vocab_emotions", "vocab_hobbies", "grammar_ba", "grammar_de_complement", "grammar_passive", "conversation_travel", "conversation_phone"],
    },
}

# Map level keys
LEVEL_NAMES = {
    "level_0": "🌱 Nhập môn",
    "level_1": "📗 HSK1",
    "level_2": "📘 HSK2",
    "level_3": "📙 HSK3",
}
