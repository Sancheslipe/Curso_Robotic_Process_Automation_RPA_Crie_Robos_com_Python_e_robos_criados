import PySimpleGUI as sg
from cotacao import pegar_cotacoes

layout = [
    [sg.Text('Pegar Cotação da Moeda')],
    [sg.InputText(key='nome_cotacao')],
    [sg.Button('Pegar Cotação'),sg.Button('Cancelar')],
    [sg.Text(key='texto_cotacao')],
]

janela = sg.Window('Janela de teste',layout=layout)

while True:
    evento,valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break
    elif evento == 'Pegar Cotação':
        codigo_cotacao = valores['nome_cotacao']
        cotacao = pegar_cotacoes(codigo_cotacao)
        janela['texto_cotacao'].update(f'a cotação do {codigo_cotacao} é de R${cotacao}')

janela.close()