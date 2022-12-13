# -*- coding: utf-8 -*-
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from APRCustomExceptions import DataBaseConnectionError
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta, date
from selenium.webdriver.common.by import By
from winotify import Notification, audio
from selenium import webdriver
from termcolor import colored
import APRTechGeneral as apr
from calendar import mdays
import pyautogui as p
import pandas as pd
import subprocess
import traceback
import openpyxl
import calendar
import locale
import pyodbc
import shutil
import time
import json
import sys
import re
import os


def download_report_and_check_pro(p_ativ, driver, path_pro, path_out, msg_json):
    try:
        found = False
        download = False
        try:
            if os.listdir(path_pro):
                print(f'pro = {os.listdir(path_pro)}')
                try:
                    # Tentar com 2 possiveis sheet names
                    try:
                        nexti_report_xls = pd.read_excel(f'{path_pro}{os.listdir(path_pro)[0]}', sheet_name='Sheet1', dtype=str)
                    except:
                        nexti_report_xls = pd.read_excel(f'{path_pro}{os.listdir(path_pro)[0]}', sheet_name='Page 1', dtype=str)

                    # Verificar se existe algum NOK para processar
                    reg_lst = nexti_report_xls['Registro processamento'].values.tolist()
                    print(f'opened file {os.listdir(path_pro)[0]}')
                    for value in reg_lst:
                        if value == 'NOK':
                            found = True
                            print(colored(f'WARNING:file {os.listdir(path_pro)[0]} has NOK! Processing this file is necessary', 'yellow'))
                            download = True
                            break

                    if not found:
                        print(colored(f'INFO:NOK not found in {os.listdir(path_pro)[0]}', 'green'))
                        shutil.move(f'{path_pro}{os.listdir(path_pro)[0]}', f'{path_out}{os.listdir(path_pro)[0]}')
                        print(f'file {os.listdir(path_pro)[0]} moved to out')
                except:
                    exc_type, error, exc_tb = sys.exc_info()
                    print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE: {exc_tb.tb_lineno}\n')

            # Se nao tiver NOK baixar outro relatorio
            if not found:
                go_to_buttom = 0
                buttom_download = False
                download_counter = 0
                downloaded_file = False
                while downloaded_file == False and download_counter < 5:
                    print('downloading new excel')
                    try:
                        download_counter += 1
                        # Menu lateral - Relatorios   
                        while go_to_buttom < 5:
                            go_to_buttom += 1
                            side_menu = False
                            for attempt in range(30):                          
                                try:                                    
                                    driver.find_element('xpath', '/html/body/core-main/div/div[1]/div[1]/div[2]/div/nexti-left-menu/nav/ul/li[11]/a').click() 
                                    side_menu = True
                                    break
                                except:
                                    p.sleep(1)

                            # Opcao - Marcacao de pontos
                            if side_menu:
                                option = False
                                for attempt in range(30):
                                    try:
                                        driver.find_element('xpath', '/html/body/core-main/div/div[1]/div[1]/div[2]/div/nexti-left-menu/nav/ul/li[11]/ul/li[10]/a').click()  
                                        option = True
                                        break
                                    except:
                                        p.sleep(1)

                                # Opcao - Inconsistencias
                                if option:
                                    inconsistencies = False
                                    for attempt in range(30):
                                        try:
                                            driver.find_element('xpath', '/html/body/core-main/div/div[2]/div[2]/div[1]/div[9]/div').click() 
                                            inconsistencies = True
                                            break
                                        except:
                                            p.sleep(1)

                                    # Opcao - Marcacoes nao tratadas
                                    if inconsistencies:
                                        marks = False
                                        for attempt in range(30):
                                            try:
                                                driver.find_element('xpath', '/html/body/core-main/div/reportfilter/div/div/div[2]/div/div[1]/div[1]/div/div[5]/div[7]/div/div/div/label').click()  
                                                marks = True
                                                break
                                            except:
                                                p.sleep(1)

                                        # Campo para primeira data                                                          
                                        if marks:
                                            now = datetime.now()
                                            today = now.strftime("%d/%m/%Y")
                                            first_date = False
                                            for attempt in range(30):
                                                try:
                                                    driver.find_element('xpath', '/html/body/core-main/div/reportfilter/div/div/div[2]/div/div[1]/div[1]/div/div[6]/div[1]/datepicker/p/input').click()  
                                                    p.sleep(1)
                                                    p.typewrite(f'{today}')
                                                    first_date = True
                                                    break
                                                except:
                                                    p.sleep(1)

                                            # Campo para segunda data
                                            if first_date:
                                                second_date = False
                                                for attempt in range(30):
                                                    try:
                                                        driver.find_element('xpath', '/html/body/core-main/div/reportfilter/div/div/div[2]/div/div[1]/div[1]/div/div[6]/div[2]/datepicker/p/input').send_keys(f'{today}')    
                                                        second_date = True
                                                        print('informed dates')
                                                        p.sleep(1)
                                                        break
                                                    except:
                                                        p.sleep(1)

                                                # Campo empresa: pois quando a segunda data for informada aparece um calendario por cima do botao
                                                # para baixar o excel, impedindo o robo de clicar no botao
                                                if second_date:
                                                    company_placeholder = False
                                                    for attempt in range(30):
                                                        try:
                                                            driver.find_element('xpath', '/html/body/core-main/div/reportfilter/div/div/div[2]/div/div[1]/div[1]/div/div[1]/div[1]/autocomplete/div/div/input').click()    
                                                            company_placeholder = True
                                                            p.sleep(2)
                                                            break
                                                        except:
                                                            p.sleep(1)

                                                    # Botao para baixar excel
                                                    if company_placeholder:
                                                        for attempt in range(30):
                                                            try:
                                                                driver.find_element('xpath', '/html/body/core-main/div/reportfilter/div/div/div[2]/div/div[1]/div[4]/div[2]/a[2]').click()     
                                                                print('clicked on download buttom')
                                                                buttom_download = True
                                                                go_to_buttom = 6
                                                                break
                                                            except:
                                                                p.sleep(1)

                        # Aguardar download e mover arquivo para pro
                        if buttom_download:
                            p.sleep(25)
                            check_download = 0
                            while check_download < 10:
                                try:
                                    pro_files = os.listdir(path_pro)
                                    if pro_files:
                                        downloaded_file = True
                                        check_download = 11
                                        print(f'pro = {pro_files}')
                                    else:
                                        print(f'checking downloads in pro: {pro_files}')
                                        p.sleep(5)
                                        check_download += 1
                                except:
                                    check_download += 1
                                    exc_type, error, exc_tb = sys.exc_info()
                                    print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE: {exc_tb.tb_lineno}\n')
                                    p.sleep(5)
                        else:
                            raise RuntimeError('Download buttom not found')
                    except:
                        driver.refresh()
                        exc_type, error, exc_tb = sys.exc_info()
                        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE: {exc_tb.tb_lineno}\n')

                # adicionar colunas para monitoramento do processo
                pro_files_lst = os.listdir(path_pro)
                if len(pro_files_lst) == 1:
                    nexti_report_xls = pd.read_excel(f'{path_pro}{pro_files_lst[0]}', sheet_name='Page 1', dtype=str)
                    if 'Registro processamento' not in nexti_report_xls.columns:  
                        nexti_report_xls['Registro processamento'] = 'NOK'
                        print('added column "registro processamento"')
                    if 'Situacao' not in nexti_report_xls.columns:
                        nexti_report_xls['Situacao'] = 'VAZIO'
                        print('added column "situacao"')
                    nexti_report_xls.to_excel(f'{path_pro}troca_escalas.xlsx', index=False)
                    download = True

                    # Remover arquivo baixado e deixar apenas arquivo que foi ajustado
                    pro_lst = os.listdir(path_pro)
                    if len(pro_lst) > 1:
                        for file in pro_lst:
                            if 'troca_escalas' not in file:
                                os.remove(f'{path_pro}{file}')
                                print(colored(f'WARNING:removed {file} from pro', 'yellow'))
                    else:
                        raise FileNotFoundError('No files found in pro')
                else:
                    raise FileNotFoundError(f'files in pro = {pro_files_lst}')
        except:
            exc_type, error, exc_tb = sys.exc_info()
            error_msg = f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE: {exc_tb.tb_lineno}\n'
            p.alert(p_ativ, msg_json['err'], msg_json['dest_apr'], 'ATIV006 ERROR', error_msg)
            # apr.SendEmailWithScreenshot(p_ativ, msg_json['err'], msg_json['dest_apr'], 'ATIV006 ERROR', error_msg)
            print(colored(error_msg, 'red'))

        return download
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')

