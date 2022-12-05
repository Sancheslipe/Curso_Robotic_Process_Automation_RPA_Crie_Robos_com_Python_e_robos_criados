import os 
import sys 
import pandas as pd
from datetime import datetime


def criar_corpo_planilha():
    try:
        planilha = pd.read_excel('C:\\Curso02_github\\atividade_12_calculo_almoço\\arquivo_teste.xlsx',sheet_name='Sheet1')
        planilha.loc['1','DIA'] = f'{30}/11'
        for l in range(1,32):
            #usar este código quando for o mês 12
            # mes = datetime.now().date().month
            planilha.loc[f'{l+1}','DIA'] = f'{l}/12'
        planilha.loc[f'{1}','COMIDA'] = ''
        planilha.loc[f'{1}','VALOR'] =''
        planilha.loc[f'{1}','TOTAL'] = "=SOMA(C2:C33)"
        planilha.to_excel('C:\\Curso02_github\\atividade_12_calculo_almoço\\arquivo_teste.xlsx',index=False)
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


def adicionar_dados_na_planilha(comida,valor):
    try:
        valor = str(valor)
        planilha = pd.read_excel('C:\\Curso02_github\\atividade_12_calculo_almoço\\arquivo_teste.xlsx',sheet_name='Sheet1')
        dia = datetime.now().day
        mes = datetime.now().month
        dia_mes = f'{dia}/{mes}'
        planilha.loc[planilha['DIA'] == f'{dia_mes}','COMIDA'] = comida
        planilha.loc[planilha['DIA'] == f'{dia_mes}','VALOR'] = float(valor)
        planilha.to_excel('C:\\Curso02_github\\atividade_12_calculo_almoço\\arquivo_teste.xlsx',index=False)
        

    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


def bot_12():
    try:
        print('robô iniciado!')
        cont = 0
        # criar_corpo_planilha()
        comida = input('Digite aqui o que você comeu hoje no seu almoço: ')
        
        while cont <1:
            valor = input('digite aqui quanto isso custou: ')
            if valor.replace('.','',1).isdigit():
                valor = float(valor)
                cont += 1
            else:
                print('digite um numero válido!')
                cont = cont
        adicionar_dados_na_planilha(comida,valor)
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


if __name__ == '__main__':
    os.system('cls')
    bot_12()
    print('robô finalizou')