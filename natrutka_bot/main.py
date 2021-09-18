import random
from config import bot, admins, profile, admin_chat, subscribers, likes, help_text, qiwi_text_nickname, QIWI_NUMBER,\
	QIWI_TOKEN, QIWI_NICKNAME, views_text, views_list, likes_tiktok, subscribers_tiktok, vk_friends_price, \
	instagram_like_price, views_tiktok_text, tiktok_views_list
from keyboard import main_keyboard, profile_keyboard, admin_menu_keyboard, service_keyboard, \
	order_keyboard, subscribe_type_keyboard, place_type_keyboard, deposit_methods_keyboard, \
	deposit_keyboard, delete_message_keyboard, views_keyboard, instagram_service_keyboard, \
	help_keyboard, vk_service_keyboard, tiktok_views_keyboard

from functions import get_user, join_to_db, order_likes, order_subscribe, check_deposit, get_comment, \
	new_deposit, delete_deposit, order_likes1, edit_balance, order_tiktok_subscribe, order_tiktok_likes, \
	search_user, ban_status_change, change_balance, mailing, order_vk_friends, order_instagram_likes, \
	order_instagram_subscribe, order_vk_messages, order_vk_subscribers


@bot.message_handler(commands=['start'])
def send_welcome(message):
	chat_id = message.chat.id
	if chat_id > 0:
		if get_user(chat_id) == None:
			join_to_db(user_id=chat_id)
		user = get_user(chat_id)
		if user[3] == "False":
			bot.send_message(chat_id=chat_id,
							text=f'Привет, {message.chat.first_name}! Воспользуйся кнопками.',
							reply_markup=main_keyboard())

@bot.message_handler(commands=['admin'])
def admin_menu(message):
	chat_id = message.chat.id
	if chat_id > 0:
		user = get_user(chat_id)
		if user != None:	
			if user[3] == "False":
				if chat_id in admins:
					bot.send_message(chat_id=message.from_user.id,
					 				text='Вы в меню админа.',
					  				reply_markup=admin_menu_keyboard())	


@bot.message_handler(content_types="text")
def main_menu(message):
	chat_id = message.chat.id
	if chat_id > 0:
		user = get_user(chat_id)
		if user != None:
			if user[3] == "False":
				if message.text == "👤Профиль":
					bot.send_message(chat_id=chat_id,
										text=profile(chat_id, user[1], user[2]),
										reply_markup=profile_keyboard(),
										parse_mode="HTML"
											)
				elif message.text == "🧾Сделать заказ":
					bot.send_message(chat_id=chat_id,
										text="<b>Выберите площадку для накрутки.</b>",
										reply_markup=place_type_keyboard(),
										parse_mode="HTML"
											)
					bot.register_next_step_handler(message, place_menu)
				
				elif message.text == "📚Помощь":
					bot.send_message(chat_id=chat_id,
										text=help_text(),
										parse_mode="HTML",
										reply_markup=help_keyboard(),
										disable_web_page_preview=True)
				else:
					bot.send_message(chat_id=chat_id,
							text=f'Неизвестная команда! Воспользуйся кнопками.',
							reply_markup=main_keyboard())
		else:
			bot.send_message(chat_id=chat_id,
						text=f'<b>❗️ Я вас не понимаю! Пропишите /start .</b>', parse_mode="HTML")

@bot.message_handler(content_types="text")
def place_menu(message):
	chat_id = message.chat.id
	user = get_user(chat_id)
	if user != None:
		if user[3] == "False":		
			if message.text == "🛒Telegram":
				bot.send_message(chat_id=chat_id,
										text="<b>Выберите тип услуги.</b>",
										reply_markup=service_keyboard(),
										parse_mode="HTML"
											)
				bot.register_next_step_handler(message, telegram_service_menu)
			
			elif message.text == "📊Вконтакте":
				bot.send_message(chat_id=chat_id,
										text="<b>Выберите тип услуги.</b>",
										reply_markup=vk_service_keyboard(),
										parse_mode="HTML"
											)
				bot.register_next_step_handler(message, vk_service_menu)
			
			elif message.text == "📱TikTok":
				bot.send_message(chat_id=chat_id,
										text="<b>Выберите тип услуги.</b>",
										reply_markup=service_keyboard(),
										parse_mode="HTML"
											)
				bot.register_next_step_handler(message, tiktok_service_menu)

			elif message.text == "📷Instagram":
				bot.send_message(chat_id=chat_id,
										text="<b>Выберите тип услуги.</b>",
										reply_markup=instagram_service_keyboard(),
										parse_mode="HTML"
											)
				
				bot.register_next_step_handler(message, instagram_service_menu)

			elif message.text == "⏪Назад":
				bot.send_message(chat_id=message.from_user.id, text=f'Вы вернулись в главное меню.', reply_markup=main_keyboard())
				bot.register_next_step_handler(message, main_menu)

	else:
		bot.send_message(chat_id=chat_id,
					text=f'<b>❗️ Я вас не понимаю! Пропишите /start .</b>', parse_mode="HTML")




