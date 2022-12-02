import os
import sys
import pandas as pd
# import PyPDF2 as pdf
from time import sleep
from keyboard import write
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#são Paulo

def inicio_sao_paulo(ref,valor):
    try:
        os.system('taskkill /f /im chrome.exe')
        #o processo abaixo é para abrir e criar o drive de acordo com a nova regra de implantação
        options = webdriver.ChromeOptions()   
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
        #def entrar no site sao paulo
        driver.get('https://www4.fazenda.sp.gov.br/DareICMS/DareAvulso')
        driver.maximize_window()
        #escolher cnpj
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/main/div[5]/fieldset[1]/div/select').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/main/div[5]/fieldset[1]/div/select/option[1]').click()
        sleep(1)
        #escrever cnpj 
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/main/div[5]/fieldset[1]/div/input[1]').send_keys('83748772000800')
        sleep(1)
        #clicar no recaptcha
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/main/div[5]/div[1]/div/div/iframe').click()
        input('resolva o captcha')
        sleep(3)
        #clicar consultar
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/main/div[5]/fieldset[1]/div/button/i').click()
        sleep(1)
        #escolher operacao 
        sleep(5)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/main/div[5]/fieldset[5]/div/div[1]/select').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/main/div[5]/fieldset[5]/div/div[1]/select/option[3]').click()
        sleep(1)
        #preencher referencia 
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/main/div[5]/fieldset[5]/div/div[2]/input').send_keys(ref)
        #preencher data de vencimento
        sleep(2)
        data = datetime.now().strftime('%d/%m/%Y')
        
        driver.find_element(By.XPATH, '//*[@id="txtVencimento"]').send_keys(data)
        sleep(2)
        #preenche o valor do imposto      
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/main/div[5]/fieldset[5]/div/div[8]/input').send_keys(valor)
        sleep(1)
        #clicando em calcular 
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/main/div[5]/fieldset[5]/div/div[8]/button').click()
        sleep(1)
        #clicando em gerar DARE
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/main/div[5]/fieldset[5]/div/div[11]/button').click()
        print('chegou ao final ')
        sleep(15)
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')



def abrir_excel_sp():
        """
        CAMPOS QUE SÃO TIRADOS DO XLSX:
        REFERÊNCIA/COMPETENCIA == DATENT (NOME REFERENTE Á COLUNA DO ARQUIVO)
        Data de Vencimento do Imposto == DATPPT (NOME REFERENTE Á COLUNA DO ARQUIVO)
        Valor do Imposto: == VLRORI (NOME REFERENTE Á COLUNA DO ARQUIVO)
        """
        
        try:
            #array que guarda todas as notas fiscais 
            list_referencia = []
            list_data_vencimento = []
            list_valor_imposto = []
            #lê a planilha na aba Select e501tcp
            planilha = pd.read_excel(r'C:\Curso02_github\atividade_13_GNRE_sao_paulo\Notas_heinigs\DadosNotas.xlsx',sheet_name='Select e501tcp')
            #passa por toda a planilha
            for l in range(len(planilha)):
                #apende o numero da nota fiscal somente se ele no campo da região de atuacao eh igual a MG
                if planilha.loc[l,"SIGUFS"] == 'SP':
                    referencia = f'{str(planilha.loc[l,"DATENT"])[5:7]}{str(planilha.loc[l,"DATENT"])[0:4]}'
                    valor_imposto = str(planilha.loc[l,"VLRORI"]).replace('.','')
                    if len(valor_imposto) == 1 :
                        valor_imposto = f'{valor_imposto}00'
                    elif len(valor_imposto) == 2 :
                        valor_imposto = f'{valor_imposto}0'
                    
                    list_referencia.append(referencia)
                    list_valor_imposto.append(valor_imposto)
                
                
            return list_referencia,list_valor_imposto   
        except:
            exc_type, error, line = sys.exc_info()
            print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


if __name__ == "__main__":
    list_ref,list_valor = abrir_excel_sp()
    # print(list_ref,list_data,list_valor)
    for l in range(len(list_ref)):    
    # inicio_sao_paulo()
        print(list_ref[l],list_valor[l])
        print(l)
        inicio_sao_paulo(list_ref[l],list_valor[l])

    
    print('robô finalizado com sucesso!')

