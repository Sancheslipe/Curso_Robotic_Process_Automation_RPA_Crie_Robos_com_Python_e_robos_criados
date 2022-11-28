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
# import pandas as pd
# import sys
# import os 

# os.makedirs('C:\\Pastas Compartilhadas\\FCI\\06_FCI\\01_Hennings\\Robo')
# print('pastas ciradas com sucesso')
# codigo_empresa = []

# planilha = pd.read_excel(f"C:\\Users\\Ana Paula\\Downloads\\listaempresas.xlsx", sheet_name='Select e070fil')
# codigo = planilha['NUMCGC']
# for empresa in range(len(codigo)):
#     codigo_empresa.append(codigo[empresa])

# print(codigo_empresa.index(83748772000567))

# teste = '83748772000133'
# print(teste[0:5])
# print(teste[15:21])


"""
Resposta para caso alguem perguntar, por que Deus permitiu que hitler nascesse, mesmo tendo em consideração que ele vê o nosso futuro e saberia quanto mal ele causaria?

resposta:
olha então, quando eu estava procurando um pouco mais sobre este assunto eu achei um video daquele pastor que é arqueologo saca, o Pastor Rodrigo Silva, 
enfim, neste video ele fala o seguinte , deus permitiu desde lá de trás desde quando jesus permitiu que satanas existisse


A: Deus não duela com seu caráter, quando ele diz na biblia que ele nos á o poder de escolha entre o bem e o mal 
base bilica deuteronomio 30:19()
    "Hoje invoco os céus e a terra como testemunhas contra vocês, de que coloquei diante de vocês a vida e a morte,
     a bênção e a maldição. Agora escolham a vida, para que vocês e os seus filhos vivam,
    20e para que vocês amem o Senhor, o seu Deus, ouçam a sua voz e se apeguem firmemente a ele.
     Pois o Senhor é a sua vida, e ele dará a vocês muitos anos na terra que jurou dar aos seus antepassados, Abraão, Isaque e Jacó".
 )
 então se ele nos deu o livre arbítrio de escolher o caminho que desejamos, eu entendo que por mais que ele seja um pai zeloso e amoror conosco,
 ele também é justo ao ponto de poder sofrer as consequências das nossas escolhas sendo elas boas ou más.
 dando um exemplo:
 quantos daqui gostam de bacon levanta a mão, mas aquele beiquinho 
 quantos aqui comem aquele miojão top temperadin e pá
 "ah felipe mas eu não gosto de miojo, beleza
 agora, quantos aqui num dia quente, talvez alguns tomem até em dia frio, gostam de tomar aquela linda, geladenha saboroooousa coquinha gelada, trincany
 entãogente voltando pro assunto original 
 , eu não falei essas comidas de maneira aleatória, todos esses alimentos são cancerigenos, basicamente você está ingerindo um veneno com sabor,
 não to falando issso para que você pare de tomar, mas o ponto é, por exemplo se uma pessoa come estes alimentos com frequência, tem uma vida alimentar e fisica desregrada 
 ela corre um risco sérissimo de adquirir cancêr , por conta própria, daí seria hipocrisia você orar para Deus te livrar de um cancêr que você passou a vida intera gerando

exemplo 2:

vou dar um exemplo bem simples,
vamos supor q tem 1 professor em uma sala de aula universitária certo, e em seu primeiro dia ele pede com que todos avaliem el com uma nota de 0 a 10
e ele promete leva-las ao diretor do colégio, só que antes de ele ir entregar as notas para o diretor, ele para em sua casa para conferir as notas,
e dai ele confere as nota, 





"""

import os 
import sys
from pathlib import Path
try:
    # os.rename(f'.\\listaempresas.xlsx', 'D:\\atividade_10_organizar_arquivos')
   file = Path('./listaempresas.xlsx')
   os.rename(file,'D:\\atividade_10_organizar_arquivos')
except:
    exc_type, error, line = sys.exc_info()
    print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')