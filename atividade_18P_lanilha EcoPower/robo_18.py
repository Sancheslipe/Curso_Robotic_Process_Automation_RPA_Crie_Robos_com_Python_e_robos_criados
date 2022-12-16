import os
import sys 
from datetime import datetime
import numpy as np
import xlsxwriter
import pandas as pd

def SaveExcelWithFilters(get_file_path, save_file_path, current_file_name, new_file_name, name_sheet, headers_list):
    try:
        # Ler arquivo
        now = datetime.now()
        current_file_name = f'{current_file_name}.xlsx' if '.xlsx' not in current_file_name else current_file_name
        lst_df = pd.read_excel(f'{get_file_path}{current_file_name}', sheet_name=name_sheet, dtype=str)
        lst_df.columns = headers_list
        # Gerar novo arquivo
        new_file_name = f'{new_file_name}.xlsx' if '.xlsx' not in new_file_name else new_file_name
        writer = pd.ExcelWriter(f'{save_file_path}{new_file_name}', engine='xlsxwriter')
        lst_df.to_excel(writer, index=False, sheet_name=name_sheet)
        work_book = writer.book
        work_sheet = writer.sheets[name_sheet]
        # Ajustar headers
        headerformat = work_book.add_format({ 'bold': True, 'text_wrap': True, 'valign': 'top', 'fg_color': '#D7E4BC', 'border': 1})
        for col_num, value in enumerate(lst_df.columns.values):
            work_sheet.write(0, col_num, value, headerformat)
        # Ajustar tamanho
        for column in lst_df:
            column_width = max(lst_df[column].astype(str).map(len).max(), len(column))
            col_idx = lst_df.columns.get_loc(column)
            writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_width)
            work_sheet.autofilter(0, 0, lst_df.shape[0], lst_df.shape[1] -1)
        writer.save()
    except:
        exctp, exc, exctb = sys.exc_info(); fname = os.path.split(exctb.tb_frame.f_code.co_filename)[1]
        error_msg = f'ARQUIVO: {fname}\nERRO: {exc}\nTIPO: {exctp}\nFUNC: {sys._getframe().f_code.co_name}\nLINHA: {exctb.tb_lineno}\n'
        print(error_msg)


def open_excel_extract_informations_and_save_informations():
    
    '''
    INFORMAÇÕES QUE FALTAM NO EXCELL :

    EMAIL DO DESTINATÁRIO
    '''
    try:
        # Verifica quais colunas que deverão ser passadas no Email
        str_enviar_campos = ''
        planilha_LISTA = pd.read_excel('proc\\BASE ENGENHARIA.xlsm',sheet_name='LISTAS')
        planilha_DADOS = pd.read_excel('proc\\BASE ENGENHARIA.xlsm',sheet_name='DADOS')
        # Cria um set(para que os nomes não sejam repetidos) dos nomes dos franqueados 
        set_franquiados = set(planilha_DADOS['FRANQUEADO'].values)
        #transforma o set acima em lista para que possa ser appendido dentro da planilha
        list_franquiados = list(set_franquiados)
        #adiciona a lista de franquiados dentro da planilha
        planilha1 = pd.DataFrame(list_franquiados)
        planilha1.columns = ['NOME FRANQUEADO']
        #adiciona todos os campos (do campo "DESC CAMPO") que na coluna RPA == SIM 
        campos = planilha_LISTA.loc[planilha_LISTA['Unnamed: 4'] == 'SIM',["Unnamed: 3"]]
        planilha1.insert(1,'CAMPOS A SEREM ENVIADOS',pd.DataFrame(campos),allow_duplicates=False)
        array_de_cores = ['','#002060','#002060','#002060','#002060','#002060','#002060','#002060','#002060',
        '#002060','#002060','#FF0000','#FF0000','#FF0000','#FF0000','#757171','#757171','#757171','#00B050',
        '#00B050','#00B050','#00B050','#00B050','#7030A0','#7030A0','#7030A0','#7030A0','#305496','#305496',
                    '#305496','#333F4F','#333F4F','#333F4F','#333F4F','#002060','#002060','#002060']
        planilha1.insert(2,'CORES DOS CAMPOS',pd.DataFrame(array_de_cores),allow_duplicates=True)
        # Salva or arquivo excel
        planilha1.to_excel('proc\\planilha_dados.xlsx',index=False)
        print('salvou os dados com sucesso ')
        # return data

    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


def find_and_store_all_informations():
    # este try eh para receber todos os campos que sao necesaarios
    quantidade_informacoes_FRANQ = []
    try:
        planilha_dados = pd.read_excel('proc\\planilha_dados.xlsx',sheet_name='Sheet1')
        campos_a_serem_enviados = list(planilha_dados["CAMPOS A SEREM ENVIADOS"])
        dados_necessarios = [campo for campo in campos_a_serem_enviados if type(campo) == str]
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')
    # este try eh para que se crie o dicionario com a todas as informacoes
    try:
        for l in range(0,len(dados_necessarios)):
            quantidade_informacoes_FRANQ.append(f'info_{l+1}')
        # dicionario que guarda todas as informacoes
        dict_info_FRANQ = {info :'' for info in quantidade_informacoes_FRANQ}
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')
    #este try eh para abrir o excell
    try:
        planilha_informacoes = pd.read_excel('proc\\BASE ENGENHARIA.xlsm',sheet_name='DADOS')
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')
    # Este try: eh para buscar todas as informacoes dentro da planilha no campo DADOS
    try:
        for l in range(len(dados_necessarios)):
            dict_info_FRANQ[f'info_{l+1}'] = planilha_informacoes.loc[planilha_informacoes['FRANQUEADO']]
            
        print(f'as informações do FRANQUEADO:{nome}')
        for l in range(len(dados_necessarios)):
            print(dados_necessarios[l])
            print(dict_info_FRANQ[f'info_{l+1}'])
            
    except:    
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


def bot_18():
    # Esta funcao verifica quais dados deverao ser passados para quem 
    try:
        open_excel_extract_informations_and_save_informations()
        # Esta funcao eh para deixar o excel mais legivel
        path = 'C:\\Curso02_github\\atividade_18P_lanilha EcoPower\\proc\\'
        headers_list = ['NOME FRANQUEADO', 'CAMPOS A SEREM ENVIADOS','CORES DOS CAMPOS']
        SaveExcelWithFilters(path, path, 'planilha_dados.xlsx', 'planilha_dados.xlsx', 'Sheet1', headers_list)
        find_and_store_all_informations()
        
    
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')
        


if (__name__ == '__main__'):
    try: 
        os.system('cls')
        
        bot_18()

    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')
