import os
import sys 
import pandas as pd 

try:
    calc = 0
    planilha = pd.read_excel('C:\\Curso02_github\\atividade_12_calculo_almoço\\arquivo_teste.xlsx',sheet_name='Sheet1')
    teste = planilha['VALOR']
    for l in range(len(teste)):
        print(teste[l])
    
    print(calc)
except:
    exc_type, error, line = sys.exc_info()
    print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')