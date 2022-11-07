import pyautogui as p 
'''
pegar posição do mouse

# p.moveTo(x=34, y=225, duration=0.1)
# p.click(x=34, y=225)

# p.sleep(2)
# print(p.position())
'''


p.hotkey('win','r')
p.sleep(1)
p.typewrite('notepad')
p.sleep(1.5)
p.press('enter')
p.sleep(1.5)
p.typewrite('Oi!! Eu sou um bot')
p.sleep(1.5)
valor = p.getActiveWindow()
valor.close()
p.press('right')
p.press('right')
p.sleep(1.5)
p.press('enter')
p.sleep(1.5)