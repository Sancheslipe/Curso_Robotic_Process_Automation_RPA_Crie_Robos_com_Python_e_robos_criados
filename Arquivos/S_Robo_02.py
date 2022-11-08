from selenium.webdriver import Chrome
from selenium.webdriver import Keys
import pyautogui as p
import time as t

navegador = Chrome()

navegador.get('https://www.google.com')
navegador.maximize_window()
input = navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
input.clear()
input.send_keys('RPA')
input.send_keys(Keys.ENTER)

navegador.save_screenshot()
