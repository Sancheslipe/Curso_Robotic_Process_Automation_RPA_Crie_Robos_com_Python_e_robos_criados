import requests
from requests.adapters import HTTPAdapter, Retry
import json
import sys


def retornar_dados_cnpj(CNPJ,UF):
    erro = None
    estados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
    try:
        #padroniza em minusculos
        UF = UF.upper()
        if str(UF) in estados:
            #info == Parametros necessários para fazer o post
            #problema no token
            info = {"token":"token aleatorio",
                    "timeout":600,
                    "uf":f"{UF}",
                    "cnpj":f"{CNPJ}"}       
            requisicao = requests.post("site de api",info)
            response_json = requisicao.json()
            data = response_json
            dict_data = data["data"]
            if  requisicao.ok:
                if data["code"] == 200:
                    new_data = dict_data[0]
#                     print(f"todos os dados. \n{data}\n")
                    
                    return new_data
                else:
                    print(f'o erro foi: {data["code"]}, \n')
                    print(f'MENSAGEM: {data["code_message"]}\n')
            else:
                erro = Exception
                print(f"o Erro foi:{erro}")
                print("\nELSE-01\n")
        else:
            print(f' digite um estado válido!')
            Exception
    except:
        exc_type, error, line = sys.exc_info()
        print(f"ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n")    
        # mandar email com o erro => nós 
if (__name__ == "__main__"):
    cnpj = input("digite aqui o cnpj da sua empresa: ")
    dado_2 = 'nada'
    #criar as variáveis que deseja utilizar
    # print(retornar_dados_cnpj(cnpj,dado_2))
    #para mostrar cada informacao em uma linha especifica use o código abaixo
    
    lista_mostrar = retornar_dados_cnpj(cnpj,dado_2)
    print(len(lista_mostrar))
    for l in range(0,len(lista_mostrar)):
        print(f'{lista_mostrar[l]}',end='\n')
    
    print("Programa Finalizado!")
