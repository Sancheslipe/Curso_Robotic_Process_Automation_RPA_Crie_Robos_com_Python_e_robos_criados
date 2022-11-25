import pandas as pd
import os 
import sys


def criar_pastas_e_sub_pastas(path):
    #cria uma pasta 2022 para cada franquia
    for x in range(1,31):      
        
        #caso seja menor que 10 adiciona um 0 ao inicio do arquivo               
        if x < 10:
            #cria o diretório da franquia
            os.mkdir(f'{path}\\0{x}')
            os.mkdir(f'{path}\\0{x}\\2022')
            os.mkdir(f'{path}\\0{x}\\2021')
            #cria 1 pasta referente ao mes
            for l in range(1,13):
                if l <10:
                    os.mkdir(f'{path}\\0{x}\\2022\\20220{l}')
                    os.mkdir(f'{path}\\0{x}\\2021\\20210{l}')
                else:
                    os.mkdir(f'{path}\\0{x}\\2022\\2022{l}')
                    os.mkdir(f'{path}\\0{x}\\2021\\2021{l}')
        else:
            os.mkdir(f'{path}\\{x}')
            os.mkdir(f'{path}\\{x}\\2022')
            os.mkdir(f'{path}\\{x}\\2021')
            for l in range(1,13):
                if l <10:
                    os.mkdir(f'{path}\\{x}\\2022\\20220{l}')
                    os.mkdir(f'{path}\\{x}\\2021\\20210{l}')
                else:
                    os.mkdir(f'{path}\\{x}\\2022\\2022{l}')
                    os.mkdir(f'{path}\\{x}\\2021\\2021{l}')

    print('Pastas criadas com Sucesso')


def organizar_arquivos_nas_pastas_nome(path_pasta_inicial,path_pastas_org):
    # print('entrou')
    try:
        #recebe todos os arquivos presentes na pasta
        lista_arquivos = os.listdir(path_pasta_inicial)
        #varre todos os arquivos
        for arquivo in lista_arquivos:
            #verifica se é um arquivo txt
            if ('txt' in arquivo) and (arquivo[0] == 'E'):
                #retira todos os caracteres de texto para poder validar a franquia
                franq = arquivo[0:6].replace('_','').replace('ENV','')
                franq = int(franq)
                #data == ano concatenado com o mes
                if arquivo[6:12].isdigit():
                    data = arquivo[6:12]
                else:
                    data = arquivo[6:13].replace('_','')
                if franq in range(1,31):
                    if franq < 10:
                        for l in range(1,13):
                            if l<10:
                                if (data == f'20220{l}'):
                                    #altera a pasta
                                    os.rename(f'{path_pasta_inicial}\\{arquivo}',f'{path_pastas_org}\\0{franq}\\2022\\20220{l}\\{arquivo}')
                                elif (data == f'20210{l}'):
                                    #altera a pasta
                                    os.rename(f'{path_pasta_inicial}\\{arquivo}',f'{path_pastas_org}\\0{franq}\\2021\\20210{l}\\{arquivo}')
                            else:
                                if (data == f'2022{l}'):
                                    #altera a pasta
                                    os.rename(f'{path_pasta_inicial}\\{arquivo}',f'{path_pastas_org}\\0{franq}\\2022\\2022{l}\\{arquivo}')
                                elif (data == f'2021{l}'):
                                    #altera a pasta
                                    os.rename(f'{path_pasta_inicial}\\{arquivo}',f'{path_pastas_org}\\0{franq}\\2021\\2021{l}\\{arquivo}')
                    else:
                        #adiciona dentro da pasta da franquia relacionado ao mês
                        for l in range(1,13):
                            if l < 10:
                                if (data == f'20220{l}'):
                                    #altera a pasta
                                    os.rename(f'{path_pasta_inicial}\\{arquivo}',f'{path_pastas_org}\\{franq}\\2022\\20220{l}\\{arquivo}')
                                elif (data == f'20210{l}'):
                                    #altera a pasta
                                    os.rename(f'{path_pasta_inicial}\\{arquivo}',f'{path_pastas_org}\\{franq}\\2021\\20210{l}\\{arquivo}')
                            else:
                                if (data == f'2022{l}'):
                                    #altera a pasta
                                    os.rename(f'{path_pasta_inicial}\\{arquivo}', f'{path_pastas_org}\\{franq}\\2022\\2022{l}\\{arquivo}')
                                elif (data == f'2021{l}'):
                                    #altera a pasta
                                    os.rename(f'{path_pasta_inicial}\\{arquivo}', f'{path_pastas_org}\\{franq}\\2021\\2021{l}\\{arquivo}')
    except:
        #printa o erro caso dê erro
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')
        print(path_pasta_inicial)
        print(data)
        


