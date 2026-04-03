import os
from telegram import ( # pyright: ignore[reportMissingImports] # pyright: ignore[reportMissingImports]
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
    InputMediaPhoto 
)
from telegram.ext import ( # pyright: ignore[reportMissingImports]
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters
)
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = "@messegesKAI2"

if not TOKEN:
    raise ValueError("BOT_TOKEN не найден")


# ---------- Константы ----------
BACK_BUTTON = InlineKeyboardMarkup(
    [[InlineKeyboardButton("⬅️ Назад", callback_data="back")]]
)
FEEDBACK_BACK_BUTTON = InlineKeyboardMarkup(
    [[InlineKeyboardButton("⬅️ Назад", callback_data="back_from_feedback")]]
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
        [InlineKeyboardButton("⚠️ Руководство для чайников", callback_data="beginners")],
        [InlineKeyboardButton("🏗️ ЖБК", callback_data="jbk")],
        [InlineKeyboardButton("📦 ГРО", callback_data="gro")], 
        [InlineKeyboardButton("💬 Жалобы и предложения", callback_data="feedback")],
    ]
    return InlineKeyboardMarkup(keyboard)


# ---------- Тексты ----------
ABOUT_TEXT = (
    "🏠 ✨ Общежитие №2 КНИТУ-КАИ\n\n"
    "Общежитие, расположенное по адресу Большая Красная, 18 🏡📍, является местом проживания студентов КНИТУ-КАИ 🎓. Это уютное пространство, где созданы комфортные условия для учёбы и отдыха.\n\n"
    "Здесь царит дружелюбная атмосфера. Студенты поддерживают друг друга, вместе готовятся к занятиям, участвуют в мероприятиях и просто проводят время в приятной компании.\n"
    "Наше общежитие - это не просто здание, а важная часть студенческой жизни, где формируется сплочённый коллектив и создаются яркие воспоминания 🌟📚\n\n"
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
    "Секретарь председателя - Кристина Ильина\n"
    "https://vk.ru/tewass\n\n"
    "Председатель КПД - Олеся Черкасова\n"
    "https://vk.com/xaseef\n\n"
    "Председатель санитарной комиссии - Дарья Докина\n"
    "https://vk.com/daryadokina\n\n"
    "Сотрудник санитарной комиссии - Мария Кунгурова\n"
    "https://vk.ru/marusya_marfaa\n\n"
    "Ответственная за информационную работу (СМИ)- Тазетдинова Лилия\n"
    "https://vk.ru/loonixsson\n\n"
    "Староста 1 этажа - Дарья Сушенцова\n"
    "https://vk.com/uyccigcuuxfurixr\n\n"
    "Староста 3 этажа левого крыла - Егор Иванов\n"
    "https://vk.com/gerka_igor\n\n"
    "Староста 3 этажа правого крыла - Илсаф Хасанзянов\n"
    "https://vk.ru/bigkler\n\n"
    "Староста 4 этажа левого крыла - Зарина Хуснутдинова\n"
    "https://vk.ru/azakatbilalbilalkakkolenochki\n\n"
    "Староста 4 этажа правого крыла - Марк Милишенко\n"
    "https://vk.ru/yyyet\n\n"
    "Командир ГРО - Анис Нуриев\n"
    "https://vk.com/id495552862\n\n"
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
    "• Медицинская справка (форма 086-у)\n"
    "• Копия прививочного сертификата\n"
    "• Фото 3x4 (4 шт)\n"
    "• Несовершеннолетние в обязательном присутсвии отвесвтенного лица\n\n"
    "📄 Документы для проживания на льготной основе:\n"
    "• ...\n\n"
    "📍 Адрес: Большая Красная, 18\n"
    "🗺️ Карта: https://yandex.com/maps/-/CPqMRP3Z\n\n"
    "📞 Контактный телефон: 8 (843) 231-01-29\n"
)

RULES_TEXT = (
    "⚖️ Правила внутреннего распорядка (ПВР)\n\n"
    "🕐 Режим работы:\n"
    "• Вход в общежитие: круглосуточно\n"
    "• Комендантский час: с 22:00 до 06:00 (в летнее время с 23:00 до 06:00)\n\n"
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
    "• Вопросы по постельному белью и прописке\n"
    "• Кабинет: (1 этаж)\n\n"
    "🛡️ Вахтеры:\n"
    "• Круглосуточный пост\n"
    "• Пропускной режим\n\n"
)

LAUNDRY_TEXT = (
    "🧺 Прачечная\n\n"
    "📍 Расположение: первый этаж, конец коридора\n\n"
    "⏰ Режим работы: круглосуточно\n"
    "💰 Стоимость и оплата: \n"
    "• Стиральная машина: 135 руб/стирка\n"
    "• Оплата происходит по ссылке: https://washer.mylaundry.ru/device/pr15kai2\n\n"
    "📋 Правила:\n"
    "• Не оставляйте вещи без присмотра\n"
    "• После использования протрите барабан\n"
    "• Загрузка не более 5 кг\n\n"
    "При возникновении проблем обращаться к технической поддержке по контактам в прачечной\n"
)

GYM_TEXT = (
    "🏋️ Спортивный зал\n\n"
    "📍 Расположение: 1 этаж\n\n"
    "⏰ График работы:\n"
    "• Ежедневно: 17:00 - 22:00\n"
    "• Для попадания в тренажерный зал ключ нужно взять у ответственного (см. Студенческий совет)\n\n"
    "💰 Бесплатно для проживающих (по студенческому)\n\n"
    "📋 Правила:\n"
    "• Занимайтесь в спортивной обуви\n"
    "• Возвращайте инвентарь на место\n"
    "• Убирайте за собой тренажеры\n"
    "• Только для совершенолетних\n"
)

