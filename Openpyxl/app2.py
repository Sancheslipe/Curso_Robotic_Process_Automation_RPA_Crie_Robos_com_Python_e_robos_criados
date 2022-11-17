import openpyxl
#carregando arquivo
book = openpyxl.load_workbook('Planilha de compras.xlsx')
#selecionando uma página
frutas_page = book['Frutas']
#imprimindo os dados de cada linha
for rows in frutas_page.iter_rows(min_row=2,max_row=5):
    for cell in rows:
        if cell.value == 'banana':
            cell.value = 'fruta1'
    #para printar formatado 
    # print(f'{rows[0].value},{rows[1].value},{rows[2].value}')
    #imprimir linha por linha
    # for cell in rows:
    #     print(cell.value)
book.save('Planilha de compras v2.xlsx')