import pyautogui as p 
from keyboard import write
from time import sleep
import datetime
import os


def abrir_github():
    p.hotkey('win','r')
    write('C:\\Users\\Ana Paula\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe')
    p.press('enter')
    sleep(1.5)


def escolher_pagina_e_subir_arquivos():
    x1,y1 = p.locateCenterOnScreen('C:\\Curso02_github\\atividade_09_automatizar_github\\ima\\listar_repositorio.png')
    p.moveTo(x1,y1,duration=1)
    p.click()
    x1,y1 = p.locateCenterOnScreen('C:\\Curso02_github\\atividade_09_automatizar_github\\ima\\Curso02_github.png')
    p.moveTo(x1,y1,duration=1)
    p.click()
    x1,y1 = 150, 550
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
    os.system('taskkill /f /im GitHubDesktop.exe')
    os.system('cls')
    abrir_github()
    escolher_pagina_e_subir_arquivos()

if __name__ == '__main__':
    os.system('cls')
    bot_09()
    print('robô executado com sucesso')