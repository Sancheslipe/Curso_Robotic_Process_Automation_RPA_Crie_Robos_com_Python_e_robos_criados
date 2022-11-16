import rpa as r
import pyautogui as p
import pandas as pd

r.init()
r.url('http://rpachallenge.com')
janela = p.getActiveWindow()
janela.maximize()
p.sleep(2)

r.click('/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/a')
p.sleep(5)
p.click(x=1350, y=688)
p.sleep(2)
# EStá dando erro o download
# r.download_location('https://rpachallenge.com/assets/downloadFiles/challenge.xlsx')
# p.sleep(1)
r.mouse()
p.sleep(3)
dados = pd.read_excel("C:\\Curso02_github\\challenge.xlsx", sheet_name='Sheet1')

df = pd.DataFrame(dados, columns=["First Name",	"Last Name ", "Company Name", "Role in Company", "Address", "Email", "Phone Number"])

r.click('/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')

for row in df.itertuples():
    r.type('//*[@ng-reflect-name="labelFirstName"]', row[1])
    r.type('//*[@ng-reflect-name="labelLastName"]', row[2])
    r.type('//*[@ng-reflect-name="labelCompanyName"]', row[3])
    r.type('//*[@ng-reflect-name="labelRole"]', row[4])
    r.type('//*[@ng-reflect-name="labelAddress"]', row[5])
    r.type('//*[@ng-reflect-name="labelEmail"]', row[6])
    r.type('//*[@ng-reflect-name="labelPhone"]', str(row[7]))
    r.click('/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input')
p.sleep(5)
p.screenshot('score.png')
r.close()

print('\nprograma encerrado com sucesso!\n')