import pyautogui as p 
import pandas as pd 
import sys
import os

def abrir_arquivo():
    arquivo = pd.read_excel(f'C:\\Users\\Ana Paula\\Downloads\\alterar_tabela.xlsx')
    tamanho = len(arquivo)
    return tamanho, arquivo

def editar_arquivo(tamanho,arquivo):
    cont = 0
    while int(cont) < int(tamanho):
        nome_atividade = input('digite aqui o nome da atividade: ')
        valor_atividade = input(f'digite aqui o valor de {nome_atividade}: ')
        if valor_atividade.replace('.','', 1).isdigit():
            valor_atividade = float(valor_atividade)
            arquivo.loc[cont, 'nome'] = nome_atividade
            arquivo.loc[cont, 'valor'] = valor_atividade
            cont+=1
        else:
            cont = cont
            print('digite um valor válido! ')
    arquivo.to_excel(f'C:\\Users\\Ana Paula\\Downloads\\alterar_tabela.xlsx',index=False)
    print('arquivo finalizado com sucesso! ')

def bot_atividade_04():
    try:
        tamanho,arq = abrir_arquivo()
        editar_arquivo(tamanho,arq)
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


if (__name__ == '__main__'):
    os.system('cls')
    bot_atividade_04()
    print('Bot finalizado com sucesso Encerrado !')