import pyautogui as p

p.doubleClick(x=48, y=229)
p.sleep(2)
p.write('www.udemy.com')
p.press('enter')
janela = p.getActiveWindow()
janela.maximize()
p.sleep(2)

localPesq = p.locateOnScreen('C:\\Curso02_github\\modulo 7\\Pesquisa1.png', confidence=0.9)
localPesquisa = p.center(localPesq)
xPesquisa,YPesquisa = localPesquisa
p.moveTo(xPesquisa, YPesquisa,duration=0.5)
p.click(xPesquisa,YPesquisa)
p.sleep(1)
p.write('Charles Lima')
p.press('enter')
p.sleep(1)
p.screenshot('Cursos.png')

localClo = p.locateOnScreen('C:\\Curso02_github\\modulo 7\\Close.PNG', confidence=0.9)
localClose = p.center(localClo)
xClose,YClose = localClose
p.moveTo(xClose, YClose,duration=0.5)
p.click(xClose,YClose)
# print(p.position())www.udemy.com
