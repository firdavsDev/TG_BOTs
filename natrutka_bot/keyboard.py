from telebot import types
from config import support_link, QIWI_NUMBER, QIWI_NICKNAME, views_list, reviews_link, \
	tiktok_views_list, qiwi_api_link

def main_keyboard():
    reply_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    reply_keyboard.row("🧾Сделать заказ")
    reply_keyboard.row("👤Профиль", "📚Помощь")
    return reply_keyboard

def confirm_keyboard():
	confirm_keyboard = types.InlineKeyboardMarkup()
	button1 = types.InlineKeyboardButton(text="✅Принять", callback_data="confirm")
	confirm_keyboard.row(button1)
	return confirm_keyboard

def profile_keyboard():
	profile_keyboard = types.InlineKeyboardMarkup()
	button1 = types.InlineKeyboardButton(text="💸Пополнить баланс💸", callback_data="deposit")
	profile_keyboard.row(button1)
	return profile_keyboard

def admin_menu_keyboard():
	admin_menu_keyboard = types.InlineKeyboardMarkup()
	button1 = types.InlineKeyboardButton(text="✉️Рассылка", callback_data="mailing_menu")
	button2 = types.InlineKeyboardButton(text="👤Поиск пользователя", callback_data="search_user")
	admin_menu_keyboard.row(button1)
	admin_menu_keyboard.row(button2)
	return admin_menu_keyboard

def service_keyboard():
    reply_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    reply_keyboard.row("👥Подписчики")
    # reply_keyboard.row("👀Просмотры")
    # reply_keyboard.row("❤️Голоса/Лайки")
    reply_keyboard.row("⏪Назад")
    return reply_keyboard

def instagram_service_keyboard():
    reply_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    reply_keyboard.row("👥Подписчики")
    reply_keyboard.row("❤️Лайки")
    reply_keyboard.row("⏪Назад")
    return reply_keyboard

def order_keyboard(service):
	order_keyboard = types.InlineKeyboardMarkup()
	button1 = types.InlineKeyboardButton(text="🔰 Заказать", callback_data=f"order:{service}")
	order_keyboard.row(button1)
	return order_keyboard

def subscribe_type_keyboard():
	reply_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
	reply_keyboard.row("🔗Канал", "🧿Чат")
	return reply_keyboard

def place_type_keyboard():
	reply_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
	reply_keyboard.row("📊Вконтакте")
	reply_keyboard.row("🛒Telegram", "📱TikTok")
	reply_keyboard.row("📷Instagram")
	reply_keyboard.row("⏪Назад")
	return reply_keyboard

def order_chat_keyboard(user_id):
	order_chat_keyboard = types.InlineKeyboardMarkup()
	button1 = types.InlineKeyboardButton(text="✅Начать выполнение", callback_data=f"start_service:{user_id}")
	button2 = types.InlineKeyboardButton(text="❌Отклонить", callback_data=f"stop_service:{user_id}")
	order_chat_keyboard.row(button1)
	order_chat_keyboard.row(button2)
	return order_chat_keyboard

def deposit_methods_keyboard():
	deposit_methods_keyboard = types.InlineKeyboardMarkup()
	button1 = types.InlineKeyboardButton(text="🥝Qiwi", callback_data=f"qiwi_method")
	button2 = types.InlineKeyboardButton(text="🙎‍♂️Через поддержку", url=support_link)
	deposit_methods_keyboard.row(button1)
	deposit_methods_keyboard.row(button2)
	return deposit_methods_keyboard

# def deposit_keyboard(comment):
# 	deposit_btn = types.InlineKeyboardMarkup(row_width=2)
# 	from functions import get_payment_url
# 	deposit_btn.add(
# 		types.InlineKeyboardButton(text='💸Оплатить💸', url=get_payment_url(comment, QIWI_NUMBER)))
# 	deposit_btn.add(
# 		types.InlineKeyboardButton(text='🔁Проверить платёж', callback_data='check_deposit'),
# 		types.InlineKeyboardButton(text='❌Отменить', callback_data='del_deposit')
# 		)
# 	return deposit_btn

def deposit_keyboard(comment):
	deposit_btn = types.InlineKeyboardMarkup(row_width=2)
	from functions import get_nickname_payment_url
	deposit_btn.add(
		types.InlineKeyboardButton(text='💸Оплатить💸', url=get_nickname_payment_url(QIWI_NICKNAME)))
	deposit_btn.add(
		types.InlineKeyboardButton(text='🔁Проверить платёж', callback_data='check_deposit'),
		types.InlineKeyboardButton(text='❌Отменить', callback_data='del_deposit')
		)
	return deposit_btn

def delete_message_keyboard():
	delete_message_keyboard = types.InlineKeyboardMarkup()
	button1 = types.InlineKeyboardButton(text="❌Закрыть", callback_data=f"delete_message")
	delete_message_keyboard.row(button1)
	return delete_message_keyboard

def views_keyboard():
	views_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
	views_keyboard.row("Автопросмотры")
	views_keyboard.row(views_list[0], views_list[1])
	views_keyboard.row(views_list[2], views_list[3])
	views_keyboard.row(views_list[4])
	return views_keyboard

def search_keyboard(user_id):
	search_keyboard = types.InlineKeyboardMarkup()
	button1 = types.InlineKeyboardButton(text="Изменить баланс", callback_data=f"change_balance:{user_id}")
	button2 = types.InlineKeyboardButton(text="Бан", callback_data=f"ban_user:{user_id}")
	button3 = types.InlineKeyboardButton(text="Разбан", callback_data=f"unban_user:{user_id}")
	button4 = types.InlineKeyboardButton(text="Закрыть", callback_data=f"delete_message")
	search_keyboard.row(button1)
	search_keyboard.row(button2, button3)
	search_keyboard.row(button4)
	return search_keyboard

def help_keyboard():
	help_keyboard = types.InlineKeyboardMarkup(row_width=1)
	button1 = types.InlineKeyboardButton(text="💊 Отзывы", url=reviews_link)
	button2 = types.InlineKeyboardButton(text="🥝Qiwi Api", url=qiwi_api_link)
	help_keyboard.row(button1, button2)
	return help_keyboard

def vk_service_keyboard():
	reply_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
	reply_keyboard.row("👥Друзья")
	reply_keyboard.row("📨Сообщения")
	reply_keyboard.row("👨‍👩‍👦‍👦Группа")
	reply_keyboard.row("⏪Назад")
	return reply_keyboard

def tiktok_views_keyboard():
	views_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
	views_keyboard.row("Автопросмотры")
	views_keyboard.row(tiktok_views_list[0], tiktok_views_list[1])
	return views_keyboard