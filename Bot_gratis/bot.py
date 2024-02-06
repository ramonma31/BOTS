
from ast import Break
from math import fabs
from imp import reload
from sqlite3 import Time
from importlib import reload
from pickle import NONE, TRUE
from bs4 import BeautifulSoup
from selenium import webdriver
from distutils.command.clean import clean
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import bd
import time
import telebot
import datetime


options = webdriver.ChromeOptions()
options.add_argument('--headless')
nav = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), chrome_options=options)
nav.get('https://blaze.com/pt/games/double')

############################### ⚪️⚪️⚪️ ####################################
api_key = ''
user_id = ''   # input('Informe seu ChatID: ') 


############################################################################

bot = telebot.TeleBot(token=api_key)

linked_suporttopteam = '[i𝐁𝐥𝐚𝐳𝐞𝐃𝐨𝐮𝐛𝐥𝐞𝐬](https://t.me/mscodex)'

bot.send_message(chat_id=user_id, text=('''
☆★  [ i𝐁𝐥𝐚𝐳𝐞𝐃𝐨𝐮𝐛𝐥𝐞𝐬 ]  ★☆

        🟩%i   ⬜️%i   🟥%i   

🔹 Win 1ª  =  %i
🔹 Win 2ª  =  %i
🔹 Win 3ª  =  %i
🔹 Branco 1ª  =  %i
🔹 Branco 2ª  =  %i
🔹 Branco 3ª  =  %i
🔹 Consecutivas  =  %i
🔹 Assertividade  =  %s

ᴀ ᴍᴇʟʜᴏʀ ᴅᴏ ʙʀᴀsɪʟ!
👨🏾‍💻       
                        ''' % (bd.wait_results, bd.branco_results, bd.loss_results, bd.win_semgale,bd.win_gale1,bd.win_gale2,bd.branco_semgale,bd.branco_gale1,bd.branco_gale2,bd.max_hate,bd.win_hate)))

#bot.send_sticker(user_id,sticker='CAACAgEAAxkBAAEBPQZi-ziImRgbjqbDkPduogMKzv0zFgACbAQAAl4ByUUIjW-sdJsr6CkE')



print('Configurado!')

############################### ⚪️⚪️⚪️ ####################################

