from openpyxl.styles import Font
import openpyxl

wb = openpyxl.load_workbook('C:\\Curso02_github\\atividade_06_web_scraping_desafio\\robo\\Dimensao.xlsx')
ws = wb['dados']
ws.column_dimensions['A'].width = 60
ws.column_dimensions['B'].width = 16
ws.column_dimensions['C'].width = 35
ws.column_dimensions['D'].width = 16
My_font = Font(color='FF0000')
for rows in ws.iter_rows(2):
    if rows[3].value != 'ATIVA':
        rows[0].font = My_font
        rows[1].font = My_font
        rows[2].font = My_font
        rows[3].font = My_font
wb.save('Dimensao10.xlsx')
wb.close()