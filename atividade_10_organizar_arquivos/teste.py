# import os
# #lista os nomes das pastas existente(relacionadas ao meses do ano )
# pastas = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
# #recebe a lista dos arquivos na determinada pasta
# lista_arq = os.listdir('C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\mover')
# #para cada arquivo na pasta:
# for arquivo in lista_arq:
#     #se tiver txt no nome do arquivo:
#     if 'txt' in arquivo:
#         #se o arquivo do indice -6 até o -4 for relacionado a um mes do ano 
#         if arquivo[-6:-4] in pastas:
#             #destino recebe o numero referente á pasta 
#             destino = arquivo[-6:-4]  
#             #altera o arquivo de lugar 
#             os.rename(f"C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\mover\\{arquivo}", f"C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\teste\\{destino}\\{arquivo}")
import pandas as pd
import sys
# codigo_empresa = []

# planilha = pd.read_excel(f"C:\\Users\\Ana Paula\\Downloads\\listaempresas.xlsx", sheet_name='Select e070fil')
# codigo = planilha['NUMCGC']
# for empresa in range(len(codigo)):
#     codigo_empresa.append(codigo[empresa])

# print(codigo_empresa.index(83748772000567))

teste = '83748772000567_20221124_094008'
print(teste[0:15])
print(teste[15:21])