import requests
from requests.adapters import HTTPAdapter, Retry
import json
import sys
campos = [
          "code","code_message","header","api_version","service","parameters","ie","client_name","token_name",
          "billable","price","requested_at","elapsed_time_in_milliseconds","remote_ip","signature", "data_count","abertura_data",
          "atividade_economica","atividade_economica_secundaria","atividade_economica_secundaria_lista","cnpj","consulta_datahora",
          "cte_situacao","efd_perfil","efd_situacao", "email","endereco_bairro","endereco_cep","endereco_complemento","endereco_logradouro",
          "endereco_municipio","endereco_numero","endereco_uf","inscricao_estadual","nfe_situacao","produtor_rural","razao_social","situacao_atual",
          "situacao_cadastral","situacao_cadastral_completa","situacao_cadastral_data","telefone","site_receipt"
          ]



#variaveis
# code,code_message,header,api_version,service,parameters,ie,client_name,token_name,
# billable,price,requested_at,elapsed_time_in_milliseconds,remote_ip,signature, data_count,data,abertura_data,
# atividade_economica,atividade_economica_secundaria,atividade_economica_secundaria_lista,cnpj,consulta_datahora,
# cte_situacao,efd_perfil,efd_situacao, email,endereco_bairro,endereco_cep,endereco_complemento,endereco_logradouro,
# endereco_municipio,endereco_numero,endereco_uf,inscricao_estadual,nfe_situacao,produtor_rural,razao_social,situacao_atual,
# situacao_cadastral,situacao_cadastral_completa,situacao_cadastral_data,telefone,site_receipt

