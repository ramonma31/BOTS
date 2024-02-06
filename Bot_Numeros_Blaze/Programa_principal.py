import telebot
import Telegram_bot
import Blaze_sinais
from time import sleep

class Bot_Gratis():
## Definir as frases e stickers ##
    def __init__(self):
        self.win_sem_gale = 'CAACAgEAAxkBAAO0ZCXyMXfUFdsBY14ixiK2Y5-hvv8AApwDAAI0GjBFVh7NWRgQwx4vBA'
        self.win_no_gale = 'CAACAgEAAx0CbiAYVAACDFhkGxt9BXeGAjMRbiLH6YvsO_wGPwAC_AADQSaBR11zLQEy5HO0LwQ'
        self.Entrada_confirmada = 'CAACAgEAAx0CbiAYVAACDFJkGxVqJpY6MSg9udscVKG5zQrunwACCgADLnPHPuJiimLffwABui8E'
        self.loss = 'CAACAgEAAx0CbiAYVAACEXtkIfsdKgRgcRje5LkVOhMs76cq6QACDgUAAm5AEUX5pf4y2CRMLC8E'
        self.em_analise = 'CAACAgEAAx0CbiAYVAACDFZkGxf2E5FkVGY2xzYr-JlPP2ckVwACDgADLnPHPvbAY0yXy1w9LwQ'
        self.atentos = 'CAACAgEAAxkBAAPZZCcq2v0l3uM6eXi0C9fVPueRdJAAAlgDAAJp7ThFwX9PqPpMjFAvBA'



        self.gale1 = '''
===============
BUSCAR PROTEÇÂO
DOBRAR APOSTA 1
===============
        '''
        self.gale2 = '''
===============
BUSCAR PROTEÇÂO
DOBRAR APOSTA 2
===============
        '''
        self.gale3 = '''
===============
BUSCAR PROTEÇÂO
DOBRAR APOSTA 3
===============
        '''

        ## Definindo os bots ##

        self.api1 = '5889355863:AAFsSSfMfpKyigvIXMULytHDeTA141a_olk'
        self.api2 = '5982431594:AAHoSiZo18nVdtyIZQre4BCLQK4EtTvQzxQ'
        self.canal = '@imperio_sinais_gratis'

        ## Iniciando os bots ##

        self.bot_enviar = telebot.TeleBot(self.api1)
        self.bot_corretor = Telegram_bot.Bot_Telegram(self.api2, self.canal)

        ## Definir variaveis  ##

        self.lista_cont = []

        ## Chamando as funções da estrategia ##
        self.pares()

