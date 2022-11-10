import pandas as pd
import pyautogui as p 
import os 
import os.path
import sys


def abrir_desafio_e_ler_planilha():
    try:
        # Abrir Chrome
        print('abrindo navegador')
        p.hotkey('win', 'r')
        p.sleep(0.3)
        p.typewrite('chrome')
        p.sleep(0.3)
        p.press('enter')
        p.sleep(0.3)
        janela = p.getActiveWindow()
        janela.maximize()
        p.sleep(1)
        # Abrir site
        p.typewrite('http://rpachallenge.com')
        p.press('enter')
        p.sleep(2)
        print('entrou site')

        # Baixar Excel
        download_planilha = p.locateCenterOnScreen('C:\\Curso02_github\\desafio_Final\\baixar_planilha.png')
        while download_planilha == None:
            p.sleep(1)
        p.click(download_planilha)
        p.sleep(2)

        c = 0
        fechar_popUp_Download = None
        while (fechar_popUp_Download is None) and (c < 15):
            p.sleep(1)
            c += 1
            fechar_popUp_Download = p.locateCenterOnScreen('C:\\Curso02_github\\desafio_Final\\fechar_Download_planilha.png')
            if (fechar_popUp_Download is not None):
                p.click(fechar_popUp_Download)
                p.sleep(1)
                print('baixou arquivo com sucesso')
                if (c >= 2):
                    break

        # Abrir Excel
        dados = pd.read_excel("C:\\Users\\Ana Paula\\Downloads\\challenge.xlsx", sheet_name='Sheet1')
        data_frame = pd.DataFrame(dados, columns=["First Name",	"Last Name ", "Company Name", "Role in Company", "Address", "Email", "Phone Number"])
        print('leu o arquivo')
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')

    return data_frame


def preencher_campos(data_frame):
    try:
        p.press('pagedown', 3)
        p.sleep(1)
        cont = 0

        # Clicar start
        start = None
        while (cont < 30):
            cont +=1
            p.sleep(1)
            start = p.locateCenterOnScreen('C:\\Curso02_github\\desafio_Final\\teclaStart.png')
            if (start is not None):
                p.sleep(1)
                p.click(start)
                print('clicou start')
                p.sleep(1)
                p.press('f11')
                break

        # Preencher campos
        for linha in data_frame.itertuples():
            for c in range(1, 8):
                p.sleep(0.5)

                cont = 0 
                while (cont < 10):
                    x = None
                    y = None
                    p.press('pageup', 3)
                    p.sleep(0.3)
                    try:
                        cont += 1
                        x, y = p.locateCenterOnScreen(f'C:\\Curso02_github\\desafio_Final\\campos\\campo{c}_{cont}.png', confidence=0.9)
                        if (x is not None) or (y is not None):
                            p.click(x, (y+30))
                            p.sleep(0.1)
                            print(f'CLICOU imagem campo{c}_{cont}')
                            p.write(str(linha[c]))
                            break
                    except:
                        p.sleep(0.3)

                    p.press('pagedown', 3)
                    p.sleep(0.3)
                    try:
                        x, y = p.locateCenterOnScreen(f'C:\\Curso02_github\\desafio_Final\\campos\\campo{c}_{cont}.png', confidence=0.9)
                        if (x is not None) or (y is not None):
                            p.click(x, (y+30))
                            p.sleep(0.1)
                            print(f'CLICOU imagem campo{c}_{cont}')
                            p.write(str(linha[c]))
                            break
                    except:
                        p.sleep(0.3)
            
            find_buttom = 0
            while (find_buttom < 15):
                print('buscando submit')
                find_buttom += 1
                bt = p.locateCenterOnScreen(f'C:\\Curso02_github\\desafio_Final\\botao_submit.png', confidence=0.9)
                if (bt is not None):
                    p.click(bt)
                    print('clicou submit')
                    break
                p.press('pagedown', 3)

        # Tirar print
        my_screenshot = p.screenshot()
        my_screenshot.save(r'C:\\Curso02_github\\desafio_Final\\screenshots\\ultimo_print.png')
        print('salvou screenshot')

    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')    


def desvaziar_downloads(full_path):
    print(f'esvaziando caminho: {full_path}')
    arq_lista = os.listdir(full_path)
    print(f'existem {len(arq_lista)} arquivos em downloads')
    for arquivo in arq_lista:
        if arquivo.endswith('xls') or arquivo.endswith('xlsx'):
            os.remove(f'{full_path}\\{arquivo}')
            print(f'removeu {full_path}\\{arquivo}')
        else:
            print(f'arquivo {arquivo} nao e excel')

  
def bot_atividade_001():
    try:
        path = "~\\Downloads\\"
        full_path = os.path.expanduser(path)
        desvaziar_downloads(full_path)
        data_frame = abrir_desafio_e_ler_planilha()
        preencher_campos(data_frame)
        desvaziar_downloads(full_path)
        #if success:
            #mandar email SUCESSO 
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')    
        # mandar email com o erro => nós 
        


if (__name__ == '__main__'):
    os.system('taskkill /f /im chrome.exe')
    os.system('cls')
    bot_atividade_001()