"""
🇨🇳 Bot Telegram Dạy Tiếng Trung Chuyên Nghiệp - Phiên Bản PRO MAX
Tác giả: AI Chinese Master Tutor
Chức năng:
- Giáo trình HSK0 - HSK3 bài bản
- Đóng vai giao tiếp đa lượt (Multi-turn Roleplay) thực tế
- Thầy giáo AI kèm riêng 1-1 (Sửa lỗi, giải nghĩa, luyện phản xạ)
- Mục Dịch Thuật Song Ngữ Khẩu Ngữ Đời Thường (Việt ➔ Trung kèm Pinyin & Trung ➔ Việt)
- Kho 200+ câu giao tiếp vàng & Tiếng lóng giới trẻ Trung Quốc
- Sổ tay ngữ pháp trọng điểm (把, 被, 了, 过, 会/能/可以...)
- Hệ thống tính điểm kinh nghiệm (XP) & Danh hiệu cao thủ
"""

import os
import sys
import json
import html
import random
import logging
import asyncio
from pathlib import Path

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.error import BadRequest
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

from lessons import CURRICULUM, QUIZZES, LEVEL_NAMES
from roleplay import ROLEPLAY_SCENARIOS
from phrasebook import PHRASE_CATEGORIES
from grammar_guide import GRAMMAR_POINTS
from ai_tutor import get_tutor_response, get_gemini_api_key, set_gemini_api_key, validate_gemini_key
from translator import translate_text
from keep_alive import keep_alive

# ============================================================
# LOGGING
# ============================================================
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ============================================================
# PROGRESS & XP TRACKING
# ============================================================
PROGRESS_DIR = Path("user_progress")
PROGRESS_DIR.mkdir(exist_ok=True)


def get_user_progress(user_id: int) -> dict:
    """Load user progress and XP from file."""
    filepath = PROGRESS_DIR / f"{user_id}.json"
    if filepath.exists():
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                if "xp" not in data:
                    data["xp"] = 0
                return data
        except Exception:
            pass
    return {
        "current_level": None,
        "completed_lessons": [],
        "quiz_scores": {},
        "total_lessons_done": 0,
        "streak_days": 1,
        "xp": 0,
    }


def save_user_progress(user_id: int, progress: dict):
    """Save user progress to file."""
    filepath = PROGRESS_DIR / f"{user_id}.json"
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)


def add_xp(user_id: int, amount: int) -> int:
    """Add XP to user and return new XP."""
    prog = get_user_progress(user_id)
    prog["xp"] = prog.get("xp", 0) + amount
    save_user_progress(user_id, prog)
    return prog["xp"]


def get_user_rank(xp: int) -> str:
    """Get pedagogical title based on XP."""
    if xp < 50:
        return "🌱 Tân Binh Tiếng Trung"
    elif xp < 150:
        return "🥉 Sơ Cấp (HSK1)"
    elif xp < 300:
        return "🥈 Trung Cấp (HSK2)"
    elif xp < 600:
        return "🥇 Cao Thủ Giao Tiếp (HSK3)"
    else:
        return "👑 Bậc Thầy Trung Hoa PRO MAX"


