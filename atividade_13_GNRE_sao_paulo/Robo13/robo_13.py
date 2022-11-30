import os
import sys
# from time import sleep
from keyboard import write
from selenium import webdriver
from selenium.webdriver.common.by import By

#São Paulo
'''
os.system('taskkill /f /im chrome.exe')

try:
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    driver.get('https://www4.fazenda.sp.gov.br/DareICMS/DareAvulso')

    driver.maximize_window()
    sleep(1)

    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/main/div[5]/div[1]/div/div/iframe').click()




except:
    exc_type, error, line = sys.exc_info()
    print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')
'''

#minas 
try:
    os.system('taskkill /f /im chrome.exe')
    options = webdriver.ChromeOptions()   
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    driver.get('https://daeonline1.fazenda.mg.gov.br/daeonline/executeEmissaoDocumentoArrecadacao.action')
    driver.maximize_window()
    driver
except:
    exc_type, error, line = sys.exc_info()
    print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')