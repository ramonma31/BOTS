import telebot
from time import sleep


api = '5889355863:AAFsSSfMfpKyigvIXMULytHDeTA141a_olk'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=["CLICK_AKI"])
def CLICK_AKI(message):
    bot.send_message(chat_id=message.chat.id, text='''
https://
    ''')


@bot.message_handler(commands=["Quero"])
def Quero(message):
    bot.send_message(chat_id=message.chat.id, text='''
OK então vamos lá voçê esta pronto para
Lucrar muito com o bot mais acertivo da BLAZE
e ganhar seu 🎁 /CLICK_AKI
    ''')


def verificar(message):
    return True


@bot.message_handler(func=verificar)
def responder(message):
    bot.send_message(chat_id=message.chat.id, text='''
OLA VAMOS FAZER PARTE DO MAIS ACERTIVO BOT DOUBLE BLAZE!!
    '''   )
    sleep(2)
    bot.send_message(chat_id=message.chat.id, text='''
E vamos nessa!
/Quero participar
/Saber mais 
/Cadastrar na Blaze   
    ''')


bot.polling()