def replace_shift(driver, p_ativ, msg_json, ajusted, shift_found):
    try:
        print(colored('\nINFO:replacing shift', 'green'))
        # Mudar shift
        find_shif_menu = 0
        while find_shif_menu < 150:
            find_shif_menu += 1
            try:
                # menu historico de troca de posto escala
                driver.find_element('xpath', '/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[2]/div[1]/ul/li[7]/a/i').click()
                print('found menu')  
                p.sleep(2)                   
                find_shif_menu = 150
                add_shift = 0
                while add_shift < 80:
                    add_shift += 1
                    try:
                        # Botao para adicionar escala
                        driver.find_element('xpath', '/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/span').click() 
                        add_shift = 80
                        click_option = 0
                        while click_option < 30:
                            click_option += 1
                            try:  
                                # Mostrar opcoes de troca
                                driver.find_element('xpath', '/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/div/div/select').click()
                                p.sleep(2)
                                click_option = 30
                                opt = 0
                                option = 0
                                # Preencher campos
                                while opt < 8:  
                                    opt += 1
                                    option += 1
                                    if option == 5:
                                        option = 1
                                    try:
                                        var_option = driver.find_element('xpath', f'/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/div/div[1]/select/option[{option}]').text
                                        var_option = str(var_option)
                                        if 'Troca de escala' in var_option:
                                            opt = 8
                                            print(f'found {var_option}')
                                            # Clicar em opcao Troca de escala
                                            driver.find_element('xpath', f'/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/div/div/select/option[{option}]').click()
                                            p.sleep(0.3)
                                            driver.find_element('xpath', '/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/div/div/select').click()
                                            p.sleep(0.3)
                                            # Informar nova escala
                                            for keys_sent in range(20):  
                                                try:
                                                    driver.find_element('xpath', f'/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/div/div[2]/autocomplete/div/div/input').clear()
                                                    driver.find_element('xpath', f'/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/div/div[2]/autocomplete/div/div/input').send_keys(f'{shift_found}')
                                                    p.sleep(2)
                                                    break
                                                except:
                                                    p.sleep(1)
                                            # Selecionar escala nova
                                            for click in range(20):  
                                                try:
                                                    driver.find_element('xpath', '/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[3]/div/div[2]/autocomplete/div/div/div[2]').click()
                                                    p.sleep(2)
                                                    break
                                                except:
                                                    try:
                                                        driver.find_element('xpath', '/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/div/div[2]/autocomplete/div/div/div[2]').click()
                                                        p.sleep(2)
                                                        break
                                                    except:
                                                        try:
                                                            driver.find_element('xpath', '/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/div/div[2]/autocomplete/div/div/div').click()
                                                            p.sleep(2)
                                                            break
                                                        except:
                                                            p.sleep(1)
                                            # Buscar campo observacao
                                            obs_cleared = False
                                            for attempt in range(20):  
                                                try:                                
                                                    driver.find_element('xpath', f'/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/div/div[5]/div/textarea').clear()
                                                    obs_cleared = True
                                                    break
                                                except:
                                                    try:
                                                        driver.find_element('xpath', f'/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/div/div[7]/div/textarea').clear()
                                                        obs_cleared = True
                                                        break
                                                    except:
                                                        p.sleep(1)
                                            # Informar observacao
                                            if obs_cleared: 
                                                try:
                                                    driver.find_element('xpath', f'/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/div/div[5]/div/textarea').send_keys(msg_json['obs'])
                                                    p.sleep(0.5)
                                                except:
                                                    driver.find_element('xpath', f'/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/div/div[7]/div/textarea').send_keys(msg_json['obs'])
                                                    p.sleep(0.5)

                                                ajusted = True
                                                situation = f' - AJUSTOU PARA ESCALA -> {shift_found}'
                                                driver.find_element('xpath', '/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/div/div[8]').click()
                                                print(colored(f'INFO:Changed to -> {shift_found} successfully!', 'green'))
                                    except:
                                        p.sleep(1)
                                        exc_type, error, exc_tb = sys.exc_info()
                                        print(colored(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE: {exc_tb.tb_lineno}\n', 'red'))
                            except:
                                p.sleep(1)
                    except:
                        p.sleep(1)
            except:
                p.sleep(1)

        return ajusted, situation
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


def ajust_shift(driver, shift, msg_json, arrow_clicks, xpath_arrow, xpath_worker, mat, esc, p_ativ, db_shifts):
    try:
        # Ajustar escalas
        today = datetime.today() 
        yesterday = today - timedelta(days=1)
        yesterday = yesterday.day
        ajusted = False
        shift_limit = ''
        situation = ' - ERRO AO REALIZAR AJUSTE'
        print(colored(f'\nINFO:initiating ajustment', 'green'))
        try:
            # Menu marcacao de ponto
            passed = False
            for click in range(200):
                try:
                    driver.find_element('xpath', '/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[2]/div[1]/ul/li[2]/a/i').click()
                    p.sleep(1)
                    passed = True
                    break                         
                except:
                    p.sleep(2)

            if passed:
                try:
                    # Esperar carregar 
                    loaded = False
                    first_day = ''
                    for extraction in range(200):   
                        try:
                            first_day = driver.find_element('xpath', f'/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]').text
                            p.sleep(0.5)
                            loaded = True
                            break
                        except:
                            p.sleep(0.5)
                    
                    if loaded:
                        # Verificar em qual mes clicar no site
                        first_day = first_day.split(' ')
                        first_day = first_day[0]
                        today = datetime.now()
                        month_to_click = today.strftime('%B')
                        month_to_click = month_to_click.upper()
                        if '16' in str(first_day) and yesterday >= 16:
                            next_month_of_today = today + timedelta(mdays[today.month])
                            month_to_click = next_month_of_today.strftime("%B")
                            month_to_click = month_to_click.upper()
                        elif '21' in str(first_day) and yesterday >= 21:
                            next_month_of_today = today + timedelta(mdays[today.month])
                            month_to_click = next_month_of_today.strftime("%B")
                            month_to_click = month_to_click.upper()
                        elif '01' in str(first_day):
                            month_to_click = month_to_click.upper()
                        
                        # Selecionar mes
                        selected_month = False
                        driver.find_element('xpath', '/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[2]/div[2]/div/div[1]/span/div[2]/button[2]/span').click() 
                        print(f'yesterday = {yesterday}\nmonth = {month_to_click}')
                        p.sleep(3)
                        for li in range(1, 13):
                            try:
                                month = driver.find_element('xpath', f'/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[2]/div[2]/div/div[1]/span/div[2]/ul/li[{li}]').text
                                if str(msg_json['months_pt'][f'{month_to_click}']) in str(month):
                                    print(f'found = {msg_json["months_pt"][f"{month_to_click}"]} in {month}')
                                    driver.find_element('xpath', f'/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[2]/div[2]/div/div[1]/span/div[2]/ul/li[{li}]').click()
                                    print(f'clicked on {month}')
                                    p.sleep(1)
                                    selected_month = True
                                    break
                            except:
                                print('searching for month')

                        if selected_month:
                            div = 0
                            # Esperar carregar 
                            for loading in range(150):
                                print('loading')
                                div = 1 if div == 32 else div + 1
                                try:
                                    driver.find_element('xpath', f'/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[{div}]')
                                    p.sleep(3.5)
                                    print('loaded')
                                    break
                                except:
                                    p.sleep(1)
                            
                            # Verificar todas as horas para extrair as do dia
                            for date_time in range(1, 32):
                                try:
                                    # Extrair horas
                                    dt = driver.find_element('xpath', f'/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[{date_time}]').text  
                                    yesterday_for_comparison = f'0{yesterday}' if len(str(yesterday)) == 1 else str(yesterday)

                                    # Filtrar horas
                                    if str(yesterday_for_comparison) == str(dt[:2]):
                                        hours = []
                                        date_hours = dt.split(' ')
                                        date_hours = list(filter(None, date_hours))
                                        full_shift = esc
                                        esc = esc.split(' ')
                                        esc = list(filter(None, esc))
                                        for hour in date_hours:
                                            if (len(hour) == 5) and (str(hour[0]) in '0123456789') and (str(hour[4]) in '0123456789'):
                                                hours.append(hour)

                                        # Separar horas web
                                        new_shift_temp = []
                                        print(f'found {len(hours)} hours on {yesterday}-{month_to_click}-{today.year}\nhours {hours}')
                                        if hours != [] and len(hours) == 4:
                                            try:
                                                # Separar e arredondar horas em lista para gerar escala nova
                                                for web_hour in hours:  
                                                    h = datetime.strptime(web_hour, '%H:%M').time()
                                                    new_hour = str(h.hour)
                                                    if len(new_hour) == 1:
                                                        new_hour = f'0{new_hour}'
                                                    if h.minute >= 0 and h.minute <= 15:
                                                        new_shift_temp.append(f'{new_hour}00')
                                                    elif h.minute > 15 and h.minute <= 45:
                                                        new_shift_temp.append(f'{new_hour}30')
                                                    elif h.minute > 45:
                                                        new_hour = f'{h.hour + 1}'
                                                        if len(new_hour) == 1:
                                                            new_hour = f'0{new_hour}'
                                                        new_shift_temp.append(f'{new_hour}00')

                                                # Gerar nova escala e separar escala web
                                                new_shift_string = ''
                                                for index in range(len(new_shift_temp)):
                                                    value = str(new_shift_temp[index])
                                                    if index == 0 or index == 2:
                                                        new_shift_string = new_shift_string + value + '-'
                                                    elif index == 1:
                                                        new_shift_string = new_shift_string + value + '/'
                                                    else:
                                                        new_shift_string = new_shift_string + value
                                                
                                                new_shift_string = new_shift_string.strip(' ')
                                                state_exists = False 
                                                shift_string = ''
                                                days_of_week = ''
                                                state = ''
                                                # Ajustar nova escala
                                                for value in esc:
                                                    # Valor com as horas da escala como string
                                                    if len(value) > 15 and ('/' in value or '-' in value):
                                                        shift_string = str(value)
                                                    # Verificar se tem sigla estadual
                                                    # OBS: Todos os estados possuem siglas menos Santa Catarina
                                                    elif len(value) == 2 and str(value.upper()) in msg_json['states']:
                                                            state_exists = True
                                                            state = value

                                                shift_string = shift_string.strip(' ')
                                                shift_found = ''
                                                valid_shif = False
                                                print(f'full shift from web = {full_shift}')
                                                print(f'STATE => {state}') if state_exists else print('NO STATE FOUND')
                                                
                                                # Verificar se escala consta como de segunda a sexta
                                                valid_week = False
                                                for week_shift in msg_json["mon_fri_valid"]:
                                                    if week_shift in full_shift:
                                                        print(colored(f'INFO:FOUND {week_shift} in {full_shift}', 'green'))
                                                        valid_week = True
                                                        break
                                                    
                                                if valid_week:
                                                    # Se escala web nao bater com escala robo chamar funcao para buscar escala nova no site
                                                    if new_shift_string == shift_string:
                                                        print(colored(f'INFO:WEB -> {shift_string} == BOT -> {new_shift_string}', 'green'))
                                                        ajusted = True
                                                        situation = ' - ESCALA WEB IGUAL ESCALA EXCEL'
                                                    # Verificar carga horario e se escala existe
                                                    else:
                                                        # shift_for_search = f'{new_shift_string} {days_of_week}'
                                                        shift_for_search = f'{new_shift_string}'
                                                        print(colored(f'WARNING:WEB -> {shift_string} != BOT -> {new_shift_string}', 'yellow'))
                                                        print(f'search = {shift_for_search}')
                                                        valid_shif, situation, shift_found, shift_limit = verify_shift(p_ativ, driver, shift_for_search, arrow_clicks, xpath_arrow, xpath_worker, mat, state_exists, msg_json, state)
                                                else:
                                                    print(colored('WARNING:No shift from Monday to Friday found!', 'yellow'))
                                                    ajusted = True
                                                    situation = ' - NAO CONSTA COMO ESCALA DE SEGUNDA A SEXTA'
                                                
                                                # Mudar escala
                                                if valid_shif == True and 'VALIDA' in situation:
                                                    ajusted, situation = replace_shift(driver, p_ativ, msg_json, ajusted, shift_found)
                                            except:
                                                exc_type, error, exc_tb = sys.exc_info()
                                                error_msg = f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE: {exc_tb.tb_lineno}\n'
                                                p.alert(p_ativ, msg_json['err'], msg_json['dest_apr'], 'ATIV006 ERROR', error_msg)
                                                # apr.SendEmailWithScreenshot(p_ativ, msg_json['err'], msg_json['dest_apr'], 'ATIV006 ERROR', error_msg)
                                                print(colored(error_msg, 'red'))
                                        else:
                                            ajusted = True
                                            situation = f' - ACHOU {len(hours)} HORA(S) NO DIA {yesterday} DE {month_to_click}'
                                            print(colored('WARNING:4 hours necessary for new shift!', 'yellow'))
                                        break
                                except:
                                    print('searching for hours')
                                    p.sleep(1)
                        else:
                            print(colored(f'WARNING:month {month_to_click} not found in web!', 'yellow'))
                except:
                    exc_type, error, exc_tb = sys.exc_info()
                    error_msg = f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE: {exc_tb.tb_lineno}\n'
                    p.alert(p_ativ, msg_json['err'], msg_json['dest_apr'], 'ATIV006 ERROR', error_msg)
                    # apr.SendEmailWithScreenshot(p_ativ, msg_json['err'], msg_json['dest_apr'], 'ATIV006 ERROR', error_msg)
                    print(colored(error_msg, 'red'))
        except:
            exc_type, error, exc_tb = sys.exc_info()
            print(colored(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE: {exc_tb.tb_lineno}\n', 'red'))

        return ajusted, situation, shift_limit
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


def verify_shift(p_ativ, driver, shift_for_search, arrow_clicks, xpath_arrow, xpath_worker, mat, state_exists, msg_json, p_state):
    try:
        print(colored('\nINFO:checking shift', 'green'))
        # Verificar escala
        valid_shif = False
        shift_found = ''
        shift_limit = ''
        situation = ' - NAO PODE VALIDAR CARGA HORARIA E/OU ESCALA DEVIDAMENTE'
        try:
            # Entrar menu de informacoes pessoais
            got_in = False
            counter_menu = 0
            while counter_menu < 20:
                counter_menu += 1
                try:
                    # Buscar informacoes pessoais
                    driver.find_element('xpath', f'/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[2]/div[1]/ul/li[1]/a/i').click()
                    p.sleep(1)
                    got_in = True
                    break
                except:
                    p.sleep(1)

            # Clicar nas informacoes encontradas
            if got_in:
                counter = 0
                shift_hours_limit = ''
                while shift_hours_limit == '' and counter < 20:
                    counter += 1
                    try:
                        shift_hours_limit = driver.find_element('xpath', f'/html/body/core-main/div/div[2]/div[1]/div/div[2]/sidebar/div/div[2]/div[2]/div[2]/div/div[3]/table/tbody/tr[6]/td[2]').text
                    except:
                        p.sleep(1)

                # Buscar carga horaria
                shift_hours_limit = shift_hours_limit.split(' ')
                shift_hours_limit = list(filter(None, shift_hours_limit))
                for value in shift_hours_limit:
                    for char in range(len(value)):
                        if str(value[char]) in '0123456789':
                            shift_limit += value[char]

                print(colored(f'INFO:found amount of hours -> {shift_limit}', 'green'))
                searched_shift = False
                for attempt in range(20):
                    try:
                        # Opcao Cadastros menu lateral 
                        driver.find_element('xpath', f'/html/body/core-main/div/div[1]/div[2]/div/nexti-left-menu/nav/ul/li[10]/a').click()  
                        for attempt in range(20):
                            try:
                                # Opcao Escala menu lateral em cadastros
                                driver.find_element('xpath', f'/html/body/core-main/div/div[1]/div[2]/div/nexti-left-menu/nav/ul/li[10]/ul/li[9]/a').click()  
                                # Campo pesquisar
                                for attempt in range(20):
                                    try:  
                                        driver.find_element('xpath', f'/html/body/core-main/div/div[2]/div[2]/div[2]/div[1]/form/div/div/input').clear()  
                                        p.sleep(0.2)
                                        driver.find_element('xpath', f'/html/body/core-main/div/div[2]/div[2]/div[2]/div[1]/form/div/div/input').send_keys(f'{shift_for_search}')
                                        p.sleep(0.2)
                                        driver.find_element('xpath', f'/html/body/core-main/div/div[2]/div[2]/div[2]/div[1]/form/div/div/span/button/i').click()
                                        searched_shift = True
                                        break
                                    except:
                                        p.sleep(0.5)
                                break
                            except:
                                p.sleep(0.5)
                        break
                    except:
                        p.sleep(0.5)

                # Buscar escala em web que bata com a pesquisa
                p.sleep(1.5)
                shift_in_web = ''
                if searched_shift:
                    index = 0
                    while index < 10000:
                        # Mudar para proxima pagina ate nao haver mais paginas
                        index += 1
                        if index > 1:
                            try:
                                driver.find_element('xpath', f'//*[@id="app"]/div[2]/div[2]/div[4]/div[2]/ul/li[{index}]').click()
                            except Exception as exc:
                                break
                        
                        # Buscar escala nos resultados da pesquisa
                        for tr_index in range(2, 12):
                            p.sleep(0.5)
                            try:
                                shift_in_web = driver.find_element('xpath', f'/html/body/core-main/div/div[2]/div[2]/div[3]/table/tbody/tr[{tr_index}]/td[2]').text
                                shift_in_web = str(shift_in_web)
                                shift_in_web = shift_in_web.strip(' ')
                                states_lst = msg_json['states'].split(',')
                                click = True
                                
                                # Verificar se tem estado na escala e se sim verificar se estados batem
                                if state_exists:
                                    for state in states_lst:
                                        state += ' '
                                        if state in shift_in_web and p_state in state:
                                            print(colored(f'INFO:found -> {state} in {shift_in_web}', 'green'))
                                            click = True
                                            break
                                        else:
                                            click = False
                                else:
                                    for state in states_lst:
                                        state += ' '
                                        if state in shift_in_web:
                                            print(colored(f'WARNING:found -> {state} in {shift_in_web}\nshift not valid because -> state_exists == False', 'yellow'))
                                            click = False
                                            break
                                
                                if click:
                                    # Verificar tipo de escala referente aos dias da semana
                                    click = False
                                    invalid = False
                                    for invalid_char in msg_json["char_invalid"]:
                                        # Se achar characteres invalidos nao considerar usar escala
                                        if invalid_char in shift_in_web:
                                            print(colored(f'WARNING:FOUND {invalid_char} in {shift_in_web}', 'yellow'))
                                            invalid = True
                                            break

                                    if not invalid:
                                        # Verificar se a escala consta como escala de segunda a sexta
                                        for valid_week_shift in msg_json["mon_fri_valid"]:
                                            if valid_week_shift in shift_in_web:
                                                print(colored(f'INFO:FOUND {valid_week_shift} in {shift_in_web}', 'green'))
                                                click = True
                                                break

                                # Clicar em escala escontrada
                                if shift_for_search in shift_in_web and click == True:
                                    driver.find_element('xpath', f'/html/body/core-main/div/div[2]/div[2]/div[3]/table/tbody/tr[{tr_index}]/td[2]').click()
                                    p.sleep(2)

                                    # Buscar carga horaria
                                    for attribute in range(10):
                                        try:
                                            limit_hours_web = driver.find_element('xpath', f'/html/body/core-main/div/div[2]/div[2]/div[4]/div/div[2]/div[1]/form/div/div[8]/div/input').get_attribute('value')
                                            limit_hours_web = limit_hours_web.strip(' ')
                                            limit_hours_web = list(filter(None, limit_hours_web))
                                            shift_limit_web = ''

                                            # Separar carga horaria
                                            for value in limit_hours_web:
                                                if ':' in value:
                                                    break
                                                else:
                                                    shift_limit_web += value
                                            shift_limit_web = str(shift_limit_web)
                                            print(f'found amount of hours {shift_limit_web}')
                                            
                                            # Verificar se carga horaria bate
                                            if shift_limit in shift_limit_web:
                                                print(colored(f'INFO:{shift_limit} == {shift_limit_web}', 'green'))
                                            else:
                                                situation = f' - CARGA HORARIA "{shift_limit}" NAO BATE COM "{shift_limit_web}" - NAO PODE VALIDAR => {shift_for_search}'
                                                valid_shif = False
                                                print(colored(f'WARNING:{shift_limit} != {shift_limit_web}', 'yellow'))
                                                break
                                            
                                            # Finalizar loop para realizar troca da escala em seguida
                                            shift_found = driver.find_element('xpath', f'/html/body/core-main/div/div[2]/div[2]/div[4]/div/div[2]/div[1]/form/div/div[4]/div/input').get_attribute('value')
                                            valid_shif = True
                                            situation = f' - ESCALA "{shift_for_search}" VALIDA EM ESCALA {shift_found} E CARGA HORARIA {shift_limit} VALIDA'
                                            print(colored(f'INFO:found valid shift {shift_found}\nvalid hours and valid shift found!', 'green'))
                                            break
                                        except:
                                            p.sleep(1)
                                    # Fechar menu com dados da escala
                                    driver.find_element('xpath', f'/html/body/core-main/div/div[2]/div[2]/div[4]/div/div[1]/div/div[2]/a/i').click()
                                    if valid_shif:
                                        break
                                else:
                                    situation = f' - NAO ENCONTROU ESCALA VALIDA COM HORAS -> "{shift_for_search}"'
                                    print(f'{shift_for_search} AND {shift_in_web}',  colored(f'= NO MATCH', 'yellow'))
                            except:
                                print('searching for shifts')
                        if not shift_in_web:
                            situation = f' - NAO ENCONTROU ESCALA VALIDA COM HORAS -> "{shift_for_search}"'
                            print(colored(f'WARNING:shift not found for hours -> {shift_for_search}', 'yellow'))
                else:
                    situation = f' - NAO ENCONTROU ESCALA VALIDA COM HORAS -> "{shift_for_search}"'
                    raise ValueError(f'Error searching for {shift_for_search}')
            else:
                print(colored('WARNING:no more infomation found', 'yellow'))
        except:
            exc_type, error, exc_tb = sys.exc_info()
            error_msg = f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE: {exc_tb.tb_lineno}\n'
            p.alert(p_ativ, msg_json['err'], msg_json['dest_apr'], 'ATIV006 ERROR', error_msg)
            # apr.SendEmailWithScreenshot(p_ativ, msg_json['err'], msg_json['dest_apr'], 'ATIV006 ERROR', error_msg)
            print(colored(error_msg, 'red'))

        # Clicar em opcao no menu lateral - mesa de operacoes 
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/core-main/div/div[1]/div[2]/div/nexti-left-menu/nav/ul/li[2]/a/span')))
        p.sleep(2)
        driver.find_element('xpath', '/html/body/core-main/div/div[1]/div[2]/div/nexti-left-menu/nav/ul/li[2]/a/span').click()  
        p.sleep(2)
        click = 0
        found_menu_and_loaded = False
        while click < 120:
            try:
                # filtro de inconsistencias para pesquisar colaborador
                driver.find_element('xpath', '//*[@id="content"]/div[2]/div/div/div[1]/div[1]/div[2]/i').click()
                element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/searchfilter/div/div[1]/div[2]/div[2]/div/form/div[4]/div[4]/div[2]/nexti-textarea/div/textarea')))
                driver.find_element('xpath', '//*[@id="app"]/searchfilter/div/div[1]/div[2]/div[2]/div/form/div[4]/div[4]/div[2]/nexti-textarea/div/textarea').clear()
                driver.find_element('xpath', '//*[@id="app"]/searchfilter/div/div[1]/div[2]/div[2]/div/form/div[4]/div[4]/div[2]/nexti-textarea/div/textarea').send_keys(f'{mat}')
                # Filtrar
                driver.find_element('xpath', '//*[@id="app"]/searchfilter/div/div[1]/div[2]/div[4]/a[2]').click() 
                # esperar carregamento dos filtros
                for click in range(120):  
                    try:
                        driver.find_element('xpath', '//*[@id="app"]/div[1]/div[2]/div/nexti-left-menu/nav/div/button/i').click()
                        found_menu_and_loaded = True
                        click = 120
                        break
                    except:
                        p.sleep(2)
            except:
                p.sleep(1)
            click += 1
        # Chegar ate o colaborador clicando na seta lateral
        if found_menu_and_loaded:
            if arrow_clicks > 1:
                for click in range(1, arrow_clicks):
                    driver.find_element('xpath', xpath_arrow).click()
                    p.sleep(0.5)
            elif arrow_clicks == 1:
                driver.find_element('xpath', xpath_arrow).click()
                p.sleep(0.5)
            # Clicar no xpath encontrado
            driver.find_element('xpath', xpath_worker).click()  

        return valid_shif, situation, shift_found, shift_limit
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


def search_for_employee(driver, excel_name, num_mat_excel, msg_json):
    try:
        # data_list.append([name, time_shift, num_mat, xpath_name, xpath_arrow, arrow_clicks])
        # name_web, shift_web, num_mat_web, xpath_name_web, xpath_arrow_web, arrow_clicks_web
        #-=-=-=-=-=-=-=-=-=-=--=-=-=-=--=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--==-=-=-=-=-=-=-=-=-=-=-=
        # a funcionalidade desta função é para que se encontre 1 pessoa parassando por parametro o nome dele(colaboradores) e pela matricula no filtro geral
        # caso não encontre este no filtro geral, tem outra maneira de pesquisar um nome 
        # a cada página existem tabelas com um campo de pesquisa como se fosse do google que você pode pesquisar qualquer tipo de informação
        # eu vou fazer 2 validações 
        # 1- É caso tenha achado o nome na primeira tela sem precisar fazer uma busca mais profunda, é só dar um drive.find_elements() e guardar estes elementos dentros de um xpath
        # 2- É caso seja necessário fazer uma busca mais avançada dentro de cada tabelinha, para fazer esta busca, é necessário entrar em cada tabelinha desta e pesquisar o nome completo da pessoa sem nenhum tipo de abreviação e ponto.
        # ao final desta função é necessário passar para a função de validar o nome, e dentro dela não é necessário fazer nada, somente chegar nela encher de p.alert em cada xpath e verificar se esstá esperando o tempo necessário ou clicando no campo certo
        # a meta de amanhã é fazer tudo o que foi passado pelo caue sem que seja necessário chamar ele para esclarecer nenhuma duvida, VOCÊ CONSEGUE FELIPE, AGORA É PAU NA MAQUINA!

        for diminuir_tela in range(0,2):
            p.hotkey('ctrl','-')
        for click in range(50):
            try:
                element = driver.find_element(By.XPATH,'/html/body/core-main/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div[2]/h4')
                element.click()
                break
            except:
                p.sleep(1.5)
        repeat = True
        cont = 0
        code_list = []
        while repeat == True :
            # elementos = driver.find_elements(By.XPATH, '/html/body/core-main/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/h5/span[2]')
            elementos = driver.find_elements(By.XPATH, '/html/body/core-main/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/h5/span[2]')
            names_list = [name.text for name in elementos]
            if '' not in names_list:
                repeat = False
                #esta sendo atribuida da forma antiga, pois o sistema nao estava aceitando comprehensions neste dado em especifico.
                for codigo in codigos_site:
                    codigos_site = driver.find_elements(By.XPATH, '/html/body/core-main/div/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[2]/h5/span[1]')
                    path_list = [path for path in elementos]
                    teste = codigo.text
                    teste = teste.replace(' ', '').replace('-','')
                    if teste.isdigit():
                        code_list.append(teste)
                for l in range(len(names_list)):
                    print(f'Nome:{names_list[l]}\ncódigo:{code_list[l]}\npath:{path_list[l]}')
                    print('-='*35)
                break    
            elif '' in names_list and cont <15:
                repeat = True
            else:
                #aqui você só tem que buscar a pessoa de acordo com o nome ou matricula!
                lista_clicavel = [] 
                try:
                    elementos = driver.find_elements(By.XPATH, '/html/body/core-main/div/div[2]/div[1]/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[2]/h5/span[2]')
                    for element in elementos :
                        lista_clicavel.append(element)

                        # print(element.get_attribute('innerHTML'))
                    
                    for pessoa in lista_clicavel:
                        if pessoa.get_attribute('innerHTML') == 'AMANDA DOS S.':
                            p.alert('é ela ')
                            # pessoa.click()
                        else:
                            print('ainda não é ela ')
                    break    
                except:
                    p.sleep(1)
                    exc_type, error, line = sys.exc_info()
                    print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')
                p.alert(lista_clicavel) 
            cont+=1

            p.sleep(1)
        xpath_arrow = ''
        arrow_clicks = 0
        data_list = []
        found_name_match = False
        print(colored('\nINFO:searching for employee', 'green'))
        name_web = ''
        p.alert(names_list)
        found_name_match = verify_names(excel_name, name_web, msg_json)
        return data_list, found_name_match
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')

def verify_names(col, name, msg_json):
    try:
        # Verificar se o nome do excel bate com o da web
        found_name_match = False
        try:
            # buscar inicais dos nomes
            initials_web = []
            initials_excel = []
            all_initials_matched = False
            full_name_web = name.split(' ')
            full_name_excel = col.split(' ')
            full_name_web = list(filter(None, full_name_web))
            full_name_excel = list(filter(None, full_name_excel))
            first_name_web = full_name_web[0]
            last_name_web = full_name_web[-1]
            first_name_excel = full_name_excel[0]
            last_name_excel = full_name_excel[-1]

            # Separar iniciais para comparacao
            for i in range(len(full_name_web)):
                initials_web.append(full_name_web[i][0])
            for i in range(len(full_name_excel)):
                initials_excel.append(full_name_excel[i][0])

            # verificar se iniciais batem
            counter = 0
            if len(initials_excel) == len(initials_web):  
                for i in range(len(full_name_excel)):
                    if str(initials_web[i]) == str(initials_excel[i]):
                        counter += 1
                        if counter == len(initials_excel):
                            all_initials_matched = True

            # verificar se ao menos um nome bate
            one_match = False
            two_names_matched = True
            for name1 in full_name_excel:
                for name2 in full_name_web:
                    if str(name1) == str(name2) and len(name1) > 2 and len(name2) > 2:
                        if one_match:
                            two_names_matched = True
                            break
                        one_match = True

            # Validar nome
            if (first_name_excel == first_name_web and last_name_excel == last_name_web) or (two_names_matched is True and all_initials_matched is True):
                found_name_match = True
                print(f'EXCEL = {col}\nWEB = {name}')
                print(colored(f'INFO:found valid name!', 'green'))
        except:
            exc_type, error, exc_tb = sys.exc_info()
            error_msg = f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE: {exc_tb.tb_lineno}\n'
            p.alert( msg_json['err'], msg_json['dest_apr'], 'ATIV006 ERROR', error_msg)
            # apr.SendEmailWithScreenshot(p_ativ, msg_json['err'], msg_json['dest_apr'], 'ATIV006 ERROR', error_msg)
            print(colored(error_msg, 'red'))
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')

    return found_name_match


def verify_type(driver, col, mat, msg_json):
    try:
        worker_type = ''
        worker_type_web = ''
        print(colored(f'\nINFO:checking type', 'green'))
        # Verificar tipo do colaborador
        for click in range(10):
            try:
                # clicar em inconsistenticas de ponto
                element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/core-header/div[1]/ul/li[3]/a/i')))  
                p.sleep(2)
                driver.find_element('xpath', '//*[@id="app"]/core-header/div[1]/ul/li[3]/a/i').click() 
                p.sleep(2)

                # Pesquisar colaborador
                for key_sent in range(10):
                    try:  
                        driver.find_element('xpath', '/html/body/core-main/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/form/div/div/input').clear()
                        driver.find_element('xpath', '/html/body/core-main/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/form/div/div/input').send_keys(col)
                        driver.find_element('xpath', '/html/body/core-main/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/form/div/div/input').click()
                        print(f'searched = {col}')
                        worker_type_web = ''

                        # Extrair tipo do colaborador
                        for extraction in range(5):
                            worker_type_web = ''
                            try:
                                worker_type_web = driver.find_element('xpath', '/html/body/core-main/div/div[1]/div[2]/div/div/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[7]').text  
                                print(f'found {worker_type_web}')
                                # terminal nao autorizado
                                if msg_json['ter_nao'] in worker_type_web:  
                                    worker_type = 'terminal nao autorizado'
                                    break
                                # nao registrado
                                elif msg_json['nao_reg'] in worker_type_web:   
                                    worker_type = 'nao registrado'
                                    break
                                # horario invalido
                                elif msg_json['hor_inv'] in worker_type_web:  
                                    worker_type = 'horario invalido'
                                    break
                                else:
                                    worker_type = f'found type = {worker_type_web}'
                                    break
                            except:
                                p.sleep(1)

                        if worker_type_web:
                            print(f'FOUND:{col} = {worker_type_web}')
                            break
                    except:
                        p.sleep(1)
                break
            except:
                p.sleep(1)
        
        # clicar em opcao no menu lateral - mesa de operacoes 
        for click in range(50): 
            try:                              
                driver.find_element('xpath', '/html/body/core-main/div/div[1]/div[1]/div[2]/div/nexti-left-menu/nav/ul/li[2]/a/span').click()
                break
            except:
                try:                              
                    driver.find_element('xpath', '/html/body/core-main/div/div[1]/div[1]/div[2]/div/nexti-left-menu/nav/ul/li[2]').click()
                    break
                except:
                    p.sleep(2)

        # filtro de inconsistencias para pesquisar colaborador
        found_menu = False
        for key_sent in range(120):
            try:
                driver.find_element('xpath', '//*[@id="content"]/div[2]/div/div/div[1]/div[1]/div[2]/i').click()  
                element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/searchfilter/div/div[1]/div[2]/div[2]/div/form/div[4]/div[4]/div[2]/nexti-textarea/div/textarea')))
                driver.find_element('xpath', '//*[@id="app"]/searchfilter/div/div[1]/div[2]/div[2]/div/form/div[4]/div[4]/div[2]/nexti-textarea/div/textarea').clear()
                driver.find_element('xpath', '//*[@id="app"]/searchfilter/div/div[1]/div[2]/div[2]/div/form/div[4]/div[4]/div[2]/nexti-textarea/div/textarea').send_keys(f'{mat}')
                # Filtrar
                driver.find_element('xpath', '//*[@id="app"]/searchfilter/div/div[1]/div[2]/div[4]/a[2]').click()  
                found_menu = True
                break
            except:
                p.sleep(1)

        # Voltar
        if found_menu:  
            for click in range(200):
                try:
                    driver.find_element('xpath', '//*[@id="app"]/div[1]/div[2]/div/nexti-left-menu/nav/div/button/i').click()
                    break
                except:
                    p.sleep(1)

        if not worker_type_web:
            print(colored(f'WARNING:{col} = type not found', 'yellow'))
            worker_type = f'nao achou tipo do colaborador'

        return worker_type
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')

def change_shifts_loop_excel(p_ativ, driver, msg_json, path_pro, path_out, db_shifts):
    try:
        shifts_log = []
        try:
            files_pro = os.listdir(path_pro)
            if files_pro:
                # Verificar se site esta aberto
                check_if_opened = 0
                while check_if_opened < 50:
                    check_if_opened += 1
                    try:       
                        driver.find_element('xpath', '//*[@id="app"]/div[1]/div[2]/div/nexti-left-menu/nav/ul/li[2]/a/i').click()
                        print('on website')
                        break
                    except:
                        print('checking if website has opened')

                # Loop principal com dados do excel
                print(colored(f'INFO:processing file {files_pro[0]}', 'green'))
                nexti_report_xls = pd.read_excel(f'{path_pro}{files_pro[0]}', sheet_name='Sheet1', dtype=str)
                loop_counter = 0
                for line in range(len(nexti_report_xls)):
                    emp = str(nexti_report_xls[msg_json['emp_header']][line])
                    cli = str(nexti_report_xls['Unnamed: 1'][line])
                    col = str(nexti_report_xls['Unnamed: 2'][line])
                    mat = str(nexti_report_xls['Unnamed: 3'][line])
                    uni = str(nexti_report_xls['Unnamed: 4'][line])
                    pos = str(nexti_report_xls['Unnamed: 5'][line])
                    qtd = str(nexti_report_xls['Unnamed: 6'][line])
                    esc = str(nexti_report_xls['Unnamed: 7'][line])
                    reg = str(nexti_report_xls['Registro processamento'][line])
                    # Para intercalar com as outras atividades
                    if loop_counter == 100:
                        break

                    if str(nexti_report_xls['Registro processamento'][line]) == "NOK" and (('Empresa' not in emp) and ('Cliente' not in cli) and ('Colaborador' not in col)):
                        print(colored('\n[LEN SHIFTS_LOG]', 'cyan'), f'= {len(shifts_log)}')
                        print(colored('[LOOP]', 'cyan'), f'= {loop_counter+1}')
                        print(f'EXCEL DATA:\nline = {line} (of {len(nexti_report_xls)})\ncompany = {emp}\nworker = {col}\ncode = {mat}\nshift = {esc}')

                        click = 0
                        loop_counter += 1
                        found_menu_and_loaded = False
                        # filtro de inconsistencias para pesquisar colaborador
                        while click < 50:
                            try:   
                                # # Clicar em mesa de operações
                                x = 1
                                for click in range(50):
                                    try:
                                        driver.find_element(By.XPATH, '/html/body/core-main/div/div[1]/div[1]/div[2]/div/nexti-left-menu/nav/ul/li[2]/a/span').click()
                                        break
                                    except:
                                        p.sleep(1)
                                x = 2
                                # Filtro geral
                                for click in range(50):
                                    try:
                                        driver.find_element(By.XPATH, '/html/body/core-main/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/i').click()
                                        break
                                    except:
                                        p.sleep(1)
                                x = 3
                                #matricula
                                for click in range(50):
                                    try:
                                        driver.find_element(By.XPATH, '/html/body/core-main/div/searchfilter/div/div[1]/div[2]/div[2]/div/form/div[4]/div[4]/div[2]/nexti-textarea/div/textarea').send_keys(f'{mat}')
                                        break
                                    except:
                                        p.sleep(1)
                                #pesquisar pelo nome do colaborador
                                for click in range(50):
                                    array_de_nomes = []
                                    try:
                                        #lembrar de alterar a mensagem padrão para o nome d apessoa, pois assim irá fazer o filtro certo.
                                        driver.find_element(By.XPATH, '/html/body/core-main/div/searchfilter/div/div[1]/div[2]/div[2]/div/form/div[4]/div[4]/div[1]/autocomplete/div/div/input').send_keys(f'AMANDA DOS ')
                                        p.sleep(4.5)
                                        p.press('enter')
                                        p.press('enter')
                                        break
                                    except:
                                        p.sleep(1)
                                x = 3
                                # Filtrar
                                driver.find_element('xpath', '/html/body/core-main/div/searchfilter/div/div[1]/div[2]/div[4]/a[2]').click() 
                                x = 7
                                # Esperar carregamento dos filtros
                                names_list = 0
                                array = []
                                for click in range(50):
                                    try:
                                        found_menu_and_loaded = True
                                        click = 50
                                        break
                                    except:
                                        p.sleep(1)
                            except Exception as e:
                                p.alert(f'parou aqui {x} \n{e}')
                                p.sleep(1)

                            click += 1
                        p.alert('concluiu a fase 1')
                        # try:
                        #     for clicar_na_pessoa in range(50):
                        #         driver.find_elemente(By.XPATH, '')
                        #         break
                        # except:
                        #     p.sleep(1)

                        
                        if found_menu_and_loaded:
                            # Buscar colaborador e verificar se os dados estao corretos
                            found_name_match = False
                            lst_data_web, found_name_match = search_for_employee(driver, col, mat, msg_json)

                            p.alert(f'lst_data_web{lst_data_web}\nfound_name_match{found_name_match}')
                            #a partir daqui você pode começar
                            continue
                            if found_name_match:
                                # Buscar tipo do colaborador
                                worker_type = verify_type(driver, col, mat, msg_json)
                                # Separar dados para ajuste dos colaboradores com tipo horario invalido
                                if 'horario invalido' in worker_type:
                                    worker_type = worker_type.upper()
                                    nexti_report_xls.loc[line, 'Registro processamento'] = 'NOK'
                                    nexti_report_xls.loc[line, 'Situacao'] = f'TIPO = "{worker_type}"'
                                    nexti_report_xls.to_excel(f'{path_pro}{files_pro[0]}', index=False)
                                    shift = f'{lst_data_web[0][1]}'
                                    xpath_arrow = f'{lst_data_web[0][4]}'
                                    xpath_worker = f'{lst_data_web[0][3]}'
                                    arrow_clicks = int(lst_data_web[0][5])

                                    # Se preciso navegar ate o colaborador
                                    if arrow_clicks > 1:
                                        for click in range(1, arrow_clicks):
                                            driver.find_element('xpath', xpath_arrow).click()
                                            p.sleep(0.5)
                                    elif arrow_clicks == 1:
                                        driver.find_element('xpath', xpath_arrow).click()
                                        p.sleep(0.5)

                                    # Clicar no colaborador
                                    driver.find_element('xpath', xpath_worker).click()  
                                    print(f'clicked on {col}')
                                    
                                    # Realizar ajuste
                                    ajusted, situation, shift_limit_hours = ajust_shift(driver, shift, msg_json, arrow_clicks, xpath_arrow, xpath_worker, mat, esc, p_ativ, db_shifts)
                                    if 'AJUSTOU PARA ESCALA' in situation or 'NAO BATE COM' in situation or 'NAO ENCONTROU ESCALA' in situation or 'IGUAL ESCALA EXCEL' in situation:
                                        emp = 'NaN' if len(str(emp)) <= 1 else emp
                                        col = 'NaN' if len(str(col)) <= 1 else col
                                        mat = 'NaN' if len(str(mat)) <= 1 else mat
                                        esc = 'NaN' if len(str(esc)) <= 1 else esc
                                        situation = 'NaN' if len(str(situation)) <= 1 else situation
                                        shift_limit_hours = 'NaN' if len(str(shift_limit_hours)) <= 1 else shift_limit_hours
                                        situation = situation.strip()
                                        shifts_log.append([emp, col, situation, mat, esc, shift_limit_hours])

                                    # Salvar processamento
                                    if ajusted:
                                        worker_type = worker_type.upper()
                                        nexti_report_xls.loc[line, 'Registro processamento'] = 'OK'
                                        nexti_report_xls.loc[line, 'Situacao'] = f'TIPO = "{worker_type}"{situation}'
                                        nexti_report_xls.to_excel(f'{path_pro}{files_pro[0]}', index=False)
                                    else:
                                        worker_type = worker_type.upper()
                                        nexti_report_xls.loc[line, 'Registro processamento'] = 'ERR'
                                        nexti_report_xls.loc[line, 'Situacao'] = f'TIPO = "{worker_type}"{situation}'
                                        nexti_report_xls.to_excel(f'{path_pro}{files_pro[0]}', index=False)

                                # Se nao for do tipo horario invalido nao precisa processar
                                elif worker_type == 'terminal nao autorizado' or worker_type == 'nao registrado' or ('achou tipo' in worker_type and worker_type != 'terminal nao autorizado' and worker_type != 'nao registrado'):
                                    print(f'{col} has type = {worker_type}')
                                    worker_type = worker_type.upper()
                                    nexti_report_xls.loc[line, 'Registro processamento'] = 'OK'
                                    nexti_report_xls.loc[line, 'Situacao'] = f'NAO PRECISOU TROCAR ESCALA: TIPO = "{worker_type}"'
                                    nexti_report_xls.to_excel(f'{path_pro}{files_pro[0]}', index=False)
                            else:
                                print(f'{col} not found')
                                shifts_log.append([emp, col, 'NAO ACHOU COLABORADOR NO NEXTI', mat, esc])
                                nexti_report_xls.loc[line, 'Registro processamento'] = 'ERR'
                                nexti_report_xls.loc[line, 'Situacao'] = f'DADOS (EXCEL/WEB) NAO BATEM OU NAO ENCONTROU COLABORADOR'
                                nexti_report_xls.to_excel(f'{path_pro}{files_pro[0]}', index=False)
                        else:
                            raise RuntimeError('Error trying to apply filters')
                    else:
                        # Primeira linha do excel
                        if 'Empresa' in emp and 'Cliente' in cli and 'Colaborador' in col:  
                            nexti_report_xls.loc[line, 'Registro processamento'] = 'OK'
                            nexti_report_xls.loc[line, 'Situacao'] = 'HEADERS'
                            nexti_report_xls.to_excel(f'{path_pro}{files_pro[0]}', index=False)
            else:
                raise FileNotFoundError('Process started with no file in pro to process')
        except:
            exc_type, error, exc_tb = sys.exc_info()
            error_msg = f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE: {exc_tb.tb_lineno}\n'
            p.alert(p_ativ, msg_json['err'], msg_json['dest_apr'], 'ATIV006 ERROR', error_msg)
            # apr.SendEmailWithScreenshot(p_ativ, msg_json['err'], msg_json['dest_apr'], 'ATIV006 ERROR', error_msg)
            print(colored(error_msg, 'red'))
                
        return shifts_log
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')

def BOTAPRAtividade006(p_ativ):
    try:
        p.FAILSAFE = False
        path_pro = os.path.dirname(os.path.realpath(__file__))+'\\'+p_ativ+'\\pro\\'
        path_out = os.path.dirname(os.path.realpath(__file__))+'\\'+p_ativ+'\\out\\'
        path_temp = os.path.dirname(os.path.realpath(__file__))+'\\'+p_ativ+'\\temp\\'
        path_imaout = os.path.dirname(os.path.realpath(__file__))+'\\'+p_ativ+'\\imaout\\'
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--start-maximized')
        prefs = {"network.http.response.timeout":120, 'download.default_directory':path_pro}
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(chrome_options=options, executable_path=r'..\\DriverWeb\\chromedriver.exe')
        msg_json = json.load(open(r'.\\'+ p_ativ+'\doc\DGLMsg.json', 'r', encoding='utf8'))
        msg_str = msg_json["msg"]
        now = datetime.now()
        ini = now.strftime("%H:%M - %d/%m/%Y")
        ini_time = datetime.now()
        print(colored('\n[ATIV006]', 'blue'), f'= troca de escalas\nstart: {ini}')
        shifts_log = []
        db_shifts = []
        cnxn_rubi = None
        opened = False
        counter = 0

        try:
            # # Criar conexoes com banco de dados do Rubi
            # cnxn_rubi = pyodbc.connect('DRIVER={SQL Server};''SERVER=FRANCA;''DATABASE=dbvetorh;''Trusted_Connection=yes;')  
            # print(f'connected = dbvetorh {cnxn_rubi}')
            # # Verificar se a conexao foi estabelecida
            # if cnxn_rubi != None:
            #     # Buscar codigos das escalas junto das mesmas
            #     cur = cnxn_rubi.cursor()
            #     sql_select = f"SELECT codesc, nomesc FROM R006esc"
            #     cur.execute(sql_select)
            #     cur = [dict(zip([column[0] for column in cur.description], row)) for row in cur.fetchall()]
            #     print(f'{len(cur)} db records')
            #     if cur:
            #         print('extracting records from db...')
            #         # Gerar escalas completas para realizar as trocas das mesmas no Nexti
            #         for row in cur:
            #             cod_esc = row['codesc']
            #             nom_esc = row['nomesc']
            #             esc = f'{cod_esc} - {nom_esc}'
            #             db_shifts.append(esc)
            # else:
            #     raise DataBaseConnectionError("Error connecting to Rubi's database")

            # hormes = dividir por 60
            # usu_datext = apenas considerar como valida as que tem 19000   =    select * from r006esc where usu_datext <> '31/12/1900'
            # select * from r006esc where codesc >= '1000000'   =  escalas acima de 1 milhao nao podem ser utilizadas

            # Verificar se o arquivo em pro ainda e do dia atual, se nao for, remover e baixar outro
            files_in_pro = os.listdir(path_pro)
            print(f'pro = {files_in_pro}')
            creation_date = ''
            if len(files_in_pro) == 1:
                creation_date = os.path.getctime(f'{path_pro}{files_in_pro[0]}')
                creation_date = time.ctime(creation_date)
                dt = datetime.now()
                day = dt.strftime('%A')
                day_3_initials = day[:3]
                print(f'creation date = {creation_date}')
                if day_3_initials not in creation_date:
                    os.remove(f'{path_pro}{files_in_pro[0]}')
                    print(colored(f'removed {files_in_pro[0]}', 'yellow'))
                else:
                    print(colored(f'{files_in_pro[0]} is from today!', 'green'))
            elif len(files_in_pro) > 1:
                for file in files_in_pro:
                    os.remove(f'{path_pro}{file}')
                    print(colored(f'removed {file}', 'yellow'))
            # Abrir Nexti website
            counter = 0
            while opened is False and counter < 5:
                opened = apr.OpenNextiWebsite(driver)
                counter += 1
            # Verificar se abriu Nexti devidamente
            if opened:
                c = 0
                got_in = False
                while c < 100:
                    try:
                        driver.find_element('xpath', '//*[@id="content"]/div[1]/div/div[1]/h1').click()
                        print('entered website')
                        got_in = True
                        break
                    except:
                        try:
                            pop_up = p.locateCenterOnScreen(f".\\GENERAL\\ima\\40DismissPopup.PNG", confidence=0.9)
                            p.click(pop_up)
                            print('clicked on popup')
                            got_in = True
                            break
                        except:
                            p.sleep(0.1)
                    c += 1
                if got_in:
                    # Aplicar zoom para que possa extrair os dados devidamente 
                    # OBS: Unica parte do robo usando imagens com pyautogui
                    apr.ValidaTelaParaSeguir(p_ativ, f".\\{p_ativ}\\ima\\nexti_logo.PNG", 15, 'nexti logo')
                    nexti_logo = p.locateCenterOnScreen(f".\\{p_ativ}\\ima\\nexti_logo.PNG", confidence = 0.9)
                    p.click(nexti_logo)
                    for click in range(5):
                        p.hotkey('ctrl', '-')
                        p.sleep(0.1)

                    # Verificar se ainda tem nok no arquivo do dia, se nao tiver baixar outro
                    file_exists = download_report_and_check_pro(p_ativ, driver, path_pro, path_out, msg_json)
                    if file_exists:
                        # Realizar loop no arquivo trocando escalas
                        shifts_log = change_shifts_loop_excel(p_ativ, driver, msg_json, path_pro, path_out, db_shifts)
                        # Salvar reporte diario completo do excel em out
                        try:
                            pro = os.listdir(path_pro)
                            now = datetime.now()
                            new_file_name = f'{now.day}_{now.month}_{now.year}dados_escalas_completo.xlsx'
                            apr.SaveExcelWithFilters(p_ativ, msg_json, path_pro, path_out, pro[0], new_file_name, 'Sheet1', msg_json["header_list"])
                        except:
                            exc_type, error, exc_tb = sys.exc_info()
                            error_msg = f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE: {exc_tb.tb_lineno}\n'
                            p.alert(p_ativ, msg_json['err'], msg_json['dest_apr'], 'ATIV006 ERROR', error_msg)
                            # apr.SendEmailWithScreenshot(p_ativ, msg_json['err'], msg_json['dest_apr'], 'ATIV006 ERROR', error_msg)
                        if shifts_log:
                            try:
                                # Separar nomes e escalas nao encontradas e modificadas para o cliente tratar
                                apr.EsvaziarDiretorio(path_temp)
                                headers_list = ['EMPRESA', 'NOME_COLABORADOR', 'SITUACAO_ESCALAS', 'MATRICULA', 'ULTIMA_ESCALA_WEB', 'CARGA_HORARIA']
                                df = pd.DataFrame(shifts_log, columns=headers_list)
                                df.to_excel(f'{path_temp}trocas_e_nao_encontradas.xlsx', index=False)
                                p.sleep(3)
                                shifts_log_file = os.listdir(path_temp)
                                apr.SaveExcelWithFilters(p_ativ, msg_json, path_temp, path_temp, 'trocas_e_nao_encontradas', 'trocas_e_nao_encontradas', 'Sheet1', headers_list)
                                p.sleep(2)
                                p.alert(msg_json["subject"], msg_json["dest"], 'Segue arquivo com escalas modificadas e não encontradas.', '', path_temp, shifts_log_file)
                                # apr.EnviarEmailAprTech(msg_json["subject"], msg_json["dest"], 'Segue arquivo com escalas modificadas e não encontradas.', '', path_temp, shifts_log_file)
                                apr.EsvaziarDiretorio(path_temp)
                            except:
                                exc_type, error, exc_tb = sys.exc_info()
                                error_msg = f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE: {exc_tb.tb_lineno}\n'
                                p.alert(p_ativ, msg_json['err'], msg_json['dest_apr'], 'ATIV006 ERROR', error_msg)
                                # apr.SendEmailWithScreenshot(p_ativ, msg_json['err'], msg_json['dest_apr'], 'ATIV006 ERROR', error_msg)
                        # else:
                        #     print(colored(f'WARNING:shifts_log = {len(shifts_log)}', 'yellow'))
                    else:
                        print(colored('WARNING:file not found in function download_report_and_check_pro', 'yellow'))
                else:
                    raise ConnectionError("Can't verify if website is active")
            else:
                raise ConnectionError('Attempt to open Nexti failed')

            driver.close()
            if shifts_log != []:
                pass
                # apr.GeraRegistroAtiv(p_ativ, datetime.now(), datetime.now(), 1, msg_str, 1)
                # apr.TransmitePing(p_ativ, msg_str, 'OK')
                if ini_time.hour > 7 and ini_time.hour < 18:
                    now = datetime.now()
                    end = now.strftime("%H:%M - %d/%m/%Y")
                    # apr.EnviarEmailAprTech(msg_json["subject"], 'caue.oliveira@aprtech.com.br', f'{msg_str}\nIniciou: {ini}\nFinalizou: {end}', '', '', '')
        except:
            exc_type, error, exc_tb = sys.exc_info()
            error_msg = f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE: {exc_tb.tb_lineno}\n'
            # apr.SendEmailWithScreenshot(p_ativ, msg_json['err'], msg_json['dest_apr'], 'ATIV006 ERROR', error_msg)
            # save_excel(p_ativ, msg_json, path_out, path_pro)
            now = datetime.now()
            end = now.strftime("%H:%M - %d/%m/%Y")
            error_msg = f'\n{error_msg}\nstart = {ini}\nend = {end}'
            # apr.GeraRegistroAtiv(p_ativ, datetime.now(), datetime.now(), 1, error_msg, 1)
            # apr.TransmitePing(p_ativ, error_msg, 'NOK')
            print(colored(error_msg, 'red'))
        finally:
            apr.FinalizarAplicacao('javaw.exe')
            apr.FinalizarAplicacao('chrome.exe')
            apr.EsvaziarDiretorio(path_imaout)
            now = datetime.now()
            end = now.strftime("%H:%M - %d/%m/%Y")
            print(f'end = {end}')
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')

### UPDATE JSON
if __name__ == '__main__':
    try:
        os.system('cls')
        BOTAPRAtividade006('ATIV006')
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')
