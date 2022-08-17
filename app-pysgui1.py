## Utilizando pysimpleGUI para criaçao de interfaces graficas

import PySimpleGUI as sg 

layout=[[sg.Text('Ola Estou criando uma Mensagem')],[sg.Button('OK')]]

# Criar a janela

window = sg.Window('Titulo do Programa',layout)

# Criar a açao ou loop do evento

while True:
    event,values = window.read()
    # Finaliza o programa
    
    if event == 'OK' or event ==sg.WIN.CLOSED:
        break
    
window.close()