def organizar_arquivos_nas_pastas_codigo(path_pasta,path_pastas_org):
    codigo_empresa = []
    try:
        #lê a planilha e retorna um array que o index de cada elemento é equivalente ao codigo da franquia
        planilha = pd.read_excel(f"C:\\Users\\Ana Paula\\Downloads\\listaempresas.xlsx", sheet_name='Select e070fil')
        codigo = planilha['NUMCGC']
        for empresa in range(len(codigo)):
            codigo_empresa.append(int(codigo[empresa]))
        #recebe todos os arquivos presentes na pasta
        lista_arquivos = os.listdir(str(path_pasta))
        #varre todos os arquivos
        for arquivo in lista_arquivos:
            #verifica se é um arquivo txt
            if ('txt' in arquivo) and (arquivo[0:5] == '83748') :
                # #retira todos os caracteres de texto para poder validar a franquia
                franq = int(arquivo[0:14])
                index = codigo_empresa.index(franq)
                franq = index + 1
                #data eh ano concatenado com o mes
                if arquivo[15:21].isdigit():
                    data = arquivo[15:21]  
                if franq in range(1,31):
                    if franq < 10:
                        #altera a pasta
                        for l in range(1,13):
                            if l<10:
                                if (data == f'20220{l}'):
                                    os.rename(f'{path_pasta}\\{arquivo}',f'{path_pastas_org}\\0{franq}\\2022\\20220{l}\\{arquivo}')
                                elif (data == f'20210{l}'):
                                    os.rename(f'{path_pasta}\\{arquivo}',f'{path_pastas_org}\\0{franq}\\2021\\20210{l}\\{arquivo}')
                            else:
                                if (data == f'2022{l}'):
                                    os.rename(f'{path_pasta}\\{arquivo}',f'{path_pastas_org}\\0{franq}\\2022\\2022{l}\\{arquivo}')
                                elif (data == f'2021{l}'):
                                    os.rename(f'{path_pasta}\\{arquivo}',f'{path_pastas_org}\\0{franq}\\2021\\2021{l}\\{arquivo}')
                    # o numero referenta a franquia eh maior do que 10 (questão de organizacao do arquivo)
                    else:
                        #adiciona dentro da pasta da franquia relacionado ao mês
                        for l in range(1,13):
                            if l < 10:
                                    #altera a pasta
                                if (data == f'20220{l}'):
                                    os.rename(f'{path_pasta}\\{arquivo}',f'{path_pastas_org}\\{franq}\\2022\\20220{l}\\{arquivo}')
                                elif (data == f'20210{l}'):
                                    os.rename(f'{path_pasta}\\{arquivo}',f'{path_pastas_org}\\{franq}\\2021\\20210{l}\\{arquivo}')
                            else:
                                if (data == f'2022{l}'):
                                    os.rename(f'{path_pasta}\\{arquivo}', f'{path_pastas_org}\\{franq}\\2022\\2022{l}\\{arquivo}')
                                elif (data == f'2021{l}'):
                                    os.rename(f'{path_pasta}\\{arquivo}', f'{path_pastas_org}\\{franq}\\2021\\2021{l}\\{arquivo}')
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')
        print(path_pasta)
        print(arquivo)


def bot_10():
    path_criar_pastas = 'C:\\Pastas Compartilhadas\\FCI\\06_FCI\\01_Hennings\\Robo\\Robo'
    criar_pastas_e_sub_pastas(path_criar_pastas)
    path1 = 'C:\\Pastas Compartilhadas\\FCI\\06_FCI\\01_Hennings\\Robo\\Robo'
    organizar_arquivos_nas_pastas_nome(path1,path_criar_pastas)
    print('organizou pasta 1')
    path2 = 'C:\\Pastas Compartilhadas\\FCI\\06_FCI\\01_Hennings\\Robo\\Robo\\Old'
    organizar_arquivos_nas_pastas_nome(path2,path_criar_pastas)
    print('organizou pasta 2 ')
    path3 = 'C:\\Pastas Compartilhadas\\FCI\\06_FCI\\01_Hennings\\Robo\\Robo\\Retorno'
    organizar_arquivos_nas_pastas_codigo(path3,path_criar_pastas)
    print('organizou pasta 3 ')
    path4 = 'C:\\Pastas Compartilhadas\\FCI\\06_FCI\\01_Hennings\\Robo\\Robo\\Retorno\\Processado\\Arquivos'
    organizar_arquivos_nas_pastas_codigo(path4,path_criar_pastas)
    print('organizou pasta 4 ')
    path5 = 'C:\\Pastas Compartilhadas\\FCI\\06_FCI\\01_Hennings\\Robo\\Robo\\Retorno\\Processado\\2022'
    organizar_arquivos_nas_pastas_codigo(path5,path_criar_pastas)
    print('organizou pasta 5 ')


if (__name__ == '__main__'):
    bot_10()
    print('Pastas organizadas com sucesso!')