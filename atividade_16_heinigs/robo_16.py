import os
import sys
import pyautogui as p 
from time import sleep
from datetime import datetime 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''
COMENTÁRIOS

função que tem parametros pasta_final == pro 
weg_jrg_ na frente
 
"sitewegjaragua":"https://www.me.com.br/do/PedidoFornecedor.mvc",
    "loginwegjaragua":"E1EDDEAB",
    "senhawegjaragua":"MEHennings@2022",
'''
def limpar_pastas(path_pasta_final):   
    try:
        #limpa a pasta de destino
        pasta_destino = os.listdir(path_pasta_final)
        for arquivo in pasta_destino:
            os.remove(f'{path_pasta_final}\\{arquivo}')
        #limpa a pasta de download
        data_padrao = datetime.now().strftime('%Y-%m-%d')
        pasta_download = os.listdir(os.path.expanduser("~")+'\\Downloads')
        path_pasta_download = os.path.expanduser("~")+'\\Downloads'
        for arquivo in pasta_download:
            if data_padrao in arquivo and '_Pedidos' in arquivo:
                os.remove(f'{path_pasta_download}\\{arquivo}')
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')
                

def entrar_no_site_e_baixar_ultimos_100(driver):
    try:
        #entra no site
        driver.get('https://www.me.com.br/supplier/inbox/transactions/13')
        driver.maximize_window()
        #preenche o login
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/main/section[2]/div[2]/form/div[1]/div/input'))).send_keys('E1EDDEAB')
        #preenche a senha 
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/main/section[2]/div[2]/form/div[2]/div/input'))).send_keys('MEHennings@2022')
        #clica no botao entrar
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/main/section[2]/div[2]/form/div[4]/button'))).click()
        # #fecha o pop up 
        p.press('esc') 
        sleep(2)
        #clicar nos 3 pontinhos
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/main/div/div/div/main/div[2]/section/section/header/nav/div/button'))).click()
        #clicar no 100 itens
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/main/div/div/div/main/div[2]/section/section/header/nav/div/ul/li[5]/ul/li[4]/a'))).click()
        #seleciona todos 
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/main/div/div/div/main/div[2]/section/section/div/div/table/thead/tr/th[1]/div'))).click()
        sleep(2)
        #clicar nos 3 pontinhos
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/main/div/div/div/main/div[2]/section/section/header/nav/div/button'))).click()
        #clicar no exportar excel
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/main/div/div/div/main/div[2]/section/section/header/nav/div/ul/li[6]/ul/li[1]'))).click()
        sleep(10)
        print('baixou o arquivo')
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


def adicionar_arquivo_na_pasta_certa(path_pasta_final):
    try:
        #pasta_download recebe a pasta download do notebook
        pasta_download = os.listdir(os.path.expanduser("~")+'\\Downloads')
        #percorre todos os arquivos da pasta_download
        for arquivo in pasta_download:
            if 'Pedidos.xls' in arquivo:
                os.rename(os.path.expanduser("~")+f'\\Downloads\\{arquivo}',f'{path_pasta_final}\\weg_jrg_{arquivo}')
                #caso ainda exista o arquivo na pasta download ele exclui
                if os.path.exists(os.path.expanduser("~")+f'\\Downloads\\{arquivo}'):
                    os.remove(os.path.expanduser("~")+f'\\Downloads\\{arquivo}')
                    print('removeu da pasta downloads')
                print('renomeou o arquivo')
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


def bot_16():
    try:
        print('robô inicializado')
        path_pasta = 'C:\\Curso02_github\\atividade_16_heinigs\\proc'
        #inicializa o webdriver
        limpar_pastas(path_pasta)
        options = webdriver.ChromeOptions()   
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
        entrar_no_site_e_baixar_ultimos_100(driver)
        #path_pasta == pasta que você deseja mover o arquivo
        adicionar_arquivo_na_pasta_certa(path_pasta)
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')
    

if __name__ == '__main__':
    try:
        #fecha todas as abas do crome (puxa da tomada)
        os.system('taskkill /f /im chrome.exe')
        #executa todas as outras funcoes acima 
        bot_16()
        print('Robô finalizado com sucesso')
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')

