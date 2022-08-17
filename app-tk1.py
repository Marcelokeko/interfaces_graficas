## Lib grafica tkinter padrao do python

import tkinter as tk

# criar janela principal

window = tk.Tk()

saudacao = tk.Label(text='Ola Essa é a LIB Tkinter')
saudacao1 = tk.Label(text='Ola Essa é a LIB Tkinter')

saudacao.pack()
saudacao1.pack()

# Executar

window.mainloop()