while True:
    def QUAL_NUM(x):
        if x == '0':
            return 0

        if x == '1':
            return 1

        if x == '2':
            return 2

        if x == '3':
            return 3

        if x == '4':
            return 4

        if x == '5':
            return 5

        if x == '6':
            return 6

        if x == '7':
            return 7

        if x == '8':
            return 8

        if x == '9':
            return 9

        if x == '10':
            return 10

        if x == '11':
            return 11

        if x == '12':
            return 12

        if x == '13':
            return 13

        if x == '14':
            return 14   
    def QUAL_COR(x):
        if x == '0':
            return 'B'

        if x == '1':
            return 'V'

        if x == '2':
            return 'V'

        if x == '3':
            return 'V'

        if x == '4':
            return 'V'

        if x == '5':
            return 'V'

        if x == '6':
            return 'V'

        if x == '7':
            return 'V'

        if x == '8':
            return 'P'

        if x == '9':
            return 'P'

        if x == '10':
            return 'P'

        if x == '11':
            return 'P'

        if x == '12':
            return 'P'

        if x == '13':
            return 'P'

        if x == '14':
            return 'P'       

    def BUTTON_LINK():
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton(text="APOSTE AQUI",
                url="https://blaze.com/pt/r/JVkoPy"))
        return markup

    def ALERT_E1():
        message_id = bot.send_message(
            user_id, text='''
⚠️ ALERTA TEREMOS UM SINAL ⚠️
                FIQUE PREPARADO
            ''').message_id
        bd.message_ids = message_id
        bd.mensage_delete = True
        return     
    def ALERT_E2():
        message_id = bot.send_message(
            user_id, text='''
⚠️ ALERTA POSSÍVEL SINAL ⚠️
                FIQUE PREPARADO
            ''').message_id
        bd.message_ids = message_id
        bd.mensage_delete = True
        return  

    def ALERT_GALE1():
        message_id = bot.send_message(
            user_id, text='''
⚠️ Vamos para o 1ª GALE ⚠️
            ''').message_id
        bd.message_ids1 = message_id
        bd.mensage_delete1 = True
        return  
    def DELET_GALE1():
        if bd.mensage_delete1 == True:
            bot.delete_message(chat_id=user_id, message_id=bd.message_ids1)
            bd.mensage_delete1 = False    

    def ALERT_GALE2():
        message_id = bot.send_message(
            user_id, text='''
⚠️ Vamos para o 2ª GALE ⚠️
            ''').message_id
        bd.message_ids2 = message_id
        bd.mensage_delete2 = True
        return  
    def DELET_GALE2():
        if bd.mensage_delete2 == True:
            bot.delete_message(chat_id=user_id, message_id=bd.message_ids2)
            bd.mensage_delete2 = False    

    def SEND_SINAL():
        bd.analise_open = 2
        bd.Entrada_Atual = 0
        bd.Notification_open = None


        b = bd.win_results+bd.branco_results
        if (bd.win_results+bd.branco_results+bd.loss_results) != 0:
            a = 100 / (bd.win_results+bd.branco_results+bd.loss_results) * b
        else:
            a = 0
        bd.win_hate = (f'{a:,.2f}%')
        bot.send_message(chat_id=user_id, text=('''
☆★ [ SINAL ENCONTRADO ] ★☆

            Entrar: %s%s%s
            Cobrir: ⬜️⬜️⬜️


    📊 RESULTADO GERAL 

            🟩%i  ⬜️%i  🟥%i   

🔹 Win 1ª  =  %i
🔹 Win 2ª  =  %i
🔹 Win 3ª  =  %i
🔹 Branco 1ª  =  %i
🔹 Branco 2ª  =  %i
🔹 Branco 3ª  =  %i
🔹 Consecutivas  =  %i
🔹 Assertividade  =  %s


ᴀ ᴍᴇʟʜᴏʀ ᴅᴏ ʙʀᴀsɪʟ!
👨🏾‍💻                      
''' % (bd.direction_operation, bd.direction_operation, bd.direction_operation, bd.win_results, bd.branco_results, bd.loss_results, bd.win_semgale,bd.win_gale1,bd.win_gale2,bd.branco_semgale,bd.branco_gale1,bd.branco_gale2,bd.max_hate,bd.win_hate)), reply_markup=BUTTON_LINK())
        return
    
    def RESET_WIN():
        bd.win_results = bd.win_results+1
        bd.max_hate = bd.max_hate+1
        bd.analise_open = 0
        bd.Entrada_Atual = 0
        bd.Notification_open = True
        bd.what_estrategy = 'TRUE'
        bd.analisar = 0
        bd.number = 0
        bd.wait_num = 0
        bd.wait_results = 0      
    def RESET_LOSS():
        bd.max_hate = 0
        bd.loss_results = bd.loss_results+1
        bd.analise_open = 0
        bd.Entrada_Atual = 0
        bd.Notification_open = True
        bd.what_estrategy = 'TRUE'
        bd.analisar = 0
        bd.number = 0
        bd.wait_num = 0
        bd.wait_results = 0
    def RESET_BRANCO():
        bd.max_hate = bd.max_hate+1
        bd.branco_results = bd.branco_results+1      
        bd.analise_open = 0
        bd.Entrada_Atual = 0
        bd.Notification_open = True
        bd.what_estrategy = 'TRUE'
        bd.analisar = 0
        bd.number = 0
        bd.wait_num = 0
        bd.wait_results = 0
        
    def GO_WIN():
        if bd.Entrada_Atual == 0:
            bd.win_semgale = bd.win_semgale+1
            bot.send_sticker(user_id,sticker='CAACAgEAAxkBAAEBPsZi_0ET9dkB3lLg7yp3fwN2Lx5_HQACYAIAAsUT4Uf9yd9LDRTRqSkE')
            RESET_WIN()
            return
        if bd.Entrada_Atual == 1:
            bd.win_gale1 = bd.win_gale1+1
            bot.send_sticker(user_id,sticker='CAACAgEAAxkBAAEBPsZi_0ET9dkB3lLg7yp3fwN2Lx5_HQACYAIAAsUT4Uf9yd9LDRTRqSkE')
            DELET_GALE1()
            RESET_WIN()
            return
        if bd.Entrada_Atual == 2:
            bd.win_gale2 = bd.win_gale2+1
            bot.send_sticker(user_id,sticker='CAACAgEAAxkBAAEBPsZi_0ET9dkB3lLg7yp3fwN2Lx5_HQACYAIAAsUT4Uf9yd9LDRTRqSkE')
            DELET_GALE2()
            RESET_WIN()
            return
    def GO_LOSS():
        if bd.Entrada_Atual == 0:
            bd.Entrada_Atual = bd.Entrada_Atual+1
            bd.Notification_open = None      
            ALERT_GALE1()
            return          
        if bd.Entrada_Atual == 1:
            bd.Entrada_Atual = bd.Entrada_Atual+1
            bd.Notification_open = None
            DELET_GALE1()
            ALERT_GALE2()
            return
        if bd.Entrada_Atual == 2:
            bot.send_sticker(user_id,sticker='CAACAgEAAxkBAAEBPspi_0EcmMPyKiJX7bWq_VKpfhKAtQACrQIAApEs6EfiJAz91XrVOSkE')
            DELET_GALE2()
            RESET_LOSS()
            return
    def GO_BRANCO():
        if bd.Entrada_Atual == 0:
            bd.branco_semgale = bd.branco_semgale+1
            bot.send_sticker(user_id,sticker='CAACAgEAAxkBAAEBPtJi_0Fxf8vwRnAmhsVmdkQGaLC0QgACuwIAAraw4UcUszFhDr1MLSkE')
            RESET_BRANCO()
            return
        if bd.Entrada_Atual == 1:
            bd.branco_gale1 =  bd.branco_gale1+1
            bot.send_sticker(user_id,sticker='CAACAgEAAxkBAAEBPtJi_0Fxf8vwRnAmhsVmdkQGaLC0QgACuwIAAraw4UcUszFhDr1MLSkE')
            DELET_GALE1()
            RESET_BRANCO()
            return
        if bd.Entrada_Atual == 2:
            bd.branco_gale2 =  bd.branco_gale2+1
            bot.send_sticker(user_id,sticker='CAACAgEAAxkBAAEBPtJi_0Fxf8vwRnAmhsVmdkQGaLC0QgACuwIAAraw4UcUszFhDr1MLSkE')
            DELET_GALE2()
            RESET_BRANCO()
            return

    def ESTRATEGIAS():

        if bd.what_estrategy == 'FALSE' or bd.what_estrategy == 'SPEED':
            pd = bd.tfg[0:3]
            mapeando = map(QUAL_NUM, pd)
            mapeando2 = map(QUAL_COR, pd)
            finalcor = list(mapeando2)
            def CHECK_VERSION(num):
                if bd.analise_open == 2:
                    # WIN
                    if num == ['V', 'P', 'P']:
                        GO_WIN()
                        return
                    if num == ['P', 'V', 'V']:
                        GO_WIN()
                        return
                    if num == ['B', 'P', 'P']:
                        GO_BRANCO()
                        return
                    if num == ['B', 'V', 'V']:
                        GO_BRANCO()
                        return

                    # LOSS
                    if num == ['P', 'P', 'P']:
                        GO_LOSS()
                        return
                    if num == ['V', 'V', 'V']:
                        GO_LOSS()
                        return

                elif bd.analise_open == 0:
                    if num == ['P', 'P', 'V']:
                        bd.what_estrategy = 'SPEED'
                        bd.direction_operation = '🟥'                        
                        SEND_SINAL()
                        return
                    if num == ['V', 'V', 'P']:
                        bd.what_estrategy = 'SPEED'
                        bd.direction_operation = '⬛️'
                        SEND_SINAL()
                        return
            
            checkVersion = CHECK_VERSION(finalcor)
        



############################### 🟢🟢🟢 ####################################
    try:
        bd.resultsDouble = nav.find_element(
            By.XPATH, '//*[@id="roulette-timer"]/div[1]').text
    except NameError as erro:
        pass
    except Exception as erro:
        pass
    
    bd.now = int(datetime.datetime.now().strftime("%H")) 
    bd.estrategy_open = False
    if bd.resultsDouble == "Girando...":
        bd.estrategy_open = True
        if bd.mensage_delete == True:
            bot.delete_message(chat_id=user_id, message_id=bd.message_ids)
            bd.mensage_delete = False
        time.sleep(13) 
        c = nav.page_source
        bd.tfg.clear()
        soup = BeautifulSoup(c, 'html.parser')
        vai = soup.find('div', class_="entries main")
        for i in vai:
            if i.getText():
                bd.tfg.append(i.getText())
            else:
                bd.tfg.append('0')
        bd.tfg = bd.tfg[:-1] 

############################### ⚠️⚠️⚠️ ###############################      

        if bd.estrategy_open == True:  # ANALISAR SINAIS
            ESTRATEGIAS()
        time.sleep(13)
















