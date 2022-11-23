import schedule
import time
from atividade_09_automatizar_github.robo_09 import bot_09
from atividade_07_automatizar_email.robo_07 import enviar_email


try:
    print('iniciou...')
    #SEMPRE ALTERAR O NOME DA PASTE SCHEDULE
    schedule.every().day.at('16:46').do(bot_09())
    while True:
        schedule.run_pending()
        time.sleep(1)
        enviar_email('fsanches.0502@gmail.com','commitado com sucesso')
except IndexError as e:
    #envia um email para alguém
    enviar_email('fsanches.0502@gmail.com',f'Erro =  {e}')