@bot.message_handler(content_types="text")
def vk_service_menu(message):
	chat_id = message.chat.id
	user = get_user(chat_id)
	if user != None:
		if user[3] == "False":		
			if message.text == "👥Друзья":
				bot.send_message(chat_id=chat_id,
						text="<i>• 1000-1500 друзей.\n"
						"• обезательно иметь аватарку.\n"
						"•  скидывать токен Kate Mobile.\n"
						"• минимальные отписки.\n"
						"• живые (время накрутки 30-90 минут)\n"
						"• узнать токен https://vkhost.github.io/\n"
						"Стоимость услуги 25₽</i>",
						reply_markup=order_keyboard("vk_friends"),
						parse_mode="HTML"
							)

				bot.register_next_step_handler(message, vk_service_menu)
			
			elif message.text == "📨Сообщения":
				bot.send_message(chat_id=chat_id,
								text="•<i>1000 личных сообщений=20₽\n"
									"• узнать токен https://vkhost.github.io/\n"
									"• получить токен VK ME\n"
									"• ВОЗМОЖНА БЛОКИРОВКА ВК‼️\n"
									"• НАКРУТКА ИДЁТ БЫСТРО\n"
									"• НАКРУТКА ЛИЧНЫХ СООБЩЕНИЙ\n</i>",
								reply_markup=order_keyboard("vk_messages"),
								parse_mode="HTML")
				bot.register_next_step_handler(message, vk_service_menu)

			elif message.text == "👨‍👩‍👦‍👦Группа":
				bot.send_message(chat_id=chat_id,
								text="<i>Подписчики в группу/паблик VK\n\n"
									"🔸 Быстрый запуск.\n"
									"⌛️ Плавная раскрутка.\n\n"
									"💲 Цена: 15 руб. за 100</i>",				
								reply_markup=order_keyboard("vk_public_subscribers"),
								parse_mode="HTML")

				bot.register_next_step_handler(message, vk_service_menu)
			
			elif message.text == "⏪Назад":
				bot.send_message(chat_id=message.from_user.id, text=f'Вы вернулись в меню выбора площадки.', reply_markup=place_type_keyboard())
				bot.register_next_step_handler(message, place_menu)

	else:
		bot.send_message(chat_id=chat_id,
						text=f'<b>❗️ Я вас не понимаю! Пропишите /start .</b>', parse_mode="HTML")

@bot.message_handler(content_types="text")
def instagram_service_menu(message):
	chat_id = message.chat.id
	user = get_user(chat_id)
	if user != None:
		if user[3] == "False":		
			if message.text == "👥Подписчики":
				bot.send_message(chat_id=chat_id,
								text="<i>🔸 Быстрый запуск.\n"
									"⌛️ Скорость: до 1500 в сутки.\n"
									"👪 Реальные пользователи\n\n"
									"💲 Цена: 20 руб. за 100\n"
									"Ccылку указывать в формате: https://www.instagram.com/***</i>",
								reply_markup=order_keyboard("instagram_subscribers"),
								parse_mode="HTML")

				bot.register_next_step_handler(message, instagram_service_menu)
			
			elif message.text == "❤️Лайки":
				bot.send_message(chat_id=chat_id,
								text="<i>Лайки Instagram (Живые)\n\n"
							 "🔸 Быстрый запуск.\n"
							" ⌛️ Скорость до 2500 в сутки.\n"
							"👪 Реальные пользователи.\n\n"
							"💲 Цена: 15 руб. за 100</i>",
								reply_markup=order_keyboard("instagram_likes"),
								parse_mode="HTML")
				bot.register_next_step_handler(message, instagram_service_menu)
			
			elif message.text == "⏪Назад":
				bot.send_message(chat_id=message.from_user.id, text=f'Вы вернулись в меню выбора площадки.', reply_markup=place_type_keyboard())
				bot.register_next_step_handler(message, place_menu)

	else:
		bot.send_message(chat_id=chat_id,
						text=f'<b>❗️ Я вас не понимаю! Пропишите /start .</b>', parse_mode="HTML")

