import requests
import sys

try:
    requisicao = requests.get('https://api.adviceslip.com/advice')
    api = requisicao.json()
    conselho = api['slip']['advice']
    print(conselho)
except:
    exc_type, error, line = sys.exc_info()
    print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')