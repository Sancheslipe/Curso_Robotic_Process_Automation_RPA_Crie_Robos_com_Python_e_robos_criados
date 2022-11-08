import rpa as r 
import pyautogui as p 
import pandas as pd
import os as o

r.init()
r.url('https://rpachallengeocr.azurewebsites.net/')
janela = p.getActiveWindow()
janela.maximize()
p.sleep(7)

countPage = 1
while countPage <= 3:
    if countPage == 1:
        r.table('//*[@id="tableSandbox"]','Temp.csv')
        dados = pd.read_csv('Temp.csv')
        dados.to_csv(r'webTable.csv', mode='a', index=None, header=True)
        r.click('//*[@id="tableSandbox_next"]')
        countPage += 1
    else:
        r.table('//*[@id="tableSandbox"]','Temp.csv')
        dados = pd.read_csv('Temp.csv')
        dados.to_csv(r'webTable.csv', mode='a', index=None, header=False)
        r.click('//*[@id="tableSandbox_next"]')
        countPage += 1
    
r.close()
o.remove('Temp.csv')
csv_xls = pd.read_csv(r'WebTable.csv')
csv_xls.to_excel(r'WebTable02.xlsx')