import schedule_org
import time
from Robo09 import bot_09
from robo_07 import enviar_email


try:
    print('iniciou...')
    #SEMPRE ALTERAR O NOME DA PASTE SCHEDULE
    schedule_org.every().day.at('16:38').do(bot_09())
    while True:
        schedule_org.run_pending()
        time.sleep(1)
        enviar_email('fsanches.0502@gmail.com','commitado com sucesso')
except IndexError as e:
    #envia um email para alguém
    enviar_email('fsanches.0502@gmail.com',f'Erro =  {e}')