import random
import sqlite3
import datetime
from config import bot, sub_price, ref_price, like_price, admin_chat, search_user_text, \
	vk_friends_price, instagram_like_price, instagram_sub_price, vk_message_price
from keyboard import order_chat_keyboard, main_keyboard, search_keyboard
import requests

def get_reg_time():
	date = datetime.datetime.today().strftime("%d.%m.%Y %H:%M")
	return date

def join_to_db(user_id):
	db = sqlite3.connect("database.db")
	cursor = db.cursor()
	cursor.execute(f"""INSERT INTO users(user_id, balance, reg_time, banned) VALUES('{user_id}', 0, '{get_reg_time()}', 'False')""")
	db.commit()

def get_user(user_id):
	db = sqlite3.connect("database.db")
	cursor = db.cursor()
	cursor.execute(f"""SELECT * FROM users WHERE user_id = '{user_id}' """)
	row = cursor.fetchone()
	return row

def edit_balance(user_id, amount):
	db = sqlite3.connect("database.db")
	cursor = db.cursor()
	cursor.execute(f"""UPDATE users SET balance = '{amount}' WHERE user_id = '{user_id}' """)
	db.commit()

def order_likes(message):
	user_id = message.chat.id
	try:	
		amount = int(message.text)
		price = amount * like_price
		if amount >= 10:
			if get_user(user_id)[1] >= price:
				bot.send_message(chat_id=user_id, text="<b>Отправьте ссылку на запись куда хотите накрутить лайки.</b>", parse_mode="HTML")
				bot.register_next_step_handler(message, order_likes1, price, amount=amount)
			else:
				bot.send_message(chat_id=user_id, text="<b>❗️ У вас недостаточно средств. Пополните баланс.</b>", parse_mode="HTML")	
				from main import telegram_service_menu
				bot.register_next_step_handler(message, telegram_service_menu)
		else:
			bot.send_message(chat_id=user_id, text="<b>❗️ Минимальный заказ равен 10.</b>", parse_mode="HTML")
			from main import telegram_service_menu
			bot.register_next_step_handler(message, telegram_service_menu)

	except:
		bot.send_message(chat_id=user_id, text="<b>❗️ Вводите цифрами.</b>", parse_mode="HTML")
		from main import telegram_service_menu
		bot.register_next_step_handler(message, telegram_service_menu)

def order_likes1(message, price, amount=None, type_order="❤️Голоса/Лайки"):
	link = message.text
	user_id = message.chat.id
	balance = get_user(user_id)[1]
	balance -= price
	edit_balance(user_id, balance)
	bot.send_message(chat_id=user_id,
					text="<b>Ваша заявка на накрутку была принята.</b>",
					parse_mode="HTML",
					reply_markup=main_keyboard())
	bot.send_message(chat_id=admin_chat, text=f"<b>Новый заказ от <a href='tg://user?id={user_id}'>пользователя</a>!</b>\n\n"
					f"Услуга: {type_order}\n"
					f"Ссылка: <code>{link}</code>\n"
					f"Количество: <code>{amount}</code>\n"
					f"ID: {user_id}\n",
					reply_markup=order_chat_keyboard(user_id),
					parse_mode="HTML")
	from main import main_menu
	bot.register_next_step_handler(message, main_menu)

def order_tiktok_subscribe(message):
	user_id = message.chat.id
	try:	
		amount = int(message.text)
		price = amount * sub_price
		if amount >= 10:
			if get_user(user_id)[1] >= price:
				bot.send_message(chat_id=user_id, text="<b>Отправьте ссылку на аккаунт куда хотите накрутить подписчиков.</b>", parse_mode="HTML")
				bot.register_next_step_handler(message, order_likes1, price, amount=amount, type_order="Подписчики в тикток")
			else:
				bot.send_message(chat_id=user_id, text="<b>❗️ У вас недостаточно средств. Пополните баланс.</b>", parse_mode="HTML")	
				from main import tiktok_service_menu
				bot.register_next_step_handler(message, tiktok_service_menu)
		else:
			bot.send_message(chat_id=user_id, text="<b>❗️ Минимальный заказ равен 10.</b>", parse_mode="HTML")
			from main import tiktok_service_menu
			bot.register_next_step_handler(message, tiktok_service_menu)
	except:
		bot.send_message(chat_id=user_id, text="<b>❗️ Вводите цифрами.</b>", parse_mode="HTML")
		from main import tiktok_service_menu
		bot.register_next_step_handler(message, tiktok_service_menu)

