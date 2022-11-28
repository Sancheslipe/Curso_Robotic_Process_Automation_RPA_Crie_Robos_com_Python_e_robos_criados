import os 


caminho_procura ="C:\\Curso02_github"
caminho = os.listdir(caminho_procura)
# for raiz, diretorios, arquivo in os.walk(caminho_procura):
#     # if 'xlsx' in arquivo:
#     #     if arquivo == 'listaempresas.xlsx':
#     #         print(f'caminho:{raiz}\nnome:{arquivo}')

if 'listaempresas.xlsx' in caminho:
    print('está')