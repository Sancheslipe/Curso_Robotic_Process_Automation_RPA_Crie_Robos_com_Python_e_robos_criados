from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

options = Options()
# options.add_argument('--headless')

navegador = webdriver.Chrome(options=options)

navegador.set_window_size(400,800)
preco = '/html/body/div[5]/div/div/div[1]/div/div/div[2]/div/main/div[1]/div/div/div/div/div/div/div[2]/div[3]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/div[1]/div/div[1]/div[4]/div/div/span/span'

navegador.get('https://www.airbnb.com.br/')
sleep(1)
navegador.find_element(By.XPATH,'/html/body/div[10]/section/div/div/div[2]/div/div[1]/button').click()
sleep(1)
test = navegador.find_element(By.XPATH,preco).text
print(test)
navegador.close()

