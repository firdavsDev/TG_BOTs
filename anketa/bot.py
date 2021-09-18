import config
import telebot
from telebot import types  # кнопки
from string import Template

bot = telebot.TeleBot(config.token)

user_dict = {}


class User:
    def __init__(self, city):
        self.city = city

        keys = ['fullname', 'phone','car',
                'carModel',  'carNumber', 'carDate']

        for key in keys:
            self.key = None

# если /help, /start


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('/about')
    itembtn2 = types.KeyboardButton('/reg')
    itembtn3 = types.KeyboardButton('/lang')
    markup.add(itembtn1, itembtn2, itembtn3)

    bot.send_message(
        message.chat.id, f"Ассалому алайкум! {message.from_user.first_name} \n\nСиз Давлат фуқаролик хизматчилари вакант лавозимлари ягона очиқ портали (vacancy.argos.uz)нинг махсус ботига уландингиз.", reply_markup=markup)

# /about


@bot.message_handler(commands=['about'])
def send_about(message):

    bot.send_message(message.chat.id, "Вакансиялар ҳақида хабардор бўлиб бориш учун қуйидаги каналларга уланинг \n\nУланиш: t.me/vacancy_argos,  t.me/yangiuzbekiston_uz \n\nДавалт хизматини ривожлантириш агентлигининг расмий сайти  https://t.me/argos_uz")

# language


@bot.message_handler(commands=['lang'])
def send_about(message):
    markup = types.ReplyKeyboardMarkup(
        one_time_keyboard=True, resize_keyboard=True)
    uz = types.KeyboardButton('/Uz')
    ru = types.KeyboardButton('/Ru')
    markup.add(uz, ru)
    bot.send_message(message.chat.id, 'Til tanlang', reply_markup=markup)


# /reg
@bot.message_handler(commands=["reg"])
def user_reg(message):
    markup = types.ReplyKeyboardMarkup(
        one_time_keyboard=True, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Toshkent')
    itembtn2 = types.KeyboardButton('Samarqand')
    itembtn3 = types.KeyboardButton('Jizzax')
    itembtn4 = types.KeyboardButton('Andijan')
    itembtn5 = types.KeyboardButton('Xorazm')
    itembtn6 = types.KeyboardButton('Navoi')
    itembtn7 = types.KeyboardButton('Qashqadaryo')
    itembtn8 = types.KeyboardButton('Guliston')
    itembtn9 = types.KeyboardButton('Termiz')
    itembtn10 = types.KeyboardButton('Buxoro')
    itembtn11 = types.KeyboardButton('Sirdaryo')
    itembtn12 = types.KeyboardButton('Surxandaryo')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6,
               itembtn7, itembtn8, itembtn9, itembtn10, itembtn11, itembtn12,)

    msg = bot.send_message(
        message.chat.id, 'Ҳудудни танланг?', reply_markup=markup)
    bot.register_next_step_handler(msg, process_city_step)


def process_city_step(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)

        # удалить старую клавиатуру
        markup = types.ReplyKeyboardRemove(selective=False)

        msg = bot.send_message(
            chat_id, 'Исм, фамилия, шарифингиз', reply_markup=markup)
        bot.register_next_step_handler(msg, process_fullname_step)

    except Exception as e:
        bot.reply_to(message, 'Xato!!!')


def process_fullname_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.fullname = message.text

        msg = bot.send_message(chat_id, 'Телефон рақамингиз')
        bot.register_next_step_handler(msg, process_phone_step)

    except Exception as e:
        bot.reply_to(message, 'Xato!!!')


