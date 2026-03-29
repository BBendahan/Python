import sys
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QPushButton,
                             QWidget, QVBoxLayout, QLabel)
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtCore import Qt, QTimer, QTime


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time=QTime(0,0,0,0)
        self.time_label = QLabel("00:00:00:00", self)
        self.timer = QTimer(self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.initUI()

        self.stop_button.clicked.connect(self.stop)
        self.start_button.clicked.connect(self.start)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)
        
    

    
    def initUI(self):
        self.setWindowTitle('Stopwatch')
        self.setGeometry(400, 250, 600, 200)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        
        self.setLayout(vbox)
            
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)
        
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
                                QPushButton {
                                    font-size: 50px;
                                    color: black;
                                    background-color: grey;
                                    border: 5px solid black;
                                    border-radius: 10px;
                                    font-family: calibri;
                                }
                                QLabel {
                                    font-size: 130px;
                                    color: black;
                                    background-color: grey;
                                    border: 5px solid black;
                                    border-radius: 10px;
                                    font-family: Consolas;
                           }
                                """)
        

    def start(self):
        self.timer.start(10)  
    def stop(self):
        self.timer.stop()
    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))
            
    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:02}"
    def update_display(self):
        self.time = self.time.addMSecs(10)  
        self.time_label.setText(self.format_time(self.time))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())