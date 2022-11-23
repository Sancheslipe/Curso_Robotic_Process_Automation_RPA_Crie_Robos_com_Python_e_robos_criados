import schedule
import time
import sys
import atividade_09_automatizar_github.robo_09 as apr
import atividade_07_automatizar_email.robo_07 as send
#aaaaaaa

try:
    # aaaa:
    print('iniciou...')
    #SEMPRE ALTERAR O NOME DA PASTE SCHEDULE
    schedule.every().day.at("17:26").do(apr.bot_09(), 'ATIV009')
    print('passou, deu boa')
    send.enviar_email('fsanches.0502@gmail.com','commitado com sucesso')
    while True:
        schedule.run_pending()
        time.sleep(1)
except:
    exc_type, error, line = sys.exc_info()
    print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')
