from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as p 
from time import sleep
import openpyxl
import os
import sys

def excluir_cookies(xpath):
    cookie = xpath
    driver.find_element(By.XPATH,cookie).click()
    

def excluir_propaganda(xpath):
    prop = xpath
    driver.find_element(By.XPATH,prop).click()


def abrir_preparar_site(driver,url):
    driver.get(url)
    driver.maximize_window()
    p.press('F11')
    sleep(7)
    excluir_cookies('/html/body/div[3]/div[1]/div/div/div[2]/button[2]/span')
    excluir_propaganda('//*[@id="clever_56734_close_btn"]')
    

def pegar_informacoes(qtde):
    #Xpaths do porte estavam dando vários problemas, por isso guardei-os em um array para serem utilizados de maneira mais eficiente
    xpath_porte = ['/html/body/div[1]/div[1]/div/div[1]/p[4]/b','/html/body/div/div[1]/div/div[1]/p[5]/b','/html/body/div/div[1]/div/div[1]/p[4]/b']
    pessoa = int(qtde)
    #clica na pessoa
    driver.find_element(By.CSS_SELECTOR ,f"body > div.bg-white > main > div.max-w-4xl.mx-auto.bg-white.shadow.overflow-hidden.sm\:rounded-md > ul > li:nth-child({pessoa}) > a > div > div.flex.items-center.justify-between > p").click()
    sleep(3)
    #Nome:
    nome = driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/p[2]/span/b').text
    #dias:
    dias = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[1]/p[3]/span[1]/b').text                              
    if dias[0:2].isdigit():
        dias = dias  
    else:
        dias = driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/p[4]/span[1]/b').text
    #porte
    try:
        porte = driver.find_element(By.XPATH,xpath_porte[0]).text
    except:
        sleep(1)
    try:       
        porte = driver.find_element(By.XPATH,xpath_porte[1]).text
    except:
        sleep(1)
    try:       
        porte = driver.find_element(By.XPATH,xpath_porte[2]).text
    except:
        sleep(1)
    return nome,dias,porte


def armazenar_informacoes():
    qtde = 1
    nome_list = []
    dias_list = []
    porte_list = []
    # for qtde in range(1,28):
    #     print(f'raspando dados da Empresa {qtde}')
    #     if qtde == 14 or qtde == 15:
    #         print()
    #     else:
    #         situacao = driver.find_element(By.CSS_SELECTOR ,f"body > div > main > div.max-w-4xl.mx-auto.bg-white.shadow.overflow-hidden.sm\:rounded-md > ul > li:nth-child({qtde}) > a > div > div.flex.items-center.justify-between > div").text
    #         if situacao.upper() == 'ATIVA':
    #             nome,dias,porte = pegar_informacoes(qtde)
    #             nome_list.append(nome)
    #             dias_list.append(dias)
    #             porte_list.append(porte)
    #             sleep(0.5)
    #             p.hotkey('browserback')
    for l in range(4):
        qtde = 1
        sleep(3)
        while qtde >=1 and qtde<28:
            print(f'raspando dados da pagina {l + 1} empresa {qtde}')
            if qtde == 14 or qtde == 15:
                print()
                qtde += 1
            else:
                situacao = driver.find_element(By.CSS_SELECTOR ,f"body > div > main > div.max-w-4xl.mx-auto.bg-white.shadow.overflow-hidden.sm\:rounded-md > ul > li:nth-child({qtde}) > a > div > div.flex.items-center.justify-between > div").text
                if situacao.upper() == 'ATIVA':
                    nome,dias,porte = pegar_informacoes(qtde)
                    nome_list.append(nome)
                    dias_list.append(dias)
                    porte_list.append(porte)
                    sleep(0.5)
                    p.hotkey('browserback')
                    qtde += 1
                else:
                    qtde += 1




        driver.find_element(By.XPATH,'/html/body/div[1]/main/div[3]/div[1]/div/a').click()
        print('\nPASSOU 1 PÁGINA!\n')
        sleep(2)

    return nome_list,dias_list,porte_list   


def salvar_em_excell(lista_1,lista_2,lista_3):
    book = openpyxl.Workbook('Dados_empresa.xlsx')
    book.create_sheet('dados')
    dados_page = book['dados']
    dados_page.append(['NOME','DATA_ABERTURA','PORTE'])
    for x in range(len(lista_1)-1):
        dados_page.append([f'{lista_1[x]}',f'{lista_2[x]}',f'{lista_3[x]}'])

    book.save('Dados_empresa.xlsx')
    print('salvou')


def bot_006(driver):
    try:
        list1 = []
        list2 = []
        list3 = []
        abrir_preparar_site(driver,'https://cnpj.biz/empresas/blumenau-sc')
        sleep(1)
        list1,list2,list3 = armazenar_informacoes()
        salvar_em_excell(list1,list2,list3)     
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')
#faster solution
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)
# bot_006(driver)

if (__name__ == '__main__'):
#    laziest solution
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    bot_006(driver)
    print('Robô executado com sucesso')
    driver.close()