import os 
import sys 
import requests
from datetime import datetime 


def pegar_cotacoes(codigo_moeda):
    try:
        requisicao = requests.get("http://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
        requisicao_dic = requisicao.json()
        cotacao = requisicao_dic[f'{codigo_moeda}BRL']['bid']
        return cotacao
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')
        print('Código de moeda inválido')
        return None

