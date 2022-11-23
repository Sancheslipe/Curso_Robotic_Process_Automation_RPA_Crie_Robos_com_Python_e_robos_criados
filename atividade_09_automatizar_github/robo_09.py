import pyautogui as p 
import os 
from keyboard import write
from time import sleep

p.hotkey('win','r')
write('C:\\Users\\Ana Paula\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe')
p.press('enter')
sleep(2)
x1,y1 = p.locateCenterOnScreen('C:\\Curso02_github\\atividade_09_automatizar_github\\ima\\listar_repositorio.png')
p.moveTo(x1,y1)
p.click()