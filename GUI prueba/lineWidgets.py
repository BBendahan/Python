# graphical user interface

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLineEdit, QPushButton)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt 
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('GUI TEST')
        self.setGeometry(450, 150, 500, 500)
        self.setWindowIcon(QIcon('Microsoft_logo.svg.png'))

        self.line_edit = QLineEdit(self)
        self.button = QPushButton('Submit', self)
        self.button.clicked.connect(self.on_submit)
        self.initUI()


    def on_submit(self):
        text = self.line_edit.text().capitalize()
        self.line_edit.clear()
        print(f'Your name is: {text}')

    def initUI(self):
        
        self.line_edit.setGeometry(100, 200, 300, 40)
        self.line_edit.setPlaceholderText('Enter your name')
        self.setStyleSheet('font-size: 25px;'
                                    'font-family: Arial;')
        
        self.button.setGeometry(200, 300, 100, 40)
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()





