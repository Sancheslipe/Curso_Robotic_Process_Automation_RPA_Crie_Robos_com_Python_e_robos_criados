import os
import sys
from time import sleep
import PyPDF2 as pdf
import pandas as pd
from datetime import datetime
from selenium import webdriver
from twocaptcha import TwoCaptcha
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def solveRecaptcha(sitekey, file, textinstructions, lang, url):
    api_key = '6a3fe4daa3e77f26f5235e8b615d3e33'
    solver = TwoCaptcha(api_key)
    try:
        result = solver.hcaptcha(
            sitekey=sitekey,
            file=file, 
            textinstructions=textinstructions, 
            lang=lang, 
            url=url)
    except Exception as e:
        print(e)
    else:
        return result

#minas 
def entrar_site_minas_e_baixa_pdf(driver,numero_nota_fiscal=0):
    try:
        #entra no Site
        driver.get('https://daeonline1.fazenda.mg.gov.br/daeonline/executeEmissaoDocumentoArrecadacao.action')
        driver.maximize_window()
        sleep(1)
        #clica no tipos
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[3]/form/div[1]/div[1]/div/div/a').click()
        #CLICAR NO CNPJ
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div/ul/li[3]/a').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[3]/form/div[3]/div[1]/div/div/a').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/ul/li[8]/a').click()
        sleep(1)
        #clicar no captcha 
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[3]/form/div[4]/div[1]/div/div/div/div/iframe').click()
        sleep(3)
        #input para pausar a aplicação enquanto estou resolvendo o captcha 
        input('resolva o captcha!')
        #preenche o cnpj
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[3]/form/div[2]/div[1]/div/div/input').send_keys('83748772000990')
        Keys.ENTER
        # clicar no cntinuar
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[3]/form/div[5]/div[1]/div/a[1]').click()
        sleep(1)
        #recebe o dia e o mês atual.
        dia = datetime.now().day
        mes = datetime.now().month
        #clica seletor data
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/fieldset[2]/div[2]/div[4]/div[1]/span[2]/div/div/a').click()
        #escolhe mes
        driver.find_element(By.XPATH, '/html/body/div[1]/div[11]/span/div[1]/div[1]/div/div/select').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[11]/span/div[1]/div[1]/div/div').click()
        sleep(1)
        driver.find_element(By.XPATH, f'/html/body/div[1]/div[11]/span/div[1]/div[1]/div/div/select/option[{mes}]').click()
        sleep(1)
        # escolhe e clica no dia 
        elementos = driver.find_elements(By.CSS_SELECTOR , 'div[class="ui-datebox-griddate ui-corner-all ui-btn ui-btn-a"]')
        #comando para achar pelo nome da classe usando o css selector passado pelo louie
        elementos.append(driver.find_element(By.CSS_SELECTOR , 'div[class="ui-datebox-griddate ui-corner-all ui-btn ui-btn-b"]')) 
        #percorre todos os elementos dentro do array elementos 
        for element in elementos:
            #caso o elemento possua o mesmo dia que o dia atual clica nele
            if element.text == str(dia):
                element.click()
        #preenche o VALOR (valor especificado pelo luciano 50,55)
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/fieldset[3]/div[2]/div[2]/div[1]/span[2]/div/input').send_keys('0555')
        Keys.ENTER
        #preenche o Numero da nota fiscal NUMNFV
        sleep(1)
        # driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/fieldset[4]/div[2]/div[2]/div[1]/span[2]/div/input').send_keys(f'{numero_nota_fiscal}')
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/fieldset[4]/div[2]/div[2]/div[1]/span[2]/div/input').send_keys('53643')
        Keys.ENTER
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/fieldset[4]/div[1]/a').click()
        Keys.END
        #clicar em continuar
        sleep(3)
        driver.find_element(By.XPATH, '//*[@id="submit"]').click()
        sleep(4)
        print('passou para outra página')
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/div[2]/div/a').click()
        print('baixou o PDF')
        sleep(5)

    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


def ler_pdf_trocar_nome():
    #o pdf por padrao é baixado nesta pasta com este nome 
    pdf_file = open('C:\\Users\\Ana Paula\\Downloads\\daeonline.pdf','rb')
    #lê os dados do pdf
    dados_do_pdf = pdf.PdfFileReader(pdf_file)
    #seleciona a primeira pagina pdo pdf
    pagina1 = dados_do_pdf.getPage(0)
    #transforma toda a pagina em string
    texto_da_pagina1 = pagina1.extract_text()
    #divide em um array onde o index é referente a linha do arquivo
    list_test = texto_da_pagina1.split('\n')
    #percorre todo o pdf 
    for linha in list_test:
        #nome_arquivo recebe somente a parde do pdf referente aos digitos do codigo de barra
        if 'Linha Digitável:' in linha : 
            nome_arquivo = linha[0:56].replace(' ','')
    pdf_file.close()  
    #altera o nome do pdf para o código de barra, e move ele para uma pasta selecionada      
    os.rename('C:\\Users\\Ana Paula\\Downloads\\daeonline.pdf',f'C:\\Curso02_github\\atividade_13_GNRE_sao_paulo\\arquivos_mod\\{nome_arquivo}.pdf')
    

def ler_excel_MG():
    try:
        #array que guarda todas as notas fiscais 
        nota_fiscal = []
        #lê a planilha na aba Select e501tcp
        planilha = pd.read_excel(r'C:\Curso02_github\atividade_13_GNRE_sao_paulo\Notas_heinigs\DadosNotas.xlsx',sheet_name='Select e501tcp')
        #passa por toda a planilha
        for l in range(len(planilha)):
            #apende o numero da nota fiscal somente se ele no campo da região de atuacao eh igual a MG
            if planilha.loc[l,"SIGUFS"] == 'MG':
                numero_nota_fiscal = planilha.loc[l,"NUMNFV"]
                nota_fiscal.append(numero_nota_fiscal)
        return nota_fiscal    
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')

        
def inicio_minas():
    try:
        #fecha abas do chrome
        os.system('taskkill /f /im chrome.exe')
        #o processo abaixo é para abrir e criar o drive de acordo com a nova regra de implantação
        options = webdriver.ChromeOptions()   
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
        # list_notas_fiscais = ler_excel_MG()
        # for nota_fiscal in list_notas_fiscais:
        #     entrar_site_minas_e_baixa_pdf(driver,nota_fiscal)
        entrar_site_minas_e_baixa_pdf(driver)
        sleep(2)
        ler_pdf_trocar_nome()

    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


if __name__ == "__main__":
    inicio_minas()
    print('robô finalizado com sucesso!')