def retornar_dados_cnpj(CNPJ,UF):
    erro = None
    try:
        #padroniza em minusculos
        UF = UF.lower()
        if str(UF) == 'pr':
            #info == Parametros necessários para fazer o post
            info = str({"cnpj":f"{CNPJ}","token": "Iy1JPISuS4azpg-i5nM1vpYv0_IjZYPeLQZY1MKB"})
            requisicao = requests.get('https://api.infosimples.com/api/v2/consultas/sintegra/pr',data=info)
            if requisicao == 200:
                dic_requisicao = requisicao.json()
                print('Requisição Retrnou 200')
                #adicionando a cada variavel o seu respectivo campo
                code = dic_requisicao.json[campos[0]]
                code_message = dic_requisicao.json[campos[1]]
                header = dic_requisicao.json[campos[2]]
                api_version = dic_requisicao.json[campos[3]]
                service = dic_requisicao.json[campos[4]]
                parameters = dic_requisicao.json[campos[5]]
                ie = dic_requisicao.json[campos[6]]
                client_name  = dic_requisicao.json[campos[7]]
                token_name = dic_requisicao.json[campos[8]]
                billable = dic_requisicao.json[campos[9]]
                price = dic_requisicao.json[campos[10]]
                requested_at = dic_requisicao.json[campos[11]]
                elapsed_time_in_milliseconds = dic_requisicao.json[campos[12]]
                remote_ip = dic_requisicao.json[campos[13]]
                signature = dic_requisicao.json[campos[14]]
                data_count = dic_requisicao.json[campos[15]]
                abertura_data = dic_requisicao.json[campos[16]]
                atividade_economica = dic_requisicao.json[campos[17]]
                atividade_economica_secundaria = dic_requisicao.json[campos[18]]
                atividade_economica_secundaria_lista = dic_requisicao.json[campos[19]]
                cnpj = dic_requisicao.json[campos[20]]
                consulta_datahora = dic_requisicao.json[campos[21]]
                cte_situacao = dic_requisicao.json[campos[22]]
                efd_perfil = dic_requisicao.json[campos[23]]
                efd_situacao = dic_requisicao.json[campos[24]]
                email = dic_requisicao.json[campos[25]]
                endereco_bairro = dic_requisicao.json[campos[26]]
                endereco_cep = dic_requisicao.json[campos[27]]
                endereco_complemento = dic_requisicao.json[campos[28]]
                endereco_logradouro = dic_requisicao.json[campos[29]]
                endereco_municipio = dic_requisicao.json[campos[30]]
                endereco_numero = dic_requisicao.json[campos[31]]
                endereco_uf = dic_requisicao.json[campos[32]]
                inscricao_estadual = dic_requisicao.json[campos[33]]
                nfe_situacao = dic_requisicao.json[campos[34]]
                produtor_rural = dic_requisicao.json[campos[35]]
                razao_social = dic_requisicao.json[campos[36]]
                situacao_atual = dic_requisicao.json[campos[37]]
                situacao_cadastral = dic_requisicao.json[campos[38]]
                situacao_cadastral_completa = dic_requisicao.json[campos[39]]
                situacao_cadastral_data = dic_requisicao.json[campos[40]]
                telefone = dic_requisicao.json[campos[41]]
                site_receipt = dic_requisicao.json[campos[42]]


                return code, code_message, header, api_version, service, parameters, ie, client_name, token_name, billable, price, requested_at, elapsed_time_in_milliseconds, remote_ip, signature, data_count, abertura_data, atividade_economica, atividade_economica_secundaria, atividade_economica_secundaria_lista, cnpj, consulta_datahora, cte_situacao, efd_perfil, efd_situacao, email, endereco_bairro, endereco_cep, endereco_complemento, endereco_logradouro, endereco_municipio, endereco_numero, endereco_uf, inscricao_estadual, nfe_situacao, produtor_rural, razao_social, situacao_atual, situacao_cadastral, situacao_cadastral_completa, situacao_cadastral_data, telefone, site_receipt
            else:
                erro = Exception
                print(f'o Erro foi:{erro}')
                print('PASSOU1')


        if str(UF) == 'sc':
            info = str({"cnpj":f"{CNPJ}","uf":f"{UF}","token": "Iy1JPISuS4azpg-i5nM1vpYv0_IjZYPeLQZY1MKB"})
            requisicao = requests.get('https://api.infosimples.com/api/v2/consultas/sintegra/sc',data=info)
            #caso retorne 200 == Deu certo, caso dê um numero diferente significa que Houve algum problema
            if str(requisicao) == '<response[200]>':
                dic_requisicao = requisicao.json()
                print('Requisição Retrnou 200')
                #adicionando a cada variavel o seu respectivo campo
                code = dic_requisicao.json[campos[0]]
                code_message = dic_requisicao.json[campos[1]]
                header = dic_requisicao.json[campos[2]]
                api_version = dic_requisicao.json[campos[3]]
                service = dic_requisicao.json[campos[4]]
                parameters = dic_requisicao.json[campos[5]]
                ie = dic_requisicao.json[campos[6]]
                client_name  = dic_requisicao.json[campos[7]]
                token_name = dic_requisicao.json[campos[8]]
                billable = dic_requisicao.json[campos[9]]
                price = dic_requisicao.json[campos[10]]
                requested_at = dic_requisicao.json[campos[11]]
                elapsed_time_in_milliseconds = dic_requisicao.json[campos[12]]
                remote_ip = dic_requisicao.json[campos[13]]
                signature = dic_requisicao.json[campos[14]]
                data_count = dic_requisicao.json[campos[15]]
                abertura_data = dic_requisicao.json[campos[16]]
                atividade_economica = dic_requisicao.json[campos[17]]
                atividade_economica_secundaria = dic_requisicao.json[campos[18]]
                atividade_economica_secundaria_lista = dic_requisicao.json[campos[19]]
                cnpj = dic_requisicao.json[campos[20]]
                consulta_datahora = dic_requisicao.json[campos[21]]
                cte_situacao = dic_requisicao.json[campos[22]]
                efd_perfil = dic_requisicao.json[campos[23]]
                efd_situacao = dic_requisicao.json[campos[24]]
                email = dic_requisicao.json[campos[25]]
                endereco_bairro = dic_requisicao.json[campos[26]]
                endereco_cep = dic_requisicao.json[campos[27]]
                endereco_complemento = dic_requisicao.json[campos[28]]
                endereco_logradouro = dic_requisicao.json[campos[29]]
                endereco_municipio = dic_requisicao.json[campos[30]]
                endereco_numero = dic_requisicao.json[campos[31]]
                endereco_uf = dic_requisicao.json[campos[32]]
                inscricao_estadual = dic_requisicao.json[campos[33]]
                nfe_situacao = dic_requisicao.json[campos[34]]
                produtor_rural = dic_requisicao.json[campos[35]]
                razao_social = dic_requisicao.json[campos[36]]
                situacao_atual = dic_requisicao.json[campos[37]]
                situacao_cadastral = dic_requisicao.json[campos[38]]
                situacao_cadastral_completa = dic_requisicao.json[campos[39]]
                situacao_cadastral_data = dic_requisicao.json[campos[40]]
                telefone = dic_requisicao.json[campos[41]]
                site_receipt = dic_requisicao.json[campos[42]]
                
                return code, code_message, header, api_version, service, parameters, ie, client_name, token_name, billable, price, requested_at, elapsed_time_in_milliseconds, remote_ip, signature, data_count, abertura_data, atividade_economica, atividade_economica_secundaria, atividade_economica_secundaria_lista, cnpj, consulta_datahora, cte_situacao, efd_perfil, efd_situacao, email, endereco_bairro, endereco_cep, endereco_complemento, endereco_logradouro, endereco_municipio, endereco_numero, endereco_uf, inscricao_estadual, nfe_situacao, produtor_rural, razao_social, situacao_atual, situacao_cadastral, situacao_cadastral_completa, situacao_cadastral_data, telefone, site_receipt
            else:
                erro = Exception
                print(f'o Erro foi:{erro}')
                print('PASSOU2')
            


    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')    
        # mandar email com o erro => nós 

    # except Exception as e :
    #     if erro != None:
    #         print(f' {erro}')
    #     print('PROGRAMA PARADO:')
    #     print(f' Erro {e}')
        

if (__name__ == '__main__'):
    cnpj = input('digite aqui o cnpj da sua empresa: ')
    uf = input('digite aqui a sigla de sua unidade federal: ')
    
    dados = retornar_dados_cnpj(cnpj,uf)
    if dados != None:
        print(f'este são os dados:{dados}')

    print('Programa Finalizado!')