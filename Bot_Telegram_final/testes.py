from modulos import *
from Bot_White import Bot_White_time

janela_principal = Tk()

class app_principal(Bot_White_time):
    def __init__(self):
        self.janela_principal = janela_principal
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.barra_de_progresso()
        janela_principal.mainloop()


    def tela(self):
        self.janela_principal.title('IMPERIO TEAM BLAZE')
        self.janela_principal.configure(background='#9E0E03')
        self.janela_principal.geometry('900x700')
        self.janela_principal.maxsize(width=900, height=700)
        self.janela_principal.minsize(width=400, height=300)


    def frames_da_tela(self):
        self.frames_1 = Frame(self.janela_principal, bd=4, bg='#F7ECEC',
                              highlightbackground='#2D0404', highlightthickness=2)
        self.frames_1.place(relx= 0.01, rely= 0.01, relwidth= 0.5, relheight= 0.49)

        self.frames_2 = Frame(self.janela_principal, bd=4, bg='#F7ECEC',
                              highlightbackground='#2D0404', highlightthickness=2)
        self.frames_2.place(relx= 0.01, rely= 0.5, relwidth= 0.98, relheight= 0.49)

        self.frames_3 = Frame(self.janela_principal, bd=4, bg='#F7ECEC',
                              highlightbackground='#2D0404', highlightthickness=2)
        self.frames_3.place(relx= 0.51, rely= 0.01, relwidth= 0.48, relheight= 0.49)




    def widgets_frame1(self):
        # BOTOÊS DE AÇÃO LABELS#

        self.desc_botao1 = Label(self.frames_1, text='INIÇIAR BOT BRANCO', background='#F7ECEC', font=('Georgia', 7, 'bold'))
        self.desc_botao1.place(relx=0.01, rely=0.0, relwidth=0.29, relheight=0.09)

        self.bt_init_bot_white = Button(self.frames_1, bd= 4, bg='white', fg='black', text='START-WHITE',
            activebackground='#87716E', activeforeground='black',
            font=('Georgia', 10, 'bold'))
        #POSIÇÃO BOTÃO BRANCO
        self.bt_init_bot_white.place(relx=0.01, rely=0.08, relwidth=0.29, relheight=0.15)

        self.desc_botao2 = Label(self.frames_1, text='INIÇIAR BOT CORES', background='#F7ECEC', font=('Georgia', 7, 'bold'))
        self.desc_botao2.place(relx=0.3, rely=0.0, relwidth=0.29, relheight=0.09)

        self.bt_init_bot_cores = Button(self.frames_1, bd= 4, bg='#961803', fg='white', text='START-COLORS',
            activebackground='#87716E', activeforeground='red',
            font=('Georgia', 10, 'bold'))
        self.bt_init_bot_cores.place(relx=0.3, rely=0.08, relwidth=0.29, relheight=0.15)

        self.enter1 = Button(self.frames_1, bd=4, bg='black', fg='#F5DEDE', text='ENTER')
        self.enter1.place(relx=0.71, rely=0.32, relwidth=0.15, relheight=0.07)

        self.enter2 = Button(self.frames_1, bd=4, bg='black', fg='#F5DEDE', text='ENTER')
        self.enter2.place(relx=0.71, rely=0.46, relwidth=0.15, relheight=0.07)

        # ENTRYS  e Labels#
        self.lb_token = Label(self.frames_1, text='TOKEN', background='#961803', fg='white', font=('Georgia', 12, 'bold'))
        self.lb_token.place(relx=0.01, rely=0.25, relwidth=0.18)

        self.token_entry = Entry(self.frames_1)
        self.token_entry.place(relx=0.01, rely=0.33, relwidth=0.7)

        self.lb_chat = Label(self.frames_1, text='CHAT_ID', background='#961803', fg='white', font=('Georgia', 10, 'bold'))
        self.lb_chat.place(relx=0.01, rely=0.4, relwidth=0.18)

        self.chat_entry = Entry(self.frames_1)
        self.chat_entry.place(relx=0.01, rely=0.47, relwidth=0.7)

        self.lb_estatisticas = Label(self.frames_3, text='')
        self.lb_estatisticas.place(relx=0.1, rely=0.1)

        self.lb_results = Label(self.frames_3, text='')
        self.lb_results.place(relx=0.1, rely=0.2)


    def barra_de_progresso(self):
        self.barra = ttk.Progressbar(self.frames_3, orient=HORIZONTAL, length=200, mode='determinate')
        self.barra.place(relx=0.1, rely=0.9, relwidth=0.8)


app_principal()

