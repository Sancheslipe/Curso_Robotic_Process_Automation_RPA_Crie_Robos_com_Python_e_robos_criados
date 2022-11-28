import pyautogui as p 
from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.google.com')
    cont = 0 
    while (cont < 10):
        x = None
        y = None
        try:
            cont += 1
            x, y = p.locateCenterOnScreen(f'C:\\Curso02_github\\atividade_11_playwright\\ima\\maximizar_tela.png', confidence=0.9)
            if (x is not None) or (y is not None):
                p.click(x, y)
                p.sleep(0.1)
        except:
            p.sleep(0.3)
    
    print(f'CLICOU imagem campo')
    page.fill('xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input','acer aspire 5 nitro')
    page.keyboard.press('Enter')
    page.click('xpath=//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[1]/div/a/h3')
    p.sleep(10)