# ============================================================
# COMMAND HANDLERS
# ============================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command - Master Welcome Hub."""
    user = update.effective_user
    prog = get_user_progress(user.id)
    rank = get_user_rank(prog.get("xp", 0))

    welcome_text = (
        f"🇨🇳 <b>XIN CHÀO {user.first_name}! 你好！</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "Chào mừng bạn đến với <b>AI CHINESE MASTER BOT PRO MAX</b> 🧑‍🏫\n"
        "Hệ thống chuyên gia đồng hành giúp bạn chinh phục tiếng Trung từ mất gốc đến giao tiếp bản xứ!\n\n"
        f"🎖️ <b>Cấp bậc hiện tại:</b> {rank} ({prog.get('xp', 0)} XP)\n\n"
        "🌟 <b>TÍNH NĂNG CHUYÊN GIA NỔI BẬT:</b>\n"
        "• 🌐 <b>Dịch Song Ngữ Khẩu Ngữ:</b> Việt ➔ Trung kèm Pinyin & Trung ➔ Việt đời thường\n"
        "• 🗣️ <b>Chat 1-1 với Thầy Lý AI:</b> Chữa lỗi, dịch câu, đàm thoại tự nhiên\n"
        "• 🎭 <b>Đóng vai giao tiếp (Roleplay):</b> Trà sữa, mặc cả, nhà hàng, taxi, khách sạn...\n"
        "• 💬 <b>Kho câu giao tiếp vàng:</b> 200+ câu thực chiến theo 8 chủ đề\n"
        "• 🔥 <b>Tiếng lóng Hot Trend:</b> YYDS, 绝绝子, 躺平, 666...\n"
        "• 📝 <b>Sổ tay ngữ pháp:</b> Câu chữ 把, 被, trợ từ 了, 过, bổ ngữ\n"
        "• 📚 <b>Lộ trình HSK0 - HSK3:</b> Bài học chuẩn khung khảo thí quốc tế\n\n"
        "👇 <b>Chọn nhanh một tính năng để bắt đầu:</b>"
    )

    keyboard = [
        [
            InlineKeyboardButton("🌐 Dịch Thuật Khẩu Ngữ", callback_data="toggle_translate_mode"),
            InlineKeyboardButton("🗣️ Chat 1-1 Thầy AI", callback_data="toggle_chat_mode"),
        ],
        [
            InlineKeyboardButton("🎭 Đóng vai giao tiếp", callback_data="show_roleplay_menu"),
            InlineKeyboardButton("💬 Kho câu giao tiếp", callback_data="phrases_main"),
        ],
        [
            InlineKeyboardButton("🔥 Tiếng lóng giới trẻ", callback_data="phrase_cat_slang"),
            InlineKeyboardButton("📝 Sổ tay ngữ pháp", callback_data="grammar_main"),
        ],
        [
            InlineKeyboardButton("📚 Bài học HSK (0-3)", callback_data="back_to_levels"),
            InlineKeyboardButton("🔤 Flashcard từ vựng", callback_data="vocab_next"),
        ],
        [
            InlineKeyboardButton("📊 Bảng vàng thành tích", callback_data="show_profile_cb"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode="HTML")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command."""
    help_text = (
        "📖 <b>DANH SÁCH LỆNH PRO MAX:</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🔹 /start - Bảng điều khiển trung tâm\n"
        "🔹 /dich hoặc /translate - Dịch thuật song ngữ khẩu ngữ đời thường (kèm Pinyin)\n"
        "🔹 /chat hoặc /tutor - Bật/tắt chế độ Chat 1-1 cùng Thầy giáo AI\n"
        "🔹 /roleplay - Đóng vai giao tiếp thực tế (mua trà sữa, mặc cả, gọi món...)\n"
        "🔹 /phrases - Kho câu giao tiếp thực chiến theo chủ đề\n"
        "🔹 /slang - Tiếng lóng giới trẻ Trung Quốc HOT TREND\n"
        "🔹 /grammar - Sổ tay ngữ pháp trọng điểm (把, 被, 了...)\n"
        "🔹 /level - Chọn trình độ bài học (Mất gốc → HSK3)\n"
        "🔹 /lessons - Danh sách bài học theo trình độ\n"
        "🔹 /quiz - Trắc nghiệm kiểm tra kiến thức\n"
        "🔹 /vocab - Ôn tập nhanh từ vựng Flashcard\n"
        "🔹 /progress hoặc /profile - Xem điểm XP, cấp bậc và tiến độ học\n"
        "🔹 /roadmap - Xem bản đồ lộ trình chi tiết\n"
        "🔹 /setkey &lt;key&gt; - Kích hoạt Gemini AI Key miễn phí từ Google\n"
        "🔹 /keyinfo - Kiểm tra trạng thái AI của bot\n\n"
        "💡 <b>MẸO DỊCH NHANH:</b> Bạn có thể gõ ngay <code>/dich hôm nay bạn muốn ăn gì</code> để nhận bản dịch tiếng Trung kèm Pinyin lập tức!"
    )
    await update.message.reply_text(help_text, parse_mode="HTML")


# ============================================================
# TRANSLATION HUB (Văn phong khẩu ngữ đời thường)
# ============================================================

async def translate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /dich or /translate command."""
    # Check if user passed arguments: /dich <text>
    if context.args:
        user_query = " ".join(context.args)
        await update.message.chat.send_action("typing")
        result = await translate_text(user_query)
        keyboard = [[InlineKeyboardButton("🌐 Dịch tiếp câu khác", callback_data="toggle_translate_mode")]]
        await update.message.reply_text(result, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")
        return

    # Enable translation mode
    context.user_data["translate_mode"] = True
    context.user_data["chat_mode"] = False
    context.user_data["active_roleplay"] = None

    text = (
        "🌐 <b>MỤC DỊCH THUẬT SONG NGỮ KHẨU NGỮ ĐỜI THƯỜNG</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎯 <b>Đặc điểm chuyên biệt:</b>\n"
        "• Dịch theo giọng văn nói chuyện hàng ngày, tự nhiên, gần gũi.\n"
        "• Không dùng từ chuyên ngành khó hiểu hay văn viết khô khan.\n"
        "• 🇻🇳 ➔ 🇨🇳 Nhập tiếng Việt: Dịch ra tiếng Trung khẩu ngữ kèm <b>Pinyin chuẩn có dấu</b>.\n"
        "• 🇨🇳 ➔ 🇻🇳 Nhập tiếng Trung: Dịch ra tiếng Việt tự nhiên, dễ hiểu.\n\n"
        "👉 <b>Hãy gửi câu bạn muốn dịch vào đây ngay nhé!</b>\n\n"
        "💡 <i>Gõ /stopdich để tắt chế độ dịch bất cứ lúc nào.</i>"
    )
    keyboard = [[InlineKeyboardButton("🛑 Dừng dịch thuật", callback_data="stop_translate_mode")]]
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")


async def stop_translate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Stop translation mode."""
    context.user_data["translate_mode"] = False
    await update.message.reply_text(
        "✅ Đã dừng chế độ Dịch thuật. Bạn có thể sử dụng các tính năng khác trên menu chính bất cứ lúc nào!",
        parse_mode="HTML"
    )


# ============================================================
# CHAT 1-1 AI TUTOR MODE
# ============================================================

async def chat_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Enable 1-1 AI Tutor mode."""
    context.user_data["chat_mode"] = True
    context.user_data["translate_mode"] = False
    context.user_data["active_roleplay"] = None

    text = (
        "🧑‍🏫 <b>CHẾ ĐỘ CHAT 1-1 VỚI THẦY LÝ ĐÃ BẬT!</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "Chào em! Từ bây giờ, bất kỳ tin nhắn nào em gửi, Thầy Lý sẽ trực tiếp:\n"
        "✅ Kiểm tra ngữ pháp & sửa lỗi dùng từ\n"
        "✅ Phiên âm Pinyin chuẩn có thanh điệu\n"
        "✅ Dịch nghĩa tiếng Việt chi tiết\n"
        "✅ Gợi ý cách nói tự nhiên như người bản xứ\n"
        "✅ Đặt câu hỏi phản xạ đối đáp cùng em!\n\n"
        "👉 <i>Hãy nhắn cho thầy một câu tiếng Trung (hoặc hỏi nghĩa câu nào đó) ngay nhé!</i>\n\n"
        "💡 <i>Gõ /stopchat để thoát chế độ chat bất cứ lúc nào.</i>"
    )
    keyboard = [[InlineKeyboardButton("🛑 Dừng Chat 1-1", callback_data="stop_chat_mode")]]
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")


async def stopchat_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Disable 1-1 AI Tutor mode."""
    context.user_data["chat_mode"] = False
    await update.message.reply_text(
        "✅ Đã dừng chế độ Chat 1-1. Bạn có thể sử dụng các lệnh khác như /roleplay, /lessons hoặc /phrases để tiếp tục học tập nhé!",
        parse_mode="HTML"
    )


# ============================================================
# ROLEPLAY SYSTEM (Multi-turn)
# ============================================================

async def roleplay_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /roleplay command."""
    text = (
        "🎭 <b>ĐÓNG VAI GIAO TIẾP THỰC CHIẾN (ROLEPLAY PRO)</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "Lựa chọn tình huống thực tế để đối thoại trực tiếp cùng nhân vật ảo:\n"
    )
    keyboard = []
    for sc_id, sc in ROLEPLAY_SCENARIOS.items():
        keyboard.append([InlineKeyboardButton(sc["title"], callback_data=f"rp_start_{sc_id}")])
    keyboard.append([InlineKeyboardButton("🔙 Menu chính", callback_data="back_to_main")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.callback_query:
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup, parse_mode="HTML")
    else:
        await update.message.reply_text(text, reply_markup=reply_markup, parse_mode="HTML")


async def handle_roleplay_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start a selected roleplay scenario."""
    query = update.callback_query
    await query.answer()

    scenario_id = query.data.replace("rp_start_", "")
    scenario = ROLEPLAY_SCENARIOS.get(scenario_id)
    if not scenario:
        return

    # Set active roleplay state
    context.user_data["active_roleplay"] = {
        "scenario_id": scenario_id,
        "step": 0
    }
    context.user_data["chat_mode"] = False
    context.user_data["translate_mode"] = False

    first_step = scenario["steps"][0]
    text = (
        f"{scenario['intro']}\n"
        f"👤 <b>Nhân vật:</b> {scenario['character']}\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        f"{first_step['bot_text']}"
    )

    keyboard = [[InlineKeyboardButton("🛑 Thoát kịch bản", callback_data="rp_exit")]]
    await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")


async def handle_roleplay_user_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle user response in active roleplay."""
    rp_state = context.user_data.get("active_roleplay")
    if not rp_state:
        return

    scenario_id = rp_state["scenario_id"]
    current_step_idx = rp_state["step"]
    scenario = ROLEPLAY_SCENARIOS.get(scenario_id)
    if not scenario:
        return

    user_text = update.message.text
    step = scenario["steps"][current_step_idx]

    matched = any(kw.lower() in user_text.lower() for kw in step["expected_keywords"])
    has_hanzi = any('\u4e00' <= c <= '\u9fff' for c in user_text)

    next_step_idx = current_step_idx + 1

    if next_step_idx < len(scenario["steps"]):
        rp_state["step"] = next_step_idx
        context.user_data["active_roleplay"] = rp_state

        next_step = scenario["steps"][next_step_idx]
        feedback_praise = step["praise"] if (matched or has_hanzi) else "很好！Bạn đã phản hồi và tiếp tục cuộc trò chuyện!"

        text = (
            f"✅ <b>{feedback_praise}</b>\n"
            f"<i>{step['feedback']}</i>\n\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"👤 <b>{scenario['character']} tiếp lời:</b>\n\n"
            f"{next_step['bot_text']}"
        )
        keyboard = [[InlineKeyboardButton("🛑 Thoát kịch bản", callback_data="rp_exit")]]
        await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")
    else:
        context.user_data["active_roleplay"] = None
        new_xp = add_xp(update.effective_user.id, 35)

        text = (
            f"✅ <b>{step['praise']}</b>\n\n"
            f"{scenario['completion_message']}\n\n"
            f"🎖️ <b>Tổng XP của bạn hiện tại:</b> {new_xp} XP"
        )
        keyboard = [
            [InlineKeyboardButton("🎭 Chọn kịch bản khác", callback_data="show_roleplay_menu")],
            [InlineKeyboardButton("🔙 Về Menu chính", callback_data="back_to_main")],
        ]
        await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")


# ============================================================
# PHRASEBOOK SYSTEM
# ============================================================

async def phrases_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /phrases command."""
    text = (
        "💬 <b>KHO CÂU GIAO TIẾP THỰC CHIẾN ĐỈNH CAO</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "Chọn một danh mục để xem các mẫu câu thông dụng nhất:\n"
    )
    keyboard = []
    for cat_id, cat in PHRASE_CATEGORIES.items():
        keyboard.append([InlineKeyboardButton(cat["title"], callback_data=f"phrase_cat_{cat_id}")])
    keyboard.append([InlineKeyboardButton("🔙 Menu chính", callback_data="back_to_main")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.callback_query:
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup, parse_mode="HTML")
    else:
        await update.message.reply_text(text, reply_markup=reply_markup, parse_mode="HTML")


async def handle_phrase_category(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Display phrases in a selected category."""
    query = update.callback_query
    await query.answer()

    cat_id = query.data.replace("phrase_cat_", "")
    cat = PHRASE_CATEGORIES.get(cat_id)
    if not cat:
        return

    text = (
        f"<b>{cat['title']}</b>\n"
        f"<i>{cat['description']}</i>\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
    )

    for i, (zh, py, vi) in enumerate(cat["phrases"], 1):
        text += f"<b>{i}. {zh}</b>\n"
        text += f"   <i>Pinyin:</i> {py}\n"
        text += f"   <i>Nghĩa:</i> {vi}\n\n"

    keyboard = [
        [InlineKeyboardButton("🔄 Xem chủ đề khác", callback_data="phrases_main")],
        [InlineKeyboardButton("🔙 Menu chính", callback_data="back_to_main")],
    ]
    await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")


# ============================================================
# GRAMMAR GUIDE SYSTEM
# ============================================================

async def grammar_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /grammar command."""
    text = (
        "📝 <b>SỔ TAY NGỮ PHÁP TIẾNG TRUNG TRỌNG ĐIỂM</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "Chọn điểm ngữ pháp bạn muốn tìm hiểu cặn kẽ:\n"
    )
    keyboard = []
    for g_id, g_item in GRAMMAR_POINTS.items():
        keyboard.append([InlineKeyboardButton(g_item["title"], callback_data=f"grammar_view_{g_id}")])
    keyboard.append([InlineKeyboardButton("🔙 Menu chính", callback_data="back_to_main")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.callback_query:
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup, parse_mode="HTML")
    else:
        await update.message.reply_text(text, reply_markup=reply_markup, parse_mode="HTML")


async def handle_grammar_view(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show details of a grammar point."""
    query = update.callback_query
    await query.answer()

    g_id = query.data.replace("grammar_view_", "")
    g_item = GRAMMAR_POINTS.get(g_id)
    if not g_item:
        return

    keyboard = [
        [InlineKeyboardButton("📖 Điểm ngữ pháp khác", callback_data="grammar_main")],
        [InlineKeyboardButton("🔙 Menu chính", callback_data="back_to_main")],
    ]
    await query.edit_message_text(g_item["content"], reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")


# ============================================================
# LEVEL & LESSON SELECTION
# ============================================================

async def select_level(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /level command - Choose learning level."""
    keyboard = [
        [InlineKeyboardButton("🌱 Nhập môn (Mất gốc)", callback_data="select_level_0")],
        [InlineKeyboardButton("📗 HSK1 - Cơ bản", callback_data="select_level_1")],
        [InlineKeyboardButton("📘 HSK2 - Sơ trung cấp", callback_data="select_level_2")],
        [InlineKeyboardButton("📙 HSK3 - Trung cấp", callback_data="select_level_3")],
        [InlineKeyboardButton("🔙 Menu chính", callback_data="back_to_main")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    msg = "📚 <b>Chọn trình độ bạn muốn học:</b>"
    if update.callback_query:
        await update.callback_query.edit_message_text(msg, reply_markup=reply_markup, parse_mode="HTML")
    else:
        await update.message.reply_text(msg, reply_markup=reply_markup, parse_mode="HTML")


async def handle_level_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle level selection callback."""
    query = update.callback_query
    await query.answer()

    level_key = query.data.replace("select_", "")
    user_id = query.from_user.id

    progress = get_user_progress(user_id)
    progress["current_level"] = level_key
    save_user_progress(user_id, progress)

    level_data = CURRICULUM[level_key]

    text = (
        f"✅ <b>Bạn đã chọn: {level_data['name']}</b>\n\n"
        f"📋 {level_data['description']}\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "📚 <b>Danh sách bài học:</b>\n\n"
    )

    keyboard = []
    for i, lesson_key in enumerate(level_data["lesson_order"], 1):
        lesson = level_data["lessons"][lesson_key]
        completed = f"{level_key}_{lesson_key}" in progress.get("completed_lessons", [])
        status = "✅" if completed else f"{i}."
        text += f"{status} {lesson['title']}\n"
        keyboard.append([
            InlineKeyboardButton(
                f"{status} {lesson['title']}",
                callback_data=f"lesson_{level_key}_{lesson_key}"
            )
        ])

    keyboard.append([InlineKeyboardButton("🧠 Làm bài Quiz", callback_data=f"quiz_{level_key}")])
    keyboard.append([InlineKeyboardButton("🔙 Chọn lại trình độ", callback_data="back_to_levels")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode="HTML")


async def show_lessons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /lessons command."""
    user_id = update.effective_user.id
    progress = get_user_progress(user_id)
    level_key = progress.get("current_level")

    if not level_key:
        await select_level(update, context)
        return

    level_data = CURRICULUM[level_key]
    text = (
        f"📚 <b>Bài học - {level_data['name']}</b>\n\n"
        "Chọn bài bạn muốn học:\n\n"
    )

    keyboard = []
    for i, lesson_key in enumerate(level_data["lesson_order"], 1):
        lesson = level_data["lessons"][lesson_key]
        completed = f"{level_key}_{lesson_key}" in progress.get("completed_lessons", [])
        status = "✅" if completed else f"{i}."
        text += f"{status} {lesson['title']}\n"
        keyboard.append([
            InlineKeyboardButton(
                f"{status} {lesson['title']}",
                callback_data=f"lesson_{level_key}_{lesson_key}"
            )
        ])

    keyboard.append([InlineKeyboardButton("🧠 Làm Quiz kiểm tra", callback_data=f"quiz_{level_key}")])
    keyboard.append([InlineKeyboardButton("🔄 Đổi trình độ", callback_data="back_to_levels")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, reply_markup=reply_markup, parse_mode="HTML")


async def handle_lesson(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Display lesson content."""
    query = update.callback_query
    await query.answer()

    parts = query.data.split("_")
    level_key = f"{parts[1]}_{parts[2]}"
    lesson_key = "_".join(parts[3:])

    level_data = CURRICULUM.get(level_key)
    if not level_data:
        return

    lesson = level_data["lessons"].get(lesson_key)
    if not lesson:
        return

    user_id = query.from_user.id
    progress = get_user_progress(user_id)
    lesson_tag = f"{level_key}_{lesson_key}"

    if lesson_tag not in progress.get("completed_lessons", []):
        if "completed_lessons" not in progress:
            progress["completed_lessons"] = []
        progress["completed_lessons"].append(lesson_tag)
        progress["total_lessons_done"] = len(progress["completed_lessons"])
        progress["xp"] = progress.get("xp", 0) + 15
        save_user_progress(user_id, progress)

    lesson_order = level_data["lesson_order"]
    curr_idx = lesson_order.index(lesson_key) if lesson_key in lesson_order else -1

    keyboard = []
    nav_row = []
    if curr_idx > 0:
        prev_key = lesson_order[curr_idx - 1]
        nav_row.append(InlineKeyboardButton("⬅️ Bài trước", callback_data=f"lesson_{level_key}_{prev_key}"))
    if curr_idx < len(lesson_order) - 1:
        next_key = lesson_order[curr_idx + 1]
        nav_row.append(InlineKeyboardButton("Bài sau ➡️", callback_data=f"lesson_{level_key}_{next_key}"))
    if nav_row:
        keyboard.append(nav_row)

    keyboard.append([InlineKeyboardButton("📋 Danh sách bài học", callback_data=f"select_{level_key}")])
    keyboard.append([InlineKeyboardButton("🧠 Làm Quiz trình độ này", callback_data=f"quiz_{level_key}")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(lesson["content"], reply_markup=reply_markup, parse_mode="HTML")


# ============================================================
# QUIZ SYSTEM
# ============================================================

async def start_quiz_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /quiz command."""
    user_id = update.effective_user.id
    progress = get_user_progress(user_id)
    level_key = progress.get("current_level", "level_0")
    await run_quiz(update.message, context, level_key)


async def handle_quiz_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle quiz start from button."""
    query = update.callback_query
    await query.answer()
    level_key = query.data.replace("quiz_", "")
    await run_quiz(query.message, context, level_key)


async def run_quiz(message, context: ContextTypes.DEFAULT_TYPE, level_key: str):
    """Initialize and run a quiz for the given level."""
    questions = QUIZZES.get(level_key, [])
    if not questions:
        await message.reply_text("Chưa có bài tập cho trình độ này.")
        return

    random.shuffle(questions)
    selected_questions = questions[:5]

    context.user_data["quiz"] = {
        "level": level_key,
        "questions": selected_questions,
        "current_index": 0,
        "score": 0,
    }
    await show_quiz_question(message, context)


async def show_quiz_question(message, context: ContextTypes.DEFAULT_TYPE):
    """Display the current quiz question."""
    quiz = context.user_data.get("quiz")
    if not quiz:
        return

    idx = quiz["current_index"]
    q = quiz["questions"][idx]
    total = len(quiz["questions"])

    text = (
        f"🧠 <b>CÂU HỎI {idx + 1}/{total}</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        f"<b>{q['question']}</b>\n\n"
    )

    keyboard = []
    for i, opt in enumerate(q["options"]):
        keyboard.append([InlineKeyboardButton(opt, callback_data=f"answer_{i}")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    if hasattr(message, "edit_text"):
        await message.edit_text(text, reply_markup=reply_markup, parse_mode="HTML")
    else:
        await message.reply_text(text, reply_markup=reply_markup, parse_mode="HTML")


async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle user's answer selection."""
    query = update.callback_query
    await query.answer()

    quiz = context.user_data.get("quiz")
    if not quiz:
        return

    chosen = int(query.data.replace("answer_", ""))
    idx = quiz["current_index"]
    q = quiz["questions"][idx]

    is_correct = chosen == q["correct"]
    if is_correct:
        quiz["score"] += 1
        result = "✅ <b>CHÍNH XÁC! 太棒了！</b>\n\n"
    else:
        correct_answer = q["options"][q["correct"]]
        result = (
            f"❌ <b>CHƯA ĐÚNG!</b>\n\n"
            f"Đáp án đúng là: <b>{correct_answer}</b>\n\n"
        )

    result += f"💡 <i>{q['explanation']}</i>\n\n"

    keyboard = []
    if idx + 1 < len(quiz["questions"]):
        quiz["current_index"] += 1
        keyboard.append([InlineKeyboardButton("Câu tiếp theo ➡️", callback_data="quiz_next")])
    else:
        keyboard.append([InlineKeyboardButton("📊 Xem kết quả", callback_data="quiz_result")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(result, reply_markup=reply_markup, parse_mode="HTML")


async def handle_quiz_next(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Go to next quiz question."""
    query = update.callback_query
    await query.answer()
    await show_quiz_question(query.message, context)


async def handle_quiz_result(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show quiz results from button."""
    query = update.callback_query
    await query.answer()
    await show_quiz_results(query.message, context)


async def show_quiz_results(message, context: ContextTypes.DEFAULT_TYPE):
    """Display quiz results and award XP."""
    quiz = context.user_data.get("quiz")
    if not quiz:
        return

    score = quiz["score"]
    total = len(quiz["questions"])
    percentage = (score / total) * 100 if total > 0 else 0
    level_key = quiz["level"]

    earned_xp = score * 5
    user_id = message.chat.id
    new_xp = add_xp(user_id, earned_xp)

    if percentage >= 90:
        grade = "🏆 XUẤT SẮC! 太棒了！"
        advice = "Bạn nắm bài cực kỳ chắc chắn!"
    elif percentage >= 70:
        grade = "👏 KHÁ TỐT! 不错！"
        advice = "Hãy ôn lại một vài điểm để đạt điểm tối đa nhé."
    elif percentage >= 50:
        grade = "📖 CẦN ÔN TẬP! 加油！"
        advice = "Nên xem lại các bài học trước khi thi lại."
    else:
        grade = "💪 CỐ GẮNG HƠN! 别放弃！"
        advice = "Đừng nản! Hãy học lại từ vựng và thử lại nhé."

    text = (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "📊 <b>KẾT QUẢ BÀI KIỂM TRA</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📋 Trình độ: {LEVEL_NAMES.get(level_key, level_key)}\n"
        f"✅ Số câu đúng: {score}/{total} ({percentage:.0f}%)\n"
        f"⭐ Thưởng: +{earned_xp} XP (Tổng: {new_xp} XP)\n\n"
        f"{grade}\n"
        f"💡 {advice}\n"
    )

    keyboard = [
        [InlineKeyboardButton("🔄 Làm lại Quiz", callback_data=f"quiz_{level_key}")],
        [InlineKeyboardButton("📚 Xem bài học", callback_data=f"select_{level_key}")],
        [InlineKeyboardButton("🔙 Menu chính", callback_data="back_to_main")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await message.reply_text(text, reply_markup=reply_markup, parse_mode="HTML")


# ============================================================
# VOCAB QUICK REVIEW
# ============================================================

QUICK_VOCAB = {
    "level_0": [
        ("你好", "nǐ hǎo", "xin chào"),
        ("谢谢", "xièxie", "cảm ơn"),
        ("再见", "zàijiàn", "tạm biệt"),
        ("对不起", "duìbuqǐ", "xin lỗi"),
        ("没关系", "méi guānxi", "không sao"),
        ("我", "wǒ", "tôi"),
        ("你", "nǐ", "bạn"),
        ("他/她", "tā", "anh ấy/cô ấy"),
        ("是", "shì", "là"),
        ("不", "bù", "không"),
    ],
    "level_1": [
        ("爸爸", "bàba", "bố"),
        ("妈妈", "māma", "mẹ"),
        ("学生", "xuéshēng", "học sinh"),
        ("老师", "lǎoshī", "giáo viên"),
        ("今天", "jīntiān", "hôm nay"),
        ("明天", "míngtiān", "ngày mai"),
        ("水", "shuǐ", "nước"),
        ("茶", "chá", "trà"),
        ("米饭", "mǐfàn", "cơm"),
        ("多少钱", "duōshao qián", "bao nhiêu tiền"),
    ],
    "level_2": [
        ("公共汽车", "gōnggòng qìchē", "xe buýt"),
        ("地铁", "dìtiě", "tàu điện ngầm"),
        ("天气", "tiānqì", "thời tiết"),
        ("下雨", "xià yǔ", "mưa"),
        ("医院", "yīyuàn", "bệnh viện"),
        ("感冒", "gǎnmào", "cảm lạnh"),
        ("远", "yuǎn", "xa"),
        ("近", "jìn", "gần"),
    ],
    "level_3": [
        ("经理", "jīnglǐ", "giám đốc"),
        ("同事", "tóngshì", "đồng nghiệp"),
        ("会议", "huìyì", "cuộc họp"),
        ("打算", "dǎsuan", "dự định"),
        ("热情", "rèqíng", "nhiệt tình"),
        ("行李", "xíngli", "hành lý"),
    ]
}


async def vocab_review(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /vocab command."""
    user_id = update.effective_user.id
    progress = get_user_progress(user_id)
    level_key = progress.get("current_level", "level_0")

    words = QUICK_VOCAB.get(level_key, QUICK_VOCAB["level_0"])
    word = random.choice(words)

    text = (
        "🔤 <b>ÔN TẬP TỪ VỰNG FLASHCARD</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        f"\n<b>🇨🇳  {word[0]}</b>\n\n"
        "<i>Bạn có nhớ cách đọc và nghĩa của từ này không?</i>\n"
    )

    keyboard = [
        [InlineKeyboardButton("👀 Xem đáp án", callback_data=f"vocab_show_{words.index(word)}_{level_key}")],
        [InlineKeyboardButton("🔄 Từ khác", callback_data="vocab_next")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.callback_query:
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup, parse_mode="HTML")
    else:
        await update.message.reply_text(text, reply_markup=reply_markup, parse_mode="HTML")


async def handle_vocab_show(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show answer for vocab card."""
    query = update.callback_query
    await query.answer()

    parts = query.data.split("_")
    word_idx = int(parts[2])
    level_key = f"{parts[3]}_{parts[4]}"

    words = QUICK_VOCAB.get(level_key, QUICK_VOCAB["level_0"])
    if word_idx < len(words):
        word = words[word_idx]
        text = (
            "🔤 <b>ĐÁP ÁN FLASHCARD</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            f"🇨🇳 Chữ Hán: <b>{word[0]}</b>\n"
            f"🎵 Pinyin: <b>{word[1]}</b>\n"
            f"🇻🇳 Nghĩa: <b>{word[2]}</b>\n"
        )
        keyboard = [
            [InlineKeyboardButton("🔄 Từ tiếp theo", callback_data="vocab_next")],
            [InlineKeyboardButton("🔙 Menu chính", callback_data="back_to_main")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text, reply_markup=reply_markup, parse_mode="HTML")


async def handle_vocab_next(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Next vocab flashcard."""
    query = update.callback_query
    await query.answer()
    await vocab_review(update, context)


# ============================================================
# PROGRESS & PROFILE DISPLAY
# ============================================================

async def show_progress(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /progress or /profile command."""
    user_id = update.effective_user.id
    progress = get_user_progress(user_id)

    level_key = progress.get("current_level")
    completed = progress.get("completed_lessons", [])
    xp = progress.get("xp", 0)
    rank = get_user_rank(xp)
    total_done = progress.get("total_lessons_done", 0)

    text = (
        "📊 <b>BẢNG VÀNG THÀNH TÍCH HỌC TẬP</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🎖️ <b>Cấp bậc học viên:</b> {rank}\n"
        f"⭐ <b>Điểm kinh nghiệm:</b> {xp} XP\n"
        f"📚 <b>Tổng bài đã hoàn thành:</b> {total_done}\n\n"
    )

    if level_key:
        text += f"🎯 <b>Trình độ hiện tại:</b> {LEVEL_NAMES.get(level_key, 'Chưa chọn')}\n\n"

    for lk, lv_data in CURRICULUM.items():
        lv_lessons = lv_data["lesson_order"]
        done_count = sum(1 for l in lv_lessons if f"{lk}_{l}" in completed)
        total_count = len(lv_lessons)
        bar = "█" * done_count + "░" * (total_count - done_count)
        pct = (done_count / total_count * 100) if total_count > 0 else 0

        text += f"<b>{lv_data['name']}</b>\n"
        text += f"   [{bar}] {done_count}/{total_count} ({pct:.0f}%)\n\n"

    text += "💪 <i>继续加油！(Jìxù jiāyóu!) - Kiên trì mỗi ngày để trở thành Bậc Thầy Tiếng Trung!</i>"

    keyboard = [
        [InlineKeyboardButton("📚 Học bài tiếp", callback_data="back_to_levels")],
        [InlineKeyboardButton("🔙 Menu chính", callback_data="back_to_main")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.callback_query:
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup, parse_mode="HTML")
    else:
        await update.message.reply_text(text, reply_markup=reply_markup, parse_mode="HTML")


async def roadmap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /roadmap command."""
    text = (
        "🗺 <b>LỘ TRÌNH HỌC TIẾNG TRUNG CHUẨN TỪNG BƯỚC</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "🌱 <b>GIAI ĐOẠN 1: MẤT GỐC (2-3 tuần)</b>\n"
        "📍 Nắm vững 4 thanh điệu & thanh nhẹ\n"
        "📍 23 phụ âm đầu + 36 vận mẫu\n"
        "📍 Quy tắc biến điệu: 一, 不, hai thanh 3\n"
        "📍 10 nét viết cơ bản & số đếm\n\n"
        "📗 <b>GIAI ĐOẠN 2: HSK1 (1-2 tháng)</b>\n"
        "📍 150 từ vựng cốt lõi\n"
        "📍 Chủ đề: Gia đình, Ăn uống, Mua sắm\n"
        "📍 Ngữ pháp: 是, 有, câu hỏi 吗/呢\n\n"
        "📘 <b>GIAI ĐOẠN 3: HSK2 (2-3 tháng)</b>\n"
        "📍 300 từ vựng nâng cao\n"
        "📍 Giao tiếp: Đi taxi, xem thời tiết, đi khám bệnh\n"
        "📍 Ngữ pháp: Trợ từ 了, câu so sánh 比\n\n"
        "📙 <b>GIAI ĐOẠN 4: HSK3 (3-4 tháng)</b>\n"
        "📍 600 từ vựng giao tiếp thành thạo\n"
        "📍 Ngữ pháp chuyên sâu: Câu chữ 把, chữ 被, các loại bổ ngữ\n"
        "📍 Tự tin du lịch, mua sắm và làm việc với người Trung!"
    )
    await update.message.reply_text(text, parse_mode="HTML")


async def setkey_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /setkey <API_KEY> to configure Gemini API Key directly in chat."""
    args = context.args
    if not args:
        current_key = get_gemini_api_key()
        masked_key = f"{current_key[:6]}...{current_key[-4:]}" if current_key else "Chưa cấu hình"
        text = (
            "🔑 <b>HƯỚNG DẪN CẤU HÌNH GEMINI AI CHO BOT</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            f"📍 <b>Trạng thái hiện tại:</b> <code>{masked_key}</code>\n\n"
            "💡 <b>Cách lấy key miễn phí từ Google:</b>\n"
            "1. Truy cập <a href='https://aistudio.google.com/'>Google AI Studio</a>\n"
            "2. Đăng nhập Gmail và nhấn <b>Get API key</b> ➔ <b>Create API key</b>\n"
            "3. Sao chép chuỗi key (bắt đầu bằng <code>AIzaSy...</code>)\n\n"
            "👉 <b>Cách kích hoạt trên bot:</b>\n"
            "Gửi cú pháp: <code>/setkey AIzaSy...</code>"
        )
        await update.message.reply_text(text, parse_mode="HTML", disable_web_page_preview=True)
        return

    new_key = args[0].strip()
    status_msg = await update.message.reply_text("⏳ <i>Đang kiểm tra kết nối với máy chủ Google Gemini AI...</i>", parse_mode="HTML")

    try:
        is_valid, info = await validate_gemini_key(new_key)
        if is_valid:
            set_gemini_api_key(new_key)
            success_text = (
                "🎉 <b>KÍCH HOẠT GEMINI AI THÀNH CÔNG!</b>\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                f"✅ <b>Mô hình hoạt động:</b> <code>{info}</code>\n\n"
                "🌟 <b>Các tính năng đã được nâng cấp siêu cấp:</b>\n"
                "1. <b>Bộ Dịch Thuật Khẩu Ngữ:</b> Dịch chuẩn xác 100% tiếng lóng, chat mạng, thuật ngữ thanh toán, nạp rút, P2P (代收, 代付, 宝, 亲...).\n"
                "2. <b>Thầy Lý AI 1-1:</b> Phản xạ thông minh, sửa ngữ pháp và kèm riêng tự nhiên như người bản xứ!"
            )
            await status_msg.edit_text(success_text, parse_mode="HTML")
        else:
            err_text = (
                "⚠️ <b>LỖI KẾT NỐI GEMINI API!</b>\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                f"Không thể xác thực Key của bạn.\n"
                f"Chi tiết: <code>{html.escape(info)}</code>\n\n"
                "💡 <i>Lưu ý: Bạn cần dán chuỗi API Key thật (lấy tại Google AI Studio), không gõ nguyên mẫu ví dụ 'AIzaSy...'.</i>\n"
                "Cú pháp: <code>/setkey &lt;MÃ_KEY_CỦA_BẠN&gt;</code>"
            )
            await status_msg.edit_text(err_text, parse_mode="HTML", disable_web_page_preview=True)
    except Exception as e:
        logger.error(f"Error in setkey_command: {e}", exc_info=True)
        await status_msg.edit_text(
            f"⚠️ <b>ĐÃ CÓ LỖI XẢY RA KHI KIỂM TRA:</b>\n<code>{html.escape(str(e))}</code>\n\nVui lòng thử lại sau.",
            parse_mode="HTML"
        )


async def keyinfo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /keyinfo command."""
    current_key = get_gemini_api_key()
    if current_key:
        masked_key = f"{current_key[:6]}...{current_key[-4:]}"
        text = (
            "🟢 <b>TRẠNG THÁI AI: ĐÃ KÍCH HOẠT GEMINI AI</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            f"🔑 <b>API Key:</b> <code>{masked_key}</code>\n"
            "⚡ Bot đang chạy bằng trí tuệ nhân tạo Gemini Flash cao cấp nhất!\n"
            "Nếu muốn thay đổi key, hãy gửi: <code>/setkey &lt;KEY_MỚI&gt;</code>"
        )
    else:
        text = (
            "🟡 <b>TRẠNG THÁI AI: CHẾ ĐỘ NỘI BỘ + HYBRID NEURAL</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "Bot đang hoạt động bằng <b>Bộ từ điển chuyên sâu giao dịch & khẩu ngữ bản xứ tích hợp</b>.\n\n"
            "💡 <b>Bạn muốn nâng cấp lên Gemini AI siêu cấp?</b>\n"
            "Gửi cú pháp: <code>/setkey &lt;API_KEY&gt;</code>\n"
            "Lấy key miễn phí 100% tại <a href='https://aistudio.google.com/'>Google AI Studio</a>"
        )
    await update.message.reply_text(text, parse_mode="HTML", disable_web_page_preview=True)


# ============================================================
# MASTER MESSAGE HANDLER (NLP, TRANSLATE & AI TUTOR)
# ============================================================

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Central intelligent message router."""
    user_text = update.message.text.strip()

    # 1. Check if user is in active multi-turn roleplay
    if context.user_data.get("active_roleplay"):
        await handle_roleplay_user_input(update, context)
        return

    # 2. Check if user is in Translation Mode or used translation prefix
    translate_mode = context.user_data.get("translate_mode", False)
    is_explicit_translate = user_text.lower().startswith("dịch ") or user_text.lower().startswith("dịch: ")

    if translate_mode or is_explicit_translate:
        query_text = user_text
        if is_explicit_translate:
            # Strip "dịch " or "dịch: " prefix
            query_text = user_text[user_text.find(" ") + 1:].strip()

        await update.message.chat.send_action("typing")
        translated_result = await translate_text(query_text)

        keyboard = [
            [
                InlineKeyboardButton("🔄 Dịch câu khác", callback_data="toggle_translate_mode"),
                InlineKeyboardButton("🛑 Dừng dịch", callback_data="stop_translate_mode"),
            ]
        ]
        await update.message.reply_text(translated_result, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")
        return

    # 3. Check if user is in 1-1 Chat Mode OR user explicitly sent Chinese characters
    chat_mode = context.user_data.get("chat_mode", False)
    has_hanzi = any('\u4e00' <= c <= '\u9fff' for c in user_text)

    if chat_mode or has_hanzi:
        await update.message.chat.send_action("typing")
        history = context.user_data.get("chat_history", [])
        
        reply = await get_tutor_response(user_text, history)
        
        # Save history
        history.append({"role": "user", "text": user_text})
        history.append({"role": "model", "text": reply})
        context.user_data["chat_history"] = history[-10:]

        keyboard = [
            [
                InlineKeyboardButton("🌐 Dịch câu này", callback_data="toggle_translate_mode"),
                InlineKeyboardButton("🎭 Đóng vai giao tiếp", callback_data="show_roleplay_menu"),
            ]
        ]
        if chat_mode:
            keyboard.append([InlineKeyboardButton("🛑 Dừng Chat 1-1", callback_data="stop_chat_mode")])

        await update.message.reply_text(reply, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")
        return

    # 4. Default quick guidance
    response = (
        "🧑‍🏫 <b>Thầy Lý (李老师) luôn ở đây đồng hành cùng bạn!</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        f"Bạn vừa nhắn: <i>\"{user_text}\"</i>\n\n"
        "💡 <b>Bạn muốn làm gì tiếp theo?</b>\n"
        "• Dịch câu trên sang khẩu ngữ Trung? 👉 Nhấn <b>🌐 Dịch Song Ngữ</b>\n"
        "• Tâm sự, luyện phản xạ 1-1? 👉 Nhấn <b>🗣️ Chat 1-1 với Thầy</b>\n"
        "• Vào vai mua trà sữa, trả giá ở chợ? 👉 Chọn <b>🎭 Đóng vai giao tiếp</b>\n"
        "• Học bài bản theo trình độ? 👉 Chọn <b>📚 Danh sách bài học</b>"
    )

    keyboard = [
        [
            InlineKeyboardButton("🌐 Dịch Thuật Khẩu Ngữ", callback_data="toggle_translate_mode"),
            InlineKeyboardButton("🗣️ Chat 1-1 Thầy AI", callback_data="toggle_chat_mode"),
        ],
        [
            InlineKeyboardButton("🎭 Đóng vai giao tiếp", callback_data="show_roleplay_menu"),
            InlineKeyboardButton("💬 Kho câu giao tiếp", callback_data="phrases_main"),
        ],
        [
            InlineKeyboardButton("📚 Danh sách bài học", callback_data="back_to_levels"),
            InlineKeyboardButton("📝 Ngữ pháp trọng điểm", callback_data="grammar_main"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(response, reply_markup=reply_markup, parse_mode="HTML")


# ============================================================
# CALLBACK QUERY ROUTING HELPERS
# ============================================================

async def back_to_levels(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Callback helper to level selection."""
    query = update.callback_query
    await query.answer()
    await select_level(update, context)


async def back_to_main_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Back to main welcome menu."""
    query = update.callback_query
    await query.answer()
    user = query.from_user
    prog = get_user_progress(user.id)
    rank = get_user_rank(prog.get("xp", 0))

    text = (
        f"🇨🇳 <b>AI CHINESE MASTER BOT PRO MAX</b> 🧑‍🏫\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        f"Xin chào <b>{user.first_name}</b>! Cấp bậc: <b>{rank}</b> ({prog.get('xp', 0)} XP)\n\n"
        "Chọn tính năng bạn muốn khám phá:"
    )

    keyboard = [
        [
            InlineKeyboardButton("🌐 Dịch Thuật Khẩu Ngữ", callback_data="toggle_translate_mode"),
            InlineKeyboardButton("🗣️ Chat 1-1 Thầy AI", callback_data="toggle_chat_mode"),
        ],
        [
            InlineKeyboardButton("🎭 Đóng vai giao tiếp", callback_data="show_roleplay_menu"),
            InlineKeyboardButton("💬 Kho câu giao tiếp", callback_data="phrases_main"),
        ],
        [
            InlineKeyboardButton("🔥 Tiếng lóng giới trẻ", callback_data="phrase_cat_slang"),
            InlineKeyboardButton("📝 Sổ tay ngữ pháp", callback_data="grammar_main"),
        ],
        [
            InlineKeyboardButton("📚 Bài học HSK (0-3)", callback_data="back_to_levels"),
            InlineKeyboardButton("🔤 Flashcard từ vựng", callback_data="vocab_next"),
        ],
        [
            InlineKeyboardButton("📊 Bảng vàng thành tích", callback_data="show_profile_cb"),
        ]
    ]
    await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")


async def toggle_translate_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Enable translate mode from callback button."""
    query = update.callback_query
    await query.answer()
    context.user_data["translate_mode"] = True
    context.user_data["chat_mode"] = False
    context.user_data["active_roleplay"] = None

    text = (
        "🌐 <b>CHẾ ĐỘ DỊCH THUẬT SONG NGỮ KHẨU NGỮ ĐỜI THƯỜNG</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎯 <b>Đặc điểm:</b>\n"
        "• Khẩu ngữ tự nhiên, nói chuyện hàng ngày, không từ chuyên ngành.\n"
        "• 🇻🇳 ➔ 🇨🇳 Nhập tiếng Việt ➔ Dịch sang tiếng Trung kèm <b>Pinyin chuẩn có dấu thanh</b>.\n"
        "• 🇨🇳 ➔ 🇻🇳 Nhập tiếng Trung ➔ Dịch sang tiếng Việt đời thường dễ hiểu.\n\n"
        "👉 <b>Hãy nhập câu bạn muốn dịch vào đây ngay nhé!</b>"
    )
    keyboard = [[InlineKeyboardButton("🛑 Dừng dịch thuật", callback_data="stop_translate_mode")]]
    await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")


async def stop_translate_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Stop translate mode from callback."""
    query = update.callback_query
    await query.answer()
    context.user_data["translate_mode"] = False
    await back_to_main_callback(update, context)


async def toggle_chat_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Toggle chat mode from inline button."""
    query = update.callback_query
    await query.answer()
    context.user_data["chat_mode"] = True
    context.user_data["translate_mode"] = False
    context.user_data["active_roleplay"] = None

    text = (
        "🧑‍🏫 <b>CHẾ ĐỘ CHAT 1-1 VỚI THẦY LÝ ĐÃ SẴN SÀNG!</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "Thầy đang lắng nghe! Em hãy gõ một câu tiếng Trung, Pinyin hoặc hỏi nghĩa của bất kỳ câu nào nhé!\n\n"
        "💡 <i>Ví dụ: '你好老师，我想学中文' hoặc 'Chúc ngủ ngon tiếng Trung là gì thầy?'</i>"
    )
    keyboard = [[InlineKeyboardButton("🛑 Dừng Chat 1-1", callback_data="stop_chat_mode")]]
    await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")


async def stop_chat_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Stop chat mode from callback."""
    query = update.callback_query
    await query.answer()
    context.user_data["chat_mode"] = False
    await back_to_main_callback(update, context)


async def roleplay_exit_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Exit roleplay scenario."""
    query = update.callback_query
    await query.answer()
    context.user_data["active_roleplay"] = None
    await roleplay_command(update, context)


# ============================================================
# MAIN
# ============================================================

def main():
    """Start the Pro Max Telegram Chinese Bot."""
    # Start Keep-Alive Web Server for Render / UptimeRobot
    keep_alive()

    TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

    if not TOKEN:
        config_file = Path("config.json")
        if config_file.exists():
            try:
                with open(config_file, "r", encoding="utf-8") as f:
                    config = json.load(f)
                    TOKEN = config.get("token")
            except Exception:
                pass

    if not TOKEN:
        print("❌ CHƯA CÓ BOT TOKEN trong config.json hoặc biến môi trường TELEGRAM_BOT_TOKEN!")
        return

    # Build Telegram Application
    app = Application.builder().token(TOKEN).build()

    # Core Command Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("dich", translate_command))
    app.add_handler(CommandHandler("translate", translate_command))
    app.add_handler(CommandHandler("stopdich", stop_translate_command))
    app.add_handler(CommandHandler("chat", chat_command))
    app.add_handler(CommandHandler("tutor", chat_command))
    app.add_handler(CommandHandler("stopchat", stopchat_command))
    app.add_handler(CommandHandler("roleplay", roleplay_command))
    app.add_handler(CommandHandler("practice", roleplay_command))
    app.add_handler(CommandHandler("phrases", phrases_command))
    app.add_handler(CommandHandler("slang", lambda u, c: handle_phrase_category(u, c)))
    app.add_handler(CommandHandler("grammar", grammar_command))
    app.add_handler(CommandHandler("level", select_level))
    app.add_handler(CommandHandler("lessons", show_lessons))
    app.add_handler(CommandHandler("quiz", start_quiz_command))
    app.add_handler(CommandHandler("progress", show_progress))
    app.add_handler(CommandHandler("profile", show_progress))
    app.add_handler(CommandHandler("roadmap", roadmap))
    app.add_handler(CommandHandler("vocab", vocab_review))
    app.add_handler(CommandHandler("setkey", setkey_command))
    app.add_handler(CommandHandler("apikey", setkey_command))
    app.add_handler(CommandHandler("keyinfo", keyinfo_command))
    app.add_handler(CommandHandler("status", keyinfo_command))

    # Core Callback Query Handlers
    app.add_handler(CallbackQueryHandler(back_to_main_callback, pattern=r"^back_to_main$"))
    app.add_handler(CallbackQueryHandler(toggle_translate_callback, pattern=r"^toggle_translate_mode$"))
    app.add_handler(CallbackQueryHandler(stop_translate_callback, pattern=r"^stop_translate_mode$"))
    app.add_handler(CallbackQueryHandler(toggle_chat_callback, pattern=r"^toggle_chat_mode$"))
    app.add_handler(CallbackQueryHandler(stop_chat_callback, pattern=r"^stop_chat_mode$"))
    app.add_handler(CallbackQueryHandler(show_progress, pattern=r"^show_profile_cb$"))

    # Roleplay Callbacks
    app.add_handler(CallbackQueryHandler(roleplay_command, pattern=r"^show_roleplay_menu$"))
    app.add_handler(CallbackQueryHandler(handle_roleplay_start, pattern=r"^rp_start_\w+$"))
    app.add_handler(CallbackQueryHandler(roleplay_exit_callback, pattern=r"^rp_exit$"))

    # Phrasebook Callbacks
    app.add_handler(CallbackQueryHandler(phrases_command, pattern=r"^phrases_main$"))
    app.add_handler(CallbackQueryHandler(handle_phrase_category, pattern=r"^phrase_cat_\w+$"))

    # Grammar Callbacks
    app.add_handler(CallbackQueryHandler(grammar_command, pattern=r"^grammar_main$"))
    app.add_handler(CallbackQueryHandler(handle_grammar_view, pattern=r"^grammar_view_\w+$"))

    # Level & Lesson Callbacks
    app.add_handler(CallbackQueryHandler(back_to_levels, pattern=r"^back_to_levels$"))
    app.add_handler(CallbackQueryHandler(handle_level_selection, pattern=r"^select_level_\d$"))
    app.add_handler(CallbackQueryHandler(handle_lesson, pattern=r"^lesson_"))

    # Quiz Callbacks
    app.add_handler(CallbackQueryHandler(handle_quiz_start, pattern=r"^quiz_level_\d$"))
    app.add_handler(CallbackQueryHandler(handle_quiz_next, pattern=r"^quiz_next$"))
    app.add_handler(CallbackQueryHandler(handle_answer, pattern=r"^answer_\d$"))
    app.add_handler(CallbackQueryHandler(handle_quiz_result, pattern=r"^quiz_result$"))

    # Vocab Callbacks
    app.add_handler(CallbackQueryHandler(handle_vocab_show, pattern=r"^vocab_show_"))
    app.add_handler(CallbackQueryHandler(handle_vocab_next, pattern=r"^vocab_next$"))

    # Message Handler (Must be last)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Global Error Handler
    async def global_error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
        if isinstance(context.error, BadRequest) and "Message is not modified" in str(context.error):
            return
        logger.warning("Telegram update warning: %s", context.error)

    app.add_error_handler(global_error_handler)

    # Event loop fix for Python 3.14 on Windows
    try:
        asyncio.get_event_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())

    print("=" * 60)
    print("🇨🇳 BOT DẠY TIẾNG TRUNG PRO MAX ĐÃ KHỞI ĐỘNG THÀNH CÔNG!")
    print("✨ Sẵn sàng: Dịch khẩu ngữ Pinyin, Chat 1-1 Thầy Lý, Roleplay")
    print("=" * 60)
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
