import telebot
import requests
import json
from datetime import datetime
from pytz import timezone 
from time import sleep  


class bot_blaze():
    ## CLASSE CONSTRUTORA ##
    def __init__(self,api,canal):
        self.results_counter()
        self.Stickers()
        self.layout2()
        self.taxa = 0
        self.alert = 0
        self.gale1 = 0
        self.gale2 = 0
        self.gale3 = 0
        self.message_id = 0
        self.cont = 0
        self.api = api
        self.canal = canal
        self.bot = telebot.TeleBot(self.api)
        message_id = self.bot.send_message(self.canal, text='''
🧿 ATENTOS BOT CONFIGURADO
📡 INICIANDO ANALISES...''').message_id
        self.message_id = message_id
        while True:
            try:
                try:
                    self.sondar_resultado()
                    self.status()
                except:
                    continue
                    ## START BOT ##
                if self.momento == 'complete':
                    self.ult_cor()
                    self.ult_numero()
                    print(f'BLAZE GIROU: {self.ult_cor()}/{self.ult_numero()}')
                    sleep(4.7)
                    self.num_estrategy(self.ult_numero())
            except:
                print('''
FALHA AO TENTAR CONTINUAR
BOT FINALIZANDO...
POR FAVOR REINICIE''')
                break



## VARIAVEIS DOS STICKERS ##
    def Stickers(self):
        self.win_sem_gale = 'CAACAgEAAxkBAAEIc0FkK2xRcIPIkJOucJQNBYO6esTgkAACqQIAAlD_YEUTThBkC36q1i8E'
        self.win_no_gale = 'CAACAgEAAxkBAAPxZCy9tjkrxVp9GZXNEG6HoqYDa-sAAnADAAIN3mhFd6jeH-5QpYgvBA'
        self.Entrada_confirmada = 'CAACAgEAAx0CbiAYVAACDFJkGxVqJpY6MSg9udscVKG5zQrunwACCgADLnPHPuJiimLffwABui8E'
        self.perdeu = 'CAACAgEAAxkBAAEIcz9kK2vmdzZ3g5qJ8I3RaniGOprNiAACywMAAp-qWUWoGfMdyjLygS8E'
        self.em_analise = 'CAACAgEAAx0CbiAYVAACDFZkGxf2E5FkVGY2xzYr-JlPP2ckVwACDgADLnPHPvbAY0yXy1w9LwQ'
        self.atentos = 'CAACAgEAAxkBAAEIc0NkK2x7yuB1yZwYoNGWCj2uR5Uw6AACoQMAAiBUYEWuPV4yCZV9Wy8E'   


## METODOS DE LAYOUT ##            
    def layout(self):
        texto = 'BOT BLAZE DEV ALENCAR'
        tam = len(texto)
        print('=' * (tam + 2))
        print('')
        print(texto)
        print('')
        print('=' * (tam + 2))  


    def layout2(self):
        RED   = "\033[1;31m"  
        BLUE  = "\033[1;34m"
        CYAN  = "\033[1;36m"
        GREEN = "\033[0;32m"
        RESET = "\033[0;0m"
        BOLD    = "\033[;1m"
        REVERSE = """\033[;7m"""


        print("""\033[;1m\033[1;31m
        ######################################################################################
        #                                                                                    #
        ######################################################################################
        #   #####      ####     ######     #####     #           ##      ######    ######    #
        #   #    #    #    #      #        #    #    #          #  #         #     #         #
        #   #####     #    #      #        #####     #         #####       #       ####      #
        #   #    #    #    #      #        #    #    #        #    #     #         #         #
        #   #####      ####       #        #####     #####   #     #     ######    ######    #
        #                                                                                    # 
        #       #    #    #    #    ##   ##    ######    #####      ####       #####         #
        #       ##   #    #    #    # # # #    #         #    #    #    #     #              #
        #       # #  #    #    #    #  #  #    #####     #####     #    #     ######         #
        #       #  # #    #    #    #  #  #    #         #  #      #    #          #         #
        #       #   ##     ####     #  #  #    ######    #   #      ####      #####          #
        #                                                                                    #
        ######################################################################################
                    

                        \033[0;0m\033[;1m\033[0;32mBEM VINDOS AO BOT MAIS ACERTIVO DO BRASIL...
    """)


