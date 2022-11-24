import pandas as pd
import os 
import sys
from time import sleep


def criar_pastas_e_sub_pastas():
    for x in range(1,31):                     
        if x < 10:
            os.mkdir(f'C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\robo\\Robo\\0{x}')
            for l in range(1,13):
                if l <10:
                    os.mkdir(f'C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\robo\\Robo\\0{x}\\20220{l}')
                else:
                    os.mkdir(f'C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\robo\\Robo\\0{x}\\2022{l}')
        else:
            os.mkdir(f'C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\robo\\Robo\\{x}')
            for l in range(1,13):
                if l <10:
                    os.mkdir(f'C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\robo\\Robo\\{x}\\20220{l}')
                else:
                    os.mkdir(f'C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\robo\\Robo\\{x}\\2022{l}')
    print('Pastas criadas com Sucesso')


def organizar_arquivos_nas_pastas_nome(path_pasta_inicial):
    # print('entrou')
    try:
        #recebe todos os arquivos presentes na pasta
        lista_arquivos = os.listdir(str(path_pasta_inicial))
        #varre todos os arquivos
        for arquivo in lista_arquivos:
            #verifica se é um arquivo txt
            if ('txt' in arquivo) and (arquivo[0] == 'E'):
                # print('3')
                #retira todos os caracteres de texto para poder validar a franquia
                franq = arquivo[0:6].replace('_','').replace('ENV','')
                franq = int(franq)
                #data == ano concatenado com o mes
                if arquivo[6:12].isdigit():
                    # print('4')
                    data = arquivo[6:12]
                else:
                    data = arquivo[6:13].replace('_','')
                    # data = int(data)
                    
                if franq in range(1,31):
                
                    if franq < 10:
                        
                        for l in range(1,13):
                            # print('8')
                            if l<10:
                                # print('9')
                                # print(data)
                                # print(type(data))
                                # print(arquivo)
                                # input()
                                if (data == f'20220{l}') or (data == f'20210{l}'):
                                    # print('10')
                                    os.rename(f'{path_pasta_inicial}\\{arquivo}',f'C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\robo\\Robo\\0{franq}\\20220{l}\\{arquivo}')
                            else:
                                # print('11')
                                # print(data)
                                # print(type(data))
                                # print(arquivo)
                                # input()
                                if (data == f'2022{l}') or (data == f'2021{l}'):
                                    # print('12')
                                    os.rename(f'{path_pasta_inicial}\\{arquivo}',f'C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\robo\\Robo\\0{franq}\\2022{l}\\{arquivo}')
                    else:
                        
                        # print('13')
                        for l in range(1,13):
                            # print('14')
                            if l < 10:
                                # print('16')
                                # print(data)
                                # print(type(data))
                                # print(arquivo)
                                # input()
                                if (data == f'20220{l}') or (data == f'20210{l}'):
                                    # print('11')
                                    os.rename(f'{path_pasta_inicial}\\{arquivo}',f'C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\robo\\Robo\\{franq}\\20220{l}\\{arquivo}')
                            else:
                                # print(data)
                                # print(type(data))
                                # print(arquivo)
                                # input()
                                # print('17')
                                if (data == f'2022{l}') or (data == f'2021{l}'):
                                    # print('18')
                                    os.rename(f'{path_pasta_inicial}\\{arquivo}',f'C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\robo\\Robo\\{franq}\\2022{l}\\{arquivo}')
    except:
        exc_type, error, line = sys.exc_info()
        print(f'\n{arquivo}\n')
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


def organizar_arquivos_nas_pastas_codigo(path_pasta):
    codigo_empresa = []
    try:
        planilha = pd.read_excel(f"C:\\Users\\Ana Paula\\Downloads\\listaempresas.xlsx", sheet_name='Select e070fil')
        codigo = planilha['NUMCGC']
        for empresa in range(len(codigo)):
            codigo_empresa.append(int(codigo[empresa]))
        #recebe todos os arquivos presentes na pasta
        lista_arquivos = os.listdir(str(path_pasta))
        #varre todos os arquivos
        for arquivo in lista_arquivos:
            
            #verifica se é um arquivo txt
            if ('txt' in arquivo):
                # print('3')
                #retira todos os caracteres de texto para poder validar a franquia
                
                franq = int(arquivo[0:14])
                index = codigo_empresa.index(franq)
                franq = index + 1
                #data == ano concatenado com o mes
                if arquivo[15:21].isdigit():
                    # print('4')
                    data = arquivo[15:21]  
                if franq in range(1,31):
                
                    if franq < 10:
                        
                        for l in range(1,13):
                            # print('8')
                            if l<10:
                                # print('9')
                                # print(data)
                                # print(type(data))
                                # print(arquivo)
                                # input()
                                if (data == f'20220{l}') or (data == f'20210{l}'):
                                    # print('10')
                                    os.rename(f'{path_pasta}\\{arquivo}',f'C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\robo\\Robo\\0{franq}\\20220{l}\\{arquivo}')
                            else:
                                # print('11')
                                # print(data)
                                # print(type(data))
                                # print(arquivo)
                                # input()
                                if (data == f'2022{l}') or (data == f'2021{l}'):
                                    # print('12')
                                    os.rename(f'{path_pasta}\\{arquivo}',f'C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\robo\\Robo\\0{franq}\\2022{l}\\{arquivo}')
                    else:
                        
                        # print('13')
                        for l in range(1,13):
                            # print('14')
                            if l < 10:
                                # print('16')
                                # print(data)
                                # print(type(data))
                                # print(arquivo)
                                # input()
                                if (data == f'20220{l}') or (data == f'20210{l}'):
                                    # print('11')
                                    os.rename(f'{path_pasta}\\{arquivo}',f'C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\robo\\Robo\\{franq}\\20220{l}\\{arquivo}')
                            else:
                                # print(data)
                                # print(type(data))
                                # print(arquivo)
                                # input()
                                # print('17')
                                if (data == f'2022{l}') or (data == f'2021{l}'):
                                    # print('18')
                                    os.rename(f'{path_pasta}\\{arquivo}',f'C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\robo\\Robo\\{franq}\\2022{l}\\{arquivo}')
        
        
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


def bot_10():
    #organiza pasta 1
    path1 = 'C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\robo\\Robo'
    organizar_arquivos_nas_pastas_nome(path1)
    print('organizou pasta 1 ')
    path2 = 'C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\robo\\Robo\\Old'
    organizar_arquivos_nas_pastas_nome(path2)
    print('organizou pasta 1 ')
    path3 = 'C:\\Users\\Ana Paula\\OneDrive\\Área de Trabalho\\robo\\Robo\\Retorno'
    organizar_arquivos_nas_pastas_codigo(path3)

if (__name__ == '__main__'):
    bot_10()
    print('Pastas organizadas com sucesso!')