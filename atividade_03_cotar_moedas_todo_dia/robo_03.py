import requests
from datetime import datetime
import sys
import os
def cotacao_dolar_euro_bitcoin():
    requisicao = requests.get("http://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()
    cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
    cotacao_euro = requisicao_dic["EURBRL"]["bid"]
    cotacao_btc = requisicao_dic["BTCBRL"]["bid"]
    print(f'Cotação Atualizada. {datetime.now()}\nDólar: R${cotacao_dolar}\nEuro: R${cotacao_euro}\nBTC: R${cotacao_btc}')
    return cotacao_dolar,cotacao_euro,cotacao_btc

def bot_atividade_003():
    try:
       cotacao_dolar_euro_bitcoin()
        #if success:
            #mandar email SUCESSO 
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')    
        # mandar email com o erro => nós 


if (__name__ == '__main__'):
    os.system('cls')
    bot_atividade_003()
    print('\nprocesso Encerrado !\no')
    