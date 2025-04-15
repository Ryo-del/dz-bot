import telebot
from telebot import types

TOKEN = "7582375690:AAHOzDEALtSjbiovqytc6cj0p1xwj_m_0nU"
bot = telebot.TeleBot(TOKEN)

ADMINS = ["1362070521", "7489804706", "1651329326", "7838731891", "5232945440", "932682372", 
          "7764018720", "5454631966", "1519783582", "1281151146", "5577471928", "1778547155", 
          "1613296671", "1193471283", "5272407016", "1927564001", "1357689799", "5213564548", 
          "5267033413", "1893898836", "1378106961", "805415400", "1635411621","962449094"]
romaks_ID = "5675488166" 
Moders = ["962449094","1635411621"] 


dz_math = "нет дз"
dz_informatics = "нет дз"
dz_physics = "нет дз"
dz_rus = "нет дз"
dz_biology = "нет дз"      
dz_lith = "нет дз" 
dz_english_113 = "нет дз" 
dz_english_208 = "нет дз" 
dz_history = "нет дз"
dz_society = "нет дз"
dz_chemistry = "нет дз"


notifi_player = ["962449094"]



@bot.message_handler(commands=['start'])
def main(message):
    global notification_text
    global notification_action
    user_id = str(message.from_user.id)
    notification_text = "Включить уведомления☎️" if user_id not in notifi_player else "Выключить уведомления☎️"
    notification_action = "yes" if user_id not in notifi_player else "no"
    if user_id == romaks_ID:
        bot.send_message(message.chat.id, 'РОМFLEXX иди нахуй')
        return
    
    # Определяем текст и действие для кнопки
    if user_id in ADMINS:
        text_vere = "✏️ Редактировать"
        action_vere = "edit" 
    else:
        text_vere = "🔒 Снять бан"
        action_vere = "vere"
    
    # Создаем клавиатуру
    markup = types.InlineKeyboardMarkup(row_width=2)
    but1 = types.InlineKeyboardButton("Математика📐", callback_data='math')
    but2 = types.InlineKeyboardButton("Информатика👨🏻‍💻", callback_data='informath')
    but3 = types.InlineKeyboardButton("Физика⚛️", callback_data='physics')
    but4 = types.InlineKeyboardButton("Русский язык✍", callback_data='rus')
    but5 = types.InlineKeyboardButton("Биология🧬", callback_data='biology')
    but6 = types.InlineKeyboardButton("Литература📖", callback_data="lith")
    but7 = types.InlineKeyboardButton("Английский язык💂(113)", callback_data='english_113')
    but8 = types.InlineKeyboardButton("Английский язык💂(208)",callback_data='english_208')
    but9 = types.InlineKeyboardButton("История🕰️", callback_data="history")
    but10 = types.InlineKeyboardButton("Обществознание📜",callback_data="society")
    but11 = types.InlineKeyboardButton("Химия🧪",callback_data="chemistry")
    but13 = types.InlineKeyboardButton(text_vere, callback_data=action_vere)
 #   but14 = types.InlineKeyboardButton(notification_text, callback_data=notification_action)
    but15 = types.InlineKeyboardButton("Панель управления🕹️", callback_data="mod_panel")
    
    
    markup.add(but1, but2, but3, but4, but5, but6, but7, but8, but9, but10, but11, but13, but15)
    bot.send_message(message.chat.id, 'Выбери предмет 📚', reply_markup=markup)
   

        
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    user_id = str(call.from_user.id)
    if call.data == "math":
        bot.send_message(call.message.chat.id, dz_math)
    elif call.data == "informath":
        bot.send_message(call.message.chat.id, dz_informatics)
    elif call.data == "edit_math":  # Объединил логику редактирования
        msg = bot.send_message(call.message.chat.id, 'Введи новое ДЗ по математике:')
        bot.register_next_step_handler(msg, process_math_input)
    elif call.data == "edit_informath":
        msg = bot.send_message(call.message.chat.id, 'Введи новое ДЗ по информатике:')
        bot.register_next_step_handler(msg, process_informatics_input)
    elif call.data == "physics":
        bot.send_message(call.message.chat.id,dz_physics)
    elif call.data == ("edit_physics"):
        msg = bot.send_message(call.message.chat.id,'Введи новое ДЗ по физике:')
        bot.register_next_step_handler(msg ,process_physics_input)
    elif call.data == "rus":
        bot.send_message(call.message.chat.id,dz_rus)
    elif call.data == ("edit_rus"):
        msg = bot.send_message(call.message.chat.id,'Введи новое ДЗ по русскому языку:')
        bot.register_next_step_handler(msg ,process_rus_input)
    elif call.data == "biology":
        bot.send_message(call.message.chat.id,dz_biology)
    elif call.data == ("edit_biology"):
        msg = bot.send_message(call.message.chat.id,'Введи новое ДЗ по биологии:')
        bot.register_next_step_handler(msg ,process_biology_input)
    elif call.data == "lith":
        bot.send_message(call.message.chat.id,dz_lith)
    elif call.data == ("edit_lith"):
        msg = bot.send_message(call.message.chat.id,'Введи новое ДЗ по литературе:')
        bot.register_next_step_handler(msg ,process_lith_input)
    elif call.data == "english_113":
        bot.send_message(call.message.chat.id,dz_english_113)
    elif call.data == ("edit_english_113"):
        msg = bot.send_message(call.message.chat.id,'Введи новое ДЗ по английсому языку(113):')
        bot.register_next_step_handler(msg ,process_english_113_input)
    elif call.data == "english_208":
        bot.send_message(call.message.chat.id,dz_english_208)
    elif call.data == ("edit_english_208"):
        msg = bot.send_message(call.message.chat.id,'Введи новое ДЗ по английскому языку(208):')
        bot.register_next_step_handler(msg ,process_english_208_input)
    elif call.data == "history":
        bot.send_message(call.message.chat.id,dz_history)
    elif call.data == ("edit_history"):
        msg = bot.send_message(call.message.chat.id,'Введи новое ДЗ по истории:')
        bot.register_next_step_handler(msg ,process_history_input)
    elif call.data == "society":
        bot.send_message(call.message.chat.id,dz_society)
    elif call.data == ("edit_society"):
        msg = bot.send_message(call.message.chat.id,'Введи новое ДЗ по обществознанию:')
        bot.register_next_step_handler(msg ,process_society_input)
    elif call.data == "chemistry":
        bot.send_message(call.message.chat.id,dz_chemistry)
    elif call.data == ("edit_chemistry"):
        msg = bot.send_message(call.message.chat.id,'Введи новое ДЗ по химии:')
        bot.register_next_step_handler(msg ,process_chemistry_input)
    elif call.data == "vere":
        msg = bot.send_message(call.message.chat.id, "Введи пароль:")
        bot.register_next_step_handler(msg, password_check)
    elif call.data == "edit":
         # Удаляем старое сообщение
        bot.delete_message(call.message.chat.id, call.message.message_id)    # Отправляем новое сообщение с обновленными кнопками            
        edit_panel(call.message)
    elif call.data == "mod_panel":
        if str(call.from_user.id) in Moders:
            moders_panel(call.message)
        else:
            bot.send_message(call.message.chat.id, "Вы не являетесь Модератором!")
    elif call.data == "ban":
        msg = bot.send_message(call.message.chat.id, "Введи username пользователя (без @), которого нужно лишить админки:")
        bot.register_next_step_handler(msg, ban_user)
    elif call.data == "unban":
        msg = bot.send_message(call.message.chat.id, "Введи username пользователя (без @), которого нужно вернуть в админы:")
        bot.register_next_step_handler(msg, unban_user)
    elif call.data == "yes":
        if user_id not in notifi_player:
            notifi_player.append(user_id)
             # Удаляем старое сообщение
            bot.delete_message(call.message.chat.id, call.message.message_id)
    # Отправляем новое сообщение с обновленными кнопками
            main(call.message)
    elif call.data == "no":
        if user_id in notifi_player:
            notifi_player.remove(user_id)
        # Удаляем старое сообщение
            bot.delete_message(call.message.chat.id, call.message.message_id)
    # Отправляем новое сообщение с обновленными кнопками
            main(call.message)

    

