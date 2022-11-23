import PyPDF2 as pdf
#abrindo arquivo binário
pdf_file = open('C:\\Users\\Ana Paula\\Downloads\\teste_pdf.pdf','rb')
#pegando os dados do pdf binário
dados_do_pdf = pdf.PdfFileReader(pdf_file)
print(dados_do_pdf.isEncrypted)
print(dados_do_pdf.numPages)

pagina1 = dados_do_pdf.getPage(0)


texto_da_pagina1 = pagina1.extract_text()

list_test = texto_da_pagina1.split('\n')

for l in range(len(list_test)):
    print(list_test[l])