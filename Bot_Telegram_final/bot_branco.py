import telebot
import Blaze_sinais
from time import sleep

### colocar seu token ####
api = '5957474118:AAGdKj1h3JAdGp_HXCwzIzDwqEcb6bpWta8'
canal = '-1001847597140'

### Criando o Bot_Telegram
bot = telebot.TeleBot(api)

# Stikers #
win_sem_gale = 'CAACAgEAAx0CbiAYVAACEXhkIfGwidCSKmhZOD1TemdYy4gFdgACQAMAAoicCEUeXRPrEAM2Li8E'
win_no_gale = 'CAACAgEAAx0CbiAYVAACDFhkGxt9BXeGAjMRbiLH6YvsO_wGPwAC_AADQSaBR11zLQEy5HO0LwQ'
Entrada_confirmada = 'CAACAgEAAx0CbiAYVAACDFJkGxVqJpY6MSg9udscVKG5zQrunwACCgADLnPHPuJiimLffwABui8E'
loss = 'CAACAgEAAx0CbiAYVAACEXtkIfsdKgRgcRje5LkVOhMs76cq6QACDgUAAm5AEUX5pf4y2CRMLC8E'
em_analise = 'CAACAgEAAx0CbiAYVAACDFZkGxf2E5FkVGY2xzYr-JlPP2ckVwACDgADLnPHPvbAY0yXy1w9LwQ'
## Lista para analise ##
lista_analise = []
min_para_jog = None
hora_sinal = None
minuto_sinal = None
total_em_caixa = 164

    # start bot #
while True:
    bot_blaze = Blaze_sinais.bot_blaze()
    m = bot_blaze.minuto_atual()
    h = bot_blaze.hora_atual()
    ## analise no minuto 0 ##
    if m == 0 or m == 10 or m == 20 or m == 30 or m == 40 or m == 50:
        resultado = bot_blaze.sondar_resultado()
        status = bot_blaze.status(resultado)
        if status == 'complete':
            numero = bot_blaze.ult_numero(resultado)
            if numero > 10:
                new_num = numero - 10
                lista_analise.append(new_num)
                lista_analise.copy()
                sleep(4.7)
            elif numero == 10:
                new_num_1 = numero - 5
                lista_analise.append(new_num_1)
                lista_analise.copy()
                sleep(4.7)
            else:
                lista_analise.append(numero)
                lista_analise.copy()
                sleep(4.7)
        else:
            continue

    if len(lista_analise) == 2:
        num_1 = lista_analise[0]
        num_2 = lista_analise[1]
        min_para_jog = bot_blaze.minuto_sinal(num1=num_1, num2=num_2)
        if min_para_jog > 10:
            minuto_sinal = m + min_para_jog
        else:
            hora_sinal = m + min_para_jog
        lista_analise.clear()
    
    if minuto_sinal:
        entrada = minuto_sinal - 1
        if m == entrada:
            final = minuto_sinal + 5
            if final == 60:
                new_h = h + 1
                final = 0
            if final > 60:
                new_h = h + 1
                final -= 60
            if final <= 59:
                new_h = bot_blaze.hora_atual()
            bot.send_sticker(chat_id=canal, sticker=Entrada_confirmada)
            bot.send_message(chat_id=canal, text=f'''
🤖ATENÇÃO🤖

ENTRAR ⚪⚪
⏰{h}:{minuto_sinal}
🎲🎲🎲ATÉ🎲🎲🎲
⏰{new_h}:{final} 
            ''')
            print(f'ok {minuto_sinal}')
            ## controle de wins ##
            sleep(60)
            while True:
                h = bot_blaze.hora_atual()
                m = bot_blaze.minuto_atual()
                resultado = bot_blaze.sondar_resultado()
                status = bot_blaze.status(resultado) 
                if status == 'complete':
                    total_em_caixa -= 2
                    numero = bot_blaze.ult_numero(resultado)
                    if numero == 0:
                        total_em_caixa += 28
                        bot.send_sticker(chat_id=canal, sticker=win_sem_gale)
                        bot.send_message(canal, f'''
BATEU ⚪ ÁS ⏰{h}:{m}
TOTAL EM CAIXA = {total_em_caixa}
                        ''')
                        minuto_sinal = None
                        break
                    if m == final + 1:
                        bot.send_sticker(chat_id=canal, sticker=loss)
                        minuto_sinal = None
                        break
                    sleep(4.7)
                else:
                    continue
                
    if hora_sinal:
        chamada = hora_sinal - 1
        if m == chamada:
            minuto_final = hora_sinal + 5
            if minuto_final == 60:
                new_h = h + 1
                minuto_final = 0
            if minuto_final > 60:
                new_h = h + 1
                minuto_final -= 60
            else:
                new_h = h
            bot.send_sticker(chat_id=canal, sticker=Entrada_confirmada)
            bot.send_message(chat_id=canal, text=f'''
🤖ATENÇÃO🤖

ENTRAR ⚪⚪
⏰{h}:{hora_sinal}
🎲🎲🎲ATÉ🎲🎲🎲
⏰{new_h}:{minuto_final}  
            ''')
            print(f'ok {hora_sinal}')
            sleep(60)
            while True:
                h = bot_blaze.hora_atual()
                m = bot_blaze.minuto_atual()
                resultado = bot_blaze.sondar_resultado()
                status = bot_blaze.status(resultado) 
                if status == 'complete':
                    total_em_caixa -= 2
                    numero = bot_blaze.ult_numero(resultado)
                    if numero == 0:
                        total_em_caixa += 28
                        bot.send_sticker(chat_id=canal, sticker=win_sem_gale)
                        bot.send_message(canal, f'''
BATEU ⚪ ÁS ⏰{h}:{m}
TOTAL EM CAIXA = {total_em_caixa}
                        ''')
                        hora_sinal = None
                        break
                    if m == minuto_final + 1:
                        bot.send_sticker(chat_id=canal, sticker=loss)
                        bot.send_message(canal, text=f'''
TOTAL EM CAIXA = {total_em_caixa}
                        ''')
                        hora_sinal = None
                        break
                    sleep(4.7)
                else:
                    continue
    
