# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from time import sleep
# options = webdriver.ChromeOptions()   
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)

# driver.get('https://www.google.com/recaptcha/api2/demo')
# sleep(5)
# imagem_captcha = driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div/table/tbody')
# sleep(2)
# imagem_captcha.screenshot(r'C:\Curso02_github\captchas\captcha1.png')
# import os 
# import fitz
# import sys 

# try:
#     #caso nao inicie a variavel, acontece alguns problemas
#     data = ''
#     #abre o pdf
#     with fitz.open(os.path.expanduser("~")+r'\Downloads\Dare.pdf') as pdf:
#         print('abriu o arquivo Dare.pdf')
#     # with fitz.open('C:\\Users\\Ana Paula\\Downloads\\Dare.pdf') as pdf:
#         #percorre todas as informacoes do arquivo pdf e armazena em um string
#         for pagina in pdf:
#             data += pagina.get_text()
#     #transforma aquele arquivo em uma lista na qual cada elemento corresponde a uma linha 
#     list_info = data.split('\n')
#     #percorre todos os elementos do array:
#     for info in range(len(list_info)):
#         # print(list_info[info])
#         #caso o campo for igual a string abaixo and 
#         # a len do proximo elemento do array for 56 and 
#         # o proximo elemento.replace('-','').replace(' ','').isdigit() este elemento é o codigo de barras
#         if (len(list_info[info]) == 56) and (list_info[info].replace('-','').replace(' ','').isdigit()):
#             nome_arquivo = list_info[info].replace('-','').replace(' ','')
    
#     print(nome_arquivo)
    
#     # print(f'nome 02 {nome_arquivo}')
#     # # renomeamos o arquivo e trocamos ele de pasta para ficar mais organizado 
#     # print('o path ','\n\n', os.path.exists(r"C:\Users\Ana Paula\Downloads\Dare.pdf"),'\n\n')
#     # os.rename(r'C:\Users\Ana Paula\Downloads\Dare.pdf',f'C:\\Curso02_github\\atividade_13_GNRE_sao_paulo\\arquivos_mod_sp\\{nome_arquivo}.pdf')
#     # print(f'trocou a pasta e renomeou ele ')
# except:
#         exc_type, error, line = sys.exc_info()
#         print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')
import os 
import sys 
import PyPDF2 as pdf
try:
    #apagar arquivos com o nome daeonline.pdf antes de fazer o download
    #o pdf por padrao é baixado nesta pasta com este nome 
    # pdf_file = open('C:\\Users\\Ana Paula\\Downloads\\daeonline.pdf','rb')
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