import config
import telebot
from telebot import types # кнопки
from string import Template
from config import token

bot = telebot.TeleBot(config.token)

user_dict = {}

class User:
    def __init__(self, city):
        self.city = city

        keys = ['fullname', 'phone', 'driverSeria', 
                'driverNumber', 'driverDate', 'car', 
                'carModel', 'carColor', 'carNumber', 'carDate']
        
        for key in keys:
            self.key = None

# если /help, /start
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('/about')
    itembtn2 = types.KeyboardButton('/reg')
    itembtn3 = types.KeyboardButton('/reg2')
    markup.add(itembtn1, itembtn2, itembtn3)
    
    bot.send_message(message.chat.id, "Assalom Alaykum "
    + message.from_user.first_name
    + ", Usoz shogird kannaliga hush kelibsiz?", reply_markup=markup)

# /about
@bot.message_handler(commands=['about'])
def send_about(message):
	bot.send_message(message.chat.id, "Dasturchi " 
    + " https://firdavsdev.vercel.app.")

# /reg
@bot.message_handler(commands=["reg"])
def user_reg(message):
       markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
       itembtn1 = types.KeyboardButton('Andijon')
       itembtn2 = types.KeyboardButton('Farg\'ona')
       itembtn3 = types.KeyboardButton('Namangan')
       itembtn4 = types.KeyboardButton('Toshkent')
       itembtn5 = types.KeyboardButton('Sirdaryo')
       itembtn6 = types.KeyboardButton('Jizzax')
       itembtn7 = types.KeyboardButton('Samarqand')
       itembtn8 = types.KeyboardButton('Surxandaryi')
       itembtn9 = types.KeyboardButton('Qashqadaryo')
       itembtn10 = types.KeyboardButton('Buxora')
       itembtn11 = types.KeyboardButton('Navoiy')
       itembtn12 = types.KeyboardButton('Xorazm')
       markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6,itembtn7,itembtn8,itembtn9,itembtn10,itembtn11,itembtn12)

       msg = bot.send_message(message.chat.id, 'Shahringiz?', reply_markup=markup)
       bot.register_next_step_handler(msg, process_city_step)

def process_city_step(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)

        # удалить старую клавиатуру
        markup = types.ReplyKeyboardRemove(selective=False)

        msg = bot.send_message(chat_id, 'Ism Familyayiz?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_fullname_step)

    except Exception as e:
        bot.reply_to(message, 'xato!!')

def process_fullname_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.fullname = message.text

        msg = bot.send_message(chat_id, 'Telefon raqamingiz')
        bot.register_next_step_handler(msg, process_phone_step)

    except Exception as e:
        bot.reply_to(message, 'Xato!!')

def process_phone_step(message):
    try:
        int(message.text)

        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.text

        msg = bot.send_message(chat_id, 'Tog\'ri farmat')
        bot.register_next_step_handler(msg, process_driverSeria_step)

    except Exception as e:
        msg = bot.reply_to(message, 'Вы ввели что то другое. Пожалуйста введите номер телефона.')
        bot.register_next_step_handler(msg, process_phone_step)

def process_driverSeria_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driverSeria = message.text

        msg = bot.send_message(chat_id, 'Texnalogiyalar')
        bot.register_next_step_handler(msg, process_driverNumber_step)

    except Exception as e:
        bot.reply_to(message, 'Xato!!')

def process_driverNumber_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driverNumber = message.text
       
        msg = bot.send_message(chat_id, 'Tug\'ulgan kuniz?\nВ формате: День.Месяц.Год')
        bot.register_next_step_handler(msg, process_driverDate_step)

    except Exception as e:
        bot.reply_to(message, 'Xato!!')

def process_driverDate_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driverDate = message.text

        msg = bot.send_message(chat_id, 'Kasbi?')
        bot.register_next_step_handler(msg, process_car_step)

    except Exception as e:
        bot.reply_to(message, 'Xato!!')

def process_car_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.car = message.text

        msg = bot.send_message(chat_id, 'Maqsadingiz? ')
        bot.register_next_step_handler(msg, process_carModel_step)

    except Exception as e:
        bot.reply_to(message, 'Xato!!')

def process_carModel_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carModel = message.text

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('14-18 yosh')
        itembtn2 = types.KeyboardButton('18-20 yosh')
        itembtn3 = types.KeyboardButton('20-25 yosh')
        itembtn4 = types.KeyboardButton('25 yoshdan katta')

        markup.add(itembtn1, itembtn2, itembtn3, itembtn4)

        msg = bot.send_message(chat_id, 'Yosh', reply_markup=markup)
        bot.register_next_step_handler(msg, process_carColor_step)

    except Exception as e:
        bot.reply_to(message, 'Xato!!')

def process_carColor_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carColor = message.text

        msg = bot.send_message(chat_id, 'Narxi?')
        bot.register_next_step_handler(msg, process_carNumber_step)

    except Exception as e:
        bot.reply_to(message, 'Xato!!')

def process_carNumber_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carNumber = message.text

        msg = bot.send_message(chat_id, 'Murojat vaqti')
        bot.register_next_step_handler(msg, process_carDate_step)

    except Exception as e:
        bot.reply_to(message, 'Xato!!')

def process_carDate_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carDate = message.text

        # ваша заявка "Имя пользователя"
        bot.send_message(chat_id, getRegData(user, 'Ism', message.from_user.first_name), parse_mode="Markdown")
        # отправить в группу
        bot.send_message(config.chat_id, getRegData(user, 'Заявка от бота', bot.get_me().username), parse_mode="Markdown")

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

# формирует вид заявки регистрации
# нельзя делать перенос строки Template
# в send_message должно стоять parse_mode="Markdown"
def getRegData(user, title, name):
    t = Template('$title *$name* \n Город: *$userCity* \n ФИО: *$fullname* \n Телефон: *$phone* \n Серия водительского удостоверения: *$driverSeria* \n Номер водительского удостоверения: *$driverNumber* \n Дата выдачи водительского удостоверения: *$driverDate* \n Марка автомобиля: *$car* \n Модель автомобиля: *$carModel* \n Цвет автомобиля: *$carColor* \n Гос. номер автомобиля: *$carNumber* \n Год выпуска: *$carDate*')

    return t.substitute({
        'title': title,
        'name': name,
        'userCity': user.city,
        'fullname': user.fullname,
        'phone': user.phone,
        'driverSeria': user.driverSeria,
        'driverNumber': user.driverNumber,
        'driverDate': user.driverDate,
        'car': user.car,
        'carModel': user.carModel,
        'carColor': user.carColor,
        'carNumber': user.carNumber,
        'carDate': user.carDate,
    })

# произвольный текст
@bot.message_handler(content_types=["text"])
def send_help(message):
    bot.send_message(message.chat.id, 'О нас - /about\nРегистрация - /reg\nПомощь - /help')

# произвольное фото
@bot.message_handler(content_types=["photo"])
def send_help_text(message):
    bot.send_message(message.chat.id, 'Напишите текст')

# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)