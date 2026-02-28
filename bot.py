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


# ---------- Константы ----------
BACK_BUTTON = InlineKeyboardMarkup(
    [[InlineKeyboardButton("⬅️ Назад", callback_data="back")]]
)


# ---------- Главное меню ----------
def main_menu():
    keyboard = [
        [InlineKeyboardButton("🏠 Об общежитии", callback_data="about")],
        [InlineKeyboardButton("👥 Студенческий совет", callback_data="council")],
        [InlineKeyboardButton("📷 Фотографии", callback_data="photos")],
        [InlineKeyboardButton("🌐 Социальные сети", callback_data="social")],
        [InlineKeyboardButton("📋 Заселение", callback_data="checkin")],
        [InlineKeyboardButton("⚖️ Правила ПВР", callback_data="rules")],
        [InlineKeyboardButton("🏢 Администрация", callback_data="administration")],
        [InlineKeyboardButton("🧺 Прачечная", callback_data="laundry")],
        [InlineKeyboardButton("🏋️ Спортзал", callback_data="gym")],
        [InlineKeyboardButton("🚿 Для новичков", callback_data="beginners")],
        [InlineKeyboardButton("🏗️ ЖБК", callback_data="jbk")]
    ]
    return InlineKeyboardMarkup(keyboard)


# ---------- Тексты ----------
ABOUT_TEXT = (
    "🏠 ✨ Общежитие на Большой Красной, 18 ✨\n\n"
    "Общежитие, расположенное по адресу Большая Красная, 18 🏡📍, является местом проживания студентов КНИТУ-КАИ 🎓. Это современное и уютное пространство, где созданы комфортные условия для учёбы и отдыха.\n\n"
    "Здесь царит дружелюбная атмосфера 🤝✨. Студенты поддерживают друг друга, вместе готовятся к занятиям, участвуют в мероприятиях и просто проводят время в приятной компании.\n"
    "Общежитие на Большой Красной, 18 — это не просто здание, а важная часть студенческой жизни, где формируется сплочённый коллектив и создаются яркие воспоминания 🌟📚\n\n"
    "📍 Адрес: Большая Красная, 18\n"
    "🗺️ Как добраться: https://yandex.com/maps/-/CPqMRP3Z\n\n"
    "👩‍💼 Комендант: Труш Лариса Александровна\n"
    "🕒 Вахта: круглосуточно\n\n"
    "На территории есть:\n"
    "• кухни\n"
    "• прачечная\n"
    "• Wi-Fi\n"
    "• спортивный зал\n"
)

COUNCIL_TEXT = (
    "👥 Студенческий совет общежития\n\n"
    "Председатель - Юлия Пелагеина\n"
    "https://vk.com/pelageina_j\n\n"
    "Заместитель председателя - [Имя]\n"
    "https://vk.com/id...\n\n"
    "Председатель КПД - Олеся Черкасова\n"
    "https://vk.com/xaseef\n\n"
    "Председатель санитарной комиссии - Дарья Докина\n"
    "https://vk.com/daryadokina\n\n"
    "Глава ГРО - Анис Нуриев\n"
    "https://vk.com/id495552862\n\n"
    "Староста первого этажа - Дарья Сушенцова\n"
    "https://vk.com/uyccigcuuxfurixr\n\n"
    "Староста второго этажа - [Имя]\n"
    "https://vk.com/id...\n\n"
    "Староста третьего этажа крыла ЛА - Егор Иванов\n"
    "https://vk.com/gerka_igor\n\n"

)

SOCIAL_TEXT = (
    "🌐 Социальные сети\n\n"
    "ВКонтакте: https://vk.com/knity_kai\n"

    "Telegram: https://t.me/KAInomerII\n"

)

