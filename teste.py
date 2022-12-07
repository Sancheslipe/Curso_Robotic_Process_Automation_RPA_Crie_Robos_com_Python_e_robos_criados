# # import os
# # #lista os nomes das pastas existente(relacionadas ao meses do ano )
# # pastas = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
# # #recebe a lista dos arquivos na determinada pasta
# # lista_arq = os.listdir('C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\mover')
# # #para cada arquivo na pasta:
# # for arquivo in lista_arq:
# #     #se tiver txt no nome do arquivo:
# #     if 'txt' in arquivo:
# #         #se o arquivo do indice -6 até o -4 for relacionado a um mes do ano 
# #         if arquivo[-6:-4] in pastas:
# #             #destino recebe o numero referente á pasta 
# #             destino = arquivo[-6:-4]  
# #             #altera o arquivo de lugar 
# #             os.rename(f"C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\mover\\{arquivo}", f"C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\teste\\{destino}\\{arquivo}")
# # import pandas as pd
# # import sys
# # import os 

# # os.makedirs('C:\\Pastas Compartilhadas\\FCI\\06_FCI\\01_Hennings\\Robo')
# # print('pastas ciradas com sucesso')
# # codigo_empresa = []

# # planilha = pd.read_excel(f"C:\\Users\\Ana Paula\\Downloads\\listaempresas.xlsx", sheet_name='Select e070fil')
# # codigo = planilha['NUMCGC']
# # for empresa in range(len(codigo)):
# #     codigo_empresa.append(codigo[empresa])

# # print(codigo_empresa.index(83748772000567))

# # teste = '83748772000133'
# # print(teste[0:5])
# # print(teste[15:21])

# import os 
# import sys
# from pathlib import Path
# try:
#     # os.rename(f'.\\listaempresas.xlsx', 'D:\\atividade_10_organizar_arquivos')
#    file = Path(r'\listaempresas.xlsx')
#    os.rename(file,r'\atividade_10_organizar_arquivos')
# except:
#     exc_type, error, line = sys.exc_info()
#     print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')

import os 
import sys 
from datetime import datetime 

def limpar_pastas(path_pasta_final):
    #limpa a pasta de destino
    pasta_destino = os.listdir(path_pasta_final)
    for arquivo in pasta_destino:
        os.remove(f'{path_pasta_final}\\{arquivo}')
    #limpa a pasta de download
    data_padrao = datetime.now().strftime('%Y-%m-%d')
    pasta_download = os.listdir(os.path.expanduser("~")+'\\Downloads')
    path_pasta_download = os.path.expanduser("~")+'\\Downloads'
    for arquivo in pasta_download:
        if data_padrao in arquivo and '_Pedidos' in arquivo:
            # os.remove(f'{pasta_download}\\{arquivo}')
            os.remove(f'{path_pasta_download}\\{arquivo}')
try:
    limpar_pastas('C:\\Curso02_github\\atividade_16_heinigs\\proc')
except:
    exc_type, error, line = sys.exc_info()
    print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')