import PySimpleGUI as sg

def janela_loguin():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout=layout,finalize= True)

def janela_pedido():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('Pizza Pepperroni',key= 'Pizza1'),sg.Checkbox('Pizza de Bacon',key= 'Pizza2')],
        [sg.Button('Voltar'),sg.Button('Fazer Pedido')]
    ]
    return sg.Window('Montar Pedido',layout=layout,finalize=True)

janela1,janela2 = janela_loguin(),None

while True:
    window,event,values = sg.read_all_windows()
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    elif window == janela1 and event == 'Continuar':
        janela2 = janela_pedido()
        janela1.hide()
    elif window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    elif window == janela2 and event == 'Fazer Pedido':
        if values['Pizza1'] == True and values['Pizza2'] == True:
            sg.popup('Foram solicitados uma pizza de Pepperroni e uma pizza de bacon!')
        elif values['Pizza1'] == True:
            sg.popup('Foi solicitados uma pizza de Pepperroni!')
        elif values['Pizza2'] == True:
            sg.popup('Foi solicitados uma pizza de Bacon!')
   