CHECKIN_TEXT = (
    "📋 Заселение в общежитие\n\n"
    "📄 Необходимые документы:\n"
    "• Паспорт (копия + оригинал)\n"
    "• Студенческий билет\n"
    "• Медицинская справка (форма 086-у)\n"
    "• Фото 3x4 (4 шт)\n"
    "• Копия прививочного сертификата\n"
    "• Договор найма (заполняется на месте)\n\n"
    "💰 Оплата:\n"
    "• Стоимость проживания: уточнять в бухгалтерии\n"
    "• Реквизиты для оплаты: [реквизиты]\n\n"
    "📍 Адрес: Большая Красная, 18\n"
    "🗺️ Карта: https://yandex.com/maps/-/CPqMRP3Z\n\n"
    "📞 Контактный телефон: 8 (843) 231-01-29\n"
)

RULES_TEXT = (
    "⚖️ Правила внутреннего распорядка (ПВР)\n\n"
    "🕐 Режим работы:\n"
    "• Вход в общежитие: круглосуточно\n"
    "• Комендантский час: с 23:00 до 06:00\n\n"
    "🚫 Запрещается:\n"
    "• Курение в помещениях\n"
    "• Распитие алкоголя\n"
    "• Шум после 22:00\n"
    "• Перестановка мебели\n"
    "• Использование обогревателей\n\n"
)

ADMINISTRATION_TEXT = (
    "🏢 Администрация общежития\n\n"
    "👩‍💼 Комендант: Труш Лариса Александровна\n"
    "• Часы приема: Пн-Пт с 10:00 до 17:00\n"
    "• Кабинет: (1 этаж)\n\n"
    "👨‍💼 Заведующий хозяйством: Галина Сергеевна\n"
    "• Вопросы по ремонту и инвентарю\n\n"
    "🛡️ Вахтеры:\n"
    "• Круглосуточный пост\n"
    "• Выдача ключей, пропускной режим\n\n"
)

LAUNDRY_TEXT = (
    "🧺 Прачечная\n\n"
    "📍 Расположение: подвальное помещение\n\n"
    "⏰ Режим работы: круглосуточно\n"
    "💰 Стоимость и оплата: \n"
    "• Стиральная машина: 135 руб/стирка\n"
    "• Оплата происходит по ссылке: https://washer.mylaundry.ru/device/pr15kai2"
    "📋 Правила:\n"
    "• Не оставляйте вещи без присмотра\n"
    "• После использования протрите барабан\n"
    "• Загрузка не более 5 кг\n\n"
    "При возникновении проблем обращаться к студенческому совету и технической поддержи по контактам в прачечной\n"
)

GYM_TEXT = (
    "🏋️ Спортивный зал\n\n"
    "📍 Расположение: 1 этаж\n\n"
    "⏰ График работы:\n"
    "• Ежедневно: 09:00 - 22:00\n"
    "• Для попадания в тренажерный зал ключ нужно взять у ответсвенного (см. Студенческий совет)\n\n"
    "💰 Бесплатно для проживающих (по студенческому)\n\n"
    "📋 Правила:\n"
    "• Занимайтесь в спортивной обуви\n"
    "• Возвращайте инвентарь на место\n"
    "• Убирайте за собой тренажеры\n"
)

BEGINNERS_TEXT = (
    "🚿 Для новичков (гигиена и быт)\n\n"
    "🧹 Уборка:\n"
    "• Ершик для унитаза используйте ТОЛЬКО в унитазе\n"
    "• Мусор выбрасывайте в пакетах, не высыпайте в ведро\n"
    "• Влажная уборка в комнате - минимум раз в неделю\n\n"
    "🚿 Душ:\n"
    "• Используйте резиновые тапочки\n"
    "• После душа убирайте волосы из слива\n\n"
    "🚽 Туалет:\n"
    "• Не бросайте в унитаз влажные салфетки, вату, наполнитель - засор гарантирован\n"
    "• Опускайте сиденье унитаза после использования\n\n"
    "🍳 Кухня:\n"
    "• Убирайте за собой\n"
    "• Не оставляйте грязную посуду в раковине\n"
    "• Не оставляйте продукты\n\n"
    "💡 Важно:\n"
    "• Вас здесь никто не убирает - чистота зависит от вас\n"
    "• Уважайте соседей, не шумите ночью\n"
    "• Общайтесь с соседями - вместе решать бытовые вопросы легче\n"
)

