import Telegram_bot
from time import sleep
import Blaze_sinais
import estrategy

bot_blaze = Blaze_sinais.bot_blaze()

m = bot_blaze.minuto_atual()
final = m + 1
while True:
    m = bot_blaze.minuto_atual()
    if m == final:
        print(m)
        break
    print(m, final)
print('fim')
