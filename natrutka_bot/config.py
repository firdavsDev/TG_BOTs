import telebot

main_token = ":-gjnXxUadRnEL7TpF4"
QIWI_NUMBER = ""
QIWI_TOKEN =""
QIWI_NICKNAME = ""

bot = telebot.TeleBot(main_token, threaded=True, num_threads=300)

admins = [, ]
admin_username = ""
chat_link = ""
channel_link = ""
support_link = "t.me/NAKPUTKATEX"
admin_chat = -
sub_price = 0.15
ref_price = 0.35
like_price = 0.10
vk_friends_price = 25
instagram_like_price = 0.015
instagram_sub_price = 0.020
vk_message_price = 0.020

qiwi_api_link = "https://t.me/"
reviews_link = "https://t.me/joincat/"

views_list = ["1К - 400₽", "5К - 600₽", "10К - 900₽", "15К - 1200₽", "20К - 1500₽"]
tiktok_views_list = ["1К - 400₽", "5К - 600₽"]

def profile(user_id, balance, time):
	profile = \
"<b>👤Профиль:\n\n" \
f"🆔Ваш ID: <code>{user_id}</code>\n\n"\
f"💳Баланс: {balance}₽\n\n"\
f"🕔Дата и время регистрации: {time}</b>"
	return profile

def subscribers():
	text = \
"<i>Подписчиков на канал/группу Telegram\n\n"\
"🔸 Быстрый запуск\n"\
"⌛️ До 5000 в сутки.\n"\
"🔹 Для публичных каналов/групп\n\n"\
"💲 Цена за 100 штук - 15 ₽</i>"
	
	return text

def likes():
	text = \
"<i>❤️ Голоса/Лайки\n\n"\
f"• Цена: {like_price} ₽ / 1 голос или лайк\n"\
"• Только на открытые каналы</i>\n"
	
	return text

def help_text():
	text = \
"📚Всем привет📚\n\n"\
"Ты зашёл в лучший телеграмм 🤖\n"\
"Мы предоставляем накрутку на данные социальные сети 🕸\n"\
"-Telegram 📌\n"\
"-TikTok 📌\n"\
"-VK 📌\n"\
"-Instagram 📌\n"\
"Поддержка данного бота: @NAKPUTKATEX\n"\
"Мы принимаем пополнения 📲\n"\
"-QIWI 🥝 (автоматически)\n"\
"-BTC 🎆 (через поддержку)\n"\
"-PAYEER🅿️ (через поддержку)\n"
	return text

# def qiwi_text(comment):
# 	text = \
# f"Пополнение Qiwi:\n\n"\
# f"➖➖➖➖➖➖➖➖\n"\
# f" Номер: <code>{QIWI_NUMBER}</code>\n"\
# f" Комментарий: <code>{comment}</code>\n"\
# f"➖➖➖➖➖➖➖➖\n\n"\
# f"⚠️ Пополнение без комментария = деньги пойдут на развитие проекта! Так что сверяйте все чтобы было.\n"
# 	return text

def qiwi_text_nickname(comment):
	text = \
f"Пополнение Qiwi:\n\n"\
f"➖➖➖➖➖➖➖➖\n"\
f" Никнейм: <code>{QIWI_NICKNAME}</code>\n"\
f" Комментарий: <code>{comment}</code>\n"\
f"➖➖➖➖➖➖➖➖\n\n"\
f"⚠️ Пополнение без комментария = деньги пойдут на развитие проекта! Так что сверяйте все чтобы было.\n"
	return text

def views_text():
	text = \
"ℹ️ Базовый тариф позволяет делать просмотры на любое количество постов из любого количества каналов."\
"<b>Для заказа просмотров базовом тарифе нужно прислать ссылку на пост.</b>\n\n"\
"ℹ️ Автопросмотры - дополнительная платная опция, которая подхватывает новые посты в канале автоматически.\n"
	return text

def views_tiktok_text():
	text = \
"ℹ️ Базовый тариф позволяет делать просмотры на любое количество видео из любого количества аккаунтов."\
"<b>Для заказа просмотров базовом тарифе нужно прислать ссылку на видео.</b>\n\n"\
"ℹ️ Автопросмотры - дополнительная платная опция, которая подхватывает новые видео в аккаунте автоматически.\n"
	return text

def subscribers_tiktok():
	text = \
"<i>👥 Подписчики:\n\n"\
f"• Цена: {sub_price} ₽ / 1 подписчик\n"\
"• Неактивные, без отписок.</i>"
	return text

def likes_tiktok():
	text = \
"<i>❤️ Лайки\n\n"\
f"• Цена: {like_price} ₽ / 1 лайк</i>"
	return text

def search_user_text(id, balance, banned):
	text = \
	f"📚Информация о <a href='tg://user?id={id}'>пользователе</a>:\n\n"\
	f"💵Баланс: {balance}\n\n"\
	f"🔰Бан: {banned}"
	return text

	