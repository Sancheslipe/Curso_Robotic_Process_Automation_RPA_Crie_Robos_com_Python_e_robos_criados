import os
import sys
import pandas as pd
import PyPDF2 as pdf
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def read_file_excell_mg():
    try:
        #array que guarda todas as notas fiscais 
        nota_fiscal = []
        list_valor_imposto = []
        list_cnpj = []
        #lê a planilha na aba Select e501tcp
        planilha = pd.read_excel(r'C:\Curso02_github\atividade_13_GNRE_sao_paulo\Notas_heinigs\DadosNotas_Def.xlsx',sheet_name='Select e501tcp')
        #passa por toda a planilha
        for l in range(len(planilha)):
            #apende o numero da nota fiscal somente se ele no campo da região de atuacao eh igual a MG
            if planilha.loc[l,"SIGUFS"] == 'MG':
                numero_nota_fiscal = planilha.loc[l,"NUMNFV"]
                valor_imposto = str(planilha.loc[l,"VLRORI"]).replace(',','')
                cnpj = str(planilha.loc[l,"NUMCGC"])
                if len(valor_imposto) == 1 :
                        valor_imposto = f'{valor_imposto}00'
                elif len(valor_imposto) == 2 :
                        valor_imposto = f'{valor_imposto}0'
                nota_fiscal.append(numero_nota_fiscal)
                list_valor_imposto.append(valor_imposto) 
                list_cnpj.append(cnpj) 
        return nota_fiscal,list_valor_imposto,list_cnpj
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


def enter_fazenda_mg(driver,cnpj):
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
        #input para pausar a aplicação enquanto estou resolvendo o captcha 
        input('resolva o captcha!')
        #preenche com o cnpj da hennings
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[3]/form/div[2]/div[1]/div/div/input').send_keys(cnpj)
        Keys.ENTER
        # clicar no cntinuar
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[3]/form/div[5]/div[1]/div/a[1]').click()
        sleep(3)
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')        


#minas 
def fill_in_information_on_the_website_and_download_pdf_mg(driver,numero_nota_fiscal,valor):
    try:
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
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/fieldset[3]/div[2]/div[2]/div[1]/span[2]/div/input').send_keys(valor)#valor_teste
        Keys.ENTER
        #preenche o Numero da nota fiscal NUMNFV
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/fieldset[4]/div[2]/div[2]/div[1]/span[2]/div/input').send_keys(f'{numero_nota_fiscal}')
        Keys.ENTER
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/fieldset[4]/div[1]/a').click()
        Keys.END
        #clicar em continuar
        sleep(3)
        driver.find_element(By.XPATH, '//*[@id="submit"]').click()
        sleep(3)
        print('passou para outra página')
        #caso já exista um arquivo com esse nome e este path ele exclui 
        if os.path.exists(os.path.expanduser("~")+r'\Downloads\daeonline.pdf'):
            os.remove(path=os.path.expanduser("~")+r'\Downloads\daeonline.pdf')
            print('removeu o arquivo chamado daeonline.pdf')

        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/div[2]/div/a').click()
        sleep(5)
        print('baixou o PDF')
        driver.close()
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


def read_pdf_change_his_name_and_change_his_folder_mg():
    try:
        #apagar arquivos com o nome daeonline.pdf antes de fazer o download
        #o pdf por padrao é baixado nesta pasta com este nome 
        pdf_file = open(os.path.expanduser("~")+r'\Downloads\daeonline.pdf','rb')
        print('abriu o arquivo daeonline.pdf')
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
                nome_arquivo = linha[0:56].replace(' ','').replace('-','')
        pdf_file.close()  
        #altera o nome do pdf para o código de barra, e move ele para uma pasta selecionada      
        os.rename(os.path.expanduser("~")+r'\Downloads\daeonline.pdf',f'C:\\Curso02_github\\atividade_13_GNRE_sao_paulo\\arquivos_mod\\{nome_arquivo}.pdf')
        print(f'trocou a pasta e o renomeou ')
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')      

        
def GNRE_mg():
    try:
        print('robô inicializado!')
        #fecha abas do chrome
        os.system('taskkill /f /im chrome.exe')
        #lê o arquivo excell
        list_notas_fiscais,list_valor,list_cnpj = read_file_excell_mg()
        for l in range(0,2): #a len de 0,2 é só para teste, caso deseje fazer com o tamanho certo é só trocar o campo por esse comentário atrasin range(len(list_notas))
            #o processo abaixo é para abrir e criar o drive de acordo com a nova regra de implantação
            options = webdriver.ChromeOptions()   
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(options=options)
            print(f'executando processo {l+1}')
            enter_fazenda_mg(driver,list_cnpj[l])
            fill_in_information_on_the_website_and_download_pdf_mg(driver,list_notas_fiscais[l],list_valor[l])
            read_pdf_change_his_name_and_change_his_folder_mg()
            print(f'processo {l+1} Finalizado com sucesso')
            sleep(5)
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


if __name__ == "__main__":
    GNRE_mg()
    print('robô finalizado com sucesso!')