JBK_TEXT = (
    "🏗️ Жилищно-бытовая комиссия (ЖБК)\n\n"
    "Что такое ЖБК?\n"
    "Комиссия, которая в конце года решает, оставить вас на следующий год или нет.\n\n"
)


# ---------- Команда /start ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏠 Добро пожаловать в информационный бот Общежития №2 КНИТУ-КАИ!\n\nВыберите раздел:",
        reply_markup=main_menu()
    )


# ---------- Отдельные команды ----------
async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ABOUT_TEXT, reply_markup=BACK_BUTTON)

async def council_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(COUNCIL_TEXT, reply_markup=BACK_BUTTON)

async def social_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(SOCIAL_TEXT, reply_markup=BACK_BUTTON)

async def photos_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRraowzVn_lO4boU8-NSkLsHCedr7V42kL3tA&s",
        caption="Фасад общежития №2",
        reply_markup=BACK_BUTTON
    )

async def checkin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(CHECKIN_TEXT, reply_markup=BACK_BUTTON)

async def rules_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(RULES_TEXT, reply_markup=BACK_BUTTON)

async def administration_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ADMINISTRATION_TEXT, reply_markup=BACK_BUTTON)

async def laundry_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(LAUNDRY_TEXT, reply_markup=BACK_BUTTON)

async def gym_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(GYM_TEXT, reply_markup=BACK_BUTTON)

async def beginners_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(BEGINNERS_TEXT, reply_markup=BACK_BUTTON)

async def jbk_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(JBK_TEXT, reply_markup=BACK_BUTTON)


# ---------- Кнопки ----------
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "about":
        await query.edit_message_text(ABOUT_TEXT, reply_markup=BACK_BUTTON)
    elif query.data == "council":
        await query.edit_message_text(COUNCIL_TEXT, reply_markup=BACK_BUTTON)
    elif query.data == "social":
        await query.edit_message_text(SOCIAL_TEXT, reply_markup=BACK_BUTTON)
    elif query.data == "checkin":
        await query.edit_message_text(CHECKIN_TEXT, reply_markup=BACK_BUTTON)
    elif query.data == "rules":
        await query.edit_message_text(RULES_TEXT, reply_markup=BACK_BUTTON)
    elif query.data == "administration":
        await query.edit_message_text(ADMINISTRATION_TEXT, reply_markup=BACK_BUTTON)
    elif query.data == "laundry":
        await query.edit_message_text(LAUNDRY_TEXT, reply_markup=BACK_BUTTON)
    elif query.data == "gym":
        await query.edit_message_text(GYM_TEXT, reply_markup=BACK_BUTTON)
    elif query.data == "beginners":
        await query.edit_message_text(BEGINNERS_TEXT, reply_markup=BACK_BUTTON)
    elif query.data == "jbk":
        await query.edit_message_text(JBK_TEXT, reply_markup=BACK_BUTTON)
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
            "Вы в главном меню!\nВыберите раздел:",
            reply_markup=main_menu()
        )


# ---------- Запуск ----------
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Команды
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(CommandHandler("council", council_command))
    app.add_handler(CommandHandler("social", social_command))
    app.add_handler(CommandHandler("photos", photos_command))
    app.add_handler(CommandHandler("checkin", checkin_command))
    app.add_handler(CommandHandler("rules", rules_command))
    app.add_handler(CommandHandler("administration", administration_command))
    app.add_handler(CommandHandler("laundry", laundry_command))
    app.add_handler(CommandHandler("gym", gym_command))
    app.add_handler(CommandHandler("beginners", beginners_command))
    app.add_handler(CommandHandler("jbk", jbk_command))

    # Кнопки
    app.add_handler(CallbackQueryHandler(buttons))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()