def order_tiktok_likes(message):
	user_id = message.chat.id
	try:	
		amount = int(message.text)
		price = amount * like_price
		if amount >= 10:
			if get_user(user_id)[1] >= price:
				bot.send_message(chat_id=user_id, text="<b>Отправьте ссылку на запись куда хотите накрутить лайки.</b>", parse_mode="HTML")
				bot.register_next_step_handler(message, order_likes1, price, amount=amount, type_order="Лайки в тикток")
			else:
				bot.send_message(chat_id=user_id, text="<b>❗️ У вас недостаточно средств. Пополните баланс.</b>", parse_mode="HTML")	
				from main import tiktok_service_menu
				bot.register_next_step_handler(message, tiktok_service_menu)
		else:
			bot.send_message(chat_id=user_id, text="<b>❗️ Минимальный заказ равен 10.</b>", parse_mode="HTML")
			from main import tiktok_service_menu
			bot.register_next_step_handler(message, tiktok_service_menu)

	except:
		bot.send_message(chat_id=user_id, text="<b>❗️ Вводите цифрами.</b>", parse_mode="HTML")
		from main import tiktok_service_menu
		bot.register_next_step_handler(message, tiktok_service_menu)

def order_subscribe(message):
	user_id = message.chat.id
	if message.text == "🔗Канал":
		bot.send_message(chat_id=user_id,
							text="<i>Введите количество подписчиков которое хотите накрутить</i>",
							parse_mode="HTML")

		bot.register_next_step_handler(message, order_subscribe1, ref_price, type_order=message.text)
	elif message.text == "🧿Чат":
		bot.send_message(chat_id=user_id,
							text="<i>Введите количество участников которое хотите накрутить</i>",
							parse_mode="HTML")
		bot.register_next_step_handler(message, order_subscribe1, sub_price, type_order=message.text)
	else:
		bot.send_message(chat_id=user_id, text="<b>❗️ Произошла ошибка.</b>", parse_mode="HTML")
		from main import telegram_service_menu
		bot.register_next_step_handler(message, telegram_service_menu)

def order_subscribe1(message, one_price, type_order):
	user_id = message.chat.id
	try:	
		amount = int(message.text)
		price = amount * one_price
		if amount >= 10:
			if get_user(user_id)[1] >= price:
				bot.send_message(chat_id=user_id, text="<b>Отправьте ссылку на запись куда хотите накрутить подписчиков/рефкралов.</b>", parse_mode="HTML")
				bot.register_next_step_handler(message, order_likes1, price, amount=amount, type_order=type_order)
			else:
				bot.send_message(chat_id=user_id, text="<b>❗️ У вас недостаточно средств. Пополните баланс.</b>", parse_mode="HTML")	
				from main import telegram_service_menu
				bot.register_next_step_handler(message, telegram_service_menu)
		else:
			bot.send_message(chat_id=user_id, text="<b>❗️ Минимальный заказ равен 10.</b>", parse_mode="HTML")
			from main import telegram_service_menu
			bot.register_next_step_handler(message, telegram_service_menu)

	except:
		bot.send_message(chat_id=user_id, text="<b>❗️ Вводите цифрами.</b>", parse_mode="HTML")
		from main import telegram_service_menu
		bot.register_next_step_handler(message, telegram_service_menu)

