import win32com.client as win32
import sys
import os

def enviar_email(remetente,str_mensagem):
    #criar a integracao com o outlook
    outlook = win32.Dispatch('outlook.application')
    #criar email
    email = outlook.CreateItem(0)
    #configurar as informacoes do seu e-mail
    email.To = remetente
    email.Subject = 'E-mail automático do python'
    email.HTMLBody = f'{str_mensagem}'
    email.Send()
    print('email enviado')


def bot_007():
    try:
        remetente = input('digite aqui o email de seu remetente: ')
        mensagem = input('digite aqui a sua mensagem\n')
        enviar_email(remetente,mensagem)
    except:
        exc_type, error, line = sys.exc_info()
        print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


if (__name__ == "__main__"):
    os.system('cls')
    bot_007()
    print('robô executado com sucesso!')


    '''
    ERROR: (-2146959355, 'Falha na execução do servidor', None, None)
    CLASS: <class 'pywintypes.com_error'>
    FUNC: bot_007
    LINE:  22
    '''