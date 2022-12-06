import os 
import sys
import time
from datetime import datetime 

def verificar_ultima_mod_e_apagar_arquivos_antigos(path_pasta):
    try:
        #recebe o ano e mes atual
        mes_ano_atual = datetime.now().strftime("%m%Y")
        #percorre todos os arquivos que estão na pasta 
        pasta = os.listdir(path_pasta)
        for arquivo in pasta:
            #seleciona apenas os arquivos excel
            if 'xlsx' in arquivo:
                #path == path do arquivo dentro da pasta 
                path = f"{path_pasta}\\{arquivo}"
                ti_m = os.path.getmtime(path) 
                m_ti = time.ctime(ti_m) 
                t_obj = time.strptime(m_ti) 
                #t_stamp == data da ultima alteracao do arquivo 
                T_stamp = time.strftime("%d%m%Y ", t_obj) 
                #caso a data da ultima alteracao for nao for igual ao mes que estamos remove o arquivo 
                if int(T_stamp[2:8]) != int(mes_ano_atual):
                    os.remove(path)
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


def bot_15():
    try:
        path_pasta = 'C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\pasta_teste'
        verificar_ultima_mod_e_apagar_arquivos_antigos(path_pasta)
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


if __name__ == '__main__':
    bot_15()