def order_vk_friends(message):
	user_id = message.chat.id
	user = get_user(user_id)
	token = message.text
	if user[1] >= vk_friends_price:
		balance = get_user(user_id)[1]
		balance -= vk_friends_price
		edit_balance(user_id, balance)
		bot.send_message(chat_id=user_id,
						text="<b>Ваша заявка на накрутку была принята.</b>",
						parse_mode="HTML",
						reply_markup=main_keyboard())
		bot.send_message(chat_id=admin_chat, text=f"<b>Новый заказ от <a href='tg://user?id={user_id}'>пользователя</a>!</b>\n\n"
						f"Услуга: Друзья в VK\n"
						f"Токен: <code>{token}</code>\n"
						f"ID: <code>{user_id}</code>\n",
						reply_markup=order_chat_keyboard(user_id),
						parse_mode="HTML")
		from main import main_menu
		bot.register_next_step_handler(message, main_menu)
	else:
		bot.send_message(chat_id=user_id, text="<b>❗️ У вас недостаточно средств. Пополните баланс.</b>", parse_mode="HTML")

def order_instagram_likes(message):
	user_id = message.chat.id
	try:	
		amount = int(message.text)
		price = amount * instagram_like_price
		if amount >= 10:
			if get_user(user_id)[1] >= price:
				bot.send_message(chat_id=user_id, text="<b>Отправьте ссылку на запись куда хотите накрутить лайки.</b>", parse_mode="HTML")
				bot.register_next_step_handler(message, order_likes1, price, amount=amount, type_order="Лайки в Instagram")
			else:
				bot.send_message(chat_id=user_id, text="<b>❗️ У вас недостаточно средств. Пополните баланс.</b>", parse_mode="HTML")	
				from main import instagram_service_menu
				bot.register_next_step_handler(message, instagram_service_menu)
		else:
			bot.send_message(chat_id=user_id, text="<b>❗️ Минимальный заказ равен 10.</b>", parse_mode="HTML")
			from main import instagram_service_menu
			bot.register_next_step_handler(message, instagram_service_menu)

	except:
		bot.send_message(chat_id=user_id, text="<b>❗️ Вводите цифрами.</b>", parse_mode="HTML")
		from main import instagram_service_menu
		bot.register_next_step_handler(message, instagram_service_menu)

def order_instagram_subscribe(message):
	user_id = message.chat.id
	try:
		amount = int(message.text)
		price = amount * instagram_sub_price
		if amount >= 100:
			if get_user(user_id)[1] >= price:
				bot.send_message(chat_id=user_id, text="<b>Отправьте ссылку на аккаунт куда хотите накрутить подписчиков.</b>", parse_mode="HTML")
				bot.register_next_step_handler(message, order_likes1, price, amount=amount, type_order="Подписчики в Instagram")
			else:
				bot.send_message(chat_id=user_id, text="<b>❗️ У вас недостаточно средств. Пополните баланс.</b>", parse_mode="HTML")	
				from main import instagram_service_menu
				bot.register_next_step_handler(message, instagram_service_menu)
		else:
			bot.send_message(chat_id=user_id, text="<b>❗️ Минимальный заказ равен 100.</b>", parse_mode="HTML")
			from main import instagram_service_menu
			bot.register_next_step_handler(message, instagram_service_menu)
	except:
		bot.send_message(chat_id=user_id, text="<b>❗️ Вводите цифрами.</b>", parse_mode="HTML")
		from main import instagram_service_menu
		bot.register_next_step_handler(message, instagram_service_menu)

def order_vk_subscribers(message):
	user_id = message.chat.id
	try:
		amount = int(message.text)
		price = amount * sub_price
		if amount >= 100:
			if get_user(user_id)[1] >= price:
				bot.send_message(chat_id=user_id, text="<b>Отправьте ссылку на аккаунт куда хотите накрутить подписчиков.</b>", parse_mode="HTML")
				bot.register_next_step_handler(message, order_likes1, price, amount=amount, type_order="Подписчики в Паблик Вконтакте")
			else:
				bot.send_message(chat_id=user_id, text="<b>❗️ У вас недостаточно средств. Пополните баланс.</b>", parse_mode="HTML")	
				from main import vk_service_menu
				bot.register_next_step_handler(message, vk_service_menu)
		else:
			bot.send_message(chat_id=user_id, text="<b>❗️ Минимальный заказ равен 100.</b>", parse_mode="HTML")
			from main import vk_service_menu
			bot.register_next_step_handler(message, vk_service_menu)
	except:
		bot.send_message(chat_id=user_id, text="<b>❗️ Вводите цифрами.</b>", parse_mode="HTML")
		from main import vk_service_menu
		bot.register_next_step_handler(message, vk_service_menu)

