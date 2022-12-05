import schedule
import datetime
import time
import sys
import atividade_09_automatizar_github.robo_09 as apr
import atividade_07_automatizar_email.robo_07 as send

print('\niniciou\n')

while True:
    t = datetime.datetime.now().strftime("%H:%M:%S")
    if t == '17:47:00':
        try:
            print('robo rodando...')
            #SEMPRE ALTERAR O NOME DA PASTE SCHEDULE
            dia = datetime.datetime.now().strftime('%A, %d de %B de %Y')
            hora = datetime.datetime.now().strftime('%H:%M:%S')
            apr.bot_09()
            print('passou, deu boa')
            send.enviar_email('fsanches.0502@gmail.com',f'commitado com sucesso {dia} as{datetime.datetime.now().strftime("%H:%M:%S")}')
            while True:
                schedule.run_pending()
                time.sleep(1)
        except:
            exc_type, error, line = sys.exc_info()
            print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')
        print('robô finalizado')
    else:
        time.sleep(1)