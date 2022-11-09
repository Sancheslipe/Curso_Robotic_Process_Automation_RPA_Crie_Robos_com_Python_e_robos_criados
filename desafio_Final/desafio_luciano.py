import pandas as pd
import pyautogui as p 
import os as o 
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

        fechar_popUp_Download = None
        while (fechar_popUp_Download is None):
            fechar_popUp_Download = p.locateCenterOnScreen('C:\\Curso02_github\\desafio_Final\\fechar_Download_planilha.png')
            if (fechar_popUp_Download is not None):
                p.click(fechar_popUp_Download)
                p.sleep(1)
                print('baixou arquivo com sucesso')
                break
            p.sleep(1)

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
        p.press('pagedown')
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
                break


        # Preencher campos
        for linha in data_frame.itertuples():
            for c in range(1, 8):
                p.press('pagedown')
                p.sleep(0.5)

                cont = 0 
                while (cont < 10):
                    try:
                        print(f'buscando imagem campo{c}_{cont}.png')
                        cont += 1
                        p.sleep(1)
                        x, y = p.locateCenterOnScreen(f'C:\\Curso02_github\\desafio_Final\\campos\\campo{c}_{cont}.png', confidence=0.9)
                        if (x is not None) or (y is not None):
                            print(f'\nACHOU imagem campo{c}_{cont}')
                            p.click(x, (y+30))
                            p.sleep(2)
                            print(f'CLICOU imagem campo{c}_{cont}')
                            p.write(str(linha[c+1]))
                            print(f'DIGITOU {linha[c+1]}\n')
                            break
                    except:
                        exc_type, error, line = sys.exc_info()
                        error_msg = f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n'
                        p.alert(error_msg)
                        p.sleep(0.5)
            
            find_buttom = 0
            while (find_buttom < 15):
                find_buttom += 1
                bt = p.locateCenterOnScreen(f'C:\\Curso02_github\\desafio_Final\\botao_submit.png', confidence=0.9)
                if (bt is not None):
                    p.click(bt)
                    print('clicou submit')
                    break
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')    
                
def main():
    data_frame = abrir_desafio_e_ler_planilha()
    preencher_campos(data_frame)


if (__name__ == '__main__'):
    o.system('taskkill /f /im chrome.exe')
    o.system('cls')
    main()