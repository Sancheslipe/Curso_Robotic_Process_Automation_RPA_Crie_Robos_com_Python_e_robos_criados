from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time as t

navegador = Chrome()
navegador.get('https://consultacnpj.com/cnpj/')
navegador.maximize_window()
t.sleep(1)
cnpjs = ["45997418000153", "72273196001090", "33000167000101"]
navegador.find_element('xpath','//*[@id="modal"]/div/div[2]/div/div[2]/a[1]').click()
t.sleep(0.5)

for cnpj in cnpjs:
    input = navegador.find_element('xpath', '//*[@id="__layout"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/input')
    input.clear()
    input.send_keys(cnpj)
    t.sleep(1)
    texto = navegador.find_element('xpath','//*[@id="company-data"]')
    with open(f'{str(cnpj)}.csv','w', encoding='UTF-8') as csv:
        csv.write(texto.text)
    t.sleep(2)

navegador.quit()