"""
Module Sổ Tay Ngữ Pháp Tiếng Trung Trọng Điểm (Grammar Guide)
Giải thích chi tiết cấu trúc, công thức, ví dụ pinyin và lỗi sai người Việt hay gặp.
"""

GRAMMAR_POINTS = {
    "ba_sentence": {
        "title": "📌 Câu chữ 把 (bǎ) - Thao tác & Tác động",
        "description": "Câu chữ 把 dùng để diễn tả chủ ngữ đã tác động, xử lý hoặc làm thay đổi trạng thái của tân ngữ.",
        "content": (
            "📌 <b>CÂU CHỮ 把 (bǎ) - NGỮ PHÁP KINH ĐIỂN</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🎯 <b>Ý nghĩa:</b> Dùng khi muốn nhấn mạnh sự xử lý, thay đổi của đối tượng sau khi chịu tác động của hành động.\n\n"
            "📐 <b>Cấu trúc chuẩn:</b>\n"
            "<code>Chủ ngữ + 把 + Tân ngữ + Động từ + Thành phần khác (了/bổ ngữ)</code>\n\n"
            "🌟 <b>Ví dụ sinh động:</b>\n"
            "1. 我<b>把</b>作业做完了。\n"
            "   <i>(Wǒ bǎ zuòyè zuò wán le.)</i>\n"
            "   → Tôi đã làm xong bài tập rồi.\n\n"
            "2. 请<b>把</b>空调关掉。\n"
            "   <i>(Qǐng bǎ kōngtiáo guān diào.)</i>\n"
            "   → Xin hãy tắt điều hòa đi.\n\n"
            "3. 他<b>把</b>手机借给我了。\n"
            "   <i>(Tā bǎ shǒujī jiè gěi wǒ le.)</i>\n"
            "   → Anh ấy đã cho tôi mượn điện thoại rồi.\n\n"
            "⚠️ <b>LƯU Ý CỐT LÕI:</b>\n"
            "• Động từ trong câu chữ 把 KHÔNG ĐƯỢC đứng trơ trọi một mình, phía sau bắt buộc phải có thành phần khác (ví dụ: 了, 在, 到, tân ngữ kết quả, bổ ngữ xu hướng).\n"
            "• Sai: ❌ 我把书看 (Wǒ bǎ shū kàn)\n"
            "• Đúng: ✅ 我把书看完了 (Wǒ bǎ shū kàn wán le)"
        )
    },
    "bei_sentence": {
        "title": "📌 Câu Bị Động chữ 被 (bèi)",
        "description": "Diễn tả sự vật, đối tượng bị hoặc được tác động bởi một ai đó/cái gì đó.",
        "content": (
            "📌 <b>CÂU BỊ ĐỘNG CHỮ 被 (bèi)</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🎯 <b>Ý nghĩa:</b> Thể hiện ý bị động (thường mang sắc thái không may hoặc kết quả xảy ra ngoài ý muốn).\n\n"
            "📐 <b>Cấu trúc chuẩn:</b>\n"
            "<code>Đối tượng chịu tác động + 被 + (Kẻ tác động) + Động từ + Thành phần khác</code>\n\n"
            "🌟 <b>Ví dụ sinh động:</b>\n"
            "1. 我的钱包<b>被</b>偷了！\n"
            "   <i>(Wǒ de qiánbāo bèi tōu le!)</i>\n"
            "   → Ví tiền của tôi bị trộm mất rồi!\n\n"
            "2. 苹果<b>被</b>弟弟吃了。\n"
            "   <i>(Píngguǒ bèi dìdi chī le.)</i>\n"
            "   → Quả táo đã bị em trai ăn mất rồi.\n\n"
            "💡 <b>Mẹo khẩu ngữ:</b> Trong văn nói thường ngày, người Trung Quốc rất hay thay <b>被</b> bằng <b>叫 (jiào)</b> hoặc <b>让 (ràng)</b>:\n"
            "• 手机让雨淋湿了。(Shǒujī ràng yǔ lín shī le) = Điện thoại bị mưa làm ướt rồi."
        )
    },
    "le_particle": {
        "title": "📌 Trợ Từ 了 (le) - Hoàn thành & Thay đổi trạng thái",
        "description": "Cách dùng chính xác của trợ từ ngữ khí và động thái 了, tránh nhầm với thì quá khứ.",
        "content": (
            "📌 <b>BÍ KÍP DÙNG TRỢ TỪ 了 (le)</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🎯 Trong tiếng Trung, <b>了</b> KHÔNG ĐỒNG NGHĨA đơn thuần với quá khứ, mà nó có 2 chức năng cực lớn:\n\n"
            "1️⃣ <b>Động thái 了 (Đứng ngay sau Động từ):</b> Nhấn mạnh hành động ĐÃ HOÀN THÀNH.\n"
            "• 我买<b>了</b>两本书。(Wǒ mǎi le liǎng běn shū) = Tôi đã mua 2 quyển sách.\n"
            "• Phủ định hoàn thành dùng <b>没 (méi)</b>, KHÔNG DÙNG 了: 我没买书 (Wǒ méi mǎi shū).\n\n"
            "2️⃣ <b>Ngữ khí 了 (Đứng ở CUỐI CÂU):</b> Nhấn mạnh CÓ SỰ THAY ĐỔI TRẠNG THÁI (Trước kia không vậy, giờ đã vậy).\n"
            "• 下雨<b>了</b>。(Xià yǔ le) = Trời mưa rồi (Trước đó không mưa, giờ bắt đầu mưa).\n"
            "• 我有女朋友<b>了</b>。(Wǒ yǒu nǚpéngyou le) = Tôi có bạn gái rồi (Trước kia độc thân, giờ có gấu)!"
        )
    },
    "hui_neng_keyi": {
        "title": "📌 Phân Biệt: 会 (huì) vs 能 (néng) vs 可以 (kěyǐ)",
        "description": "Ba từ cùng có nghĩa là 'có thể / biết' nhưng dùng trong các trường hợp hoàn toàn khác nhau.",
        "content": (
            "📌 <b>PHÂN BIỆT: 会 (huì) - 能 (néng) - 可以 (kěyǐ)</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🎯 <b>1. 会 (huì) - Biết làm nhờ qua học tập, rèn luyện:</b>\n"
            "• 我<b>会</b>说汉语。(Wǒ huì shuō Hànyǔ) = Tôi biết nói tiếng Trung (do học mà biết).\n"
            "• 我<b>会</b>游泳。(Wǒ huì yóuyǒng) = Tôi biết bơi.\n\n"
            "🎯 <b>2. 能 (néng) - Có khả năng làm được / Năng lực tự nhiên / Điều kiện cho phép:</b>\n"
            "• 今天我生病了，不<b>能</b>去上班。(Jīntiān wǒ shēngbìng le, bù néng qù shàngbān) = Hôm nay tôi bị ốm, không thể đi làm.\n"
            "• 他一分钟<b>能</b>游100米。(Tā yì fēnzhōng néng yóu 100 mǐ) = Anh ấy một phút có thể bơi 100m (năng lực thể chất).\n\n"
            "🎯 <b>3. 可以 (kěyǐ) - Được phép làm / Cho phép / Đưa ra gợi ý:</b>\n"
            "• 这里<b>可以</b>吸烟吗？(Zhèlǐ kěyǐ xīyān ma?) = Ở đây có được hút thuốc không? (Hỏi sự cho phép)\n"
            "• 你<b>可以</b>坐地铁去。(Nǐ kěyǐ zuò dìtiě qù) = Bạn có thể đi tàu điện ngầm (gợi ý giải pháp)."
        )
    },
    "xiang_yao": {
        "title": "📌 Phân Biệt: 想 (xiǎng) vs 要 (yào)",
        "description": "Đều mang nghĩa 'Muốn', nhưng mức độ và quyết tâm khác nhau.",
        "content": (
            "📌 <b>PHÂN BIỆT: 想 (xiǎng) vs 要 (yào)</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🎯 <b>1. 想 (xiǎng) - 'Muốn, Nghĩ, Nhớ':</b>\n"
            "• Thiên về suy nghĩ trong đầu, mong muốn nhưng chưa chắc đã thực hiện ngay.\n"
            "• 我<b>想</b>去北京旅游。(Wǒ xiǎng qù Běijīng lǚyóu) = Tôi muốn/nghĩ đến việc đi Bắc Kinh du lịch (dự định, ước muốn).\n"
            "• 我很<b>想</b>你。(Wǒ hěn xiǎng nǐ) = Tôi rất nhớ bạn.\n\n"
            "🎯 <b>2. 要 (yào) - 'Cần, Phải, Quyết tâm muốn':</b>\n"
            "• Mức độ mạnh hơn rất nhiều, quyết định chắc chắn làm hoặc yêu cầu ngay lập tức.\n"
            "• 我<b>要</b>一杯水。(Wǒ yào yì bēi shuǐ) = Tôi muốn 1 cốc nước (gọi món, lấy ngay).\n"
            "• 明天我<b>要</b>考试。(Míngtiān wǒ yào kǎoshì) = Ngày mai tôi phải thi (sự việc sắp diễn ra).\n\n"
            "💡 <b>Phủ định:</b>\n"
            "• 不想 (bù xiǎng) = Không muốn\n"
            "• 不要 (bú yào) = Đừng (cấm đoán) hoặc Không cần (khi mua đồ: 不要了 - không lấy nữa)."
        )
    },
    "complements": {
        "title": "📌 Các Loại Bổ Ngữ Quan Trọng Nhất (补语)",
        "description": "Bổ ngữ kết quả (完, 懂, 到) và Bổ ngữ xu hướng (来, 去, 上来, 下去).",
        "content": (
            "📌 <b>CÁC LOẠI BỔ NGỮ KINH ĐIỂN CỦA TIẾNG TRUNG</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🎯 <b>1. Bổ ngữ kết quả (Động từ + Kết quả):</b>\n"
            "• 吃<b>完</b> (chī wán) = Ăn xong\n"
            "• 听<b>懂</b> (tīng dǒng) = Nghe hiểu\n"
            "• 看<b>见</b> (kàn jiàn) = Nhìn thấy\n"
            "• 找<b>到</b> (zhǎo dào) = Tìm được, tìm thấy\n\n"
            "🎯 <b>2. Bổ ngữ xu hướng (Động từ + 来/去):</b>\n"
            "• <b>来 (lái)</b>: Hướng về phía người nói (Tiến lại gần)\n"
            "• <b>去 (qù)</b>: Đi xa khỏi người nói (Rời xa)\n"
            "• 进<b>来</b> (jìn lái) = Đi vào đây (Người nói ở trong phòng)\n"
            "• 出<b>去</b> (chū qù) = Đi ra ngoài kia (Người nói ở trong phòng đuổi ra ngoài)\n\n"
            "🎯 <b>3. Bổ ngữ khả năng (Động từ + 得/不 + Kết quả):</b>\n"
            "• 看<b>得</b>懂 (kàn de dǒng) = Xem/Đọc có thể hiểu được\n"
            "• 看<b>不</b>懂 (kàn bu dǒng) = Xem/Đọc không hiểu nổi\n"
            "• 吃<b>得</b>完 (chī de wán) = Có thể ăn hết\n"
            "• 吃<b>不</b>完 (chī bu wán) = Không thể ăn hết nổi"
        )
    }
}
