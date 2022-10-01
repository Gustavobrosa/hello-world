# Gravador de programas 
import sys
from datetime import datetime

#for parametro in sys.argv:
#    print(parametro, type(parametro))

# exemplo inha de comando
#                             python3 grava.py 01/07/2022 20:59 21:02


print (sys.argv)
 
data_e_hora_ini_texto = sys.argv[1] + ' ' + sys.argv[2]
data_e_hora_fim_texto = sys.argv[1] + ' ' + sys.argv[3]
data_e_hora_ini = datetime.strptime(data_e_hora_ini_texto, '%d/%m/%Y %H:%M')
data_e_hora_fim = datetime.strptime(data_e_hora_fim_texto, '%d/%m/%Y %H:%M')

data_e_hora_atuais = datetime.now()
print (data_e_hora_atuais)

# loop aguarda horario de inicio
print ('Aguardando horário de início...')
while data_e_hora_atuais < data_e_hora_ini:
    data_e_hora_atuais = datetime.now()
print ('Gravando...')

# loop aguarda horario de fim
while  data_e_hora_atuais < data_e_hora_fim:
    data_e_hora_atuais = datetime.now()
print ('Fim da gravação')

from pynput.mouse import Button, Controller
mouse = Controller()
#print (mouse.position)
#mouse.position = (120, 320)
print (mouse.position)
mouse.click(Button.right)
mouse.move(5,50)
print (mouse.position)

'''
from pynput.keyboard import Key, Controller
keyb = Controller()
#keyb.type('Olá mundo')
with keyb.pressed(Key.alt):
    keyb.press(Key.tab)
    keyb.release(Key.tab)
with keyb.pressed(Key.alt):
    keyb.press('p')
    keyb.release('p')
keyb.press(Key.up)
keyb.release(Key.up)
'''





