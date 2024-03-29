import pyautogui as p 
from keyboard import write
from time import sleep
import datetime
import sys
import os


def abrir_github():
    p.FAILSAFE = False
    p.hotkey('win','r')
    write('C:\\Users\\Ana Paula\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe')
    p.press('enter')
    sleep(1.5)


def escolher_pagina_e_subir_arquivos():
    p.FAILSAFE = False
    x1,y1 = p.locateCenterOnScreen('C:\\Curso02_github\\atividade_09_automatizar_github\\ima\\listar_repositorio.png')
    p.moveTo(x1,y1,duration=1)
    p.click()
    x1,y1 = p.locateCenterOnScreen('C:\\Curso02_github\\atividade_09_automatizar_github\\ima\\Curso02_github.png')
    p.moveTo(x1,y1,duration=1)
    p.click()
    try:
        x1,y1 = p.locateCenterOnScreen('C:\\Curso02_github\\atividade_09_automatizar_github\\ima\\comentario_1.png')
        p.moveTo(x1,y1,duration=1)
        p.click()
        write(f'{datetime.datetime.now()}')
    except:
        test = p.locateCenterOnScreen('C:\\Curso02_github\\atividade_09_automatizar_github\\ima\\comentario_2.png')
        if (test == None) :
            p.moveTo(x=216, y=532)
            p.click()
            write(f'{datetime.datetime.now()}')
        else:
            x1,y1 = test
        p.moveTo(x1,y1,duration=1)
        p.click()
        write(f'{datetime.datetime.now()}')
    x1,y1 = p.locateCenterOnScreen('C:\\Curso02_github\\atividade_09_automatizar_github\\ima\\descriptions.png')
    p.moveTo(x1,y1)
    p.click()
    write(f'teste')
    p.hotkey('ctrl','p')
    x1,y1 = p.locateCenterOnScreen('C:\\Curso02_github\\atividade_09_automatizar_github\\ima\\commit_to_main.png')
    p.moveTo(x1,y1,duration=1)
    p.click()
    sleep(3)
    p.hotkey('ctrl','p')


def bot_09():
    try:
        p.FAILSAFE = False
        os.system('taskkill /f /im GitHubDesktop.exe')
        # os.system('cls')
        abrir_github()
        escolher_pagina_e_subir_arquivos()
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')

if __name__ == '__main__':
    # os.system('cls')
    bot_09()
    print('robô executado com sucesso')