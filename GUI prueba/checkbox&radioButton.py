# graphical user interface

from PyQt5.QtWidgets import (QApplication, QMainWindow, QCheckBox
                             , QRadioButton, QButtonGroup)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('GUI TEST')
        self.setGeometry(450, 150, 500, 500)
        self.setWindowIcon(QIcon('Microsoft_logo.svg.png'))

        self.checkbox = QCheckBox('Bananas', self)
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.change)   

        self.radio1 = QRadioButton('VISA', self)
        self.radio2 = QRadioButton('MASTERCARD', self)
        self.radio3 = QRadioButton('AMERICAN EXPRESS', self)
        self.radio4 = QRadioButton('TARJETA', self)
        self.radio5 = QRadioButton('EFECTIVO', self)

        self.metodo = QButtonGroup(self)
        self.metodo.addButton(self.radio4)
        self.metodo.addButton(self.radio5)
        self.tarjeta = QButtonGroup(self)
        self.tarjeta.addButton(self.radio1)
        self.tarjeta.addButton(self.radio2)
        self.tarjeta.addButton(self.radio3)
        
        self.radio1.toggled.connect(self.radio_button_change)
        self.radio2.toggled.connect(self.radio_button_change)
        self.radio3.toggled.connect(self.radio_button_change)
        self.radio4.toggled.connect(self.radio_button_change)
        self.radio5.toggled.connect(self.radio_button_change)

        self.initUI()

    def change(self):
        if self.checkbox.isChecked():
            print('you like bananas')
        else:
            print('you dont like bananas')

    def radio_button_change(self):
        radio_button = self.sender() 
        if radio_button.isChecked():
            print(f'Se seleccionó: {radio_button.text()}')
    
    def initUI(self):
        
        self.checkbox.setGeometry(100, 150, 200, 40)
        self.setStyleSheet('font-size: 30px;'
                                    'font-family: Arial;')
        
        self.radio1.setGeometry(100, 400, 200, 40)
        
        self.radio2.setGeometry(100, 300, 300, 40)
        self.radio3.setGeometry(100, 350, 400, 40)
        self.radio4.setGeometry(100, 200, 400, 40)
        self.radio5.setGeometry(100, 250, 400, 40)
        
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()





