# graphical user interface

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QWidget, QVBoxLayout, QHBoxLayout, 
                             QGridLayout)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('GUI TEST')
        self.setGeometry(450, 150, 500, 500)
        self.setWindowIcon(QIcon('Microsoft_logo.svg.png'))
        self.setFont(QFont('times new roman', 30))
        label = QLabel('que onda la banda', self)
        label.setGeometry(90,25, 320, 200)
        label.setStyleSheet('color: Black;'
                            'background-color: White;' 
                            'font-weight: bold;'
                            'text-decoration: underline;')
        label.setAlignment(Qt.AlignVCenter) #Qt.AlignTop , Qt.AlignBottom 
        label.setAlignment(Qt.AlignHCenter) #Qt.AlignLeft , Qt.AlignRight
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        image = QLabel(self)
        image.setGeometry(90,190,320,320)
        pixeles = QPixmap('Microsoft_logo.svg.png')
        image.setPixmap(pixeles)
        image.setScaledContents(True)
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

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()





