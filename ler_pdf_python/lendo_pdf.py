# import PyPDF2 as pdf
# #abrindo arquivo binário
# pdf_file = open('C:\\Users\\Ana Paula\\Downloads\\daeonline (4).pdf','rb')
# #pegando os dados do pdf binário
# dados_do_pdf = pdf.PdfFileReader(pdf_file)
# # print(dados_do_pdf.isEncrypted)
# # print(dados_do_pdf.numPages)

# pagina1 = dados_do_pdf.getPage(0)


# texto_da_pagina1 = pagina1.extract_text()

# list_test = texto_da_pagina1.split('\n')

# for linha in list_test:
#     print(f'{linha}\n')

#     if  'Linha Digitável' == linha: 
#         print(f'{list_test}\n')

teste = '85640000000 1 50550213221 8 20112970096 3 07492100119 9'

print(teste)
print(len(teste)-7)