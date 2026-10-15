"""
Module Đóng Vai Giao Tiếp (Roleplay Scenarios) - Đa Lượt & Thực Chiến
Giúp học viên luyện phản xạ giao tiếp tiếng Trung như người bản xứ.
"""

ROLEPLAY_SCENARIOS = {
    "boba": {
        "id": "boba",
        "title": "🥤 Tiệm Trà Sữa & Cà Phê (点奶茶)",
        "character": "小美 (Tiểu Mỹ - Nhân viên tiệm trà sữa)",
        "intro": (
            "🥤 <b>TÌNH HUỐNG: Mua Trà Sữa / Cà Phê</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "Bạn đang đứng trước quầy gọi món của tiệm trà sữa HEYTEA (喜茶).\n"
            "Nhân viên tươi cười chào đón bạn!\n"
            "Hãy đóng vai khách hàng và giao tiếp bằng tiếng Trung nhé.\n"
        ),
        "steps": [
            {
                "bot_text": (
                    "你好！欢迎光临喜茶！请问今天想喝点什么？\n"
                    "<i>(Nǐ hǎo! Huānyíng guānglín Xǐchá! Qǐngwèn jīntiān xiǎng hē diǎn shénme?)</i>\n\n"
                    "👉 <b>Nhiệm vụ:</b> Chào lại và gọi 1 ly trà sữa trân châu hoặc cà phê.\n"
                    "💡 <b>Gợi ý câu:</b>\n"
                    "• 我要一杯珍珠奶茶 (Wǒ yào yì bēi zhēnzhū nǎichá)\n"
                    "• 给我一杯拿铁咖啡 (Gěi wǒ yì bēi nátiě kāfēi)"
                ),
                "expected_keywords": ["奶茶", "咖啡", "珍珠", "一杯", "我要", "来一杯", "nǎichá", "kāfēi", "zhēnzhū", "yī bēi"],
                "praise": "太棒了！Gọi món rất chuẩn xác!",
                "feedback": "Nhân viên đã ghi nhận món nước của bạn.",
            },
            {
                "bot_text": (
                    "好的！请问要大杯还是中杯？甜度和冰块怎么选？\n"
                    "<i>(Hǎo de! Qǐngwèn yào dà bēi háishì zhōng bēi? Tiándù hé bīngkuài zěnme xuǎn?)</i>\n\n"
                    "👉 <b>Nhiệm vụ:</b> Chọn kích cỡ (Cốc to/vừa), độ ngọt (ít đường/không đường), độ đá (ít đá/không đá).\n"
                    "💡 <b>Từ vựng hữu ích:</b>\n"
                    "• 大杯 (dà bēi) = Cốc lớn | 中杯 (zhōng bēi) = Cốc vừa\n"
                    "• 微糖 / 少糖 (wēitáng / shǎotáng) = Ít đường\n"
                    "• 少冰 / 去冰 (shǎobīng / qùbīng) = Ít đá / Không đá\n"
                    "💡 <b>Mẫu câu:</b> 大杯，少糖，去冰。(Dà bēi, shǎotáng, qùbīng.)"
                ),
                "expected_keywords": ["大杯", "中杯", "少糖", "半糖", "微糖", "无糖", "少冰", "去冰", "正常", "dà bēi", "zhōng bēi", "bīng", "táng"],
                "praise": "专业！Bạn gọi đồ uống chuyên nghiệp như người bản địa luôn!",
                "feedback": "Nhân viên đã set đúng size, đường và đá cho bạn.",
            },
            {
                "bot_text": (
                    "好的，大杯少糖去冰，记下了！总共是22块钱。请问怎么支付？微信还是支付宝？\n"
                    "<i>(Hǎo de, dà bēi shǎotáng qùbīng, jì xià le! Zǒnggòng shì 22 kuài qián. Qǐngwèn zěnme zhīfù? Wēixìn háishì Zhīfùbǎo?)</i>\n\n"
                    "👉 <b>Nhiệm vụ:</b> Báo phương thức thanh toán (WeChat Pay, Alipay hoặc Tiền mặt) và bảo quét mã.\n"
                    "💡 <b>Gợi ý câu:</b>\n"
                    "• 微信支付，我扫你 (Wēixìn zhīfù, wǒ sǎo nǐ) = WeChat, tôi quét bạn\n"
                    "• 支付宝 (Zhīfùbǎo) = Alipay\n"
                    "• 我付现金 (Wǒ fù xiànjīn) = Tôi trả tiền mặt"
                ),
                "expected_keywords": ["微信", "支付宝", "现金", "扫", "刷卡", "wēixìn", "zhīfùbǎo", "xiànjīn"],
                "praise": "完美！(Wánměi! Hoàn hảo!)",
                "feedback": "Thanh toán thành công! Bạn nhận phiếu số và chờ lấy trà sữa.",
            },
        ],
        "completion_message": (
            "🎉 <b>HOÀN THÀNH KỊCH BẢN: Mua Trà Sữa</b>\n\n"
            "👏 Bạn đã xuất sắc hoàn thành cuộc đối thoại 3 lượt!\n"
            "🏆 +30 Điểm kinh nghiệm (XP) giao tiếp.\n"
            "💡 Giờ bạn hoàn toàn tự tin bước vào bất kỳ tiệm trà sữa nào ở Trung Quốc để order rồi đấy!"
        )
    },
    "market": {
        "id": "market",
        "title": "🛒 Chợ & Mặc Cả Mua Sắm (购物砍价)",
        "character": "老板娘 (Chủ tiệm Vương - Người bán hàng kỳ cựu)",
        "intro": (
            "🛒 <b>TÌNH HUỐNG: Mua Quần Áo & Trả Giá Ở Chợ</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "Bạn đang đi dạo chợ đêm tại Quảng Châu và ưng ý một chiếc áo khoác.\n"
            "Bà chủ tiệm nhanh nhẹn bước ra đon đả chào hàng!\n"
        ),
        "steps": [
            {
                "bot_text": (
                    "帅哥/美女，来看衣服啊！这件外套质量特别好，纯棉的！你穿肯定好看！\n"
                    "<i>(Shuàigē/Měinǚ, lái kàn yīfu a! Zhè jiàn wàitào zhìliàng tèbié hǎo, chúnmián de! Nǐ chuān kěndìng hǎokàn!)</i>\n\n"
                    "👉 <b>Nhiệm vụ:</b> Hỏi giá chiếc áo này bao nhiêu tiền.\n"
                    "💡 <b>Gợi ý câu:</b>\n"
                    "• 这件衣服多少钱？(Zhè jiàn yīfu duōshao qián?)\n"
                    "• 请问这个怎么卖？(Qǐngwèn zhè ge zěnme mài?)"
                ),
                "expected_keywords": ["多少钱", "怎么卖", "duōshao qián", "zěnme mài", "几块", "多少"],
                "praise": "很好！Hỏi giá rất tự nhiên!",
                "feedback": "Bà chủ đang chuẩn bị báo giá cho bạn.",
            },
            {
                "bot_text": (
                    "不贵不贵，看你诚心要，给你一口价：200块！\n"
                    "<i>(Bú guì bú guì, kàn nǐ chéngxīn yào, gěi nǐ yì kǒu jià: 200 kuài!)</i>\n\n"
                    "👉 <b>Nhiệm vụ:</b> Chê đắt và mặc cả (yêu cầu giảm giá / bớt tiền).\n"
                    "💡 <b>Mẫu câu mặc cả kinh điển:</b>\n"
                    "• 太贵了！便宜一点吧！(Tài guì le! Piányi yìdiǎn ba!)\n"
                    "• 100块卖不卖？(100 kuài mài bu mài?)\n"
                    "• 能打折吗？(Néng dǎzhé ma?)"
                ),
                "expected_keywords": ["太贵", "便宜", "打折", "tài guì", "piányi", "dǎzhé", "少一点", "贵"],
                "praise": "哈哈，太专业了！Biết chê đắt và đòi giảm giá chuẩn bài!",
                "feedback": "Bà chủ bắt đầu nhượng bộ bạn rồi đấy.",
            },
            {
                "bot_text": (
                    "哎呀，100块我亏本啦！这样吧，折中一下，120块卖给你，交个朋友！怎么样？\n"
                    "<i>(Āiyā, 100 kuài wǒ kuīběn la! Zhèyàng ba, zhézhōng yíxià, 120 kuài mài gěi nǐ, jiāo ge péngyou! Zěnmeyàng?)</i>\n\n"
                    "👉 <b>Nhiệm vụ:</b> Đồng ý mua, bảo gói lại và hỏi thanh toán.\n"
                    "💡 <b>Gợi ý câu:</b>\n"
                    "• 行，我要了，帮我包起来！(Xíng, wǒ yào le, bāng wǒ bāo qǐlái!)\n"
                    "• 好吧，可以扫微信吗？(Hǎo ba, kěyǐ sǎo Wēixìn ma?)"
                ),
                "expected_keywords": ["行", "好", "可以", "包起来", "我要", "买", "hǎo", "xíng", "wǒ yào"],
                "praise": "成交！(Chéngjiāo - Chốt đơn!)",
                "feedback": "Bạn đã mặc cả thành công từ 200 tệ xuống còn 120 tệ!",
            },
        ],
        "completion_message": (
            "🎉 <b>HOÀN THÀNH KỊCH BẢN: Trả Giá Chợ Đêm</b>\n\n"
            "👏 Bạn đã tiết kiệm được 80 tệ nhờ kỹ năng giao tiếp tiếng Trung đỉnh cao!\n"
            "🏆 +35 Điểm kinh nghiệm (XP) giao tiếp.\n"
            "💡 Bí quyết: Nhớ câu thần chú: <b>太贵了，便宜一点吧！(Tài guì le, piányi yìdiǎn ba!)</b>"
        )
    },
    "restaurant": {
        "id": "restaurant",
        "title": "🍜 Nhà Hàng & Gọi Món Lẩu (餐馆点菜)",
        "character": "服务员 (Phục vụ bàn A Bân)",
        "intro": (
            "🍜 <b>TÌNH HUỐNG: Đi Ăn Tại Nhà Hàng Trung Quốc</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "Bạn và bạn bè bước vào một nhà hàng món Tứ Xuyên thơm nức mũi.\n"
            "Nhân viên phục vụ nhanh chóng mang menu đến bàn.\n"
        ),
        "steps": [
            {
                "bot_text": (
                    "几位里面请！请问一共几位？先喝点茶，这是菜单。\n"
                    "<i>(Jǐ wèi lǐmiàn qǐng! Qǐngwèn yígòng jǐ wèi? Xiān hē diǎn chá, zhè shì càidān.)</i>\n\n"
                    "👉 <b>Nhiệm vụ:</b> Báo số lượng người (ví dụ: 2 người / 3 người) và xin giới thiệu món đặc sản.\n"
                    "💡 <b>Gợi ý câu:</b>\n"
                    "• 两位。你们有什么特色菜？(Liǎng wèi. Nǐmen yǒu shénme tèsè cài?)\n"
                    "• 我们三个人，有什么招牌菜吗？(Wǒmen sān ge rén, yǒu shénme zhāopái cài ma?)"
                ),
                "expected_keywords": ["位", "个", "特色菜", "招牌菜", "两位", "三位", "一个人", "tèsè", "zhāopái"],
                "praise": "很地道！Hỏi đúng từ khóa '招牌菜' (món đặc sản của quán)!",
                "feedback": "Phục vụ hào hứng giới thiệu món ăn cho bạn.",
            },
            {
                "bot_text": (
                    "我们店的麻婆豆腐和宫保鸡丁最有名！特别下饭！你们能吃辣吗？\n"
                    "<i>(Wǒmen diàn de Mápó dòufu hé Gōngbǎo jīdīng zuì yǒumíng! Tèbié xiàfàn! Nǐmen néng chī là ma?)</i>\n\n"
                    "👉 <b>Nhiệm vụ:</b> Báo mức độ ăn cay (không ăn cay / ít cay) và gọi 2 món đó kèm 2 bát cơm.\n"
                    "💡 <b>Gợi ý câu:</b>\n"
                    "• 我们不吃辣 / 微辣。来这两道菜，再来两碗米饭。(Wǒmen bù chī là / wēilà. Lái zhè liǎng dào cài, zài lái liǎng wǎn mǐfàn.)"
                ),
                "expected_keywords": ["辣", "米饭", "不吃辣", "微辣", "来", "要", "là", "mǐfàn", "wēilà", "bù chī là"],
                "praise": "很好！Dặn nhà bếp đúng độ cay khẩu vị!",
                "feedback": "Nhà bếp bắt đầu xào nấu các món ăn.",
            },
            {
                "bot_text": (
                    "菜上齐了，请慢用！如果还需要什么随时叫我！\n"
                    "<i>(Cài shàng qí le, qǐng màn yòng! Rúguǒ hái xūyào shénme suíshí jiào wǒ!)</i>\n\n"
                    "👉 <b>Nhiệm vụ:</b> Ăn xong, gọi phục vụ thanh toán tiền.\n"
                    "💡 <b>Gợi ý câu:</b>\n"
                    "• 服务员，买单！(Fúwùyuán, mǎidān!)\n"
                    "• 结账，请问多少钱？(Jiézhàng, qǐngwèn duōshao qián?)"
                ),
                "expected_keywords": ["买单", "结账", "多少钱", "mǎidān", "jiézhàng", "fúwùyuán", "服务员"],
                "praise": "非常好！Gọi tính tiền cực kỳ dứt khoát!",
                "feedback": "Nhân viên in hóa đơn và thanh toán cho bạn.",
            },
        ],
        "completion_message": (
            "🎉 <b>HOÀN THÀNH KỊCH BẢN: Gọi Món Nhà Hàng</b>\n\n"
            "👏 Bạn đã hoàn thành bữa ăn tuyệt vời bằng 100% tiếng Trung!\n"
            "🏆 +35 Điểm kinh nghiệm (XP).\n"
            "💡 Từ bỏ túi: <b>服务员，买单！(Fúwùyuán, mǎidān!)</b> - Phục vụ ơi, tính tiền!"
        )
    },
    "taxi": {
        "id": "taxi",
        "title": "🚖 Đi Taxi & Chỉ Đường (打车出行)",
        "character": "师傅 (Bác tài Trương - Tài xế taxi Bắc Kinh)",
        "intro": (
            "🚖 <b>TÌNH HUỐNG: Đi Taxi Đến Ga Tàu / Sân Bay</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "Bạn vừa bước lên một chiếc xe taxi tại trung tâm thành phố.\n"
            "Bác tài xế bấm đồng hồ và quay lại hỏi bạn.\n"
        ),
        "steps": [
            {
                "bot_text": (
                    "您好！请问去哪儿啊？\n"
                    "<i>(Nín hǎo! Qǐngwèn qù nǎr a?)</i>\n\n"
                    "👉 <b>Nhiệm vụ:</b> Nói điểm đến (ví dụ: đến sân bay, ga tàu, hoặc khách sạn) và bảo đi gấp.\n"
                    "💡 <b>Gợi ý câu:</b>\n"
                    "• 师傅，去首都机场，我有急事，请开快一点。(Shīfu, qù Shǒudū jīchǎng, wǒ yǒu jíshì, qǐng kāi kuài yìdiǎn.)\n"
                    "• 我去北京南站。(Wǒ qù Běijīng nánzhàn.)"
                ),
                "expected_keywords": ["师傅", "去", "机场", "车站", "酒店", "qù", "jīchǎng", "shīfu"],
                "praise": "很棒！Dùng từ '师傅' (Shīfu) xưng hô với bác tài rất chuẩn văn hóa Trung Hoa!",
                "feedback": "Bác tài gật đầu và bắt đầu cho xe lăn bánh.",
            },
            {
                "bot_text": (
                    "好嘞！前面路口有点堵车，咱们走高速还是走地面环路？走高速可能快20分钟。\n"
                    "<i>(Hǎo lei! Qiánmiàn lùkǒu yǒudiǎn dǔchē, zánmen zǒu gāosù háishì zǒu dìmiàn huánlù? Zǒu gāosù kěnéng kuài 20 fēnzhōng.)</i>\n\n"
                    "👉 <b>Nhiệm vụ:</b> Chọn đi đường cao tốc (走高速) để tiết kiệm thời gian.\n"
                    "💡 <b>Gợi ý câu:</b>\n"
                    "• 走高速吧，我不赶时间 / 我赶时间。(Zǒu gāosù ba, wǒ gǎn shíjiān.)"
                ),
                "expected_keywords": ["高速", "快", "走高速", "gāosù", "kuài"],
                "praise": "决断利落！Quyết định chuẩn xác giúp tránh tắc đường!",
                "feedback": "Xe rẽ vào làn cao tốc chạy băng băng.",
            },
            {
                "bot_text": (
                    "机场T3航站楼到了！打表一共58块，加上高速费10块，总共68块。\n"
                    "<i>(Jīchǎng T3 hángzhànlóu dào le! Dǎbiǎo yígòng 58 kuài, jiā shàng gāosù fèi 10 kuài, zǒnggòng 68 kuài.)</i>\n\n"
                    "👉 <b>Nhiệm vụ:</b> Xin hóa đơn (发票 - fāpiào) và cảm ơn bác tài.\n"
                    "💡 <b>Gợi ý câu:</b>\n"
                    "• 好的，给我一张发票，谢谢师傅！(Hǎo de, gěi wǒ yì zhāng fāpiào, xièxie shīfu!)\n"
                    "• 微信付了，谢谢！(Wēixìn fù le, xièxie!)"
                ),
                "expected_keywords": ["发票", "谢谢", "微信", "好了", "fāpiào", "xièxie", "fù"],
                "praise": "太厉害了！Đi taxi thành thạo không thua gì người bản địa!",
                "feedback": "Bác tài in hóa đơn, chúc bạn thượng lộ bình an.",
            },
        ],
        "completion_message": (
            "🎉 <b>HOÀN THÀNH KỊCH BẢN: Đi Taxi</b>\n\n"
            "👏 Bạn đã đến sân bay đúng giờ và an toàn!\n"
            "🏆 +35 Điểm kinh nghiệm (XP).\n"
            "💡 Nhớ xin hóa đơn: <b>请给我发票 (Qǐng gěi wǒ fāpiào)</b> nhé!"
        )
    },
    "hotel": {
        "id": "hotel",
        "title": "🏨 Khách Sạn & Nhận Phòng (酒店入住)",
        "character": "前台 (Tiểu Lâm - Lễ tân khách sạn 4 sao)",
        "intro": (
            "🏨 <b>TÌNH HUỐNG: Check-in Khách Sạn & Nhận Phòng</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "Bạn vừa đáp chuyến bay đến Thượng Hải và đến khách sạn nhận phòng.\n"
            "Lễ tân lịch sự cúi đầu chào đón bạn.\n"
        ),
        "steps": [
            {
                "bot_text": (
                    "您好，欢迎来到全季酒店！请问有什么可以帮您？\n"
                    "<i>(Nín hǎo, huānyíng lái dào Quánjì Jiǔdiàn! Qǐngwèn yǒu shénme kěyǐ bāng nín?)</i>\n\n"
                    "👉 <b>Nhiệm vụ:</b> Nói bạn muốn làm thủ tục nhận phòng (check-in) đã đặt trước trên mạng.\n"
                    "💡 <b>Gợi ý câu:</b>\n"
                    "• 我要办理入住，我在网上预订了房间。(Wǒ yào bànlǐ rùzhù, wǒ zài wǎngshang yùdìng le fángjiān.)\n"
                    "• 我预订了房间，我叫 [Tên bạn]。(Wǒ yùdìng le fángjiān, wǒ jiào...)"
                ),
                "expected_keywords": ["入住", "预订", "房间", "rùzhù", "yùdìng", "fángjiān", "订"],
                "praise": "很好！Dùng từ chuyên ngành '办理入住' (check-in) rất chuẩn xác!",
                "feedback": "Lễ tân đang tìm thông tin đặt phòng trên hệ thống.",
            },
            {
                "bot_text": (
                    "查到了，是大床房，一共住三晚。请出示一下您的护照，并交300块押金。\n"
                    "<i>(Chá dào le, shì dàchuáng fáng, yígòng zhù sān wǎn. Qǐng chūshì yíxià nín de hùzhào, bìng jiāo 300 kuài yājīn.)</i>\n\n"
                    "👉 <b>Nhiệm vụ:</b> Đưa hộ chiếu và nhờ sắp xếp phòng yên tĩnh tầng cao.\n"
                    "💡 <b>Gợi ý câu:</b>\n"
                    "• 这是我的护照。可以给我安排一个高楼层安静的房间吗？(Zhè shì wǒ de hùzhào. Kěyǐ gěi wǒ ānpái yí ge gāo lóucéng ānjìng de fángjiān ma?)"
                ),
                "expected_keywords": ["护照", "房间", "安静", "高", "hùzhào", "ānjìng", "gāo"],
                "praise": "太会提要求了！Yêu cầu phòng tầng cao yên tĩnh cực kỳ thực tế!",
                "feedback": "Lễ tân chọn ngay cho bạn phòng 1608 cực đẹp.",
            },
            {
                "bot_text": (
                    "好的，已经为您安排了16楼的无烟静音房！这是您的房卡。早餐在二楼，早上7点到10点。请问还需要什么帮助吗？\n"
                    "<i>(Hǎo de, yǐjīng wèi nín ānpái le 16 lóu de wúyān jìngyīn fáng! Zhè shì nín de fángkǎ. Zǎocān zài èr lóu, zǎoshang 7 diǎn dào 10 diǎn. Qǐngwèn hái xūyào shénme bāngzhù ma?)</i>\n\n"
                    "👉 <b>Nhiệm vụ:</b> Hỏi mật khẩu Wifi và cảm ơn.\n"
                    "💡 <b>Gợi ý câu:</b>\n"
                    "• 请问房间WiFi密码是多少？谢谢！(Qǐngwèn fángjiān WiFi mìmǎ shì duōshao? Xièxie!)"
                ),
                "expected_keywords": ["wifi", "密码", "谢谢", "mìmǎ", "xièxie", "无线网"],
                "praise": "完美！(Wánměi!)",
                "feedback": "Lễ tân báo wifi không cần mật khẩu, chỉ cần nhập số phòng.",
            },
        ],
        "completion_message": (
            "🎉 <b>HOÀN THÀNH KỊCH BẢN: Check-in Khách Sạn</b>\n\n"
            "👏 Bạn đã nhận phòng 1608 view ngắm trọn thành phố!\n"
            "🏆 +40 Điểm kinh nghiệm (XP).\n"
            "💡 Ghi nhớ từ khóa: <b>办理入住 (check-in) | 押金 (tiền đặt cọc) | 房卡 (thẻ phòng)</b>."
        )
    },
    "friendship": {
        "id": "friendship",
        "title": "🤝 Kết Bạn & Trò Chuyện Thường Ngày (日常闲聊)",
        "character": "小华 (Tiểu Hoa - Du học sinh Bắc Kinh thân thiện)",
        "intro": (
            "🤝 <b>TÌNH HUỐNG: Làm Quen Bạn Mới Người Trung Quốc</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "Bạn đang ngồi đọc sách ở quán cà phê thì một bạn người Trung Quốc ngồi cạnh bắt chuyện.\n"
            "Cơ hội vàng để luyện giao tiếp tự nhiên đây rồi!\n"
        ),
        "steps": [
            {
                "bot_text": (
                    "哈喽！你在看中文书啊？你的中文学了多久了？感觉你很有语言天赋！\n"
                    "<i>(Hālóu! Nǐ zài kàn Zhōngwén shū a? Nǐ de Zhōngwén xué le duōjiǔ le? Gǎnjué nǐ hěn yǒu yǔyán tiānfù!)</i>\n\n"
                    "👉 <b>Nhiệm vụ:</b> Cảm ơn và trả lời bạn học tiếng Trung được bao lâu rồi (ví dụ: vài tháng / 1 năm).\n"
                    "💡 <b>Gợi ý câu:</b>\n"
                    "• 哪里哪里，我学了三个月。(Nǎlǐ nǎlǐ, wǒ xué le sān ge yuè.)\n"
                    "• 谢谢夸奖！我刚学不久。(Xièxie kuājiǎng! Wǒ gāng xué bù jiǔ.)"
                ),
                "expected_keywords": ["月", "年", "天", "学", "谢谢", "哪里", "xué", "xièxie", "nǎlǐ", "yuè", "nián"],
                "praise": "谦虚有礼！Đáp lại bằng '哪里哪里' thể hiện đức tính khiêm tốn rất chuẩn phong cách Trung Hoa!",
                "feedback": "Tiểu Hoa rất ấn tượng với khả năng tiếng Trung của bạn.",
            },
            {
                "bot_text": (
                    "发音很标准呢！你平时有什么兴趣爱好？周末一般喜欢做什么？\n"
                    "<i>(Fāyīn hěn biāozhǔn ne! Nǐ píngshí yǒu shénme xìngqù àihào? Zhōumò yìbān xǐhuan zuò shénme?)</i>\n\n"
                    "👉 <b>Nhiệm vụ:</b> Chia sẻ sở thích của bạn (nghe nhạc, xem phim, du lịch, đá bóng, nấu ăn...).\n"
                    "💡 <b>Gợi ý câu:</b>\n"
                    "• 我喜欢听音乐和看中国电影。(Wǒ xǐhuan tīng yīnyuè hé kàn Zhōngguó diànyǐng.)\n"
                    "• 我喜欢旅游和吃美食。(Wǒ xǐhuan lǚyóu hé chī měishí.)"
                ),
                "expected_keywords": ["喜欢", "听音乐", "看电影", "旅游", "看书", "运动", "xǐhuan", "yīnyuè", "diànyǐng", "lǚyóu"],
                "praise": "分享得很棒！Nói về sở thích rất lưu loát!",
                "feedback": "Tiểu Hoa phát hiện hai người có rất nhiều sở thích chung.",
            },
            {
                "bot_text": (
                    "太巧了，我也特别喜欢！我们要不加个微信吧？以后可以一起练习中文，我还能带你吃地道中国菜！\n"
                    "<i>(Tài qiǎo le, wǒ yě tèbié xǐhuan! Wǒmen yàobù jiā ge Wēixìn ba? Yǐhòu kěyǐ yìqǐ liànxí Zhōngwén, wǒ hái néng dài nǐ chī dìdao Zhōngguó cài!)</i>\n\n"
                    "👉 <b>Nhiệm vụ:</b> Đồng ý kết bạn WeChat, mở mã QR cho bạn ấy quét.\n"
                    "💡 <b>Gợi ý câu:</b>\n"
                    "• 太好了！这是我的二维码，你扫我吧！(Tài hǎo le! Zhè shì wǒ de èrwéimǎ, nǐ sǎo wǒ ba!)\n"
                    "• 好啊，很高兴认识你！(Hǎo a, hěn gāoxìng rènshi nǐ!)"
                ),
                "expected_keywords": ["好", "微信", "扫", "二维码", "认识你", "hǎo", "sǎo", "wēixìn", "rènshi"],
                "praise": "恭喜！Kết thêm một người bạn bản xứ tuyệt vời!",
                "feedback": "Ting ting! Bạn và Tiểu Hoa đã là bạn bè trên WeChat.",
            },
        ],
        "completion_message": (
            "🎉 <b>HOÀN THÀNH KỊCH BẢN: Kết Bạn Giao Tiếp</b>\n\n"
            "👏 Bạn đã tự tin kết bạn và trò chuyện như người bản xứ!\n"
            "🏆 +40 Điểm kinh nghiệm (XP).\n"
            "💡 Câu thần chú giao lưu: <b>加个微信吧 (Jiā ge Wēixìn ba - Cho mình xin WeChat nhé!)</b>"
        )
    }
}