## MÉTODOS DE REQUISIÇÃO PARA API ##
    def sondar_resultado(self):
        self.roulette_current = 'https://blaze.com/api/roulette_games/current'
        response = requests.get(self.roulette_current)
        self.resposta = json.loads(response.content)


    def ult_numero(self):
        self.res_num = self.resposta['roll']
        return self.res_num
    

    def ult_cor(self):
        res_cor = self.resposta['color']
        if res_cor == 1:
            return '🔴'
        if res_cor == 2:
            return '⚫'
        if res_cor == 0:
            return '⚪'   
    

    def status(self):
        self.momento = self.resposta['status']


    def minuto_atual(self):
        fuso_horario = timezone('America/Fortaleza')
        atual = datetime.now(tz=fuso_horario)
        hora_minuto = atual.strftime('%M')
        self.minuto_atual = int(hora_minuto)

    
    def hora_atual(self):
        fuso_horario = timezone('America/Fortaleza')
        atual = datetime.now(tz=fuso_horario)
        hora = atual.strftime('%H')
        self.hora_atual = int(hora)
    
    
    def minuto_sinal(self, num1, num2):
        numero_da_jogada = (num1 + num2) - 2
        if numero_da_jogada < 0:
            numero_da_jogada = 2
        if numero_da_jogada >= 0 and numero_da_jogada <= 2:
            numero_da_jogada == 2
        return numero_da_jogada


## FUNÇÕES PARA MANDAR OS SINAIS PARA O CANAL DO TELEGRAM ##
    def sinal_preto(self):
        message_id = self.bot.send_message(self.canal, text=f'''
ATENÇÃO📣📣
==============
💰JOGAR ⚫
APOS {self.ult_cor()} {self.ult_numero()} 
MAXIMO 3 GALE
============== 
        ''').message_id
        self.message_id = message_id
    

    def sinal_vermelho(self):
        message_id = self.bot.send_message(self.canal, text=f'''
ATENÇÃO📣📣
==============
💰JOGAR 🔴
APOS {self.ult_cor()} {self.ult_numero()} 
MAXIMO 3 GALE
==============        
        ''').message_id
        self.message_id = message_id


    def sinal_gale1(self):
        message_id = self.bot.send_message(self.canal, text='''
===============
VAMOS AO GALE 1
"DOBRAR APOSTA"
===============
        ''').message_id
        self.message_id = message_id


    def sinal_gale2(self):
        message_id = self.bot.send_message(self.canal, text='''
===============
VAMOS AO GALE 2
"DOBRAR APOSTA"
===============
        ''').message_id
        self.message_id = message_id
    

    def sinal_gale3(self):
        message_id = self.bot.send_message(self.canal, text='''
===============
VAMOS AO GALE 3
"DOBRAR APOSTA"
===============
        ''').message_id
        self.message_id = message_id


    def win_direct(self):
        message_id = self.bot.send_sticker(self.canal, self.win_sem_gale).message_id
        self.message_id = message_id


    def win_gale(self):
        message_id = self.bot.send_sticker(self.canal, self.win_no_gale).message_id
        self.message_id = message_id
    

    def derrora(self):
        self.bot.send_sticker(self.canal, self.perdeu)


    def atencao(self):
        message_id = self.bot.send_sticker(self.canal, self.atentos).message_id
        self.message_id = message_id


    def sinal_result(self):
        message_id = self.bot.send_message(self.canal, text=f'''
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✳ RESULTADOS DAS ENTRADAS ✳
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
▪ TOTAL DE ENTRADAS = {self.total_rounds}
                      
▪ TOTAL DE WINS = {self.total_wins}
                      
▪ WINS CONSECUTIVOS = {self.consecutive_wins}
                      
▪ WIN DE PRIMEIRA = {self.win_0}
                      
▪ WIN GALE 1 = {self.win_gale_one}
                      
▪ WIN GALE 2 = {self.win_gale_two}
                      
▪ WIN GALE 3 = {self.win_gale_three} 
                      
▪ TOTAL DE LOSS = {self.Loss}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
▪ ACERTIVIDADE =        {self.hit_hat()}%

▪ ACERTIVIDADE DE 1° =  {self.first_time_hit_hat()}%
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
        ''').message_id
        self.message_id = message_id


    def delete_message(self):
        self.bot.delete_message(self.canal, self.message_id)


    def sinal_prompt(self):
        print(f'''
RESULTADOS DAS ENTRADAS
=========================
TOTAL DE ENTRADAS = {self.total_rounds}
TOTAL DE WINS = {self.total_wins}
WINS CONSECUTIVOS = {self.consecutive_wins}
WINS DE PRIMEIRA = {self.win_0}
WINS GALE 1 = {self.win_gale_one}
WINS GALE 2 = {self.win_gale_two}
WINS NO BRANCO = {self.win_white}
TOTAL DE LOSS = {self.Loss}
=========================
=========================
ACERTOS TOTAIS = {self.hit_hat()}%
ACERTOS DE PRIMEIRA = {self.first_time_hit_hat()}%
=========================
        ''')