BEGINNERS_TEXT = (
    "⚠️ Для новичков\n\n"
    "🚿 Душ:\n"
    "• Используйте резиновые тапочки\n"
    "• Убирайте средства личной гигиены в свою мусорку\n"
    "• После душа убирайте волосы из слива\n\n"
    "🚽 Туалет:\n"
    "• Не бросайте в унитаз влажные салфетки, вату и средства личной гигиены - засор гарантирован\n"
    "• Опускайте сиденье унитаза после использования\n\n"
    "🍳 Кухня:\n"
    "• Убирайте за собой\n"
    "• Не оставляйте грязную посуду\n"
    "• Не оставляйте продукты\n\n"
    "🧹 Уборка:\n"
    "• Ершик для унитаза используйте ТОЛЬКО в унитазе\n"
    "• Мусор выбрасывайтся только в своей комнате (не в туалеты)\n"
    "• Влажная уборка в комнате - минимум раз в неделю\n\n"
    "💡 Важно:\n"
    "• Чистота зависит от вас\n"
    "• Уважайте соседей, не шумите ночью\n"
    "• Общайтесь с соседями - вместе решать бытовые вопросы легче\n"
    "• Не бойтесь обращаться к студенческому совету - они помогут решить ваши проблемы\n"
    )

JBK_TEXT = (
    "🏗️ Жилищно-бытовая комиссия (ЖБК)\n\n"
    "Что такое ЖБК?\n"
    "Жилищно-бытовая комиссия (ЖБК) в общежитии — это специальная комиссия при учебном заведении, которая занимается вопросами проживания студентов.\n\n"
    "📌 Чем занимается ЖБК:\n"
    "📚 Рассматривает учебную успеваемость (есть ли академические задолженности)\n"
    "⚠️ Рассматривает нарушения за год (замечания, выговоры, нарушения правил проживания)\n"
    "🧹 Рассматривает участие в жизни общежития (посещение субботников, мероприятий, соблюдение порядка)\n"
    "🏠 Рассматриват вопрос о дальнейшем проживании (продление, переселение или отказ в заселении)\n\n"
    "📌 Члены ЖБК:\n"
    "👩‍💼 представитель вуза\n🏢 комендант общежития\n🎓 представители студенческого совета\n"
)

GRO_TEXT = (
    "📦 Группа режима общежития (ГРО)\n\n"
    "Группа режима общежития - добровольное специализированное объединение обучающихся, проживающих вобщежитиях КНИТУ-КАИ, отвечающее за соблюдение правил внутреннегораспорядка в общежитии.\n\n"
    "👤 Командир ГРО:\n"
    "Анис Нуриев - https://vk.com/id495552862\n\n"
    "👥 Сотрудники ГРО:\n"
    "Лия Хасанова - https://vk.ru/wnxptl\n"
    "Софья Талашова - https://vk.ru/sofia_talashova\n"
    "Ганина Екатерина - https://vk.ru/mewsex\n"
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

async def gro_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(GRO_TEXT, reply_markup=BACK_BUTTON)


# ---------- Кнопки ----------
# ---------- Обработка текста (пожелание) ----------
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if context.user_data.get("waiting_feedback"):
        text = update.message.text

        username = update.effective_user.username
        user_info = f"@{username}" if username else update.effective_user.full_name

        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"📩 Новое сообщение:\n\n{text}\n\nОт: {user_info}\nID: {update.effective_user.id}"
        )

        context.user_data["waiting_feedback"] = False

        await update.message.reply_text(
            "Спасибо! Сообщение отправлено ✅",
            reply_markup=main_menu()
        )
    else:
        await update.message.reply_text(
            "Пожалуйста, используйте кнопки меню.",
            reply_markup=main_menu()
        )


# ---------- Отмена ----------
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["waiting_feedback"] = False
    await update.message.reply_text(
        "Отправка отменена.",
        reply_markup=main_menu()
    )

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
    elif query.data == "gro":  
        await query.edit_message_text(GRO_TEXT, reply_markup=BACK_BUTTON)
    elif query.data == "photos":
        await query.message.delete()
        await query.message.reply_photo(
            photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRraowzVn_lO4boU8-NSkLsHCedr7V42kL3tA&s",
            caption="Фасад общежития №2",
            reply_markup=BACK_BUTTON
        )
    elif query.data == "feedback":
        await query.message.delete()
        context.user_data["waiting_feedback"] = True
        await query.message.chat.send_message(
            "Напишите ваше сообщение одним сообщением.\nОбразец: Иванов Иван, 105ком. Сломалась тумбочка.",
            reply_markup=FEEDBACK_BACK_BUTTON
        )
    elif query.data == "back_from_feedback":
        context.user_data["waiting_feedback"] = False
        await query.message.delete()
        await query.message.chat.send_message(
            "Вы в главном меню!\nВыберите раздел:",
            reply_markup=main_menu()
        )
    elif query.data == "back":
    # если сообщение с фото — удаляем его
        if query.message.photo:
            await query.message.delete()
            await query.message.chat.send_message(
                "Вы в главном меню!\nВыберите раздел:",
                reply_markup=main_menu()
            )
        else:
            await query.edit_message_text(
                "Вы в главном меню!\nВыберите раздел:",
                reply_markup=main_menu()
            )


# ---------- Запуск ----------
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Команды
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cancel", cancel))
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
    app.add_handler(CommandHandler("gro", gro_command)) 

    # Кнопки
    app.add_handler(CallbackQueryHandler(buttons))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()