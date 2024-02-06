import Telegram_bot

api2 = '5982431594:AAHoSiZo18nVdtyIZQre4BCLQK4EtTvQzxQ'
canal = '@imperio_sinais_gratis'
bot = Telegram_bot.Bot_Telegram(api2, canal)

update = bot.update_id()
id = bot.message_id(update)
print(id)