@bot.message_handler(content_types="text")
def telegram_service_menu(message):
	chat_id = message.chat.id
	user = get_user(chat_id)
	if user != None:
		if user[3] == "False":		
			if message.text == "👥Подписчики":
				bot.send_message(chat_id=chat_id,
								text=subscribers(),
								reply_markup=order_keyboard("subscribers"),
								parse_mode="HTML")
				bot.register_next_step_handler(message, telegram_service_menu)
			
			# elif message.text == "👀Просмотры":
			# 	bot.send_message(chat_id=chat_id,
			# 					text=views_text(),
			# 					reply_markup=views_keyboard(),
			# 					parse_mode="HTML")
			# 	bot.register_next_step_handler(message, views_menu)
			
			# elif message.text == "❤️Голоса/Лайки":
			# 	bot.send_message(chat_id=chat_id,
			# 					text=likes(),
			# 					reply_markup=order_keyboard("likes"),
			# 					parse_mode="HTML")
			# 	bot.register_next_step_handler(message, telegram_service_menu)
			
			elif message.text == "⏪Назад":
				bot.send_message(chat_id=message.from_user.id, text=f'Вы вернулись в меню выбора площадки.', reply_markup=place_type_keyboard())
				bot.register_next_step_handler(message, place_menu)

	else:
		bot.send_message(chat_id=chat_id,
						text=f'<b>❗️ Я вас не понимаю! Пропишите /start .</b>', parse_mode="HTML")

@bot.message_handler(content_types="text")
def tiktok_service_menu(message):
	chat_id = message.chat.id
	user = get_user(chat_id)
	if user != None:
		if user[3] == "False":		
			if message.text == "👥Подписчики":
				bot.send_message(chat_id=chat_id,
								text=subscribers_tiktok(),
								reply_markup=order_keyboard("tiktok_subscribers"),
								parse_mode="HTML")
				bot.register_next_step_handler(message, tiktok_service_menu)
			
			elif message.text == "👀Просмотры":
				bot.send_message(chat_id=chat_id,
								text=views_tiktok_text(),
								reply_markup=tiktok_views_keyboard(),
								parse_mode="HTML")
				bot.register_next_step_handler(message, tiktok_views_menu)

			elif message.text == "❤️Голоса/Лайки":
				bot.send_message(chat_id=chat_id,
								text=likes_tiktok(),
								reply_markup=order_keyboard("tiktok_likes"),
								parse_mode="HTML")
				bot.register_next_step_handler(message, tiktok_service_menu)
			
			elif message.text == "⏪Назад":
				bot.send_message(chat_id=message.from_user.id, text=f'Вы вернулись в меню выбора площадки.', reply_markup=place_type_keyboard())
				bot.register_next_step_handler(message, place_menu)

	else:
		bot.send_message(chat_id=chat_id,
					text=f'<b>❗️ Я вас не понимаю! Пропишите /start .</b>', parse_mode="HTML")

@bot.message_handler(content_types="text")
def tiktok_views_menu(message):
	chat_id = message.chat.id
	user = get_user(chat_id)
	if user != None:
		if user[3] == "False":		
			if message.text == "Автопросмотры":
				user = get_user(chat_id)
				if user != None:
					price = 100
					if user[1] >= price:
						bot.send_message(chat_id=chat_id, 
							text="<b>Отправьте ссылку на аккаунт куда хотите накручивать просмотры.</b>",
							parse_mode="HTML")
						bot.register_next_step_handler(message, order_likes1, price, amount=1, type_order="👀Автопросмотры TIKTOK")
					else:
						bot.send_message(chat_id=chat_id,
							text="<b>❗️ У вас недостаточно средств. Пополните баланс.</b>",
							parse_mode="HTML")

			elif message.text in tiktok_views_list:
				user = get_user(chat_id)
				if user != None:
					price = int(message.text.split(" ")[2][:-1])			
					if user[1] >= price:
						bot.send_message(chat_id=chat_id,
							text="<b>Отправьте ссылку на видео куда хотите накрутить просмотры.</b>",
							parse_mode="HTML")
						bot.register_next_step_handler(message, order_likes1, price, amount=message.text.split(" ")[0], type_order="👀Просмотры TIKTOK")
					else:
						bot.send_message(chat_id=chat_id,
							text="<b>❗️ У вас недостаточно средств. Пополните баланс.</b>",
							parse_mode="HTML")

