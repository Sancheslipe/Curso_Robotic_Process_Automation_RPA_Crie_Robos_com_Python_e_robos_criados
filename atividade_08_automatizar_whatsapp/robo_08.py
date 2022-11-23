import pyautogui as p 
from time import sleep
from keyboard import write
import os 
def abrir_chrome(): 
    os.system('taskkill /f /im chrome.exe')
    os.system('cls')
    p.hotkey('win','r')
    sleep(1)
    p.typewrite('chrome.exe')
    p.press('enter')
    sleep(1)


def entrar_no_whatsapp():
    p.typewrite('https://web.whatsapp.com/')
    p.press('enter')
    sleep(5)
    try:
        x,y = p.locateCenterOnScreen('C:\\Curso02_github\\atividade_08_automatizar_whatsapp\\ima\\restaurar_pagina.png')
        p.click(x,y)
    except TypeError:
        sleep(1)


def escolher_chat_e_enviar_mensagem():
    quant = 0
    cont = 0
    x1 = None
    y1 = None
    while cont <20:
        #espera x1,y1 ser diferente de None
        try:
            x1,y1 = p.locateCenterOnScreen('C:\\Curso02_github\\atividade_08_automatizar_whatsapp\\ima\\pesquisar_nome_whats.png')
        except TypeError:
            p.sleep(1) 
        if (x1 != None) and (y1 != None):
            break
        cont+=1  
    #Define a quantidade de mensagens que serao enviadas
    qtde = input('digite aqui o numero de mensagens que você deseja enviar: ')
    while quant <1:
        if qtde.isdigit():
            qtde = int(qtde)
            quant +=1
        else:
            print('digite um numero válido')
            quant = quant
    #envia a quantidade de mensagens escolhida
    for l in range(qtde):
        nome = input(f'\ndigite aqui o nome do remetente n° {l+1}:  ')
        if l == 0:
            texto = input('digite abaixo o seu texto:\n')
            # escolher_chat(remetente,text)
            p.moveTo(x1,y1,duration=0.75)
            p.click()
            p.typewrite(f'{nome}')
            p.press('enter')
            write(f'{texto}',delay=0.10)
            p.press('enter')
            sleep(3)
        else:
            alt = input('Deseja alterar a mensagem?\nDigite S para sim, ou qualquer outra coisa para não: ')
            if alt.upper() =='S':
                texto = input('digite abaixo o seu texto:\n')
            p.moveTo(x1,y1,duration=0.75)
            p.click()
            p.typewrite(f'{nome}')
            p.press('enter')
            write(f'{texto}',delay=0.10)
            p.press('enter')
            sleep(2)
    

def lista_de_transmissao():
    pessoas_list = list()
    cont = 0
    while cont <20:
        #espera x1,y1 ser diferente de None
        try:
            x1,y1 = p.locateCenterOnScreen('C:\\Curso02_github\\atividade_08_automatizar_whatsapp\\ima\\pesquisar_nome_whats.png')
        except TypeError:
            p.sleep(1) 
        if (x1 != None) and (y1 != None):
            break
        cont+=1 
    cont = 0
    while (cont < 1):
        quant_pessoas = input('digite aqui o numero de pessoas desta lista: ')
        if quant_pessoas.isdigit():
            quant_pessoas = int(quant_pessoas)
            cont += 1
        else:
            print('digite uma quantidade válida')
            cont = cont
        for x in range(quant_pessoas):
            nome = input(f'digite aqui o nome da pessoa {x} da lista: ')
            pessoas_list.append(nome)
        mensagem = input('digite aqui a mensagem que será enviada para esta lista de transmissão: ')
        for x in range(quant_pessoas):
            p.moveTo(x1,y1,duration=0.75)
            p.click()
            p.typewrite(f'{pessoas_list[x]}')
            p.press('enter')
            write(f'{mensagem}',delay=0.10)
            p.press('enter')
            sleep(2)


def bot_08():
    abrir_chrome()
    entrar_no_whatsapp()
    transmissao = input('deseja fazer uma lista de transmissão?\nDigite [S] para sim, ou qualquer outra coisa para não:')
    if transmissao.upper() == 'S':
        lista_de_transmissao()
    else:
        escolher_chat_e_enviar_mensagem()
    p.sleep(2)
    p.hotkey('alt','f4')


if (__name__ == "__main__"):
    bot_08()
    print('robô finalizado com sucesso!')