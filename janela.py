import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QTextEdit, QDialog

class MainJanela(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Primeira Guia')
        self.setGeometry(100, 100, 400, 300)

        self.btn_open_secondary = QPushButton('Guia Secundária', self)
        self.btn_open_secondary.clicked.connect(self.openSecondary)

        self.message_display = QTextEdit(self)
        self.message_display.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.btn_open_secondary)
        layout.addWidget(self.message_display)
        self.setLayout(layout)

        self.show()

    def updateMessage(self, name, message):
        current_text = self.message_display.toPlainText()
        new_text = f'{current_text}\n{name}: {message}'
        self.message_display.setPlainText(new_text)

    def openSecondary(self):
        self.secondary_window = SecondaryJanela(self)
        self.secondary_window.show()

class SecondaryJanela(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Janela Secundária')
        self.setGeometry(200, 200, 300, 200)

        self.name_input = QLineEdit(self)
        self.message_input = QLineEdit(self)

        self.btn_send = QPushButton('Enviar', self)
        self.btn_send.clicked.connect(self.sendClicked)

        layout = QVBoxLayout()
        layout.addWidget(self.name_input)
        layout.addWidget(self.message_input)
        layout.addWidget(self.btn_send)
        self.setLayout(layout)

    def sendClicked(self):

        name = self.name_input.text()
        message = self.message_input.text()

        if name and message:
            self.parent().updateMessage(name, message)
            self.accept()
        else:
            self.setWindowTitle('Campos em branco! Insira nome e mensagem.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainJanela = MainJanela()
    sys.exit(app.exec_())
