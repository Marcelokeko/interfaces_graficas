import PySimpleGUI as sg 

#Criar uma janela

layout = [[sg.Text('Qual Seu Nome ?')],
        [sg.Input(key='-INPUT-')],
        [sg.Text(size=(40,1),key='-OUTPUT-')],
        [sg.Button('OK'),sg.Button("Sair")]]

# Criar a janela com os itens acima

window = sg.Window('Titulo do programa',layout)

# Criar a açoes do programa e botoes

while True:
    event,values=window.read()
    # Validaçao usuario sair e fechar a janela
    
    if event == sg.WINDOW_CLOSED or event== 'Sair':
        break
    # Criar a saida do imput em console
    window["-OUTPUT-"].update("Olá "+values['-INPUT-']+' , Gravando saida em console')
    
window.close()