## MÉTODOS DE ANALISE ##
    def num_estrategy(self, num):
        if num == 3:
            print('EM ANALISE...')
            self.total_rounds += 1
            self.alert = 2
            self.sinal = 3
            self.control = 4
            self.gale1 = 5
            self.gale2 = 6
            self.gale3 = 7
            while True:
                try:
                    try:
                        self.sondar_resultado()
                        self.status()
                    except:
                        break
                    if self.momento == 'complete':
                        self.cont += 1
                        sleep(4.7)
                        if self.cont == self.alert:
                            self.delete_message()
                            self.atencao()
                        if self.cont == self.sinal:
                            self.delete_message()
                            self.sinal_preto()
                        if self.cont == self.control:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN!''')
                                self.filter_control(0)
                                self.win_direct()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} GALE 1''')
                                self.sinal_gale1()
                                continue
                        if self.cont == self.gale1:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN GALE 1!''')
                                self.filter_control(1)
                                self.delete_message()
                                self.win_gale()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} GALE 2''')
                                self.delete_message()
                                self.sinal_gale2()
                                continue
                        if self.cont == self.gale2:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN GALE 2!''')
                                self.filter_control(2)
                                self.delete_message()
                                self.win_gale()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} GALE 3!''')
                                self.delete_message()
                                self.sinal_gale3()
                                continue
                        if self.cont == self.gale3:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN GALE 3!''')
                                self.filter_control(3)
                                self.delete_message()
                                self.win_gale()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} LOSS!''')
                                self.Loss += 1
                                self.consecutive_wins = 0
                                self.delete_message()
                                self.derrora()
                                self.reset()
                                break
                    else:
                        continue
                except TimeoutError:
                    break
            self.taxa = self.hit_hat()
            self.first_time_hit_hat()
            self.sinal_prompt()
            self.sinal_result()
            return
        if num == 4:
            print('EM ANALISE...')
            self.total_rounds += 1
            self.alert = 3
            self.sinal = 4
            self.control = 5
            self.gale1 = 6
            self.gale2 = 7
            self.gale3 = 8
            while True:
                try:
                    try:
                        self.sondar_resultado()
                        self.status()
                    except:
                        break
                    if self.momento == 'complete':
                        self.cont += 1
                        sleep(4.7)
                        if self.cont == self.alert:
                            self.delete_message()
                            self.atencao()
                        if self.cont == self.sinal:
                            self.delete_message()
                            self.sinal_preto()
                        if self.cont == self.control:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN!''')
                                self.filter_control(0)
                                self.win_direct()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} GALE 1''')
                                self.sinal_gale1()
                                continue
                        if self.cont == self.gale1:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN GALE 1!''')
                                self.filter_control(1)
                                self.delete_message()
                                self.win_gale()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} GALE 2''')
                                self.delete_message()
                                self.sinal_gale2()
                                continue
                        if self.cont == self.gale2:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN GALE 2!''')
                                self.filter_control(2)
                                self.delete_message()
                                self.win_gale()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} GALE 3!''')
                                self.delete_message()
                                self.sinal_gale3()
                                continue
                        if self.cont == self.gale3:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN GALE 3!''')
                                self.filter_control(3)
                                self.delete_message()
                                self.win_gale()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} LOSS!''')
                                self.Loss += 1
                                self.consecutive_wins = 0
                                self.delete_message()
                                self.derrora()
                                self.reset()
                                break
                    else:
                        continue
                except TimeoutError:
                    break
            self.hit_hat()
            self.first_time_hit_hat()
            self.sinal_prompt()
            self.sinal_result()
            return
        if num == 5:
            print('EM ANALISE...')
            self.total_rounds += 1
            self.alert = 4
            self.sinal = 5
            self.control = 6
            self.gale1 = 7
            self.gale2 = 8
            self.gale3 = 9
            while True:
                try:
                    try:
                        self.sondar_resultado()
                        self.status()
                    except:
                        break
                    if self.momento == 'complete':
                        self.cont += 1
                        sleep(4.7)
                        if self.cont == self.alert:
                            self.delete_message()
                            self.atencao()
                        if self.cont == self.sinal:
                            self.delete_message()
                            self.sinal_preto()
                        if self.cont == self.control:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN!''')
                                self.filter_control(0)
                                self.win_direct()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} GALE 1''')
                                self.sinal_gale1()
                                continue
                        if self.cont == self.gale1:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN GALE 1!''')
                                self.filter_control(1)
                                self.delete_message()
                                self.win_gale()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} GALE 2''')
                                self.delete_message()
                                self.sinal_gale2()
                                continue
                        if self.cont == self.gale2:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN GALE 2!''')
                                self.filter_control(2)
                                self.delete_message()
                                self.win_gale()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} GALE 3!''')
                                self.delete_message()
                                self.sinal_gale3()
                                continue
                        if self.cont == self.gale3:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN GALE 3!''')
                                self.filter_control(3)
                                self.delete_message()
                                self.win_gale()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} LOSS!''')
                                self.Loss += 1
                                self.consecutive_wins = 0
                                self.delete_message()
                                self.derrora()
                                self.reset()
                                break
                    else:
                        continue
                except TimeoutError:
                    break
            self.hit_hat()
            self.first_time_hit_hat()
            self.sinal_prompt()
            self.sinal_result()
            return
        if num == 6:
            print('EM ANALISE...')
            self.total_rounds += 1
            self.alert = 5
            self.sinal = 6
            self.control = 7
            self.gale1 = 8
            self.gale2 = 9
            self.gale3 = 10
            while True:
                try:
                    try:
                        self.sondar_resultado()
                        self.status()
                    except:
                        break
                    if self.momento == 'complete':
                        self.cont += 1
                        sleep(4.7)
                        if self.cont == self.alert:
                            self.delete_message()
                            self.atencao()
                        if self.cont == self.sinal:
                            self.delete_message()
                            self.sinal_preto()
                        if self.cont == self.control:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN!''')
                                self.filter_control(0)
                                self.win_direct()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} GALE 1''')
                                self.sinal_gale1()
                                continue
                        if self.cont == self.gale1:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN GALE 1!''')
                                self.filter_control(1)
                                self.delete_message()
                                self.win_gale()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} GALE 2''')
                                self.delete_message()
                                self.sinal_gale2()
                                continue
                        if self.cont == self.gale2:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN GALE 2!''')
                                self.filter_control(2)
                                self.delete_message()
                                self.win_gale()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} GALE 3!''')
                                self.delete_message()
                                self.sinal_gale3()
                                continue
                        if self.cont == self.gale3:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN GALE 3!''')
                                self.filter_control(3)
                                self.delete_message()
                                self.win_gale()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} LOSS!''')
                                self.Loss += 1
                                self.consecutive_wins = 0
                                self.delete_message()
                                self.derrora()
                                self.reset()
                                break
                    else:
                        continue
                except TimeoutError:
                    break
            self.hit_hat()
            self.first_time_hit_hat()
            self.sinal_prompt()
            self.sinal_result()
            return
        if num == 7:
            print('EM ANALISE...')
            self.total_rounds += 1
            self.alert = 6
            self.sinal = 7
            self.control = 8
            self.gale1 = 9
            self.gale2 = 10
            self.gale3 = 11
            while True:
                try:
                    try:
                        self.sondar_resultado()
                        self.status()
                    except:
                        break
                    if self.momento == 'complete':
                        self.cont += 1
                        sleep(4.7)
                        if self.cont == self.alert:
                            self.delete_message()
                            self.atencao()
                        if self.cont == self.sinal:
                            self.delete_message()
                            self.sinal_preto()
                        if self.cont == self.control:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN!''')
                                self.filter_control(0)
                                self.win_direct()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} GALE 1''')
                                self.sinal_gale1()
                                continue
                        if self.cont == self.gale1:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN GALE 1!''')
                                self.filter_control(1)
                                self.delete_message()
                                self.win_gale()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} GALE 2''')
                                self.delete_message()
                                self.sinal_gale2()
                                continue
                        if self.cont == self.gale2:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN GALE 2!''')
                                self.filter_control(2)
                                self.delete_message()
                                self.win_gale()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} GALE 3!''')
                                self.delete_message()
                                self.sinal_gale3()
                                continue
                        if self.cont == self.gale3:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN GALE 3!''')
                                self.filter_control(3)
                                self.delete_message()
                                self.win_gale()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} LOSS!''')
                                self.Loss += 1
                                self.consecutive_wins = 0
                                self.delete_message()
                                self.derrora()
                                self.reset()
                                break
                    else:
                        continue
                except TimeoutError:
                    break
            self.hit_hat()
            self.first_time_hit_hat()
            self.sinal_prompt()
            self.sinal_result()
            return
        if num == 8:
            print('EM ANALISE...')
            self.total_rounds += 1
            self.alert = 7
            self.sinal = 8
            self.control = 9
            self.gale1 = 10
            self.gale2 = 11
            self.gale3 = 12
            while True:
                try:
                    try:
                        self.sondar_resultado()
                        self.status()
                    except:
                        break
                    if self.momento == 'complete':
                        self.cont += 1
                        sleep(4.7)
                        if self.cont == self.alert:
                            self.delete_message()
                            self.atencao()
                        if self.cont == self.sinal:
                            self.delete_message()
                            self.sinal_vermelho()
                        if self.cont == self.control:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN!''')
                                self.filter_control(0)
                                self.win_direct()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} GALE 1''')
                                self.sinal_gale1()
                                continue
                        if self.cont == self.gale1:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN GALE 1!''')
                                self.filter_control(1)
                                self.delete_message()
                                self.win_gale()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} GALE 2''')
                                self.delete_message()
                                self.sinal_gale2()
                                continue
                        if self.cont == self.gale2:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN GALE 2!''')
                                self.filter_control(2)
                                self.delete_message()
                                self.win_gale()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} GALE 3!''')
                                self.delete_message()
                                self.sinal_gale3()
                                continue
                        if self.cont == self.gale3:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN GALE 3!''')
                                self.filter_control(3)
                                self.delete_message()
                                self.win_gale()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} LOSS!''')
                                self.Loss += 1
                                self.consecutive_wins = 0
                                self.delete_message()
                                self.derrora()
                                self.reset()
                                break
                    else:
                        continue
                except TimeoutError:
                    break
            self.hit_hat()
            self.first_time_hit_hat()
            self.sinal_prompt()
            self.sinal_result()
            return
        if num == 9:
            print('EM ANALISE...')
            self.total_rounds += 1
            self.alert = 8
            self.sinal = 9
            self.control = 10
            self.gale1 = 11
            self.gale2 = 12
            self.gale3 = 13
            while True:
                try:
                    try:
                        self.sondar_resultado()
                        self.status()
                    except:
                        break
                    if self.momento == 'complete':
                        self.cont += 1
                        sleep(4.7)
                        if self.cont == self.alert:
                            self.delete_message()
                            self.atencao()
                        if self.cont == self.sinal:
                            self.delete_message()
                            self.sinal_vermelho()
                        if self.cont == self.control:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN!''')
                                self.filter_control(0)
                                self.win_direct()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} GALE 1''')
                                self.sinal_gale1()
                                continue
                        if self.cont == self.gale1:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN GALE 1!''')
                                self.filter_control(1)
                                self.delete_message()
                                self.win_gale()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} GALE 2''')
                                self.delete_message()
                                self.sinal_gale2()
                                continue
                        if self.cont == self.gale2:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN GALE 2!''')
                                self.filter_control(2)
                                self.delete_message()
                                self.win_gale()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} GALE 3!''')
                                self.delete_message()
                                self.sinal_gale3()
                                continue
                        if self.cont == self.gale3:
                            correcao = self.correct(num)
                            if correcao:
                                print(f'''BLAZE GIROU {self.ult_numero()} WIN GALE 3!''')
                                self.filter_control(3)
                                self.delete_message()
                                self.win_gale()
                                self.reset()
                                break
                            else:
                                print(f'''BLAZE GIROU {self.ult_numero()} LOSS!''')
                                self.Loss += 1
                                self.consecutive_wins = 0
                                self.delete_message()
                                self.derrora()
                                self.reset()
                                break
                    else:
                        continue
                except TimeoutError:
                    break
            self.hit_hat()
            self.first_time_hit_hat()
            self.sinal_prompt()
            self.sinal_result()
            return


    def reset(self):
        self.control = 0
        self.alert = 0
        self.gale1 = 0
        self.gale2 = 0
        self.gale3 = 0
        self.message_id = 0
        self.cont = 0


    def correct(self, num):
        if num == 3 or num == 4 or num == 5 or num == 6 or num == 7:
            verfy = 'preto'
        if num == 8 or num == 9:
            verfy = 'vermelho'
        if verfy == 'preto':
            if self.ult_cor() == '⚫':
                self.total_wins += 1
                return True
            else:
                return False
        if verfy == 'vermelho':
            if self.ult_cor() == '🔴':
                self.total_wins += 1
                return True
            else:
                return False


    def filter_control(self, gale):
        self.consecutive_wins += 1
        if gale == 0:
            self.win_0 += 1
            return
        elif gale == 1:
            self.win_gale_one += 1
            return
        elif gale == 2:
            self.win_gale_two += 1
            return
        else:
            self.win_gale_three += 1
            return


