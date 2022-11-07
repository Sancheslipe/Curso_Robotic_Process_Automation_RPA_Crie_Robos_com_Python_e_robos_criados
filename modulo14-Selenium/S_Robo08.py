from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time as t 
navegador = Chrome()

navegador.get("https://busca.inpi.gov.br/pePI/servlet/LoginController?action=login")
navegador.maximize_window()

t.sleep(2)

# navegador.find_element_by_id("//map/area[2]")
c = 0
while c < 7:
    c += 1
    try:
        navegador.find_element('xpath', '//*[@id="Map3"]/area[2]').click()
        
        break
    except:
        t.sleep(1)
navegador.find_element('name','ExpressaoPesquisa').send_keys('03768202000176')
t.sleep(0.5)
navegador.find_element('xpath', '//select[2]/option[4]').click()
t.sleep(1)
navegador.find_element('css_selector','input[type="submit"]').click()


