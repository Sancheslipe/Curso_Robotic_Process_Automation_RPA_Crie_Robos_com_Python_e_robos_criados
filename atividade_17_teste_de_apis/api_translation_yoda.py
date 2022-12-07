import requests
import sys

try:
    mensagem = input('digite uma mensagem que você deseja traduzir para a linguagem de nosso sublime mestre yoda!\n')
    mensagem = mensagem.replace(' ', '%20')
    requisicao = requests.get(f'https://api.funtranslations.com/translate/yoda.json?text={mensagem}.')
    if requisicao.ok:
        api = requisicao.json()
        print(api)
        mensagem_na_voz_de_yoda = api['contents']['translated']
        print(mensagem_na_voz_de_yoda)
    else:
        print(requisicao)
        print(requisicao.json()['error']['message'])

#{'error': {'code': 429, 'message': 'Too Many Requests: Rate limit of 5 requests per hour exceeded. Please wait for 56 minutes and 16 seconds.'}}

except:
    exc_type, error, line = sys.exc_info()
    print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')