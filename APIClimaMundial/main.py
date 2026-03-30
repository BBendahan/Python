import sys
import requests
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout,
                             QPushButton, QLineEdit)
from PyQt5.QtCore import (Qt)


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel('Enter city Name:', self)
        self.city_input = QLineEdit(self)
        self.acceptButton = QPushButton('Get Weather',self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)

        self.acceptButton.clicked.connect(self.get_weather) 
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Wheather APP')
        vbox = QVBoxLayout() 

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.acceptButton)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)

        self.setLayout(vbox)
        
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName('city_label')
        self.temperature_label.setObjectName('temperature_label')
        self.emoji_label.setObjectName('emoji_label')

        self.setStyleSheet(""" 
                            QLabel{
                           font-size: 30px;
                           font-family: calibri;
                           }  
                           QLabel#city_label{
                           font-style: italic;
                           }
                           QLabel#temperature_label{
                           font-size: 50px;
                           }
                           QLabel#emoji_label{
                           font-size: 70px;
                           font-family: Segoe UI emoji;
                           }
                           QPushButton{
                           font-size: 20px;
                           font-weight: bold;
                           }
                           QLineEdit{
                           font-size: 30px;
                           font-family: calibri;
                           }
        """)

    def get_weather(self):
        api_key = 'bd5e378503939ddaee76f12ad7a97608'
        city_name = self.city_input.text()
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

        try: 
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            print(data)

            if data['cod'] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400:
                    self.display_error('Bad request\nPlease Check your input')
                case 401:
                    self.display_error('Unauthorized\nInvalid API key')
                case 403:
                    self.display_error('Forbidden\nAccess is denied')
                case 404:
                    self.display_error('Not found\nCity Not Found')
                case 500:
                    self.display_error('Internal Server Error\nPlease Try again Later')
                case 501:
                    self.display_error('Bad gateway\nInvalid response from server')
                case 503:
                    self.display_error('Server is down\n Service Unavailable')
                case 504:
                    self.display_error('Gateway Timeout\n No response from the server')
                case _: 
                    self.display_error('http error ocurred')
        except requests.exceptions.RequestException:
            self.display_error(response.status_code)
        except requests.exceptions.ConnectionError:
            self.display_error('Connection error:\nCheck your internet connection')
        except requests.exceptions.Timeout:
            self.display_error('Timeout error\n The request timed out')
        except requests.exceptions.TooManyRedirects:
            self.display_error('Too Many Redirects\n Check the url')
        except requests.exceptions.RequestException as req_error:
            self.display_error(f'Request Error:\n{req_error}')
    def display_error(self, message):
        self.temperature_label.setText(message)
        self.temperature_label.setStyleSheet('font-size: 30px')
        self.emoji_label.setText('⚠')
    
    def display_weather(self, data):
        self.temperature_label.setStyleSheet('font-size: 50px')
        self.temperature_label.setText(f'{data['main']['temp']-273:.0f}°C')
        match data['weather'][0]['id']:
            case _ if 200 <= data['weather'][0]['id'] <= 232:
                self.emoji_label.setText('⛈')
            case _ if 300 <= data['weather'][0]['id'] <= 321:
                self.emoji_label.setText('⛅')
            case _ if 500 <= data['weather'][0]['id'] <= 531:
                self.emoji_label.setText('🌧')
            case _ if 600 <= data['weather'][0]['id'] <= 622:
                self.emoji_label.setText('❄')
            case _ if 701 <= data['weather'][0]['id'] <= 741:
                self.emoji_label.setText('🌫')
            case _ if 801 <= data['weather'][0]['id'] <= 804:
                self.emoji_label.setText('☁')
            case 762:
                self.emoji_label.setText('🌋')
            case 771:
                self.emoji_label.setText('💨')
            case 781:
                self.emoji_label.setText('🌪')
            case 800:
                self.emoji_label.setText('🌞')
            case _:
                self.emoji_label.setText('')
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wheatherApp = WeatherApp()
    wheatherApp.show()
    sys.exit(app.exec_())