def edit_panel(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("✏️ Математика", callback_data='edit_math'),
        types.InlineKeyboardButton("✏️ Информатика", callback_data='edit_informath'),
        types.InlineKeyboardButton("✏️ Физика", callback_data='edit_physics'),
        types.InlineKeyboardButton("✏️ Русский язык", callback_data='edit_rus'),
        types.InlineKeyboardButton("✏️ Биология", callback_data='edit_biology'),
        types.InlineKeyboardButton("✏️ Литература", callback_data='edit_lith'),  
        types.InlineKeyboardButton("✏️ Английский язык(113)", callback_data='edit_english_133'),
        types.InlineKeyboardButton("✏️ Английский язык(208)", callback_data='edit_english_208'),
        types.InlineKeyboardButton("✏️ История", callback_data='edit_history'),
        types.InlineKeyboardButton("✏️ Обществознание", callback_data='edit_society'),
        types.InlineKeyboardButton("✏️ Химия", callback_data='edit_chemistry')
    )
    bot.send_message(message.chat.id, 'Выбери предмет для редактирования:', reply_markup=markup)

def ban_user(message):
    global username
    username = message.text.strip()
    if username in ADMINS:
        ADMINS.remove(username)
        bot.send_message(message.chat.id, f"Пользователь @{username} больше не админ")
    else:
        bot.send_message(message.chat.id, f"Пользователь @{username} не найден среди админов")

