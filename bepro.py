#modular
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import *
import time

#tugma
kurs = ReplyKeyboardMarkup([
    ['Kompyuter Savodxonligi👨🏻‍💻','C++ Dasturlash tili🧰'],
    ['Kengaytirilgan Excel xususiyatlari💻','MC Office💻'],
    ['Veb-saytlarni ishlab chiqish🛠','Java dasturlash tili Inter-darajagacha⚙'],
    ['Tizim Ma\'muriyati⚙','C# 5.0 dasturlash tili🛠'],
    ['Dizayn🪄','Windows Server 2012🧰'],
    ['Wordpress-da veb-saytlarni ishlab chiqish💻','Loyiha Boshqaruvi🛠'],
    ['Bolalar uchun Kampyuter savotxonligi🧸','SEO🛠'],
    ['Web Design🧰','Axborot xavfsizligi⚙'],
    ['Linux tizim ma\'muriyati🛠','Modellashtirish🛠'],
    ['Texnik xizmat ko\'rsatish⚙']], 
    resize_keyboard=True, one_time_keyboard=True, selective=True)

surov = ReplyKeyboardMarkup([
    ['Ro\'yhatdan o\'tish📩','Bosh sahifaga qaytish🔙']
    ], resize_keyboard=True, one_time_keyboard=True, selective=True)

sungi= ReplyKeyboardMarkup([['Bosh sahifaga qaytish🔙']], resize_keyboard=True)

#start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_html(f'Assalom alaykum {update.effective_user.first_name} \n <strong>Bepro Education center Xush  kelibsiz!🎉🎊</strong> ')
    time.sleep(2)
    update.message.reply_text('O\'quv markazimizda quydagi kurslar mavjud⬇️',reply_markup=kurs)
    return 1

#about
def about(update, context):
    update.message.reply_html('Biz haqimizda batafsil📄 \n \nTelefon raqamiz📱: +998935090809 +712775544 \n \nAdmin🧑‍💻: @BeproItAcademy \n\nBizning manzilimiz📍: <a href="https://maps.app.goo.gl/qF9s3pyMebUDeCvz5">Xaritadan ko\'rish</a>\n \n<a href="https://t.me/beproedu">Telegram kanalimiz</a> \n\nWeb-site🌎: https://beproedu.uz "',reply_markup=kurs)

#kurs malumot
def KS(update, context):
    update.message.reply_text('Kompyuter Savodxonligi👨🏻‍💻 \n ✳️Texnalogiya: Microsoft Office \n 💵Narxi:1 500 000 sum \n ⏳Kurs davomiyligi: 1 oy ', reply_markup=surov)

def CD(update, context):
    update.message.reply_text('C++ Dasturlash tili🧰 \n ✳️Texnalogiya: C++ Dastrlash tili \n 💵Narxi:7 500 000 sum \n ⏳Kurs davomiyligi: 3-Oy', reply_markup=surov)

def KEX(update, context):
    update.message.reply_text('Kengaytirilgan Excel xususiyatlari💻 \n ✳️Texnalogiya: Chuqurlashtirligan Excel  \n 💵Narxi:2 000 000 sum \n ⏳Kurs davomiyligi: 1-Oy', reply_markup=surov)

def MCO(update, context):
    update.message.reply_text('MC Office \n ✳️Texnalogiya: Word, Excel, Powe-point, Outlook \n 💵Narxi:1 500 000 sum \n ⏳Kurs davomiyligi: 1-Oy', reply_markup=surov)

def VIC(update, context):
    update.message.reply_text('Veb-saytlarni ishlab chiqish🛠 \n ✳️Texnalogiya: PHP, HTML,CSS,JS \n 💵Narxi:7 600 000 sum \n ⏳Kurs davomiyligi: 4-Oy \n 2-Modul \n ✳️Texnalogiya: Pyhon, HTML, CSS, JS   \n 💵Narxi:7 600 000 sum \n ⏳Kurs davomiyligi: 4-Oy', reply_markup=surov)

def JDI(update, context):
    update.message.reply_text('Java dasturlash tili (Inter-darajagacha)⚙\n ✳️Texnalogiya: Java Dastrlash tili \n 💵Narxi:18 900 000 sum \n ⏳Kurs davomiyligi: 6-Oy', reply_markup=surov)

def TM(update, context):
    update.message.reply_text('Tizim Ma\'muriyati⚙\n ✳️Texnalogiya: Tizim Adminstatori \n 💵Narxi:5 000 000 sum \n ⏳Kurs davomiyligi: 2-Oy', reply_markup=surov)

def CDT(update, context):
    update.message.reply_text('C# 5.0 dasturlash tili🛠 \n ✳️Texnalogiya: C# Dastrlash tili \n 💵Narxi:18 900 000 sum \n ⏳Kurs davomiyligi: 6-Oy', reply_markup=surov)

def D(update, context):
    update.message.reply_text('Dizayn🪄\n ✳️Texnalogiya: Corel Draw \n 💵Narxi:2 000 000 sum \n ⏳Kurs davomiyligi: 1-Oy \n \n 2-Modul \n \n ✳️Texnalogiya: Adobe Photoshop \n 💵Narxi:4 000 000 sum \n ⏳Kurs davomiyligi: 2-Oy', reply_markup=surov)

def WC2(update, context):
    update.message.reply_text('Windows Server 2012🧰\n ✳️Texnalogiya: Windows Server 2012 Sistema adminstatori  \n 💵Narxi:5 000 000 sum \n ⏳Kurs davomiyligi: 2-Oy', reply_markup=surov)

