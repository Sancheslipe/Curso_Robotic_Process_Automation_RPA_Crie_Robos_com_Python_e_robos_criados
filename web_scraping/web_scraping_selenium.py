from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

navegador = webdriver.Chrome()

navegador.get('https://walisson-silva-website.vercel.app/blog')
navegador.maximize_window()
sleep(2)
elemento = navegador.find_element(By.TAG_NAME, "input")
elemento.send_keys('Data')


