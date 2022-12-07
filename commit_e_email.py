import sys
import datetime
import atividade_09_automatizar_github.robo_09 as apr
import atividade_07_automatizar_email.robo_07 as send

print('\niniciou\n')

try:
    print('robo rodando...')
    #SEMPRE ALTERAR O NOME DA PASTE SCHEDULE
    dia = datetime.datetime.now().strftime('%A, %d de %B de %Y')
    hora = datetime.datetime.now().strftime('%H:%M:%S')
    apr.bot_09()
    print('deu commit')
    send.enviar_email('fsanches.0502@gmail.com',f'commitado com sucesso {dia} as{datetime.datetime.now().strftime("%H:%M:%S")}')
    print('enviou o email')
    print('robô finalizado')
except:
    exc_type, error, line = sys.exc_info()
    print(f'ERROR: {error}\nCLASS: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE:  {line.tb_lineno}\n')


#esta mensagem é um teste
'''
ERRO REFERENTE Á FALHA DO OUTLOOK PADRÃO!
para solucionar: reinicie a maquina e depois abra o outlook em seguida
ERROR: (-2146959355, 'Falha na execução do servidor', None, None)
CLASS: <class 'pywintypes.com_error'>
FUNC: <module>
LINE:  16
'''
def retorna_cot_eur_ch(dia_ant, driver, msgjson):
    try:
        dia_ant = dia_ant.replace('-', '')
        if dia_ant[0] == '0':
            dia_ant = dia_ant[1:]
        driver.get('https://es.investing.com/currencies/eur-clp-historical-data')

        html = driver.page_source
        tables = pd.read_html(html, decimal=',', thousands='.')
        table = pd.DataFrame(tables[1], dtype=str)

        cot = format(float(table.loc[table['Fecha'] == f'{dia_ant}'][msgjson['ultimo']].values[0]), '.3f')
        return cot
    except Exception as e:
        print(repr(e))
        apr.EnviarEmailAprTech(
            'ATIV004 - Cot moedas', msgjson['emailDestErr'], 'Cot eur/ch retornou 0', '', '', '')
        return '0'

