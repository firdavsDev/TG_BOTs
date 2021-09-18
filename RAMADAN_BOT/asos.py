from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, ConversationHandler
from  telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
import time


btn_bugun,btn_erta,btn_oy,btn_viloyat,btn_duo=('Bugun','Ertaga','To\'liq taqvim','Mintaqa','Duo')
tugma= ReplyKeyboardMarkup([
    [btn_bugun],[btn_erta,btn_oy],[btn_viloyat],[btn_duo]
],resize_keyboard=True)


STATE_REGION=1
STATE_CALENDAR=2

#Firdavs_Dev

def start(updater,context):
    user=updater.message.from_user


    viloyat=[
        [
            InlineKeyboardButton('Toshkent',callback_data='tosh'),
            InlineKeyboardButton('Samarqand',callback_data='sam')
        ]
    ]

    updater.message.reply_html(f'Assalom alaykum <b>{user.first_name}!</b>\n\n<b>Ramozon oyi muborak bo\'lsin</b>')
    time.sleep(1)
    updater.message.reply_html('Qaysi mintaqa bo\'yicha malumot beray? ',reply_markup=InlineKeyboardMarkup(viloyat))

    return STATE_REGION


def inline_callback(updater,context):
    try:

        query=updater.callback_query
        query.message.delete()
        query.message.reply_html(text='Ramozon taqvimi \nQuydagilardan birini tanlang ',reply_markup=tugma)
        return STATE_CALENDAR

    except Exception as e:
        print(str(e))

def calandar_bugun(updater,context):
    updater.message.reply_html('Bugun belgilandi')


def calandar_erta(updater,context):
    updater.message.reply_html('erta  belgilandi')


def calandar_tuliq(updater,context):
    updater.message.reply_html('tuliq belgilandi')


def calandar_viloyat(updater,context):
    updater.message.reply_html('viloyat Tanlash')


def calandar_duo(updater,context):
    updater.message.reply_html('Duo belgilandi')

def main():
    #updater bu
    TOKEN='TOKEN'
    updater=Updater(TOKEN,use_context=True)

    #Dispetcher eventlani aniqlaydi
    dispatcher=updater.dispatcher

    #Commandani ushkab qoladi
    #dispatcher.add_handler(CommandHandler('start',start))

    #inline button query
    #dispatcher.add_handler(CallbackQueryHandler(inline_callback))

    conv_handler=ConversationHandler(

        entry_points=[CommandHandler('start',start)],
        states={

        

            STATE_REGION:[CallbackQueryHandler(inline_callback)],
            STATE_CALENDAR:[
                MessageHandler(Filters.regex('^('+btn_bugun+')$'),calandar_bugun ),
                MessageHandler(Filters.regex('^('+btn_erta+')$'),calandar_erta ),
                MessageHandler(Filters.regex('^('+btn_oy+')$'),calandar_tuliq),
                MessageHandler(Filters.regex('^('+btn_viloyat+')$'),calandar_viloyat),
                MessageHandler(Filters.regex('^('+btn_duo+')$'),calandar_duo ),
            ],
        },
        fallbacks=[CommandHandler('start',start)]
    )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()

main()