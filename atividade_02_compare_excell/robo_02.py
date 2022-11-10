import pandas as pd
import numpy as np
import os
import sys

def abrir_arquivos_e_separar():
    #le o aquivo geral
    arquivo_principal_df = pd.read_excel(f'C:\\Curso02_github\\atividade_02_compare_excell\\base_de_dados\\Arquivo_Principal.xlsx')
    nomes_principal_df = arquivo_principal_df['nome']
    nomes_totais_df = []
    #caso a colunapossui nao exista ele cria e adiciona caracteres vázios
    if 'possui' not in arquivo_principal_df:
        arquivo_principal_df['possui'] = np.NaN

    #apende todos os arquivos em  so para fazer as comparacoes
    for x in range(1,11):
        nomes_df = pd.read_excel(f'C:\\Curso02_github\\atividade_02_compare_excell\\base_de_dados\\arquivo_{x}.xlsx')
        nomes_totais_df.append(nomes_df['nome'])
    print(f'a quantidade de linhas do arquivo principal é {len(nomes_principal_df)}\n')
    return nomes_principal_df,nomes_totais_df,arquivo_principal_df


def verifica_e_adiciona_no_arquivo(nomes_principal_df,nomes_totais_df,arquivo_principal_df):
    #conta quantos numeros estao em mais de um excell
    qtdsim = 0
    #verifica se um nome do excell geral aparece em algum excel alem dele, caso apareca o campo possui = 'Sim, caso nao apareca o campo possui = 'Não'
    for row in range(len(nomes_principal_df)):
        if str(nomes_principal_df[row]) in str(nomes_totais_df):
            qtdsim +=1
            arquivo_principal_df.loc[row, 'possui'] = 'Sim'
        else:
            arquivo_principal_df.loc[row, 'possui'] = 'Não'
    #printa a quantidade de nomes que aparecem mais de 1 vez
    print(f'a quantidade de nomes que está em mais de 1 planilha é {qtdsim}\n')
    #salva as alteracoes no arquivo geral
    arquivo_principal_df.to_excel(f'C:\\Curso02_github\\atividade_02_compare_excell\\base_de_dados\\Arquivo_Principal.xlsx',index=False)

  
def bot_atividade_002():
    try:
        nome1,total_nome,arquivo_geral = abrir_arquivos_e_separar()
        verifica_e_adiciona_no_arquivo(nome1,total_nome,arquivo_geral)
        #if success:
            #mandar email SUCESSO 
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')    
        # mandar email com o erro => nós 


if (__name__ == '__main__'):
    os.system('cls')
    bot_atividade_002()
    print('processo Encerrado !')


'''
Anotações e dicas de programas 
Luiz. 

#     # #baixa arquivo
#     # #se baixou:
#     # #editar
#     #     df.loc[row, 'possui'] = 'OK'
#     # #else:
#     #     df.loc[row, 'possui'] = 'NOK'

# if 'PROC' not in df.columns:
#     df['PROC'] = 'NOK
#     '



# print(os.listdir(r'C:\Curso02_github\atividade_02_compare_excell\base_de_dados'))

# excel_em_bs = [arq for arq in os.listdir(r'C:\Curso02_github\atividade_02_compare_excell\base_de_dados') if arq.endswith('xlsx')]
'''