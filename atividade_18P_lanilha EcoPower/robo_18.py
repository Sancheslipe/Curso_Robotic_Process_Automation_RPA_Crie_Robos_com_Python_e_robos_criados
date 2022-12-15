import os
import sys 
import pandas as pd

planilha = pd.read_excel(r'C:\Curso02_github\atividade_18P_lanilha EcoPower\proc\BASE ENGENHARIA.xlsm',sheet_name='LISTAS')
print(planilha)