def WVI(update, context):
    update.message.reply_text('Wordpress-da veb-saytlarni ishlab chiqish💻\n ✳️Texnalogiya: Wordpress \n 💵Narxi:2 500 000 sum \n ⏳Kurs davomiyligi: 1-Oy', reply_markup=surov)

def LB(update, context):
    update.message.reply_text('Loyiha Boshqaruvi🛠\n ✳️Texnalogiya: Prayekt boshqaruvi \n 💵Narxi:11 250 000 sum \n ⏳Kurs davomiyligi: 3-Oy', reply_markup=surov)

def BUK(update, context):
    update.message.reply_text('Bolalar uchun Kampyuter savotxonligi🧸\n ✳️Texnalogiya: Python \n 💵Narxi:1 600 000 sum \n ⏳Kurs davomiyligi: 1-Oy', reply_markup=surov)

def SEO(update, context):
    update.message.reply_text('SEO🛠\n ✳️Texnalogiya: SE0 \n 💵Narxi:11 250 000 sum \n ⏳Kurs davomiyligi: 3-Oy', reply_markup=surov)

def WDD(update, context):
    update.message.reply_text('Web Design🧰\n ✳️Texnalogiya: Web Dezayni \n 💵Narxi:5 000 000 sum \n ⏳Kurs davomiyligi: 2-Oy', reply_markup=surov)

def AX(update, context):
    update.message.reply_text('Axborot xavfsizligi⚙\n ✳️Texnalogiya: Xafsizlik boshlang\'ich malumot \n 💵Narxi:2 500 000 sum \n ⏳Kurs davomiyligi: 1-Oy', reply_markup=surov)

def LT(update, context):
    update.message.reply_text('Linux tizim ma\'muriyati🛠\n ✳️Texnalogiya: Linux Sistema admenstatori \n 💵Narxi:5 000 000 sum \n ⏳Kurs davomiyligi: 2-Oy', reply_markup=surov)

def M(update, context):
    update.message.reply_text('Modellashtirish🛠\n ✳️Texnalogiya: 3D MAX \n 💵Narxi:7 500 000 sum \n ⏳Kurs davomiyligi: 3-Oy \n\n 2-Modul \n\n ✳️Texnalogiya: AutoCAD \n 💵Narxi:5 000 000 sum \n ⏳Kurs davomiyligi: 2-Oy', reply_markup=surov)

def TXX(update, context):
    update.message.reply_text('Texnik xizmat ko\'rsatish⚙\n \n ✳️Texnalogiya: Kampyuterni yig\'ish va modernizatsiya qilish  \n 💵Narxi:1 500 000 sum \n ⏳Kurs davomiyligi: 1-Oy', reply_markup=surov)



def bosh(update,context):
    update.message.reply_text('Bosh sahifaga qaytingiz🎊 \nKurslarimiz haqida ⬇️', reply_markup=kurs)

def ruyhat(update,context):
    update.message.reply_html('<a href="https://beproedu.uz/nabor-na-kursy-v-bepro-it-academy/">Ushbu link orqali ro\'yhatdan o\'tishingiz mumkin!</a>', reply_markup=sungi)

updater = Updater('token')

#handler
conv_handler = ConversationHandler(entry_points =[CommandHandler('start', start)],
    states={
        1: [ MessageHandler(Filters.regex('^(/start)$'), start),
        MessageHandler(Filters.regex('^(/about)$'), about),
        MessageHandler(Filters.regex('^(Bosh sahifaga qaytish🔙)$'), bosh),
        MessageHandler(Filters.regex('^(Ro\'yhatdan o\'tish📩)$'), ruyhat),
     
        MessageHandler(Filters.regex('^(Kompyuter Savodxonligi👨🏻‍💻)$'), KS),
        MessageHandler(Filters.regex('^(C\++ Dasturlash tili🧰)$'), CD),
        MessageHandler(Filters.regex('^(Kengaytirilgan Excel xususiyatlari💻)$'), KEX),
        MessageHandler(Filters.regex('^(MC Office💻)$'), MCO),
        MessageHandler(Filters.regex('^(Veb-saytlarni ishlab chiqish🛠)$'), VIC),
        MessageHandler(Filters.regex('^(Java dasturlash tili Inter-darajagacha⚙)$'), JDI),
        MessageHandler(Filters.regex('^(Tizim Ma\'muriyati⚙)$'), TM),
        MessageHandler(Filters.regex('^(C# 5.0 dasturlash tili🛠)$'), CDT),
        MessageHandler(Filters.regex('^(Dizayn🪄)$'), D),
        MessageHandler(Filters.regex('^(Windows Server 2012🧰)$'), WC2),
        MessageHandler(Filters.regex('^(Wordpress-da veb-saytlarni ishlab chiqish💻)$'), WVI),
        MessageHandler(Filters.regex('^(Loyiha Boshqaruvi🛠)$'), LB),
        MessageHandler(Filters.regex('^(Bolalar uchun Kampyuter savotxonligi🧸)$'), BUK),
        MessageHandler(Filters.regex('^(SEO🛠)$'), SEO),
        MessageHandler(Filters.regex('^(Web Design🧰)$'), WDD),
        MessageHandler(Filters.regex('^(Axborot xavfsizligi⚙)$'), AX),
        MessageHandler(Filters.regex('^(Linux tizim ma\'muriyati🛠)$'), LT),
        MessageHandler(Filters.regex('^(Modellashtirish🛠)$'), M),
        MessageHandler(Filters.regex('^(Texnik xizmat ko\'rsatish⚙)$'), TXX),
        ]
        },
    fallbacks=[MessageHandler(Filters.text, kurs)]
)

updater.dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()
