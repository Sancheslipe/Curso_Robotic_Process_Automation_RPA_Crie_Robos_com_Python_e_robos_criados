# import time 
# import sys
# from plyer import notification 
  
  
# if __name__=="__main__": 
#     try:
#         notification.notify(title='TITULO', message='MENSAGEM', app_name='FELIPE', app_icon=r"C:\Users\Ana Paula\Downloads\picwish.ico", timeout=10, ticker='ticker', toast=False)
#         # notification.notify( 
#         #             title = "HEADING HERE", 
#         #             message=" DESCRIPTION HERE" , 
#         #             app_name='app_name',
#         #                 timeout=2 
#         # ) 
#         time.sleep(3)
#     except:
#         exc_type, error, line = sys.exc_info()
#         print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')

# //array 10 x 10 ?

lista = []


lista = [[35*i+j for j in range(35)] for i in range(35)]
# print(lista)
for l in range(len(lista)):
    for c in range(len(lista[l])):
        print(f'[{lista[l][c]}]', end=' ')
    print()

