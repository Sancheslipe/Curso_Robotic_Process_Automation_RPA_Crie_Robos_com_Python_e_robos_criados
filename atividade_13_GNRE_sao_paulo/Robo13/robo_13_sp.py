import os
import sys
import fitz
import pandas as pd
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

#GNRE SAO PAULO

def read_file_excell_sp():
        """
        CAMPOS QUE SÃO TIRADOS DO XLSX:
        REFERÊNCIA/COMPETENCIA == DATENT (NOME REFERENTE Á COLUNA DO ARQUIVO)
        Data de Vencimento do Imposto == data de hoje 
        Valor do Imposto: == VLRORI (NOME REFERENTE Á COLUNA DO ARQUIVO)
        """
        try:
            #array que guarda todas as notas fiscais 
            list_referencia = []
            list_valor_imposto = []
            #lê a planilha na aba Select e501tcp
            planilha = pd.read_excel(r'C:\Curso02_github\atividade_13_GNRE_sao_paulo\Notas_heinigs\DadosNotas.xlsx',sheet_name='Select e501tcp')
            #passa por toda a planilha
            for l in range(len(planilha)):
                #apende o numero da nota fiscal somente se ele no campo da região de atuacao eh igual a MG
                if planilha.loc[l,"SIGUFS"] == 'SP':
                    #as variaveis abaixo recebem as informacoes desejadas
                    referencia = f'{str(planilha.loc[l,"DATENT"])[5:7]}{str(planilha.loc[l,"DATENT"])[0:4]}'
                    valor_imposto = str(planilha.loc[l,"VLRORI"]).replace(',','')
                    #ajusta o formato de valor_imposto para que fique de acordo com o padrao do site
                    if len(valor_imposto) == 1 :
                        valor_imposto = f'{valor_imposto}00'
                    elif len(valor_imposto) == 2 :
                        valor_imposto = f'{valor_imposto}0'
                    list_referencia.append(referencia)
                    list_valor_imposto.append(valor_imposto)
            #retorna todas as listas com as informacoes, sendo cada index referente a um cliente (o index 0 retorna as informacoes do cliente 0 e assim por diante)
            return list_referencia,list_valor_imposto   
        except:
            exc_type, error, line = sys.exc_info()
            print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


def enter_fazenda_sp(driver):
    try:
        #entra no site e maximiza a tela
        driver.get('https://www4.fazenda.sp.gov.br/DareICMS/DareAvulso')
        driver.maximize_window()
        #seleciona o campo cnpj
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/main/div[5]/fieldset[1]/div/select').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/main/div[5]/fieldset[1]/div/select/option[1]').click()
        sleep(1)
        #escrever o cnpj no campo
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/main/div[5]/fieldset[1]/div/input[1]').send_keys('83748772000800')
        sleep(1)
        #clicar no recaptcha
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/main/div[5]/div[1]/div/div/iframe').click()
        #espera até que o humano resolva o captcha
        input('resolva o captcha')
        sleep(3)
        #clicar consultar == abre todos os campos abaixo
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/main/div[5]/fieldset[1]/div/button/i').click()
        sleep(3)
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


def fill_in_information_on_the_website_and_download_pdf_sp(driver,ref,valor):
    try:
        #escolhe o tipo de débito
        sleep(3)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/main/div[5]/fieldset[5]/div/div[1]/select').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/main/div[5]/fieldset[5]/div/div[1]/select/option[3]').click()
        sleep(1)
        #prencher o campo referencia 
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/main/div[5]/fieldset[5]/div/div[2]/input').send_keys(ref)
        #preencher o campo data de vencimento
        sleep(2)
        data = datetime.now().strftime('%d/%m/%Y')
        driver.find_element(By.XPATH, '//*[@id="txtVencimento"]').send_keys(data)
        sleep(2)
        #preenche o campo valor do imposto      
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/main/div[5]/fieldset[5]/div/div[8]/input').send_keys(valor)
        sleep(1)
        #clica no botao em calcular 
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/main/div[5]/fieldset[5]/div/div[8]/button').click()
        sleep(1)
        #clica no botao em gerar DARE
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/main/div[5]/fieldset[5]/div/div[11]/button').click()
        #caso apareça o Pop up ele fecha 
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            #printa a mensagem escrita dentro do pop up
            print('mensagem:', alert_text)
            # validate the alert text
            alert.accept()
        except Exception as e:
            msgAlert = str(format(e))
            print('Erro', msgAlert)
            pass  
        sleep(5)
        print('baixou o PDF')
        sleep(2)
        driver.close()
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


def read_pdf_change_his_name_and_change_his_folder_sp():
    try:
        #caso nao inicie a variavel, acontece alguns problemas
        data = ''
        #abre o pdf
        print('abriu o arquivo Dare.pdf')
        with fitz.open('C:\\Users\\Ana Paula\\Downloads\\Dare.pdf') as pdf:
            #percorre todas as informacoes do arquivo pdf e armazena em um string
            for pagina in pdf:
                data += pagina.get_text()
        #transforma aquele arquivo em uma lista na qual cada elemento corresponde a uma linha 
        list_info = data.split('\n')
        #percorre todos os elementos do array:
        for info in range(len(list_info)):
            #caso o campo for igual a string abaixo and 
            # a len do proximo elemento do array for 56 and 
            # o proximo elemento.replace('-','').replace(' ','').isdigit() este elemento é o codigo de barras
            if ('Documento de Arrecadação de Receitas Estaduais' == list_info[info]) and (len(list_info[info+1]) == 56) and (list_info[info+1].replace('-','').replace(' ','').isdigit()):
                nome_arquivo = list_info[info+1].replace('-','').replace(' ','')
        #renomeamos o arquivo e trocamos ele de pasta para ficar mais organizado 
        os.rename(f'C:\\Users\\Ana Paula\\Downloads\\Dare.pdf',f'C:\\Curso02_github\\atividade_13_GNRE_sao_paulo\\arquivos_mod_sp\\{nome_arquivo}.pdf')
        print(f'trocou a pasta e renomeou ele ')
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


def GNRE_sp():
    try:
        print('robô inicializado!')
        #verifica se possui alguma guia do chrome aberta e "puxa elas da tomada"
        os.system('taskkill /f /im chrome.exe')
        #o processo abaixo é para abrir e criar o drive de acordo com a nova regra de implantação
        list_ref,list_valor = read_file_excell_sp()
        for l in range(len(list_ref)):    
            options = webdriver.ChromeOptions()   
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(options=options)
            print(f'executando processo {l+1}')
            enter_fazenda_sp(driver)
            fill_in_information_on_the_website_and_download_pdf_sp(driver,list_ref[l],list_valor[l])
            read_pdf_change_his_name_and_change_his_folder_sp()
            print(f'processo {l+1} Finalizado com sucesso')
            sleep(5)
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


if __name__ == "__main__":
    GNRE_sp()
    print('robô finalizado com sucesso!')