def unban_user(message):
    username = message.text.strip()
    if username not in ADMINS:
        ADMINS.append(username)
        bot.send_message(message.chat.id, f"Пользователь @{username} снова админ")
    else:
        bot.send_message(message.chat.id, f"Пользователь @{username} уже админ")
def moders_panel(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("Забрать админку⛔", callback_data='ban'),
        types.InlineKeyboardButton("Вернуть админку✅", callback_data='unban'),
    )
    bot.send_message(message.chat.id, "Панель модератора:", reply_markup=markup)
def process_math_input(message):
    global dz_math
    user_id = str(message.from_user.id)
    user_name = message.from_user.first_name  # Имя пользователя
    username = f"@{message.from_user.username}" if message.from_user.username else "без username"  # @username если есть
    dz_math = message.text.strip()
    bot.send_message(message.chat.id, f"✅ ДЗ по математике обновлено:\n{dz_math}")
    moderators = ["1635411621", "962449094"]
    # Отправляем каждому модератору отдельно
    for moderator_id in moderators:
        try:
            bot.send_message(
                moderator_id,
                f"✅ ДЗ по математике обновлено пользователем:\n"
                f"Имя: {user_name}\n"
                f"Username: {username}\n"
                f"ID: {user_id}\n"
                f"Новое ДЗ: {dz_math}"
            )
        except Exception as e:
            print(f"Ошибка отправки модератору {moderator_id}: {e}")
def process_informatics_input(message):
    global dz_informatics
    user_id = str(message.from_user.id)
    user_name = message.from_user.first_name  # Имя пользователя
    username = f"@{message.from_user.username}" if message.from_user.username else "без username"  # @username если есть
    dz_informatics = message.text.strip()
    bot.send_message(message.chat.id, f"✅ ДЗ по информатике обновлено:\n{dz_informatics}")
    moderators = ["1635411621", "962449094"]
    # Отправляем каждому модератору отдельно
    for moderator_id in moderators:
        try:
            bot.send_message(
                moderator_id,
                f"✅ ДЗ по информатике обновлено пользователем:\n"
                f"Имя: {user_name}\n"
                f"Username: {username}\n"
                f"ID: {user_id}\n"
                f"Новое ДЗ: {dz_informatics}"
            )
        except Exception as e:
            print(f"Ошибка отправки модератору {moderator_id}: {e}")

