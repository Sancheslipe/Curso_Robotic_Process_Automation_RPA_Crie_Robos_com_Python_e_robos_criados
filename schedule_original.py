import sys
import time 
from datetime import datetime
import schedule
import atividade_08_automatizar_whatsapp.robo_08 as whats


try:

    schedule.every(1).days.at("09:16").do(whats.bot_08)
    while True:
        schedule.run_pending()
        # print(datetime.now().strftime("%H:%M:%S")) # printa hora minuto e segundo, com a finalidade de descobrir quanto tempo falta para a atividade começar  
        cont = 1
        print('aguardando'+'.'*cont) 
        time.sleep(1)
        cont+=1
except:
    exc_type, error, line = sys.exc_info()
    print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')