@bot.message_handler(content_types="text")
def views_menu(message):
	chat_id = message.chat.id
	user = get_user(chat_id)
	if user != None:
		if user[3] == "False":		
			if message.text == "Автопросмотры":
				user = get_user(chat_id)
				if user != None:
					price = 100
					if user[1] >= price:
						bot.send_message(chat_id=chat_id, 
							text="<b>Отправьте ссылку на канал куда хотите накручивать просмотры.</b>",
							parse_mode="HTML")
						bot.register_next_step_handler(message, order_likes1, price, amount=1, type_order="👀Автопросмотры")
					else:
						bot.send_message(chat_id=chat_id,
							text="<b>❗️ У вас недостаточно средств. Пополните баланс.</b>",
							parse_mode="HTML")

			elif message.text in views_list:
				user = get_user(chat_id)
				if user != None:
					price = int(message.text.split(" ")[2][:-1])			
					if user[1] >= price:
						bot.send_message(chat_id=chat_id,
							text="<b>Отправьте ссылку на запись куда хотите накрутить просмотры.</b>",
							parse_mode="HTML")
						bot.register_next_step_handler(message, order_likes1, price, amount=message.text.split(" ")[0], type_order="👀Просмотры")
					else:
						bot.send_message(chat_id=chat_id,
							text="<b>❗️ У вас недостаточно средств. Пополните баланс.</b>",
							parse_mode="HTML")

	else:
		bot.send_message(chat_id=chat_id,
					text=f'<b>❗️ Я вас не понимаю! Пропишите /start .</b>', parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
	chat_id = call.message.chat.id
	message_id = call.message.message_id
	message = call.message

	if chat_id > 0:
		user = get_user(chat_id)
		if user != None:
			if user[3] == "False":
				if call.data.startswith("order"):
					service = call.data.split(":")[1]
					
					if service == "subscribers":
						bot.send_message(chat_id=chat_id,
									text="<i>Выберите тип накрутки</i>",
									reply_markup=subscribe_type_keyboard(),
									parse_mode="HTML")

						bot.register_next_step_handler(message, order_subscribe)		
					
					elif service == "likes":
						bot.send_message(chat_id=chat_id,
									text="<i>Введите количество лайков которое хотите накрутить</i>",
									parse_mode="HTML")

						bot.register_next_step_handler(message, order_likes)

					elif service == "tiktok_subscribers":
						bot.send_message(chat_id=chat_id,
									text="<i>Введите количество подписчиков которое хотите накрутить</i>",
									parse_mode="HTML")

						bot.register_next_step_handler(message, order_tiktok_subscribe)

					elif service == "tiktok_likes":
						bot.send_message(chat_id=chat_id,
									text="<i>Введите количество лайков которое хотите накрутить</i>",
									parse_mode="HTML")

						bot.register_next_step_handler(message, order_tiktok_likes)

					elif service == "vk_friends":
						if user[1] >= vk_friends_price:
							bot.send_message(chat_id=chat_id,
										text="<i>Введите токен Вконтакте.</i>",
										parse_mode="HTML")

							bot.register_next_step_handler(message, order_vk_friends)

						else:
							bot.send_message(chat_id=chat_id, text="<b>❗️ У вас недостаточно средств. Пополните баланс.</b>", parse_mode="HTML")
					
					elif service == "vk_public_subscribers":
						bot.send_message(chat_id=chat_id,
									text="<i>Введите количество подписчиков которое хотите накрутить</i>",
									parse_mode="HTML")

						bot.register_next_step_handler(message, order_vk_subscribers)

					elif service == "instagram_likes":
						bot.send_message(chat_id=chat_id,
									text="<i>Введите количество лайков которое хотите накрутить</i>",
									parse_mode="HTML")

						bot.register_next_step_handler(message, order_instagram_likes)

					elif service == "instagram_subscribers":
						bot.send_message(chat_id=chat_id,
									text="<i>Введите количество подписчиков которое хотите накрутить</i>",
									parse_mode="HTML")

						bot.register_next_step_handler(message, order_instagram_subscribe)

					elif service == "vk_messages":
						bot.send_message(chat_id=chat_id,
										text="<i>Введите количество сообщений которое хотите накрутить.</i>",
										parse_mode="HTML")

						bot.register_next_step_handler(message, order_vk_messages)

				elif call.data == "deposit":
					bot.edit_message_text(chat_id=chat_id,
									message_id=message_id,
									text="<i>Выберите вариант пополнения.</i>",
									reply_markup=deposit_methods_keyboard(),
									parse_mode="HTML")
				
				elif call.data == "qiwi_method":
					comment = get_comment(chat_id)
					if comment == None:
						comment = random.randint(1000, 9999)
						new_deposit(chat_id, comment)
					bot.send_message(chat_id=chat_id,
									text=qiwi_text_nickname(comment),
									reply_markup=deposit_keyboard(comment),
									parse_mode="HTML")

				elif call.data == 'check_deposit':
					user = get_user(chat_id)
					if user != None:
						balance = user[1]
						answer, amount = check_deposit(chat_id, QIWI_NUMBER, QIWI_TOKEN, 20)
						if answer:
							delete_deposit(chat_id)
							edit_balance(chat_id, balance + amount)
							bot.send_message(chat_id=chat_id, text=f"<b>✅Баланс успешно пополнен на {amount}</b>", parse_mode="HTML")
							bot.delete_message(chat_id=chat_id, message_id=message_id)
						else:
							bot.send_message(chat_id=chat_id, text=f'<b>❌Платёж не найден</b>',
							parse_mode="HTML",
							reply_markup=delete_message_keyboard())

				elif call.data == "del_deposit":
					delete_deposit(chat_id)			
					bot.delete_message(chat_id=chat_id, message_id=message_id)
					bot.send_message(chat_id=chat_id, text=f"<b>Платеж успешно отменён</b>", parse_mode="HTML")

				elif call.data == "delete_message":
					bot.delete_message(chat_id=chat_id, message_id=message_id)

				elif call.data == "search_user":
					bot.send_message(chat_id=chat_id, text=f"Введите id пользователя.")
					bot.register_next_step_handler(message, search_user)

				elif call.data.startswith("change_balance"):
					user_id = call.data.split(":")[1]
					bot.send_message(chat_id=chat_id, text=f"Введите на какую сумму хотите изменить баланс пользователю.")
					bot.register_next_step_handler(message, change_balance, user_id)
				
				elif call.data.startswith("ban_user"):
					user_id = call.data.split(":")[1]
					ban_status_change(user_id, "True")
					bot.send_message(chat_id=chat_id, text=f"Пользователь был забанен.")

				elif call.data.startswith("unban_user"):
					user_id = call.data.split(":")[1]
					ban_status_change(user_id, "False")
					bot.send_message(chat_id=chat_id, text=f"Пользователь был разабанен.")

				elif call.data == "mailing_menu":
					bot.send_message(chat_id=chat_id, text=f"Введите текст рассылки.")
					bot.register_next_step_handler(message, mailing)
		else:
			bot.send_message(chat_id=chat_id,
						text=f'<b>❗️ Я вас не понимаю! Пропишите /start .</b>', parse_mode="HTML")
	else:		
		
		if call.data.startswith("start_service"):
			bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=None)
			user_id = call.data.split(":")[1]
			bot.send_message(chat_id=user_id,
							text="<i>Ваш заказ начал выполняться</i>",
							parse_mode="HTML",
							reply_markup=main_keyboard())
			bot.register_next_step_handler(message, main_menu)

		elif call.data.startswith("stop_service"):
			bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=None)
			user_id = call.data.split(":")[1]
			bot.send_message(chat_id=user_id,
							text="<i>Ваш заказ был отклонён. Для выяснения причины свяжитесь с администратором.</i>",
							parse_mode="HTML",
							reply_markup=main_keyboard())
			bot.register_next_step_handler(message, main_menu)

				
if __name__ == '__main__':
	try:
		bot.polling(none_stop = True, interval = 0)
	except Exception as e:
		bot.send_message(chat_id=1347410943, text=f"<b>Возникла ошибка!</b>\n\n{e}", parse_mode="HTML")
		while True:
			try:
				bot.polling(none_stop = True, interval = 0)
			except Exception as e:
				bot.send_message(chat_id=1347410943, text=f"<b>Возникла ошибка!</b>\n\n{e}", parse_mode="HTML")