def process_physics_input(message):
    global dz_physics
    user_id = str(message.from_user.id)
    user_name = message.from_user.first_name  # Имя пользователя
    username = f"@{message.from_user.username}" if message.from_user.username else "без username"  # @username если есть
    dz_physics = message.text.strip()
    bot.send_message(message.chat.id, f"✅ ДЗ по физике обновлено:\n{dz_physics}")
    moderators = ["1635411621", "962449094"]
    # Отправляем каждому модератору отдельно
    for moderator_id in moderators:
        try:
            bot.send_message(
                moderator_id,
                f"✅ ДЗ по физике обновлено пользователем:\n"
                f"Имя: {user_name}\n"
                f"Username: {username}\n"
                f"ID: {user_id}\n"
                f"Новое ДЗ: {dz_physics}"
            )
        except Exception as e:
            print(f"Ошибка отправки модератору {moderator_id}: {e}")
def process_rus_input(message):
    global dz_rus
    user_id = str(message.from_user.id)
    user_name = message.from_user.first_name  # Имя пользователя
    username = f"@{message.from_user.username}" if message.from_user.username else "без username"  # @username если есть
    dz_rus = message.text.strip()
    bot.send_message(message.chat.id, f"✅ ДЗ по русскому языку обновлено:\n{dz_rus}")
    moderators = ["1635411621", "962449094"]
    # Отправляем каждому модератору отдельно
    for moderator_id in moderators:
        try:
            bot.send_message(
                moderator_id,
                f"✅ ДЗ по русскому обновлено пользователем:\n"
                f"Имя: {user_name}\n"
                f"Username: {username}\n"
                f"ID: {user_id}\n"
                f"Новое ДЗ: {dz_rus}"
            )
        except Exception as e:
            print(f"Ошибка отправки модератору {moderator_id}: {e}")

def process_biology_input(message):
    global dz_biology
    user_id = str(message.from_user.id)
    user_name = message.from_user.first_name  # Имя пользователя
    username = f"@{message.from_user.username}" if message.from_user.username else "без username"  # @username если есть
    dz_biology  = message.text.strip()
    bot.send_message(message.chat.id, f"✅ ДЗ по биологии обновлено:\n{dz_biology}")
    moderators = ["1635411621", "962449094"]
    # Отправляем каждому модератору отдельно
    for moderator_id in moderators:
        try:
            bot.send_message(
                moderator_id,
                f"✅ ДЗ по биологии обновлено пользователем:\n"
                f"Имя: {user_name}\n"
                f"Username: {username}\n"
                f"ID: {user_id}\n"
                f"Новое ДЗ: {dz_biology}"
            )
        except Exception as e:
            print(f"Ошибка отправки модератору {moderator_id}: {e}")
def process_lith_input(message):
    global dz_lith
    user_id = str(message.from_user.id)
    user_name = message.from_user.first_name  # Имя пользователя
    username = f"@{message.from_user.username}" if message.from_user.username else "без username"  # @username если есть
    dz_lith = message.text.strip()
    bot.send_message(message.chat.id, f"✅ ДЗ по литературе обновлено:\n{dz_lith}")
    moderators = ["1635411621", "962449094"]
    # Отправляем каждому модератору отдельно
    for moderator_id in moderators:
        try:
            bot.send_message(
                moderator_id,
                f"✅ ДЗ по литературе обновлено пользователем:\n"
                f"Имя: {user_name}\n"
                f"Username: {username}\n"
                f"ID: {user_id}\n"
                f"Новое ДЗ: {dz_lith}"
            )
        except Exception as e:
            print(f"Ошибка отправки модератору {moderator_id}: {e}")
def process_english_113_input(message):
    global dz_english_113
    user_id = str(message.from_user.id)
    user_name = message.from_user.first_name  # Имя пользователя
    username = f"@{message.from_user.username}" if message.from_user.username else "без username"  # @username если есть
    dz_english_113 = message.text.strip()
    bot.send_message(message.chat.id, f"✅ ДЗ по английскому языку(113) обновлено:\n{dz_english_113}")
    moderators = ["1635411621", "962449094"]
    # Отправляем каждому модератору отдельно
    for moderator_id in moderators:
        try:
            bot.send_message(
                moderator_id,
                f"✅ ДЗ по английскому языку(113) обновлено пользователем:\n"
                f"Имя: {user_name}\n"
                f"Username: {username}\n"
                f"ID: {user_id}\n"
                f"Новое ДЗ: {dz_english_113}"
            )
        except Exception as e:
            print(f"Ошибка отправки модератору {moderator_id}: {e}")
