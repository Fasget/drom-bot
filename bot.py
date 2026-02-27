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

# Главное меню
def main_menu():
    keyboard = [
        [InlineKeyboardButton("🏠 Об общежитии", callback_data="about")],
        [InlineKeyboardButton("👥 Студенческий совет", callback_data="council")],
        [InlineKeyboardButton("📷 Фотографии", callback_data="photos")],
        [InlineKeyboardButton("🌐 Социальные сети", callback_data="social")]
    ]
    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏠 Добро пожаловать в бот общежития №2 КНИТУ-КАИ 👋\n\n"
        "Здесь вы можете получить актуальную информацию:\n"
        "• об общежитии\n"
        "• о студенческом совете\n"
        "• посмотреть фотографии\n"
        "• найти социальные сети\n\n"
        "Выберите раздел:",
        reply_markup=main_menu()
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Кнопка назад
    back_button = InlineKeyboardMarkup(
        [[InlineKeyboardButton("⬅️ Назад", callback_data="back")]]
    )

    if query.data == "about":
        await query.edit_message_text(
            "🏠 *Общежитие №2 КНИТУ-КАИ*\n\n"
            "📍 Адрес: г. Казань, ул. Большая Красная, д. 18\n\n"
            "👩‍💼 Комендант: Труш Лариса Александровна\n"
            "🕒 Вахта: круглосуточно\n\n"
            "🏢 Общежитие предназначено для проживания студентов "
            "и оснащено всем необходимым для комфортной учебы и жизни:\n"
            "• оборудованные комнаты\n"
            "• кухни на этажах\n"
            "• прачечная\n"
            "• учебные зоны\n"
            "• Wi-Fi\n\n"
            "По всем вопросам можно обращаться к коменданту или "
            "в студенческий совет.",
            parse_mode="Markdown",
            reply_markup=back_button
        )

    elif query.data == "council":
        await query.edit_message_text(
            "👥 *Студенческий совет общежития*\n\n"
            "Председатель — Юлия Пелагеина\n"
            "https://vk.com/@pelageina_j\n\n"
            "Председатель КПД — Олеся Черкасова\n"
            "https://vk.com/xaseef\n\n"
            "Председатель санитарной комиссии — Дарья Докина\n"
            "https://vk.com/daryadokina\n\n"
            "Глава ГРО — Анис Нуриев\n"
            "https://vk.com/id495552862\n\n"
            "Студсовет помогает решать вопросы проживания, "
            "организует мероприятия и поддерживает порядок.",
            parse_mode="Markdown",
            reply_markup=back_button
        )

    elif query.data == "photos":
        media = [
            InputMediaPhoto(
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRraowzVn_lO4boU8-NSkLsHCedr7V42kL3tA&s",
                caption="Фасад общежития №2"
            )
        ]

        await query.message.reply_media_group(media)

    elif query.data == "social":
        await query.edit_message_text(
            "🌐 *Социальные сети общежития*\n\n"
            "ВКонтакте:\n"
            "https://vk.com/knity_kai\n\n"
            "Telegram-канал:\n"
            "https://t.me/KAInomerII\n\n"
            "Подписывайтесь, чтобы быть в курсе новостей и мероприятий!",
            parse_mode="Markdown",
            reply_markup=back_button
        )

    elif query.data == "back":
        await query.edit_message_text(
            "Выберите раздел:",
            reply_markup=main_menu()
        )


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()