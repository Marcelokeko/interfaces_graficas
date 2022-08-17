from PyQt5.QtWidgets import *

app = QApplication([])
button = QPushButton('Botão Clique')

# Funçao botao

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('Mensagem Gerada com Sucesso')
    alert.exec()
    
# Ação de botão

button.clicked.connect(on_button_clicked)
button.show()
app.exec()