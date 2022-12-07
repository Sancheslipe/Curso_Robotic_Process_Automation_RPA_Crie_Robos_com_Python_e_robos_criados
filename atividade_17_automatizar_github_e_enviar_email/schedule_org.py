import datetime
import sys
import atividade_09_automatizar_github as apr
import atividade_07_automatizar_email.robo_07 as send

print('\niniciou\n')
try:
    print('robo rodando...')
    #SEMPRE ALTERAR O NOME DA PASTE SCHEDULE
    dia = datetime.datetime.now().strftime('%A, %d de %B de %Y')
    hora = datetime.datetime.now().strftime('%H:%M:%S')
    apr.bot_09()
    print('deu commit')
    send.enviar_email('fsanches.0502@gmail.com',f'commitado com sucesso {dia} as {hora}')
    print('enviou o email')
    print('robô finalizado')

except:
    exc_type, error, line = sys.exc_info()
    print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')



        