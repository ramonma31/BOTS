from modulos import *
from Blaze_sinais import bot_blaze

class Bot_White_time(bot_blaze):

    def variaveis(self):
        self.round_counter = 0
        self.red_counter = 0
        self.black_counter = 0
        self.white_counter = 0
        self.time_counter = 0
        self.round_control = 0
        self.time_control = 0
        self.hold_control_one = 0
        self.hold_control_two = 0
        self.hold_control_three = 0 
        self.bank_control = 0
        self.number1_control = 0
        self.number2_control = 0
        self.number3_control = 0
        self.number4_control = 0
        self.number5_control = 0
        self.number6_control = 0
        self.number7_control = 0
        self.number8_control = 0
        self.number9_control = 0
        self.number10_control = 0
        self.number11_control = 0
        self.number12_control = 0
        self.number13_control = 0
        self.number14_control = 0
        self.statistics_control = 0


    def mostrar_resultados(self):
        self.lb_results['text'] = '''
DEU MAIS QUE CERTO
        '''


    def mostrar_estatisticas(self):
        self.lb_estatisticas['text'] = '''
DEU CERTO
        '''