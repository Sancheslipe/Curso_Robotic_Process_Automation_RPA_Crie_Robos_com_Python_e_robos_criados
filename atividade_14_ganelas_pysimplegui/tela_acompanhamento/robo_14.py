import os 
import sys 
import PySimpleGUI as sg


def janela_escolher_robo():
    sg.theme('Material2')
    layout = [
        [sg.Text('escolha qual Robô você deseja cacompanhar o processo: \n')],
        [sg.Text('Robo_01'),sg.Button('Click here',key= 'Robo_01')],
        [sg.Text('Robo_02'),sg.Button('Click here',key= 'Robo_02')],
        [sg.Text('\n')]
    ]
    return sg.Window('janela_escolher_robo', layout=layout,finalize= True)


def janela_proc_robo():
    sg.theme('Material2')
    layout = [
        [sg.Text(key='nome_robo')],
        [sg.Text(key='desc_robo')],
        [sg.Button('Situação',key= 'situacao'), sg.Button('Erros',key= 'erros'), sg.Button('Voltar')]
    ]
    return sg.Window('janela_proc', layout=layout,finalize= True)

def janela_erros():
    sg.theme('Material2')
    layout = [
        [sg.Text('Os erros foram!\n')],
        [sg.Text(key = 'error')],
        [sg.Text(key = 'exc_type')],
        [sg.Text(key = 'func')],
        [sg.Text(key = 'line')],
        [sg.Button('Voltar')]
    ]
    return sg.Window('janela_erros', layout=layout,finalize= True)


def janela_situacao():
    sg.theme('Material2')
    layout = [
        [sg.Text('Os erros foram!\n')],
        [sg.Text(key = 'error')],
        [sg.Text(key = 'exc_type')],
        [sg.Text(key = 'func')],
        [sg.Text(key = 'line')],
        [sg.Button('Voltar')]
    ]
    return sg.Window('janela_situacao', layout=layout,finalize= True)

janela1, janela2 = janela_escolher_robo(),None


while True:
    window,event,values = sg.read_all_windows()
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    elif window == janela1 and event == 'Robo_01':
        janela1.hide()
        janela2 = janela_proc_robo()
        janela2['nome_robo'].update('Robo_01')
        janela2['desc_robo'].update('esta é uma janela para mostrar as descrições do robô 01')

    elif window == janela1 and event == 'Robo_02':
        janela1.hide()
        janela2 = janela_proc_robo()
        janela2['nome_robo'].update('Robo_02')
        janela2['desc_robo'].update('esta é uma janela para mostrar as descrições do robô 02')

    elif window == janela2 and event == sg.WINDOW_CLOSED or event == 'Voltar':
        janela2.hide()
        janela1.un_hide()

    elif window == janela2 and event == 'erros':
        janela2.hide()
        janela3 = janela_erros()
        f
    elif window == janela2 and event == 'Voltar' or event == sg.WIN_CLOSED:
        janela3.hide()
        janela2.un_hide()