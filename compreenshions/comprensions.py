#list comprehensions
array = [numero * 3 for numero in range(1,7+1)]
print(array)
#dict comprehensions
chaves = 'feliph'
valores = [0,1,2,3,4,5]
mist = {chaves[i]: valores[i] for i in range(0,6)}
print(mist)
#logica usando list comprehensions e if comprehensions
numeros = [i for i in range(1,6)]
res = {num:('par' if num % 2 == 0 else 'impar')for num in numeros}
print(res.values())
# import sys

# def DisplayPopups(p_title=None, p_msg=None, p_secs=None, p_icon=None, p_print=False, p_upper=False):
#     # pip install plyer
#     # from plyer import notification
#     try:
#     # Maximum lenght = 64
#     # Call .upper() if p_upper == True
#         if p_title != None:
#             p_title = p_title[0:64] if len(p_title) > 64 else p_title
#             p_title = p_title.upper() if p_upper else p_title
#         if p_msg != None:
#             p_msg = p_msg[0:64] if len(p_msg) > 64 else p_msg
#             p_msg = p_msg.upper() if p_upper else p_msg

#     # Default values
#         title_popup = '' if p_title is None else p_title
#         message_popup = '' if p_msg is None else p_msg
#         icon_popup = 'robot_apr' if p_icon is None else p_icon
#         seconds_popup = 0 if p_secs is None else p_secs
#         txt_default = 'No text in parameters => title_popup and message_popup!'
#         title_popup = txt_default if title_popup == '' and message_popup == '' else title_popup

#     # Display notification
#         notification.notify(
#         title=title_popup,
#         message=message_popup,
#         app_icon=f'C:\\Temp\\Robo001\\GENERAL\\icons\\{icon_popup}.ico', # Cliente
#         # app_icon=f'C:\\APRTech\\orbenk\\Robo001\\GENERAL\\icons\\{icon_popup}.ico', # Local
#         timeout=seconds_popup,
#         )

#     # Print title and message value if p_print == True
#         print(f'{title_popup}') if p_print and title_popup != '' else None
#         print(f'{message_popup}') if p_print and message_popup != '' else None
#     except:
#         exc_type, error, line = sys.exc_info()
#         msg_error = f'ERROR: {error}\nTYPE: {exc_type}\nFUNC: {sys._getframe().f_code.co_name}\nLINE: {line.tb_lineno}\n'
#         print(msg_error)
