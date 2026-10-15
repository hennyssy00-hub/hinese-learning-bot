"""
Module Ngân Hàng Câu Giao Tiếp Thực Chiến & Tiếng Lóng Hot Trend Trung Quốc
Phân loại theo từng chủ đề thực tế đời sống.
"""

PHRASE_CATEGORIES = {
    "daily": {
        "title": "🌟 Chào Hỏi & Xã Giao Thường Ngày",
        "description": "Các câu cửa miệng lịch sự, thân mật khi gặp gỡ hàng ngày",
        "phrases": [
            ("你好！好久不见！", "Nǐ hǎo! Hǎojiǔ bú jiàn!", "Xin chào! Lâu lắm không gặp!"),
            ("最近怎么样？还顺利吗？", "Zuìjìn zěnmeyàng? Hái shùnlì ma?", "Dạo này thế nào rồi? Vẫn thuận lợi chứ?"),
            ("挺好的，老样子。", "Tǐng hǎo de, lǎo yàngzi.", "Khá tốt, vẫn như mọi khi."),
            ("你吃了吗？", "Nǐ chī le ma?", "Bạn ăn cơm chưa? (Câu chào hỏi thân thiết của người Trung)"),
            ("吃了，你呢？", "Chī le, nǐ ne?", "Ăn rồi, còn bạn?"),
            ("借过一下，谢谢！", "Jièguò yíxià, xièxie!", "Xin cho tôi đi nhờ một chút, cảm ơn!"),
            ("辛苦了！", "Xīnkǔ le!", "Vất vả cho bạn rồi! (Dùng để cảm ơn người vừa giúp mình hoặc đồng nghiệp)"),
            ("别客气，小事一桩！", "Bié kèqi, xiǎoshì yì zhuāng!", "Đừng khách sáo, chuyện nhỏ như con thỏ!"),
            ("改天再聊，我先走了！", "Gǎitiān zài liáo, wǒ xiān zǒu le!", "Hôm khác nói chuyện tiếp nhé, tôi đi trước đây!"),
            ("保持联系！", "Bǎochí liánxì!", "Giữ liên lạc nhé!"),
        ]
    },
    "shopping": {
        "title": "🛍️ Mua Sắm & Mặc Cả Đỉnh Cao",
        "description": "Bí quyết hỏi giá, trả giá và thanh toán không sợ bị hớ",
        "phrases": [
            ("老板，这个怎么卖？", "Lǎobǎn, zhè ge zěnme mài?", "Chủ quán ơi, cái này bán thế nào?"),
            ("太贵了！便宜一点吧！", "Tài guì le! Piányi yìdiǎn ba!", "Đắt quá! Bớt chút đi mà!"),
            ("算我便宜点，下次我还来！", "Suàn wǒ piányi diǎn, xià cì wǒ hái lái!", "Tính rẻ cho tôi chút, lần sau tôi lại tới!"),
            ("能不能打个折？", "Néng bu néng dǎ ge zhé?", "Có thể giảm giá một chút không?"),
            ("买两件送一件吗？", "Mǎi liǎng jiàn sòng yí jiàn ma?", "Mua 2 tặng 1 không ạ?"),
            ("不要了，太贵了，我去别家看看。", "Bú yào le, tài guì le, wǒ qù bié jiā kànkan.", "Thôi không lấy nữa, đắt quá, tôi sang tiệm khác xem."),
            ("我可以试穿一下吗？", "Wǒ kěyǐ shìchuān yíxià ma?", "Tôi có thể thử đồ một chút không?"),
            ("有没有大一号的？", "Yǒu méiyǒu dà yí hào de?", "Có cỡ to hơn một số không?"),
            ("支持微信或者支付宝吗？", "Zhīchí Wēixìn huòzhě Zhīfùbǎo ma?", "Có nhận WeChat hay Alipay không?"),
            ("我扫您，还是您扫我？", "Wǒ sǎo nín, háishì nín sǎo wǒ?", "Tôi quét mã của bạn, hay bạn quét mã tôi?"),
        ]
    },
    "food": {
        "title": "🍲 Ẩm Thực & Gọi Món Nhà Hàng",
        "description": "Cách gọi món chuẩn xác, dặn dò gia vị, thanh toán",
        "phrases": [
            ("服务员，请给我们一份菜单！", "Fúwùyuán, qǐng gěi wǒmen yí fèn càidān!", "Phục vụ ơi, cho chúng tôi xin một cuốn menu!"),
            ("你们这里的招牌菜是什么？", "Nǐmen zhèlǐ de zhāopái cài shì shénme?", "Món đặc sản/cháy hàng ở quán mình là gì?"),
            ("我不吃辣，请不要放辣椒！", "Wǒ bù chī là, qǐng bú yào fàng làjiāo!", "Tôi không ăn cay, xin đừng cho ớt!"),
            ("微辣就可以了。", "Wēilà jiù kěyǐ le.", "Cay nhẹ là được rồi ạ."),
            ("不要香菜，我吃不惯。", "Bú yào xiāngcài, wǒ chī bu guàn.", "Đừng cho rau mùi (ngò rí), tôi ăn không quen."),
            ("再来两碗米饭和一壶水。", "Zài lái liǎng wǎn mǐfàn hé yì hú shuǐ.", "Cho thêm 2 bát cơm và 1 ấm nước nữa nhé."),
            ("这个菜有点咸，能换一下吗？", "Zhè ge cài yǒudiǎn xián, néng huàn yíxià ma?", "Món này hơi mặn, đổi giúp tôi được không?"),
            ("吃不完，麻烦帮我打包！", "Chī bu wán, máfan bāng wǒ dǎbāo!", "Ăn không hết, phiền bạn đóng hộp mang về giúp tôi!"),
            ("服务员，买单！分开付还是一起付？", "Fúwùyuán, mǎidān! Fēnkāi fù háishì yìqǐ fù?", "Phục vụ ơi tính tiền! Trả riêng hay trả chung?"),
            ("今天我请客，谁都别跟我抢！", "Jīntiān wǒ qǐngkè, shéi dōu bié gēn wǒ qiǎng!", "Hôm nay tôi bao/mời, ai cũng đừng tranh trả tiền với tôi!"),
        ]
    },
    "travel": {
        "title": "✈️ Du Lịch, Khách Sạn & Di Chuyển",
        "description": "Hỏi đường, đi lại, đi máy bay, ở khách sạn",
        "phrases": [
            ("请问，地铁站怎么走？", "Qǐngwèn, dìtiězhàn zěnme zǒu?", "Xin hỏi, trạm tàu điện ngầm đi đường nào?"),
            ("一直往前走，在十字路口右转。", "Yìzhí wǎng qián zǒu, zài shízì lùkǒu yòuzhuǎn.", "Cứ đi thẳng phía trước, đến ngã tư thì rẽ phải."),
            ("这里离市中心有多远？", "Zhèlǐ lí shì zhōngxīn yǒu duō yuǎn?", "Chỗ này cách trung tâm thành phố bao xa?"),
            ("坐地铁需要换乘吗？", "Zuò dìtiě xūyào huànchéng ma?", "Đi tàu điện ngầm có cần đổi tuyến không?"),
            ("师傅，去这个地址，麻烦打表。", "Shīfu, qù zhè ge dìzhǐ, máfan dǎbiǎo.", "Bác tài ơi, đến địa chỉ này, phiền bác bấm đồng hồ cước."),
            ("我赶时间，能不能快一点？", "Wǒ gǎn shíjiān, néng bu néng kuài yìdiǎn?", "Tôi đang vội, có thể đi nhanh chút được không?"),
            ("我要办理退房，押金怎么退？", "Wǒ yào bànlǐ tuìfáng, yājīn zěnme tuì?", "Tôi muốn trả phòng (check-out), tiền cọc hoàn lại thế nào?"),
            ("可以帮我寄存一下行李吗？", "Kěyǐ bāng wǒ jìcún yíxià xíngli ma?", "Có thể giữ hộ hành lý giúp tôi một lát không?"),
            ("请问登机口在哪儿？", "Qǐngwèn dēngjīkǒu zài nǎr?", "Xin hỏi cửa lên máy bay ở đâu?"),
            ("祝你旅途愉快，一路平安！", "Zhù nǐ lǚtú yúkuài, yílù píng'ān!", "Chúc bạn chuyến đi vui vẻ, thượng lộ bình an!"),
        ]
    },
    "romance": {
        "title": "💬 Tình Cảm, Cảm Xúc & Khen Ngợi",
        "description": "Bày tỏ cảm xúc, khen ngợi và làm thân siêu ngọt ngào",
        "phrases": [
            ("你今天真好看！", "Nǐ jīntiān zhēn hǎokàn!", "Hôm nay bạn trông xinh/đẹp trai thật đấy!"),
            ("你笑起来真甜！", "Nǐ xiào qǐlái zhēn tián!", "Bạn cười lên nhìn ngọt ngào quá!"),
            ("我想你了。", "Wǒ xiǎng nǐ le.", "Tôi nhớ bạn rồi."),
            ("周末有空吗？一起看电影吧！", "Zhōumò yǒu kòng ma? Yìqǐ kàn diànyǐng ba!", "Cuối tuần rảnh không? Cùng đi xem phim nhé!"),
            ("跟你在一起，我特别开心。", "Gēn nǐ zài yìqǐ, wǒ tèbié kāixīn.", "Ở bên cạnh bạn, tôi cảm thấy vô cùng vui vẻ."),
            ("放心吧，有我在呢！", "Fàngxīn ba, yǒu wǒ zài ne!", "Yên tâm đi, có tôi ở đây rồi!"),
            ("别难过，一切都会好起来的。", "Bié nánguò, yíqiè dōu huì hǎo qǐlái de.", "Đừng buồn nữa, mọi chuyện rồi sẽ ổn thôi."),
            ("你真是太厉害了，佩服！", "Nǐ zhēn shì tài lìhai le, pèifú!", "Bạn thực sự quá đỉnh, khâm phục!"),
            ("我永远支持你！", "Wǒ yǒngyuǎn zhīchí nǐ!", "Tôi mãi luôn ủng hộ bạn!"),
            ("很高兴生命中有你。", "Hěn gāoxìng shēngmìng zhōng yǒu nǐ.", "Thật may mắn vì trong cuộc đời có bạn."),
        ]
    },
    "business": {
        "title": "💼 Công Sở, Phỏng Vấn & Kinh Doanh",
        "description": "Giao tiếp lịch thiệp trong công việc, đàm phán hợp đồng",
        "phrases": [
            ("请多关照！", "Qǐng duō guānzhào!", "Xin nhờ được giúp đỡ/chỉ giáo nhiều hơn!"),
            ("这是我的名片，请多指教。", "Zhè shì wǒ de míngpiàn, qǐng duō zhǐjiào.", "Đây là danh thiếp của tôi, xin được chỉ giáo."),
            ("我们几点开会？", "Wǒmen jǐ diǎn kāihuì?", "Mấy giờ chúng ta họp vậy?"),
            ("我已经把文件发到您的邮箱了。", "Wǒ yǐjīng bǎ wénjiàn fā dào nín de yóuxiāng le.", "Tôi đã gửi tài liệu vào email của bạn rồi."),
            ("关于这个项目，您有什么看法？", "Guānyú zhè ge xiàngmù, nín yǒu shénme kànfǎ?", "Về dự án này, bạn có quan điểm/góp ý gì không?"),
            ("合作愉快！", "Hézuò yúkuài!", "Hợp tác vui vẻ thành công!"),
            ("我们很期待与贵公司的长期合作。", "Wǒmen hěn qīdài yǔ guì gōngsī de chángqī hézuò.", "Chúng tôi rất mong đợi hợp tác lâu dài với quý công ty."),
            ("我会尽快处理这件事。", "Wǒ huì jǐnkuài chǔlǐ zhè jiàn shì.", "Tôi sẽ nhanh chóng xử lý việc này."),
            ("请问什么时候能出结果？", "Qǐngwèn shénme shíhou néng chū jiéguǒ?", "Xin hỏi khi nào có kết quả ạ?"),
            ("感谢您的宝贵时间！", "Gǎnxiè nín de bǎoguì shíjiān!", "Cảm ơn thời gian quý báu của bạn!"),
        ]
    },
    "slang": {
        "title": "🔥 Tiếng Lóng Giới Trẻ Trung Quốc (网络流行语)",
        "description": "Khẩu ngữ hiện đại trên Douyin, Weibo, Xiaohongshu mà giới trẻ hay dùng",
        "phrases": [
            ("躺平 (Tǎng píng)", "Tǎng píng", "Nằm yên / Buông xuôi không bon chen, sống an nhiên."),
            ("内卷 (Nèi juǎn)", "Nèi juǎn", "Cuốn vào cạnh tranh khốc liệt, đua đòi áp lực."),
            ("绝绝子！(Jué jué zi!)", "Jué jué zi!", "Đỉnh chóp! Hết nước chấm! Tuyệt đỉnh cú mèo!"),
            ("给力！(Gěi lì!)", "Gěi lì!", "Cháy quá! Đỉnh của chóp! Tuyệt vời ông mặt trời!"),
            ("666 (Liù liù liù)", "Liù liù liù", "Đỉnh quá, trâu bò quá! (Chữ 六 đồng âm với 溜 - trôi chảy, thuần thục)."),
            ("打工人 (Dǎgōng rén)", "Dǎgōng rén", "Người làm công ăn lương (cách tự trào phúng đáng yêu của dân văn phòng)."),
            ("破防了 (Pò fáng le)", "Pò fáng le", "Vỡ phòng thủ cảm xúc / Quá cảm động hoặc chạm đúng nỗi đau."),
            ("种草 (Zhòng cǎo)", "Zhòng cǎo", "Bị mê mẩn/được giới thiệu một món đồ muốn mua ngay."),
            ("拔草 (Bá cǎo)", "Bá cǎo", "Đã mua món đồ đó hoặc dập tắt ham muốn mua sau khi xem review chê."),
            ("剁手 (Duò shǒu)", "Duò shǒu", "Chặt tay (Nghiện shopping mua sắm quá đà đến mức muốn 'chặt tay' để thôi mua)."),
            ("吃瓜 (Chī guā)", "Chī guā", "Hóng drama, ngồi ăn dưa hóng biến mạng xã hội."),
            ("凡尔赛 (Fán'ěrsài)", "Fán'ěrsài", "Khoe khoang tinh tế (khoe của/khoe tài giả vờ như đang than vãn)."),
            ("YYDS (Yǒngyuǎn de shén)", "Yǒngyuǎn de shén", "Mãi mãi là vị thần / Đỉnh nhất mọi thời đại (GOAT)."),
        ]
    },
    "idioms": {
        "title": "📖 Thành Ngữ Thông Dụng Nhất (常用成语)",
        "description": "Những câu thành ngữ 4 chữ dùng trong giao tiếp khiến người Trung nể phục",
        "phrases": [
            ("半途而废 (Bàn tú ér fèi)", "Bàn tú ér fèi", "Bỏ cuộc giữa chừng, đứt gánh giữa đường."),
            ("入乡随俗 (Rù xiāng suí sú)", "Rù xiāng suí sú", "Nhập gia tùy tục (đến đâu thì theo phong tục ở đó)."),
            ("一石二鸟 (Yì shí èr niǎo)", "Yì shí èr niǎo", "Một mũi tên trúng hai đích (Một hòn đá bắn hai con chim)."),
            ("马到成功 (Mǎ dào chéng gōng)", "Mǎ dào chéng gōng", "Mã đáo thành công (Làm đâu thắng đó)."),
            ("水滴石穿 (Shuǐ dī shí chuān)", "Shuǐ dī shí chuān", "Nước chảy đá mòn (Kiên trì ắt có ngày thành công)."),
            ("心想事成 (Xīn xiǎng shì chéng)", "Xīn xiǎng shì chéng", "Vạn sự như ý, muốn gì được nấy."),
            ("莫名其妙 (Mò míng qí miào)", "Mò míng qí miào", "Kỳ quặc, khó hiểu, chẳng hiểu ra làm sao."),
            ("自以为是 (Zì yǐ wéi shì)", "Zì yǐ wéi shì", "Tự cho mình là đúng, kiêu ngạo bảo thủ."),
            ("津津有味 (Jīnjīn yǒu wèi)", "Jīnjīn yǒu wèi", "Say sưa thích thú, ăn uống ngon lành."),
            ("画蛇添足 (Huà shé tiān zú)", "Huà shé tiān zú", "Vẽ rắn thêm chân (Làm thừa thãi phản tác dụng)."),
        ]
    }
}
