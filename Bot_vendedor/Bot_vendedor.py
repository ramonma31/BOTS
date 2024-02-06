import telebot
from time import sleep

api = '5889355863:AAFsSSfMfpKyigvIXMULytHDeTA141a_olk'
canal = '-1001847597140'
bot = telebot.TeleBot(api)


@bot.message_handler(commands=['BOT_SINAIS_GRATIS'])
def sala_gratis(menssagem):
    name1 = menssagem.chat.first_name
    name2 = menssagem.chat.last_name
    texto = f'''
OLA {name1} {name2}
TA PREPADO PARA ENTRAR NA MAIOR SALA DE SINAIS DO BRASIL E AINDA POR CIMA DE GRAÇA
👇👇💸💸👇👇 CLICA E VEM CONFERIR
https://t.me/imperio_sinais_gratis

    '''
    bot.send_message(menssagem.chat.id, texto)

@bot.message_handler(commands=['BOT_BRANCO_14X'])
def addaobot(menssagem):
    name1 = menssagem.chat.first_name
    name2 = menssagem.chat.last_name
    texto = f'''
OI BOA NOITE {name1} {name2}
    
VAGAS LIBERADAS✅📣

IMPERIO TEAM BLAZE ⚪⚪

FAÇA O PIX DE R$ 79,90 REAIS NO PIX ABAIXO ⬇️ 
PIX COPIA E COLA 👈

5febf639-6348-42c5-af44-bddd5e5f3e81

AO FAZER O PAGAMENTO, ENVIE O COMPROVANTE PARA O CONTATO ABAIXO PARA ENTRAR NO GRUPO VIP. ⬇️ 

@Vipteamblaze 

VENHA FAZER PARTE DO GRUPO MILIONÁRIO. 💰💸

APROVEITEM, IREMOS AUMENTAR O VALOR, ESSE VALOR É PARA O PRIMEIRO LOTE! 😍😍😍

MUITA GENTE APROVEITANDO GALERA! 👏👏👏

AO MANDAR COMPROVANTE SÓ AGUARDAR QUE IREMOS ATENDER VC ! 💣🟦⭐️👏

PIX COPIA E COLA 👈

5febf639-6348-42c5-af44-bddd5e5f3e81

OBS:("TRANSFERÊNCIA NO NOME DE RAMON")

         '''
    bot.send_message(menssagem.chat.id, texto)

@bot.message_handler(commands=['SUPORTE_TEAM_BLAZE'])
def suport(menssagem):
    name1 = menssagem.chat.first_name
    name2 = menssagem.chat.last_name
    texto = f'''
OLÁ BOA NOITE {name1} {name2}

SEGUE O LINK PARA FALAR COM NOSSO SUPORTE PREMIUM

@Vipteamblaze
    '''
    bot.send_message(menssagem.chat.id, texto)

def message(menssagem):
    return True

@bot.message_handler(func=message, content_types=['text', 'sticker'])
def iniciar(menssagem):
    name1 = menssagem.chat.first_name
    name2 = menssagem.chat.last_name
    texto1 = f'''
OI TUDO BEM COM VC {name1} {name2}
SEJA BEM VINDO AO IMPERIO_TEAM_BLAZE BRANCO
💥💥💥💥💥💥👇👇👇👇👇👇👇💥💥💥💥💥💥

/BOT_BRANCO_14X 🔥:CLICK AQUI:🔥 ACESSO VITALICIO A IA🤖

/BOT_SINAIS_GRATIS 🔥:CLICK AQUI:🔥 ACESSO AO BOT GRATIS VENHA FAZER PARTE!

/SUPORTE_TEAM_BLAZE CONTATAR SUPORT PREMIUM

(cLICK EM UMA DAS OPCOES CASO CONTRARIO NAO VAI FUNCIONAR)
    '''
    texto2 = f'''
/BOT_BRANCO_14X {name1} O QUE TA ESPERANDO CLICA
VEM GARANTIR SUA VAGA 
    '''
    print(menssagem)
    bot.send_message(menssagem.chat.id, texto1)
    sleep(5)
    bot.send_message(menssagem.chat.id, texto2)
bot.polling()


