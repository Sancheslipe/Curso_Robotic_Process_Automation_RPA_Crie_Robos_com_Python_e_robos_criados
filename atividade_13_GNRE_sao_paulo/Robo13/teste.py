import os 
import sys
import PyPDF2 as pdf

try:
    #o pdf por padrao é baixado nesta pasta com este nome 
    pdf_file = open('C:\\Users\\Ana Paula\\Downloads\\Dare.pdf','rb')
    #lê os dados do pdf
    print(f'\n\n{pdf_file}\n\n')
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
        print(linha)
        # if 'Linha Digitável:' in linha : 
        #     nome_arquivo = linha[0:56].replace(' ','')
    pdf_file.close()
        #altera o nome do pdf para o código de barra, e move ele para uma pasta selecionada      
    # os.rename('C:\\Users\\Ana Paula\\Downloads\\daeonline.pdf',f'C:\\Curso02_github\\atividade_13_GNRE_sao_paulo\\arquivos_mod\\{nome_arquivo}.pdf')
    # opens the file for reading
except:
    exc_type, error, line = sys.exc_info()
    print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')