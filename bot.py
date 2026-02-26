import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN рррр")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🏠 Об общежитии", callback_data="about")],
        [InlineKeyboardButton("👥 Студенческий совет", callback_data="council")],
        [InlineKeyboardButton("📷 Фотографии", callback_data="photos")]
    ]

    await update.message.reply_text(
        "Добро пожаловать в бот общежития 👋\nВыберите раздел:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "about":
        await query.message.reply_text(
            "🏠 Общежитие №2\n\n"
            "Адрес: ул. Большая красная, д. 18\n"
            "Комендант: Труш Лариса Александровна\n"
            "Вахта: круглосуточно"
        )

    elif query.data == "council":
        await query.message.reply_text(
            "👥 Студенческий совет:\n\n"
            "Председатель Пелагеина Юлия — https://vk.com/@pelageina_j\n"
            "Заместитель — https://vk.com/username2"
        )

    elif query.data == "photos":
        media = [
            InputMediaPhoto("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRraowzVn_lO4boU8-NSkLsHCedr7V42kL3tA&s", caption="Фасад общежития"),
            InputMediaPhoto("https://international.kai.ru/prozivanie-v-obsezitiah")
        ]
        await query.message.reply_media_group(media)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()