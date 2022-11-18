from selenium.webdriver import Chrome
import selenium as s
import pyautogui as p 
import time
import os

class CookieClicker:
    def __init__(self):
        self.SITE_LINK = "https://orteil.dashnet.org/cookieclicker/"
        self.SITE_MAP = {
            "buttons" : {
                "biscoito":{
                    "xpath": '/html/body/div/div[2]/div[15]/div[8]/button'
                },
                "upgrade" :{
                    "xpath": "/html/body/div/div[2]/div[19]/div[3]/div[6]/div[$$NUMBER$$]"
                }
            }   
        }
        
        self.driver = Chrome()
        self.driver.maximize_window()
    

    def abrir_site(self):
        time.sleep(2)
        self.driver.get(self.SITE_LINK)
        time.sleep(10)


    def clicar_no_cookie(self):
        self.driver.find_element('xpath',self.SITE_MAP["buttons"]["biscoito"]["xpath"]).click()
    

    def pega_melhor_upgrade(self):
        encontrei = False
        elemento_atual = 2
        while not encontrei:
            objeto = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace("$$NUMBER$$", str(elemento_atual))
            classes_objeto = self.driver.find_element('xpath',objeto).get_attribute("class")
            if not "enabled" in classes_objeto:
                encontrei = True
            else:
                elemento_atual +=1
        return elemento_atual -1


    def comprar_upgrade(self):
        objeto = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace("$$NUMBER$$", str(self.pega_melhor_upgrade()))
        self.driver.find_element('xpath',objeto).click()


def abrir_e_configurar_site():
    biscoito = CookieClicker()
    biscoito.abrir_site()
    time.sleep(5)
    p.moveTo(x=683, y=496)
    print('achou')
    p.click()
    print('clicou')
    time.sleep(8)
    print('achou 2')
    p.moveTo(x=1310, y=694)
    p.doubleClick()
    print('clicou 2')
    time.sleep(5)
    return biscoito


def bot_005():
    biscoito = abrir_e_configurar_site()
    i = 0
    while True:
        if (i % 500 == 0)and (i != 0):
            time.sleep(1)
            biscoito.comprar_upgrade()
            time.sleep(1)
        biscoito.clicar_no_cookie()
        i += 1


if (__name__ == '__main__'):
    os.system('taskkill /f /im chrome.exe')
    os.system('cls')
    bot_005()