import requests
import json


class Bot_Telegram:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.url_base = f'https://api.telegram.org/bot{self.token}'

    # pegar message_id
    def message_id(self, id):
        url = f'https://api.telegram.org/bot{self.token}/getUpdates?offset={id}'
        requisicao2 = requests.get(url)
        resposta2 = json.loads(requisicao2.content)
        message = resposta2['result']
        filtro = message[0]
        menssagem = filtro['channel_post']
        message_id = menssagem['message_id']
        return message_id



    # pegar update_id
    def update_id(self):
        url = f'{self.url_base}/getUpdates?allowed_updates=[]'
        requisicao = requests.get(url)
        resposta = json.loads(requisicao.content)
        message = resposta['result']
        controle_message = [x['update_id'] for x in message]
        tam = len(controle_message)
        update_id = controle_message[tam - 1]
        return update_id


    def send_message(self, text):
        link_requisicao = f'{self.url_base}/sendMessage?chat_id={self.chat_id}&text={text}'
        response = requests.get(link_requisicao)
        if response.status_code == 200:
            return 'OK'
        else:
            return 'erro ao enviar mensagem'
        

    def send_sticker(self, file_id):
        link_requisicao = f'{self.url_base}/sendSticker?chat_id={self.chat_id}&sticker={file_id}'
        response = requests.get(link_requisicao)
        if response.status_code == 200:
            return True
        else:
            return False
        
    
    def delete_message(self, message_id):
        link_requisicao = f'{self.url_base}/deleteMessage?chat_id={self.chat_id}&message_id={message_id}'
        response = requests.get(link_requisicao)
        if response.status_code == 200:
            return 'ok'
        else:
            return 'erro'
    

    def message(self, id):
        url = f'https://api.telegram.org/bot{self.token}/getUpdates?offset={id}'
        requisicao = requests.get(url)
        resposta = json.loads(requisicao.content)
        message = resposta['result']
        filtro = message[0]
        menssagem = filtro['channel_post']
        message = menssagem['text']
        return message

