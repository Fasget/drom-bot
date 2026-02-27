import os
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
    InputMediaPhoto
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN не найден")


# ---------- Главное меню ----------
def main_menu():
    keyboard = [
        [InlineKeyboardButton("🏠 Об общежитии", callback_data="about")],
        [InlineKeyboardButton("👥 Студенческий совет", callback_data="council")],
        [InlineKeyboardButton("📷 Фотографии", callback_data="photos")],
        [InlineKeyboardButton("🌐 Социальные сети", callback_data="social")]
    ]
    return InlineKeyboardMarkup(keyboard)


# ---------- Тексты ----------
ABOUT_TEXT = (
    "🏠 Общежитие №2 КНИТУ-КАИ\n\n"
    "📍 Адрес: г. Казань, ул. Большая Красная, д. 18\n\n"
    "👩‍💼 Комендант: Труш Лариса Александровна\n"
    "🕒 Вахта: круглосуточно\n\n"
    "На территории есть:\n"
    "• кухни\n"
    "• прачечная\n"
    "• Wi-Fi\n"
)

COUNCIL_TEXT = (
    "👥 Студенческий совет общежития\n\n"
    "Председатель — Юлия Пелагеина\n"
    "https://vk.com/pelageina_j\n\n"
    "Председатель КПД — Олеся Черкасова\n"
    "https://vk.com/xaseef\n\n"
    "Председатель санитарной комиссии — Дарья Докина\n"
    "https://vk.com/daryadokina\n\n"
    "Глава ГРО — Анис Нуриев\n"
    "https://vk.com/id495552862\n"
)

SOCIAL_TEXT = (
    "🌐 Социальные сети\n\n"
    "ВКонтакте:\n"
    "https://vk.com/knity_kai\n\n"
    "Telegram:\n"
    "https://t.me/KAInomerII\n"
)


# ---------- Команда /start ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏠 Добро пожаловать!\n\nВыберите раздел:",
        reply_markup=main_menu()
    )


# ---------- Отдельные команды ----------
async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        ABOUT_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("⬅️ Назад", callback_data="back")]]
        )
    )


async def council_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        COUNCIL_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("⬅️ Назад", callback_data="back")]]
        )
    )


async def social_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        SOCIAL_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("⬅️ Назад", callback_data="back")]]
        )
    )


async def photos_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    media = [
        InputMediaPhoto(
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRraowzVn_lO4boU8-NSkLsHCedr7V42kL3tA&s",
            caption="Фасад общежития №2"
        )
    ]
    await update.message.reply_media_group(media)


# ---------- Кнопки ----------
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    back_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton("⬅️ Назад", callback_data="back")]]
    )

    if query.data == "about":
        await query.edit_message_text(ABOUT_TEXT, reply_markup=back_markup)

    elif query.data == "council":
        await query.edit_message_text(COUNCIL_TEXT, reply_markup=back_markup)

    elif query.data == "social":
        await query.edit_message_text(SOCIAL_TEXT, reply_markup=back_markup)

    elif query.data == "photos":
        media = [
            InputMediaPhoto(
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRraowzVn_lO4boU8-NSkLsHCedr7V42kL3tA&s",
                caption="Фасад общежития №2"
            )
        ]
        await query.message.reply_media_group(media)

    elif query.data == "back":
        await query.edit_message_text(
            "Выберите раздел:",
            reply_markup=main_menu()
        )


# ---------- Запуск ----------
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(CommandHandler("council", council_command))
    app.add_handler(CommandHandler("social", social_command))
    app.add_handler(CommandHandler("photos", photos_command))

    app.add_handler(CallbackQueryHandler(buttons))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()