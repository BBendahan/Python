# graphical user interface

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QWidget, QVBoxLayout, QHBoxLayout, 
                             QGridLayout, QPushButton)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('GUI TEST')
        self.setGeometry(450, 150, 500, 500)
        self.setWindowIcon(QIcon('Microsoft_logo.svg.png'))
        
        self.initUI()


    def initUI(self):
        central_Widget = QWidget()
        self.setCentralWidget(central_Widget)
        label1 = QLabel('#1')
        label1.setStyleSheet('background-color: Red')
        label2 = QLabel('#2')
        label2.setStyleSheet('background-color: Blue')
        label3 = QLabel('#3')
        label3.setStyleSheet('background-color: Green')
        label4 = QLabel('#4')
        label4.setStyleSheet('background-color: Black')
        label5 = QLabel('#5')
        label5.setStyleSheet('background-color: Brown')

        grid = QGridLayout()
        grid.addWidget(label1, 0,0)
        grid.addWidget(label2 , 0, 1)
        grid.addWidget(label3 , 1 , 0)
        grid.addWidget(label4 ,2,2)
        grid.addWidget(label5, 3, 3)

        central_Widget.setLayout(grid)
    #botones 
        self.button = QPushButton('Click me', self)
        self.button.setGeometry(200, 450, 100, 30)
        self.button.setStyleSheet('background-color: Yellow;'
                            'font-size: 30;')
        self.button.clicked.connect(self.on_click)
    
    def on_click(self):
        print('Button clicked!')
        self.button.setText('Clicked!')

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()