## CONTADORES DE RESULTADOS ##
    def hit_hat(self):
        self.porcent = (self.total_wins * 100) // self.total_rounds
        return self.porcent


    def first_time_hit_hat(self):
        self.taxa = (self.win_0 * 100) // self.total_rounds
        return self.taxa


    def results_counter(self):
        self.consecutive_wins = 0
        self.total_rounds = 0
        self.Loss = 0
        self.win_0 = 0
        self.win_gale_one = 0
        self.win_gale_two = 0
        self.win_gale_three = 0
        self.max_count = 0
        self.win_white = 0
        self.total_wins = 0

    
    def control_count(self, count):
        if count == 500:
            self.reset_count()


    def reset_count(self):
        self.win_0 = 0
        self.win_gale_one = 0
        self.win_gale_two = 0
        self.win_gale_three = 0
        self.max_count = 0
        self.win_white = 0

        


print('''\033[;1m\033[0;32m''')
token = input('DIGITE SEU TOKEN DO BOT: ')
sleep(1)
chat_id = input('DIGITE SEU CHAT_ID: ')
sleep(1)
print('''\033[;1m\033[0;32m
BOT CONFIGURADO INICIANDO ANALISES...
\033[0;0m
''')   
sleep(2)     

bot_blaze(token, chat_id)
print("Tempo de execução exedida por favor reinicie o Bot")

