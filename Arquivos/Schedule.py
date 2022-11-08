import schedule
import time
from Robo01 import bot_robo01
try:
    print('iniciou...')
    #SEMPRE ALTERAR O NOME DA PASTE SCHEDULE
    schedule.every().day.at('14:58').do(bot_robo01)
    while True:
        schedule.run_pending()
        time.sleep(1)
except IndexError as e:
    #envia um email para alguém
    f'''
    
    '''