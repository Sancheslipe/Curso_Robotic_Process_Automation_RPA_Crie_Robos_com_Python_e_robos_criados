from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Imovel:
    def __init__(self) -> None:
        self.SITE_LINK = "https://www.imoveis-sc.com.br/florianopolis/alugar/apartamento?utm_term=alugar%20apartamento%20florian%C3%B3polis&utm_campaign=%5BJD%5D+Tr%C3%A1fego+Floripa&utm_source=adwords&utm_medium=ppc&hsa_acc=5223211896&hsa_cam=10815708918&hsa_grp=142039480765&hsa_ad=635584440694&hsa_src=g&hsa_tgt=kwd-321072486189&hsa_kw=alugar%20apartamento%20florian%C3%B3polis&hsa_mt=p&hsa_net=adwords&hsa_ver=3&gclid=Cj0KCQiA99ybBhD9ARIsALvZavXRWTFyZLhbhLfdB2f-86v0C2pn6pta-E9CD2IrZjkib2Inil3MswEaAiEiEALw_wcB"
        self.SITE_MAP = {
            "buttons" : {
                "descricao":{
                    "xpath": '/html/body/main/div/div/div/div[1]/article[1]/div[1]/p/text()'
                },
                "valor" :{
                    "xpath": "/html/body/main/div/div/div/div[1]/article[1]/div[1]/span/small"
                }
            }   
        }
        self.driver = webdriver.Chrome()
    
    def abrir_e_maximizar_site(self):
        sleep(2)
        self.driver.get(self.SITE_LINK)
        self.driver.maximize_window()


    def pegar_dados(self, quantidade):
        pass