def order_vk_messages(message):
	user_id = message.chat.id
	try:
		amount = int(message.text)
		price = amount * vk_message_price
		if amount >= 100:
			if get_user(user_id)[1] >= price:
				bot.send_message(chat_id=user_id, text="<b>Отправьте токен аккаунта куда хотите накрутить сообщения.</b>", parse_mode="HTML")
				bot.register_next_step_handler(message, order_vk_messages1, price, amount)
			else:
				bot.send_message(chat_id=user_id, text="<b>❗️ У вас недостаточно средств. Пополните баланс.</b>", parse_mode="HTML")	
				from main import vk_service_menu
				bot.register_next_step_handler(message, vk_service_menu)
		else:
			bot.send_message(chat_id=user_id, text="<b>❗️ Минимальный заказ равен 100.</b>", parse_mode="HTML")
			from main import vk_service_menu
			bot.register_next_step_handler(message, vk_service_menu)
	except:
		bot.send_message(chat_id=user_id, text="<b>❗️ Вводите цифрами.</b>", parse_mode="HTML")
		from main import vk_service_menu
		bot.register_next_step_handler(message, vk_service_menu)

def order_vk_messages1(message, price, amount):
	user_id = message.chat.id
	user = get_user(user_id)
	token = message.text
	if user[1] >= price:
		balance = get_user(user_id)[1]
		balance -= price
		edit_balance(user_id, balance)
		bot.send_message(chat_id=user_id,
						text="<b>Ваша заявка на накрутку была принята.</b>",
						parse_mode="HTML",
						reply_markup=main_keyboard())
		bot.send_message(chat_id=admin_chat, text=f"<b>Новый заказ от <a href='tg://user?id={user_id}'>пользователя</a>!</b>\n\n"
						f"Услуга: Сообщения в VK\n"
						f"Токен: <code>{token}</code>\n"
						f"Количество: <code>{amount}</code>\n"
						f"ID: <code>{user_id}</code>\n",
						reply_markup=order_chat_keyboard(user_id),
						parse_mode="HTML")
		from main import main_menu
		bot.register_next_step_handler(message, main_menu)
	else:
		bot.send_message(chat_id=user_id, text="<b>❗️ У вас недостаточно средств. Пополните баланс.</b>", parse_mode="HTML")

def mailing(message):
	user_id = message.chat.id
	text = message.text
	bot.send_message(chat_id=user_id, text="Введите + для подтверждения действия.")
	bot.register_next_step_handler(message, mailing1, text)

def mailing1(message, text):
	user_id = message.chat.id
	good = 0
	error = 0
	if message.text == "+":
		bot.send_message(chat_id=user_id, text="<b>❗️ Рассылка запущена.</b>", parse_mode="HTML")
		for user in get_users():
			try:
				bot.send_message(chat_id=user[0], text=text, parse_mode="HTML")
				good += 1
			except:
				error += 1
		bot.send_message(chat_id=user_id, 
					text="<b>✅Рассылка завершена!\n\n"
						f"❗️Отправлено: {good}\n"
						f"❗️Не отправлено: {error}\n</b>",
		 			parse_mode="HTML")

	else:
		bot.send_message(chat_id=user_id, text="<b>❗️ Рассылка отменена.</b>", parse_mode="HTML")

def get_users():
	db = sqlite3.connect("database.db")
	cursor = db.cursor()
	cursor.execute(f"""SELECT * FROM users""")
	row = cursor.fetchall()
	return row

