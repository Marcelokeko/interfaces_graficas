
from tkinter.tix import Form
from PyQt5 import uic
from PySide6 import *
from PyQt5.QtWidgets import QApplication

Form,Window=uic.loadUiType('main.ui')

app= QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()