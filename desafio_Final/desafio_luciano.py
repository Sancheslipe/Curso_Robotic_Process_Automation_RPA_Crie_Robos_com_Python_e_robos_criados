import pyautogui as p
import pandas as pd

# p.sleep(3)
# print(p.position())
star = 0
p.click(x=874, y=742) #clicar no chrome
p.sleep(3)
janela = p.getActiveWindow()
janela.maximize()
p.click(x=350, y=51)
p.write('http://rpachallenge.com')
p.press('enter')
p.sleep(20)
# dados = pd.read_excel("C:\\Users\\Ana Paula\\Downloads\\challenge.xlsx", sheet_name='Sheet1')
# df = pd.DataFrame(dados, columns=["First Name",	"Last Name ", "Company Name", "Role in Company", "Address", "Email", "Phone Number"])

localPesq = p.locateOnScreen('C:\\Curso02_github\\desafio_Final\\TeclaStart.png', confidence=0.9)
print(localPesq)
localPesquisa = p.center(localPesq)
xPesquisa, yPesquisa = localPesquisa
p.moveTo(xPesquisa, yPesquisa, duration=1)

# p.click(xPesquisa, yPesquisa)
# p.sleep(5)

# p.write('Charles Lima')
# p.press('enter')
# p.sleep(3)