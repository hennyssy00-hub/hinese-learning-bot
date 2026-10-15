# 🇨🇳 Bot Telegram Dạy Tiếng Trung

Bot Telegram giáo trình tiếng Trung từ **mất gốc** đến **HSK3**, đóng vai trò một thầy giáo dạy tiếng Trung toàn diện.

## ✨ Tính năng

### 📚 Lộ trình học 4 cấp độ
| Cấp độ | Nội dung | Từ vựng |
|--------|----------|---------|
| 🌱 Nhập môn | Thanh điệu, Pinyin, Số đếm, Chào hỏi | ~50 từ |
| 📗 HSK1 | Gia đình, Thời gian, Ăn uống, Mua sắm | 150 từ |
| 📘 HSK2 | Giao thông, Thời tiết, Sức khỏe, Nhà hàng | 300 từ |
| 📙 HSK3 | Công việc, Cảm xúc, Du lịch, Ngữ pháp nâng cao | 600 từ |

### 🎯 Các chức năng
- 📖 **Bài học chi tiết** - Từ vựng, ngữ pháp, viết chữ Hán
- 💬 **Luyện giao tiếp** - Hội thoại tương tác theo tình huống
- 🧠 **Bài quiz** - Kiểm tra kiến thức với giải thích chi tiết
- 🔤 **Flashcard từ vựng** - Ôn từ vựng nhanh
- 📊 **Theo dõi tiến độ** - Xem lại quá trình học tập
- 🗺 **Lộ trình rõ ràng** - Biết mình đang ở đâu, cần học gì

### 📝 Mỗi bài học bao gồm
- Chữ Hán (汉字)
- Phiên âm Pinyin (拼音)
- Nghĩa tiếng Việt
- Hội thoại mẫu
- Mẹo ghi nhớ

## 🚀 Cài đặt & Sử dụng

### Bước 1: Tạo Bot Telegram
1. Mở Telegram, tìm **@BotFather**
2. Gửi `/newbot`
3. Đặt tên bot (VD: `Học Tiếng Trung`)
4. Đặt username (VD: `hoc_tieng_trung_bot`)
5. Sao chép **TOKEN** mà BotFather gửi cho bạn

### Bước 2: Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### Bước 3: Cấu hình Token
**Cách 1:** Sửa file `config.json`:
```json
{
    "token": "YOUR_TOKEN_HERE"
}
```

**Cách 2:** Đặt biến môi trường:
```bash
set TELEGRAM_BOT_TOKEN=YOUR_TOKEN_HERE
```

### Bước 4: Chạy bot
```bash
python bot.py
```

## 📋 Các lệnh bot

| Lệnh | Chức năng |
|-------|-----------|
| `/start` | Bắt đầu, chọn trình độ |
| `/level` | Chọn lại trình độ |
| `/lessons` | Xem danh sách bài học |
| `/quiz` | Làm bài kiểm tra |
| `/practice` | Luyện giao tiếp |
| `/vocab` | Ôn từ vựng flashcard |
| `/progress` | Xem tiến độ học tập |
| `/roadmap` | Xem lộ trình chi tiết |
| `/help` | Hướng dẫn sử dụng |

## 📁 Cấu trúc project

```
chinese-learning-bot/
├── bot.py              # File chính của bot
├── lessons.py          # Dữ liệu bài học (4 cấp độ)
├── config.json         # Token bot Telegram
├── requirements.txt    # Dependencies
├── README.md           # Hướng dẫn
└── user_progress/      # Thư mục lưu tiến độ học viên
```
