from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time as t 

navegador = Chrome()
navegador.get('https://ferendum.com/pt/')
navegador.maximize_window()
t.sleep(2)
navegador.find_element('name','titulo').send_keys('A automação é uma coisa boa? (Felipe 3)')
navegador.find_element('name','descripcion').send_keys('Os robôs estão cada vez mais frequentes em nossas vidas..')
navegador.find_element('name','creador').send_keys('Felipe Curso Rpa com Python')
navegador.find_element('id','op1').send_keys('Sim! Ela me ajuda muito..')
navegador.find_element('id','op2').send_keys('Não! Estou com medo de perder o emprego..')
navegador.find_element('name','config_anonimo').click()
navegador.find_element('name','config_priv_pub').click()
navegador.find_element('name','config_un_solo_voto').click()
navegador.find_element('name','accept_terms_checkbox').click()
t.sleep(0.5)
navegador.find_element('xpath','/html/body/spamtrap/main/div[1]/div/form/input[5]').click()
t.sleep(1)
navegador.find_element('id', 'crear_votacion').click()
t.sleep(2)
texto = navegador.find_element('id','textoACopiar').text
print(texto)
navegador.quit()