## Startando o bot ##
    def impares(self):
        while True:
            bot_blaze = Blaze_sinais.bot_blaze()
            atualizacao = bot_blaze.sondar_resultado()
            status = bot_blaze.status(atualizacao)
            if status == 'complete':
                numero = bot_blaze.ult_numero(atualizacao)
                # estrategia do 3 #
                if numero == 3:
                    while True:
                        try:
                            update_id = self.bot_corretor.update_id()
                            message_id = self.bot_corretor.message_id(update_id)
                        except:
                            pass
                        atualizacao = bot_blaze.sondar_resultado()
                        status = bot_blaze.status(atualizacao)
                        if status == 'complete':
                            cor = bot_blaze.ult_cor(atualizacao)
                            numero = bot_blaze.ult_numero(atualizacao)
                            self.lista_cont.append(cor)
                            self.lista_cont.copy()
                            sleep(4.7)
                        else:
                            continue
                        if len(self.lista_cont) == 3:
                            self.bot_enviar.send_sticker(self.canal, self.atentos)
                        if len(self.lista_cont) == 4:
                            self.preto = f'''
ATENÇÃO📣📣
==============
💰JOGAR ⚫ 
APOS {cor} {numero}
COBRIR /⚪
MAXIMO 2 GALE
============== 
    '''
                            self.bot_enviar.delete_message(self.canal, message_id)
                            self.bot_enviar.send_message(self.canal, self.preto)
                        if len(self.lista_cont) == 5:
                            if cor == '⬛️' or cor == '⬜️':
                                self.bot_enviar.send_sticker(self.canal, self.win_sem_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.send_message(self.canal, self.gale1)
                                continue
                        if len(self.lista_cont) == 6:
                            if cor == '⬛️' or cor == '⬜️':
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.win_no_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_message(self.canal, self.gale2)
                                continue
                        if len(self.lista_cont) == 7:
                            if cor == '⬛️' or cor == '⬜️':
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.win_no_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.loss)
                                self.lista_cont.clear()
                                break
                # estrategia do 5 #
                if numero == 5:
                    while True:
                        try:
                            update_id = self.bot_corretor.update_id()
                            message_id = self.bot_corretor.message_id(update_id)
                        except:
                            pass
                        atualizacao = bot_blaze.sondar_resultado()
                        status = bot_blaze.status(atualizacao)
                        if status == 'complete':
                            cor = bot_blaze.ult_cor(atualizacao)
                            numero = bot_blaze.ult_numero(atualizacao)
                            self.lista_cont.append(cor)
                            self.lista_cont.copy()
                            sleep(4.7)
                        else:
                            continue  
                        if len(self.lista_cont) == 5:
                            self.bot_enviar.send_sticker(self.canal, self.atentos)
                        if len(self.lista_cont) == 6:
                            self.preto = f'''
ATENÇÃO📣📣
==============
💰JOGAR ⚫ 
APOS {cor} {numero}
COBRIR /⚪
MAXIMO 2 GALE
============== 
    '''
                            self.bot_enviar.delete_message(self.canal, message_id)
                            self.bot_enviar.send_message(self.canal, self.preto)
                        else:
                            continue
                        if len(self.lista_cont) == 7:
                            if cor == '⬛️' or cor == '⬜️':
                                self.bot_enviar.send_sticker(self.canal, self.win_sem_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.send_message(self.canal, self.gale1)
                                continue
                        if len(self.lista_cont) == 8:
                            if cor == '⬛️' or cor == '⬜️':
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.win_no_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_message(self.canal, self.gale2)
                                continue
                        if len(self.lista_cont) == 9:
                            if cor == '⬛️' or cor == '⬜️':
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.win_no_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.loss)
                                self.lista_cont.clear()
                                break
                # estrategia do 7 #
                if numero == 7:
                    while True:
                        try:
                            update_id = self.bot_corretor.update_id()
                            message_id = self.bot_corretor.message_id(update_id)
                        except:
                            pass
                        atualizacao = bot_blaze.sondar_resultado()
                        status = bot_blaze.status(atualizacao)
                        if status == 'complete':
                            cor = bot_blaze.ult_cor(atualizacao)
                            numero = bot_blaze.ult_numero(atualizacao)
                            self.lista_cont.append(cor)
                            self.lista_cont.copy()
                            sleep(4.7)
                        else:
                            continue           
                        if len(self.lista_cont) == 7:
                            self.bot_enviar.send_sticker(self.canal, self.atentos)
                        if len(self.lista_cont) == 8:
                            self.preto = f'''
ATENÇÃO📣📣
==============
💰JOGAR ⚫ 
APOS {cor} {numero}
COBRIR /⚪
MAXIMO 2 GALE
============== 
    '''
                            self.bot_enviar.delete_message(self.canal, message_id)
                            self.bot_enviar.send_message(self.canal, self.preto)
                        if len(self.lista_cont) == 9:
                            if cor == '⬛️' or cor == '⬜️':
                                self.bot_enviar.send_sticker(self.canal, self.win_sem_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.send_message(self.canal, self.gale1)
                                continue
                        if len(self.lista_cont) == 10:
                            if cor == '⬛️' or cor == '⬜️':
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.win_no_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_message(self.canal, self.gale2)
                                continue
                        if len(self.lista_cont) == 11:
                            if cor == '⬛️' or cor == '⬜️':
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.win_no_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.loss)
                                self.lista_cont.clear()
                                break
                # estrategia do 9 #
                if numero == 9:
                    while True:
                        try:
                            update_id = self.bot_corretor.update_id()
                            message_id = self.bot_corretor.message_id(update_id)
                        except:
                            pass
                        atualizacao = bot_blaze.sondar_resultado()
                        status = bot_blaze.status(atualizacao)
                        if status == 'complete':
                            cor = bot_blaze.ult_cor(atualizacao)
                            numero = bot_blaze.ult_numero(atualizacao)
                            self.lista_cont.append(cor)
                            self.lista_cont.copy()
                            sleep(4.7)
                        else:
                            continue    
                        if len(self.lista_cont) == 9:
                            self.bot_enviar.send_sticker(self.canal, self.atentos)
                        if len(self.lista_cont) == 10:
                            self.vermelho = f'''
ATENÇÃO📣📣
==============
💰JOGAR 🔴
APOS {cor} {numero}
COBRIR /⚪
MAXIMO 2 GALE
==============        
'''
                            self.bot_enviar.delete_message(self.canal, message_id)
                            self.bot_enviar.send_message(self.canal, self.vermelho)
                        if len(self.lista_cont) == 11:
                            if cor == '🟥' or cor == '⬜️':
                                self.bot_enviar.send_sticker(self.canal, self.win_sem_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.send_message(self.canal, self.gale1)
                                continue
                        if len(self.lista_cont) == 12:
                            if cor == '🟥' or cor == '⬜️':
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.win_no_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_message(self.canal, self.gale2)
                                continue
                        if len(self.lista_cont) == 13:
                            if cor == '🟥' or cor == '⬜️':
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.win_no_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.loss)
                                self.lista_cont.clear()
                                break
            else:
                continue



    def pares(self):
        while True:
            try:
                bot_blaze = Blaze_sinais.bot_blaze()
                atualizacao = bot_blaze.sondar_resultado()
                status = bot_blaze.status(atualizacao)
            except ConnectionError:
                continue
            if status == 'complete':
                numero = bot_blaze.ult_numero(atualizacao)
                # estrategia do 2 #
                if numero == 2:
                    while True:
                        try:
                            update_id = self.bot_corretor.update_id()
                            message_id = self.bot_corretor.message_id(update_id)
                        except:
                            pass
                        atualizacao = bot_blaze.sondar_resultado()
                        status = bot_blaze.status(atualizacao)
                        if status == 'complete':
                            cor = bot_blaze.ult_cor(atualizacao)
                            numero = bot_blaze.ult_numero(atualizacao)
                            self.lista_cont.append(cor)
                            self.lista_cont.copy()
                            sleep(4.7)
                        else:
                            continue
                        if len(self.lista_cont) == 2:
                            self.bot_enviar.send_sticker(self.canal, self.atentos)
                        if len(self.lista_cont) == 3:
                            self.preto = f'''
ATENÇÃO📣📣
==============
💰JOGAR ⚫ 
APOS {cor} {numero}
COBRIR /⚪
MAXIMO 2 GALE
============== 
    '''
                            self.bot_enviar.delete_message(self.canal, message_id)
                            self.bot_enviar.send_message(self.canal, self.preto)
                        if len(self.lista_cont) == 4:
                            if cor == '⬛️' or cor == '⬜️':
                                self.bot_enviar.send_sticker(self.canal, self.win_sem_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.send_message(self.canal, self.gale1)
                                continue
                        if len(self.lista_cont) == 5:
                            if cor == '⬛️' or cor == '⬜️':
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.win_no_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_message(self.canal, self.gale2)
                                continue
                        if len(self.lista_cont) == 6:
                            if cor == '⬛️' or cor == '⬜️':
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.win_no_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.loss)
                                self.lista_cont.clear()
                                break
                # estrategia do 4 #
                if numero == 4:
                    while True:
                        try:
                            update_id = self.bot_corretor.update_id()
                            message_id = self.bot_corretor.message_id(update_id)
                        except:
                            pass
                        atualizacao = bot_blaze.sondar_resultado()
                        status = bot_blaze.status(atualizacao)
                        if status == 'complete':
                            cor = bot_blaze.ult_cor(atualizacao)
                            numero = bot_blaze.ult_numero(atualizacao)
                            self.lista_cont.append(cor)
                            self.lista_cont.copy()
                            sleep(4.7)
                        else:
                            continue
                        if len(self.lista_cont) == 4:
                            self.bot_enviar.send_sticker(self.canal, self.atentos)
                        if len(self.lista_cont) == 5:
                            self.preto = f'''
ATENÇÃO📣📣
==============
💰JOGAR ⚫ 
APOS {cor} {numero}
COBRIR /⚪
MAXIMO 2 GALE
============== 
    '''
                            self.bot_enviar.delete_message(self.canal, message_id)
                            self.bot_enviar.send_message(self.canal, self.preto)
                        if len(self.lista_cont) == 6:
                            if cor == '⬛️' or cor == '⬜️':
                                self.bot_enviar.send_sticker(self.canal, self.win_sem_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.send_message(self.canal, self.gale1)
                                continue
                        if len(self.lista_cont) == 7:
                            if cor == '⬛️' or cor == '⬜️':
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.win_no_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_message(self.canal, self.gale2)
                                continue
                        if len(self.lista_cont) == 8:
                            if cor == '⬛️' or cor == '⬜️':
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.win_no_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.loss)
                                self.lista_cont.clear()
                                break        
                # estrategia do 6 #
                if numero == 6:
                    while True:
                        try:
                            update_id = self.bot_corretor.update_id()
                            message_id = self.bot_corretor.message_id(update_id)
                        except:
                            pass
                        atualizacao = bot_blaze.sondar_resultado()
                        status = bot_blaze.status(atualizacao)
                        if status == 'complete':
                            cor = bot_blaze.ult_cor(atualizacao)
                            numero = bot_blaze.ult_numero(atualizacao)
                            self.lista_cont.append(cor)
                            self.lista_cont.copy()
                            sleep(4.7)
                        else:
                            continue
                        if len(self.lista_cont) == 6:
                            self.bot_enviar.send_sticker(self.canal, self.atentos)
                        if len(self.lista_cont) == 7:
                            self.preto = f'''
ATENÇÃO📣📣
==============
💰JOGAR ⚫ 
APOS {cor} {numero}
COBRIR /⚪
MAXIMO 2 GALE
============== 
    '''
                            self.bot_enviar.delete_message(self.canal, message_id)
                            self.bot_enviar.send_message(self.canal, self.preto)
                        if len(self.lista_cont) == 8:
                            if cor == '⬛️' or cor == '⬜️':
                                self.bot_enviar.send_sticker(self.canal, self.win_sem_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.send_message(self.canal, self.gale1)
                                continue
                        if len(self.lista_cont) == 9:
                            if cor == '⬛️' or cor == '⬜️':
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.win_no_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_message(self.canal, self.gale2)
                                continue
                        if len(self.lista_cont) == 10:
                            if cor == '⬛️' or cor == '⬜️':
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.win_no_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.loss)
                                self.lista_cont.clear()
                                break        
                # estrategia do 8 #
                if numero == 8:
                    while True:
                        try:
                            update_id = self.bot_corretor.update_id()
                            message_id = self.bot_corretor.message_id(update_id)
                        except:
                            pass
                        atualizacao = bot_blaze.sondar_resultado()
                        status = bot_blaze.status(atualizacao)
                        if status == 'complete':
                            cor = bot_blaze.ult_cor(atualizacao)
                            numero = bot_blaze.ult_numero(atualizacao)
                            self.lista_cont.append(cor)
                            self.lista_cont.copy()
                            sleep(4.7)
                        else:
                            continue
                        if len(self.lista_cont) == 8:
                            self.bot_enviar.send_sticker(self.canal, self.atentos)
                        if len(self.lista_cont) == 9:
                            self.vermelho = f'''
ATENÇÃO📣📣
==============
💰JOGAR 🔴
APOS {cor} {numero}
COBRIR /⚪
MAXIMO 2 GALE
==============        
'''
                            self.bot_enviar.delete_message(self.canal, message_id)
                            self.bot_enviar.send_message(self.canal, self.vermelho)
                        if len(self.lista_cont) == 10:
                            if cor == '🟥' or cor == '⬜️':
                                self.bot_enviar.send_sticker(self.canal, self.win_sem_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.send_message(self.canal, self.gale1)
                                continue
                        if len(self.lista_cont) == 11:
                            if cor == '🟥' or cor == '⬜️':
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.win_no_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_message(self.canal, self.gale2)
                                continue
                        if len(self.lista_cont) == 12:
                            if cor == '🟥' or cor == '⬜️':
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.win_no_gale)
                                self.lista_cont.clear()
                                break
                            else:
                                self.bot_enviar.delete_message(self.canal, message_id)
                                self.bot_enviar.send_sticker(self.canal, self.loss)
                                self.lista_cont.clear()
                                break   
            else:
                continue

Bot_Gratis()
         