import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QWidget, QHBoxLayout)
from PyQt5.QtGui import QIcon

 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('GUI TEST')
        self.setWindowIcon(QIcon('Microsoft_logo.svg.png'))

        self.button1 = QPushButton('#A')
        self.button2 = QPushButton('#B')
        self.button3 = QPushButton('#C')

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        Hbox = QHBoxLayout()
        Hbox.addWidget(self.button1)
        Hbox.addWidget(self.button2)    
        Hbox.addWidget(self.button3)
        central_widget.setLayout(Hbox)
        self.button1.setObjectName('button1')
        self.button2.setObjectName('button2')
        self.button3.setObjectName('button3')

        self.setStyleSheet("""
            QPushButton {
                font-size: 40px;
                font-family: Arial;
                padding: 10px 75px;
                margin : 10px;
                border-radius: 10px;
                border: 2px solid;                
            }
            QPushButton#button1 {
                background-color: hsl(0, 100%, 50%);}
            QPushButton#button2 {
                background-color: hsl(120, 100%, 50%);}
            QPushButton#button3 {
                background-color: hsl(240, 100%, 50%);}
              QPushButton#button1:hover {
                background-color: hsl(0, 100%, 70%);}
            QPushButton#button2:hover {
                background-color: hsl(120, 100%, 70%);}
            QPushButton#button3:hover {
                background-color: hsl(240, 100%, 70%);}
                                          
                           """)


    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()



