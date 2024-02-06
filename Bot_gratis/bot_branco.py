import telebot


class Bot_Branco_Vip():
    def __init__(self):
        ### colocar seu token ####
        api = '5957474118:AAGdKj1h3JAdGp_HXCwzIzDwqEcb6bpWta8'
        self.canal = '-1001847597140'

        ### Criando o Bot_Telegram
        self.bot = telebot.TeleBot(api)
        self.bot_corretor = Telegram_bot.Bot_Telegram(api, self.canal)

        ## Lista para analise ##
        self.lista_analise = []
        self.min_para_jog = None
        self.hora_sinal = None
        self.minuto_sinal = None
        self.start_minute_0()

        # start bot #
    def start_minute_0(self):
            while True:
                bot_blaze = Blaze_sinais.bot_blaze()
                m = bot_blaze.minuto_atual()
                h = bot_blaze.hora_atual()
                ## analise no minuto 0 ##
                if m == 0 or m == 10 or m == 20 or m == 30 or m == 40 or m == 50:
                    resultado = bot_blaze.sondar_resultado()
                    if resultado:
                        status = bot_blaze.status(resultado)
                    else:
                        status = None
                    if status == 'complete':
                        numero = bot_blaze.ult_numero(resultado)
                        cor = bot_blaze.ult_cor(resultado)
                        
                        if numero > 10:
                            new_num = numero - 10
                            self.lista_analise.append(new_num)
                            self.lista_analise.copy()
                            sleep(4.7)
                        elif numero == 10:
                            new_num_1 = numero - 5
                            self.lista_analise.append(new_num_1)
                            self.lista_analise.copy()
                            sleep(4.7)
                        else:
                            self.lista_analise.append(numero)
                            self.lista_analise.copy()
                            sleep(4.7)
                    else:
                        continue

                if len(self.lista_analise) == 2:
                    num_1 = self.lista_analise[0]
                    num_2 = self.lista_analise[1]
                    min_para_jog = bot_blaze.minuto_sinal(num1=num_1, num2=num_2)
                    if min_para_jog > 10:
                        self.minuto_sinal = m + min_para_jog
                    else:
                        self.hora_sinal = m + min_para_jog
                    self.lista_analise.clear()
                
                if self.minuto_sinal:
                    entrada = self.minuto_sinal - 1
                    if m == entrada:
                        final = self.minuto_sinal + 4
                        if final == 60:
                            new_h = h + 1
                            final = 0
                        if final > 60:
                            new_h = h + 1
                            final -= 60
                        else:
                            new_h = h
                        self.bot.send_sticker(chat_id=self.canal, sticker=self.Entrada_confirmada)
                        self.bot.send_message(chat_id=self.canal, text=f'''
            🤖ATENÇÃO🤖

            ENTRAR ⚪⚪
            ⏰{h}:{self.minuto_sinal}
            🎲🎲🎲ATÉ🎲🎲🎲
            ⏰{new_h}:{final} 
                        ''')
                        print(f'ok {self.minuto_sinal}')
                        ## controle de wins ##
                        sleep(60)
                        while True:
                            h = bot_blaze.hora_atual()
                            m = bot_blaze.minuto_atual()
                            resultado = bot_blaze.sondar_resultado()
                            status = bot_blaze.status(resultado) 
                            if status == 'complete':
                                numero = bot_blaze.ult_numero(resultado)
                                if numero == 0:
                                    self.bot.send_sticker(chat_id=self.canal, sticker=self.win_sem_gale)
                                    self.bot.send_message(self.canal, f'''
            BATEU ⚪ ÁS ⏰{h}:{m}
                                    ''')
                                    self.minuto_sinal = None
                                    break
                                if m == final + 1:
                                    self.bot.send_sticker(chat_id=self.canal, sticker=self.loss)
                                    self.minuto_sinal = None
                                    break
                                sleep(4.7)
                            else:
                                continue
                            
                if self.hora_sinal:
                    chamada = self.hora_sinal - 1
                    if m == chamada:
                        minuto_final = self.hora_sinal + 5
                        if minuto_final == 60:
                            new_h = h + 1
                            minuto_final = 0
                        if minuto_final > 60:
                            new_h = h + 1
                            minuto_final -= 60
                        else:
                            new_h = h
                        self.bot.send_sticker(chat_id=self.canal, sticker=self.Entrada_confirmada)
                        self.bot.send_message(chat_id=self.canal, text=f'''
            🤖ATENÇÃO🤖

            ENTRAR ⚪⚪
            ⏰{h}:{self.hora_sinal}
            🎲🎲🎲ATÉ🎲🎲🎲
            ⏰{new_h}:{minuto_final}  
                        ''')
                        print(f'ok {self.hora_sinal}')
                        sleep(60)
                        while True:
                            h = bot_blaze.hora_atual()
                            m = bot_blaze.minuto_atual()
                            resultado = bot_blaze.sondar_resultado()
                            status = bot_blaze.status(resultado) 
                            if status == 'complete':
                                numero = bot_blaze.ult_numero(resultado)
                                if numero == 0:
                                    self.bot.send_sticker(chat_id=self.canal, sticker=self.win_sem_gale)
                                    self.bot.send_message(self.canal, f'''
            BATEU ⚪ ÁS ⏰{h}:{m}
                                    ''')
                                    self.hora_sinal = None
                                    break
                                if m == minuto_final + 1:
                                    self.bot.send_sticker(chat_id=self.canal, sticker=self.loss)
                                    self.hora_sinal = None
                                    break
                                sleep(4.7)
                            else:
                                continue
    def start_minute_05(self):
        while True:
            bot_blaze = Blaze_sinais.bot_blaze()
            m = bot_blaze.minuto_atual()
            h = bot_blaze.hora_atual()
            ## analise no minuto 0 ##
            if m == 5 or m == 15 or m == 25 or m == 35 or m == 45 or m == 55:
                resultado = bot_blaze.sondar_resultado()
                status = bot_blaze.status(resultado)
                if status == 'complete':
                    numero = bot_blaze.ult_numero(resultado)
                    if numero > 10:
                        new_num = numero - 10
                        self.lista_analise.append(new_num)
                        self.lista_analise.copy()
                        sleep(4.7)
                    elif numero == 10:
                        new_num_1 = numero - 5
                        self.lista_analise.append(new_num_1)
                        self.lista_analise.copy()
                        sleep(4.7)
                    else:
                        self.lista_analise.append(numero)
                        self.lista_analise.copy()
                        sleep(4.7)
                else:
                    continue

            if len(self.lista_analise) == 2:
                num_1 = self.lista_analise[0]
                num_2 = self.lista_analise[1]
                min_para_jog = bot_blaze.minuto_sinal(num1=num_1, num2=num_2)
                if min_para_jog > 10:
                    self.minuto_sinal = m + min_para_jog
                else:
                    self.hora_sinal = m + min_para_jog
                self.lista_analise.clear()
            
            if self.minuto_sinal:
                entrada = self.minuto_sinal - 1
                if m == entrada:
                    final = self.minuto_sinal + 4
                    if final == 60:
                        new_h = h + 1
                        final = 0
                    if final > 60:
                        new_h = h + 1
                        final -= 60
                    else:
                        new_h = h
                    self.bot.send_sticker(chat_id=self.canal, sticker=self.Entrada_confirmada)
                    self.bot.send_message(chat_id=self.canal, text=f'''
        🤖ATENÇÃO🤖

        ENTRAR ⚪⚪
        ⏰{h}:{self.minuto_sinal}
        🎲🎲🎲ATÉ🎲🎲🎲
        ⏰{new_h}:{final} 
                    ''')
                    print(f'ok {self.minuto_sinal}')
                    ## controle de wins ##
                    sleep(60)
                    while True:
                        h = bot_blaze.hora_atual()
                        m = bot_blaze.minuto_atual()
                        resultado = bot_blaze.sondar_resultado()
                        status = bot_blaze.status(resultado) 
                        if status == 'complete':
                            numero = bot_blaze.ult_numero(resultado)
                            if numero == 0:
                                self.bot.send_sticker(chat_id=self.canal, sticker=self.win_sem_gale)
                                self.bot.send_message(self.canal, f'''
        BATEU ⚪ ÁS ⏰{h}:{m}
                                ''')
                                self.minuto_sinal = None
                                break
                            if m == final + 1:
                                self.bot.send_sticker(chat_id=self.canal, sticker=self.loss)
                                self.minuto_sinal = None
                                break
                            sleep(4.7)
                        else:
                            continue
            else:
                pass            
            if self.hora_sinal:
                chamada = self.hora_sinal - 1
                if m == chamada:
                    minuto_final = self.hora_sinal + 5
                    if minuto_final == 60:
                        new_h = h + 1
                        minuto_final = 0
                    if minuto_final > 60:
                        new_h = h + 1
                        minuto_final -= 60
                    else:
                        new_h = h
                    self.bot.send_sticker(chat_id=self.canal, sticker=self.Entrada_confirmada)
                    self.bot.send_message(chat_id=self.canal, text=f'''
        🤖ATENÇÃO🤖

        ENTRAR ⚪⚪
        ⏰{h}:{self.hora_sinal}
        🎲🎲🎲ATÉ🎲🎲🎲
        ⏰{new_h}:{minuto_final}  
                    ''')
                    print(f'ok {self.hora_sinal}')
                    sleep(60)
                    while True:
                        h = bot_blaze.hora_atual()
                        m = bot_blaze.minuto_atual()
                        resultado = bot_blaze.sondar_resultado()
                        status = bot_blaze.status(resultado) 
                        if status == 'complete':
                            numero = bot_blaze.ult_numero(resultado)
                            if numero == 0:
                                self.bot.send_sticker(chat_id=self.canal, sticker=self.win_sem_gale)
                                self.bot.send_message(self.canal, f'''
        BATEU ⚪ ÁS ⏰{h}:{m}
                                ''')
                                self.hora_sinal = None
                                break
                            if m == minuto_final + 1:
                                self.bot.send_sticker(chat_id=self.canal, sticker=self.loss)
                                self.hora_sinal = None
                                break
                            sleep(4.7)
                        else:
                            continue                
            else:
                continue  


Bot_Branco_Vip()