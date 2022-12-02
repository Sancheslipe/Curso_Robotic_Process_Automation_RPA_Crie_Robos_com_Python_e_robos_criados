from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
options = webdriver.ChromeOptions()   
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get('https://www.google.com/recaptcha/api2/demo')
sleep(5)
imagem_captcha = driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div/table/tbody')
sleep(2)
imagem_captcha.screenshot(r'C:\Curso02_github\captchas\captcha1.png')