def process_phone_step(message):
    try:
        int(message.text)

        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.text

        markup = types.ReplyKeyboardMarkup(
            one_time_keyboard=True, resize_keyboard=True)
        xa = types.KeyboardButton('Xa')
        yuq = types.KeyboardButton('Yo\'q')
        markup.add(xa, yuq)

        msg = bot.send_message(
            chat_id, 'Танлов иштирокчимисиз?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_carModel_step)

    except Exception as e:
        msg = bot.reply_to(
            message, 'Siz boshqa narsani kiritdingiz. Iltimos, telefon raqamingizni kiriting..')
        bot.register_next_step_handler(msg, process_phone_step)

# def process_driverSeria_step(message):
#     try:
#         chat_id = message.chat.id
#         user = user_dict[chat_id]
#         user.driverSeria = message.text

#         markup = types.ReplyKeyboardRemove(selective=False)

#         msg = bot.send_message(chat_id, 'Номер водительского удостоверения')
#         bot.register_next_step_handler(msg, process_driverNumber_step)

#     except Exception as e:
#         bot.reply_to(message, 'Xato!!!')

# def process_driverNumber_step(message):
#     try:
#         chat_id = message.chat.id
#         user = user_dict[chat_id]
#         user.driverNumber = message.text

#         msg = bot.send_message(chat_id, 'Дата выдачи водительского удостоверения\nВ формате: День.Месяц.Год')
#         bot.register_next_step_handler(msg, process_driverDate_step)

#     except Exception as e:
#         bot.reply_to(message, 'Xato!!!')

# def process_driverDate_step(message):
#     try:
#         chat_id = message.chat.id
#         user = user_dict[chat_id]
#         user.driverDate = message.text

#         msg = bot.send_message(chat_id, 'Марка автомобиля')
#         bot.register_next_step_handler(msg, process_car_step)

#     except Exception as e:
#         bot.reply_to(message, 'Xato!!!')

# def process_car_step(message):
#     try:
#         chat_id = message.chat.id
#         user = user_dict[chat_id]
#         user.car = message.text

#         msg = bot.send_message(chat_id, 'Модель автомобиля')
#         bot.register_next_step_handler(msg, process_carModel_step)

#     except Exception as e:
#         bot.reply_to(message, 'Xato!!!')


def process_carModel_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carModel = message.text

        markup = types.ReplyKeyboardMarkup(
            one_time_keyboard=True, resize_keyboard=True)

        itembtn1 = types.KeyboardButton('Chilonzor')
        itembtn2 = types.KeyboardButton('Beruniy')
        itembtn3 = types.KeyboardButton('Chorsu')
        itembtn4 = types.KeyboardButton('Orikzor')
        itembtn5 = types.KeyboardButton('Algaritm')

        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)

        msg = bot.send_message(
            chat_id, 'Туманни танланг:', reply_markup=markup)
        bot.register_next_step_handler(msg, process_carNumber_step)

    except Exception as e:
        bot.reply_to(message, 'Xato!!!')

# def process_carColor_step(message):
#     try:
#         chat_id = message.chat.id
#         user = user_dict[chat_id]
#         user.carColor = message.text

#         msg = bot.send_message(chat_id, 'Гос. номер автомобиля')
#         bot.register_next_step_handler(msg, process_carNumber_step)

#     except Exception as e:
#         bot.reply_to(message, 'Xato!!!')


def process_carNumber_step(message):
    try:
        markup = types.ReplyKeyboardRemove(selective=False)
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carNumber = message.text

        msg = bot.send_message(chat_id, 'Мурожаатингизни йўлланг: ',reply_markup=markup)
        bot.register_next_step_handler(msg, process_carDate_step)

    except Exception as e:
        bot.reply_to(message, 'Xato!!!')


def process_carDate_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carDate = message.text

        # ваша заявка "Имя пользователя"
        bot.send_message(chat_id, getRegData(
            user, 'Username', message.from_user.first_name), parse_mode="Markdown")
        # отправить в группу
        bot.send_message(config.chat_id, getRegData(
            user, f"Guruhga  {message.from_user.first_name} shu inson tomonidan yuborildi \n\n",message.from_user.username), parse_mode="Markdown")

    except Exception as e:
        print(e)
        bot.reply_to(message, 'Xato!!!')

# формирует вид заявки регистрации
# нельзя делать перенос строки Template
# в send_message должно стоять parse_mode="Markdown"


def getRegData(user, title, name):
    t = Template('$title *$name* \n Viloyat: *$userCity* \n FIO: *$fullname* \n Telefon: *$phone*  \n Tuman: *$carNumber* \n Malumot: *$carDate*')

    return t.substitute({
        'title': title,
        'name': name,
        'userCity': user.city,
        'fullname': user.fullname,
        'phone': user.phone,
        'carModel': user.carModel,       
        'carNumber': user.carNumber,
        'carDate': user.carDate,
    })

# произвольный текст


@bot.message_handler(content_types=["text"])
def send_help(message):
    bot.send_message(
        message.chat.id, 'Biz haqimizda - /about\n\nRo\'yxatdan o\'tish - /reg\n\n Yordam - /help')

# произвольное фото
@bot.message_handler(content_types=["photo"])
def send_help_text(message):
    bot.send_message(message.chat.id, 'So\'z yozing!')


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

if __name__ == '__main__':
    # bot.remove_webhook()
    bot.polling(none_stop=True)
