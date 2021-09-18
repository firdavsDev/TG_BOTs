import re
from typing import Text
from six import text_type
from telegram import Update, ReplyKeyboardMarkup #pip install python-telegram-bot
import telegram
from telegram.ext import *


from PIL import Image,ImageDraw,ImageFont
from pathlib import Path
import random

p=Path(__file__).parent / "rasm1.jpg"
q=Path(__file__).parent 

rasm=Image.open(p)
font_t=ImageFont.truetype("font.ttf",40)
yoz=ImageDraw.Draw(rasm)

import os
import time
import requests
import gspread as gool
from pathlib import Path
from datetime import datetime


import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#googleshetga ulash
p=Path(__file__).parent / "cred.json"
#googlesheet
gc=gool.service_account(p)
wb=gc.open('sheet')
sh=wb.sheet1 

#tugma
ruyhat=ReplyKeyboardMarkup([['Ro\'yhatdan o\'tish']],resize_keyboard=True,one_time_keyboard=True,selective=True)
uraa=ReplyKeyboardMarkup([['Logout']],resize_keyboard=True,selective=True,one_time_keyboard=True)



#start bosilganda shu ishlaydi
def hello(update, context):
    rasm='https://t.me/IT_PRO_channel/4'
    update.message.reply_photo(rasm,f'Assalom alaykum \n {update.effective_user.first_name}\n\nXush kelibsiz sizning id {update.effective_user.id} ')
    # for i in sh.get_all_records():
    #     iddd=i['chat_id']
    #     if iddd!=update.effective_user.id:
    #         update.message.reply_text('siz ruyhatdan utgansiz',reply_markup=uraa)
    #         return 3
    #     else:
    time.sleep(2)
    update.message.reply_text('Iltimos ruyhatdan o\'ting',reply_markup=ruyhat)
    return 1


#Ism familya suaraydi
def Login(update,context: Text):
    update.message.reply_html('<b>Ism,familyangizni kiriting!</b>')
    return 1



#mufaqiyatli
def mufaqiyat(update,context,ism1):
    yoz.text(xy=(350,330),text=ism1,fill=(255,69,0),font=font_t)
    rr=str(update.effective_user.id)
    rasm.save(str(rr)+'.png')
    with open(str(rr)+'.png','rb') as ss:
        aa=update.message.reply_photo(ss,'Bizdan uzolashmang @IT_PRO_CHANNEL')
    update.message.reply_html('<a href="https://docs.google.com/spreadsheets/d/1LOMoDWFfUXEeW9VFZklgRxP_Qq3HK2fuNnm7ADwqIFY/">Mufaqiyatli qushildi</a>',reply_markup=uraa)
    time.sleep(2)
    if aa:
        os.remove(str(rr)+'.png')
    return 3



#google shetga ulash uchun
def Login2(update,context):
    ism1=update.message.text
    idd=str(update.effective_user.id)
    sh.append_row([ism1,idd,datetime.now().isoformat()])
    if sh:
        return mufaqiyat(update,context,ism1)




def Logout(update,context):
    try:
        if sh.delete_rows(1):
            update.message.reply_html('<a href="https://docs.google.com/spreadsheets/d/1LOMoDWFfUXEeW9VFZklgRxP_Qq3HK2fuNnm7ADwqIFY/">Mufaqiyatli Logout</a>',reply_markup=ruyhat)
            return 1
        else:
            update.message.reply_text('Xatolik')
    except Exception as error:
        update.message.reply_text('Xatolik bor'+error)
        return 3


updater = Updater('TOKEN')

#############################

conv_handler = ConversationHandler(entry_points =[CommandHandler('start', hello)],
    states={
        1: [

            MessageHandler(Filters.regex('^(Ro\'yhatdan o\'tish)$'), Login),
            MessageHandler(Filters.text,Login2),
        ],
        3:[

            MessageHandler(Filters.regex('^(Logout)$'), Logout),
        ]

        },
    fallbacks=[MessageHandler(Filters.text, ruyhat)]
)

updater.dispatcher.add_handler(conv_handler)

##############################

updater.start_polling()
updater.idle()