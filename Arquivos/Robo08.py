import pyautogui as p

p.hotkey('win','r')
p.sleep(1)
p.write('"C:\\Curso02_github\\modulo 8\\RPA.pbix"')
p.sleep(1)
p.press('enter')
p.sleep(25)
p.click(x=733, y=114)
print('click 1')
p.sleep(10)
p.click(x=1342, y=10)
print('click 2')
p.sleep(7)

# salvar
p.click(x=700, y=397)

print('click 3')