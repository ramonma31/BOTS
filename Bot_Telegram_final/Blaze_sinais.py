import requests
import json
from datetime import datetime
from pytz import timezone   

class bot_blaze:
    def __init__(self):
        self.url = 'https://blaze.com/api/roulette_games/current'
    
    ## Método de requisicao ##
    def sondar_resultado(self):
        response = requests.get(self.url)
        self.resposta = json.loads(response.content)


    def ult_numero(self):
        res_num = self.resposta['roll']
        self.num_jogada = res_num
    

    def ult_cor(self):
        res_cor = self.resposta['color']
        if res_cor == 1:
            return '🟥'
        if res_cor == 2:
            return '⬛️'
        if res_cor == 0:
            return '⬜️'
             
    

    def status(self, dicionario):
        atualizacao = dicionario['status']
        return atualizacao
    

    def minuto_atual(self):
        fuso_horario = timezone('America/Fortaleza')
        atual = datetime.now(tz=fuso_horario)
        hora_minuto = atual.strftime('%M')
        minuto_atual = int(hora_minuto)
        return minuto_atual

    
    def hora_atual(self):
        fuso_horario = timezone('America/Fortaleza')
        atual = datetime.now(tz=fuso_horario)
        hora = atual.strftime('%H')
        hora_atual = int(hora)
        return hora_atual
    
    
    def minuto_sinal(self, num1, num2):
        numero_da_jogada = (num1 + num2) - 2
        if numero_da_jogada < 0:
            numero_da_jogada = 2
        if numero_da_jogada >= 0 and numero_da_jogada <= 2:
            numero_da_jogada == 2
        return numero_da_jogada