def process_english_208_input(message):
    global dz_english_208
    user_id = str(message.from_user.id)
    user_name = message.from_user.first_name  # Имя пользователя
    username = f"@{message.from_user.username}" if message.from_user.username else "без username"  # @username если есть
    dz_english_208 = message.text.strip()
    bot.send_message(message.chat.id, f"✅ ДЗ по английскому языку(208) обновлено:\n{dz_english_208}")
    moderators = ["1635411621", "962449094"]
    # Отправляем каждому модератору отдельно
    for moderator_id in moderators:
        try:
            bot.send_message(
                moderator_id,
                f"✅ ДЗ по английскому языку(208) обновлено пользователем:\n"
                f"Имя: {user_name}\n"
                f"Username: {username}\n"
                f"ID: {user_id}\n"
                f"Новое ДЗ: {dz_english_208}"
            )
        except Exception as e:
            print(f"Ошибка отправки модератору {moderator_id}: {e}")
def process_history_input(message):
    global dz_history
    user_id = str(message.from_user.id)
    user_name = message.from_user.first_name  # Имя пользователя
    username = f"@{message.from_user.username}" if message.from_user.username else "без username"  # @username если есть
    dz_history = message.text.strip()
    bot.send_message(message.chat.id, f"✅ ДЗ по истории обновлено:\n{dz_history}")
    moderators = ["1635411621", "962449094"]
    # Отправляем каждому модератору отдельно
    for moderator_id in moderators:
        try:
            bot.send_message(
                moderator_id,
                f"✅ ДЗ по биологии обновлено пользователем:\n"
                f"Имя: {user_name}\n"
                f"Username: {username}\n"
                f"ID: {user_id}\n"
                f"Новое ДЗ: {dz_biology}"
            )
        except Exception as e:
            print(f"Ошибка отправки модератору {moderator_id}: {e}")
def process_society_input(message):
    global dz_society
    user_id = str(message.from_user.id)
    user_name = message.from_user.first_name  # Имя пользователя
    username = f"@{message.from_user.username}" if message.from_user.username else "без username"  # @username если есть
    dz_society = message.text.strip()
    bot.send_message(message.chat.id, f"✅ ДЗ по обществознанию обновлено:\n{dz_society}")
    moderators = ["1635411621", "962449094"]
    # Отправляем каждому модератору отдельно
    for moderator_id in moderators:
        try:
            bot.send_message(
                moderator_id,
                f"✅ ДЗ по обществознанию обновлено пользователем:\n"
                f"Имя: {user_name}\n"
                f"Username: {username}\n"
                f"ID: {user_id}\n"
                f"Новое ДЗ: {dz_society}"
            )
        except Exception as e:
            print(f"Ошибка отправки модератору {moderator_id}: {e}")
def process_chemistry_input(message):
    global dz_chemistry
    user_id = str(message.from_user.id)
    user_name = message.from_user.first_name  # Имя пользователя
    username = f"@{message.from_user.username}" if message.from_user.username else "без username"  # @username если есть
    dz_chemistry = message.text.strip()
    bot.send_message(message.chat.id, f"✅ ДЗ по химии обновлено:\n{dz_chemistry}")
    moderators = ["1635411621", "962449094"]
    # Отправляем каждому модератору отдельно
    for moderator_id in moderators:
        try:
            bot.send_message(
                moderator_id,
                f"✅ ДЗ по химии обновлено пользователем:\n"
                f"Имя: {user_name}\n"
                f"Username: {username}\n"
                f"ID: {user_id}\n"
                f"Новое ДЗ: {dz_chemistry}"
            )
        except Exception as e:
            print(f"Ошибка отправки модератору {moderator_id}: {e}")
    
def password_check(message):
    global ADMINS
    password = "admin_p24"  
    user_input = message.text.strip()
    user_id = str(message.from_user.id)
    
    if user_input == password:
        if user_id not in ADMINS:
            ADMINS.append(user_id)
        bot.send_message(message.chat.id, "✅ Пароль верный! Теперь вы администратор.")
    else:
        bot.send_message(message.chat.id, "❌ Неверный пароль")

bot.polling(none_stop=True)
