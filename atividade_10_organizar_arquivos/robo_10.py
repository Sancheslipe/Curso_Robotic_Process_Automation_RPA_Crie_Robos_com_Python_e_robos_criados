import pandas as pd
import os 
import sys 


def criar_pastas_franquia(path_criar_pasta):
    try:
        #cria uma pasta para cada franquia
        for x in range(1,32):
            franq = str(x)
            #caso o numero da franquia seja menor que 10 adiciona "0" ao inicio do numero 
            if int(franq) < 10:
                franq = '0'+franq 
            #caso a pasta não exista ele cria 
            if (not os.path.exists(f'{path_criar_pasta}\\{franq}')):  
                os.mkdir(f'{path_criar_pasta}\\{franq}')
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')

def ler_arquivos_e_adicionar_na_pasta(path_inicial):
    try:
        #é o path de onde as pastas serão criadas
        path_criar_pasta = 'C:\\Pastas Compartilhadas\\FCI\\06_FCI\\01_Hennings\\Robo\\Robo'        
        lista_arquivo = os.listdir(path_inicial)
        for arquivo in lista_arquivo:
            if ('txt' in arquivo) and (arquivo[0] == 'E'):
                #validando a franquia
                franq = arquivo[0:6].replace('_','').replace('ENV','')
                franq = str(franq)
                if int(franq) < 10:
                    franq = '0'+franq
                #validando o ano
                if arquivo[6:10].isdigit():
                    ano = arquivo[6:10]
                else:
                    ano = arquivo[6:11].replace('_','')
                #caso não exista a pasta do ano criada, ele cria a pasta
                if (not os.path.exists(f'{path_criar_pasta}\\{franq}\\{ano}')):  
                    os.mkdir(f'{path_criar_pasta}\\{franq}\\{ano}')
                #validando data padrao {anomes}
                if arquivo[6:12].isdigit():
                    data = arquivo[6:12]
                else:
                    data = arquivo[6:13].replace('_','')
                #caso a pasta de data padrão não estar criada dentro da pasta do mês ele cria 
                if (not os.path.exists(f'{path_criar_pasta}\\{franq}\\{ano}\\{data}')):  
                    os.mkdir(f'{path_criar_pasta}\\{franq}\\{ano}\\{data}')
                # move o arquivo para sua respectiva pasta
                os.rename(f'{path_inicial}\\{arquivo}',f'{path_criar_pasta}\\{franq}\\{ano}\\{data}\\{arquivo}')
            elif ('txt' in arquivo) and (arquivo[0:5] == '83748'):
                #problema em alterar o local do arquivo xlsx para onde o robô (.py) está
                #os.rename(f'.\\listaempresas.xlsx',f'D:\\atividade_10_organizar_arquivos')
                #codigo empresa == array que guarda os códigos na qual o index +1 é igual ao numero da franquia
                codigo_empresa = []
                #lê a planilha que possui os códigos
                planilha = pd.read_excel(f"C:\\Curso02_github\\atividade_10_organizar_arquivos\\listaempresas.xlsx", sheet_name='Select e070fil')
                #recebe a coluna NUMCGC inteira
                codigo = planilha['NUMCGC']
                #apende código por código de cada empresa pesente na coluna NUMCGC
                for empresa in range(len(codigo)):
                    codigo_empresa.append(int(codigo[empresa]))
                #verifica a franquia 
                franq = int(arquivo[0:14])
                index = codigo_empresa.index(franq)
                franq = index + 1
                if franq<10:
                    franq = f'0{franq}'
                #verifica o ano 
                if arquivo[15:19].isdigit():
                    ano = arquivo[15:19]
                #caso já não tenha sido criada a pasta, ele cria uma pasta referente ao ano da nota 
                if (not os.path.exists(f'{path_criar_pasta}\\{franq}\\{ano}')):  
                    os.mkdir(f'{path_criar_pasta}\\{franq}\\{ano}')
                #verifica a data padrao (anoMes)
                if arquivo[15:21].isdigit():
                    data = arquivo[15:21]
                #caso já não tenha sido criada a pasta, ele cria uma pasta referente á data padrao da nota 
                if (not os.path.exists(f'{path_criar_pasta}\\{franq}\\{ano}\\{data}')):  
                    os.mkdir(f'{path_criar_pasta}\\{franq}\\{ano}\\{data}')
                # move o arquivo para sua respectiva pasta
                os.rename(f'{path_inicial}\\{arquivo}',f'{path_criar_pasta}\\{franq}\\{ano}\\{data}\\{arquivo}')
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


def bot_10():
    try:
        criar_pastas_franquia('C:\\Pastas Compartilhadas\\FCI\\06_FCI\\01_Hennings\\Robo\\Robo')
        print('criou Pastas')
        ler_arquivos_e_adicionar_na_pasta('C:\\Pastas Compartilhadas\\FCI\\06_FCI\\01_Hennings\\Robo\\Robo')
        print('organizou pasta 1')
        ler_arquivos_e_adicionar_na_pasta('C:\\Pastas Compartilhadas\\FCI\\06_FCI\\01_Hennings\\Robo\\Robo\\Old')
        print('organizou pasta 2')
        ler_arquivos_e_adicionar_na_pasta('C:\\Pastas Compartilhadas\\FCI\\06_FCI\\01_Hennings\\Robo\\Robo\\Retorno')
        print('organizou pasta 3')
        ler_arquivos_e_adicionar_na_pasta('C:\\Pastas Compartilhadas\\FCI\\06_FCI\\01_Hennings\\Robo\\Robo\\Retorno\\Processado\\2022')
        print('organizou pasta 4')
        ler_arquivos_e_adicionar_na_pasta('C:\\Pastas Compartilhadas\\FCI\\06_FCI\\01_Hennings\\Robo\\Robo\\Retorno\\Processado\\Arquivos')
        print('organizou pasta 5')
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


if __name__ == '__main__':
    bot_10()
    print('rodou com sucesso')