def search_user(message):
	chat_id = message.chat.id
	try:
		user_id = int(message.text)
		user = get_user(user_id)
		if user != None:
			bot.send_message(chat_id=chat_id,
					text=search_user_text(user_id, user[1], user[3]),
					reply_markup=search_keyboard(user_id),
					parse_mode="HTML")
		else:
			bot.send_message(chat_id=chat_id, text="<b>❗️ Пользователя с таким id нет в базе данных.</b>", parse_mode="HTML")
	except:
		bot.send_message(chat_id=chat_id, text="<b>❗️ Вводите цифрами.</b>", parse_mode="HTML")

def change_balance(message, user_id):
	chat_id = message.chat.id
	try:
		amount = int(message.text)
		bot.send_message(chat_id=chat_id, text="<b>Введите + для подтверждения действия.</b>", parse_mode="HTML")
		bot.register_next_step_handler(message, change_balance1, user_id, amount)
	except:
		bot.send_message(chat_id=chat_id, text="<b>❗️ Вводите цифрами.</b>", parse_mode="HTML")

def change_balance1(message, user_id, amount):
	chat_id = message.chat.id
	try:
		answer = message.text
		if answer == "+":
			edit_balance(user_id, amount)
			bot.send_message(chat_id=chat_id, text="<b>✅Баланс успешно изменён.</b>", parse_mode="HTML")
		else:
			bot.send_message(chat_id=chat_id, text="<b>❗️ Смена баланса отменена</b>", parse_mode="HTML")
	except:
		bot.send_message(chat_id=chat_id, text="<b>❗️ Вводите цифрами.</b>", parse_mode="HTML")

def new_deposit(user_id, comment):
	db = sqlite3.connect('database.db')
	cursor = db.cursor()
	cursor.execute(f'''INSERT INTO deposits VALUES('{user_id}', '{comment}') ''')
	db.commit()

def ban_status_change(user_id, status):
	db = sqlite3.connect("database.db")
	cursor = db.cursor()
	cursor.execute(f"""UPDATE users SET banned = '{status}' WHERE user_id = '{user_id}' """)
	db.commit()

def delete_deposit(user_id):
	db = sqlite3.connect('database.db')
	cursor = db.cursor()
	cursor.execute(f"DELETE FROM deposits WHERE user_id = '{user_id}'")
	db.commit()

def get_comment(user_id):
	db = sqlite3.connect('database.db')
	cursor = db.cursor()
	cursor.execute(f'''SELECT comment FROM deposits WHERE user_id = '{user_id}' ''')
	row = cursor.fetchone()
	if row != None:
		return row[0]
	else:
		return row

def check_deposit(id, number, token, rows_num):
	comment = get_comment(id)
	if comment != None:
		payments = deposit_check(number, token, rows_num)
		pay_len = len(payments['data'])
		if rows_num > pay_len:
			rows_num = pay_len
		for i in range(rows_num):
			if payments['data'][i]['comment'] == str(comment):
				amount = payments['data'][i]['sum']['amount']
				return True, amount
	return False, 0

# def get_payment_url(code, number):
# 	s = requests.Session()
# 	parameters = {"extra['comment']": code, "extra['account']": number, "blocked[0]": 'comment', "blocked[1]": 'account'}
# 	url = 'https://qiwi.com/payment/form/99'
# 	h = s.get(url,params = parameters)
# 	return h.url

def get_nickname_payment_url(nickname):
    s = requests.Session()
    parameters = {"extra['account']": nickname, "blocked[0]": 'account', "extra['accountType']" : "nickname"}
    url = 'https://qiwi.com/payment/form/99999'
    h = s.get(url,params = parameters)
    return h.url


def deposit_check(number, token, rows_num):
	s = requests.Session()
	s.headers['authorization'] = 'Bearer ' + token
	parameters = {'rows': rows_num, 'operation': 'IN'}
	h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + number + '/payments', params = parameters)
	return h.json()