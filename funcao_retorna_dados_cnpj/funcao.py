import requests
from requests.adapters import HTTPAdapter, Retry
import json
import sys

lista_mostrar = []

def retornar_dados_cnpj(CNPJ,UF):
    erro = None
    estados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
    try:
        #padroniza em minusculos
        UF = UF.upper()
        if str(UF) in estados:
            #info == Parametros necessários para fazer o post
            #problema no token
            info = {"token":"Iy1JPISuS4azpg-i5nM1vpYv0_IjZYPeLQZY1MKB",
                    "timeout":600,
                    "uf":f"{UF}",
                    "cnpj":f"{CNPJ}"}       
            requisicao = requests.post("https://api.infosimples.com/api/v2/consultas/sintegra/unificada",info)
            response_json = requisicao.json()
            data = response_json
            dict_data = data["data"]
            if  requisicao.ok:
                if data["code"] == 200:
                    new_data = dict_data[0]
                    # print(f"todos os dados. \n{data}\n")
                    abertura_data = new_data["abertura_data"]
                    atividade_economica = new_data["atividade_economica"]
                    atividade_economica_secundaria = new_data["atividade_economica_secundaria"]
                    cnpj = new_data["cnpj"]
                    cnpj_cpf = new_data["cnpj_cpf"]
                    consulta_data = new_data["consulta_data"]                
                    consulta_datahora = new_data["consulta_datahora"]
                    cpf = new_data["cpf"]
                    email = new_data["email"]
                    endereco_bairro = new_data["endereco_bairro"]
                    endereco_cep = new_data["endereco_cep"]
                    endereco_complemento = new_data["endereco_complemento"]
                    endereco_logradouro = new_data["endereco_logradouro"]
                    endereco_municipio = new_data["endereco_municipio"]
                    endereco_numero = new_data["endereco_numero"]
                    endereco_uf = new_data["endereco_uf"]
                    inscricao_estadual = new_data["inscricao_estadual"]
                    nome_fantasia = new_data["nome_fantasia"]
                    razao_social = new_data["razao_social"]
                    regime_apuracao = new_data["regime_apuracao"]
                    situacao_cadastral = new_data["situacao_cadastral"]
                    situacao_cadastral_data = new_data["situacao_cadastral_data"]
                    telefone = new_data["telefone"]
                    site_receipt = new_data["site_receipt"]
                    return abertura_data,atividade_economica,atividade_economica_secundaria,cnpj,cnpj_cpf,consulta_data,consulta_datahora,cpf,email,endereco_bairro, endereco_cep,endereco_complemento,endereco_logradouro,endereco_municipio,endereco_numero,endereco_uf,inscricao_estadual,nome_fantasia,razao_social,regime_apuracao,situacao_cadastral,situacao_cadastral_data,telefone,site_receipt
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
    uf = input("digite aqui a sigla de sua unidade federal: ")
    #criar as variáveis que deseja utilizar
    print(retornar_dados_cnpj(cnpj,uf))
    #para mostrar cada informacao em uma linha especifica use o código abaixo
    '''
    lista_mostrar = []
    lista_mostrar = retornar_dados_cnpj(cnpj,uf)
    for l in range(0,len(lista_mostrar)):
        print(f'{lista_mostrar[l]}',end='\n')
    '''
    print("Programa Finalizado!")