import sys
import requests
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QPushButton,QLineEdit,QVBoxLayout)
from PyQt5.QtCore import Qt #this is used for alignment
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter the city name:",self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather",self)
        self.temperature_Label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description= QLabel(self)
        
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setGeometry(650,300,500,500)
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_Label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description)
    
        self.setLayout(vbox)
        
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_Label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description.setAlignment(Qt.AlignCenter)
        
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_Label.setObjectName("temperature_Label")
        self.emoji_label.setObjectName("emoji_label")
        self.description.setObjectName("description")
        
        self.setStyleSheet("""
                           QLabel,QPushButton{
                               font-family : calibri;
                               
                           }
                           QLabel#city_label{
                               font-size:40px;
                               font-style:italic;
                               
                           }
                           QLineEdit#city_input{
                               font-size:40px;
                           }
                           QPushButton#get_weather_button{
                               font-size : 50px;
                               font-weight:bold;
                               
                           }
                           QLabel#temperature_Label{
                               font-size:75px;
                           }
                           QLabel#emoji_label{
                               font-size:100px;
                               font-family:sepoe UI emoji;
                           }
                           QLabel#description{
                               font-size:50px;
                               
                           }
                           """)
        self.get_weather_button.clicked.connect(self.get_weather)
    def get_weather(self):
        api_key = "954e4226cf3b91e1f97d93da530a2164"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data["cod"]==200:
                self.display_weather(data)
        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400:
                    self.display_error("Bad request: \nplease check your input")
                case 401:
                    self.display_error("Unauthorized: \ninvalid api key")
                case 403:
                    self.display_error("Forbidden: \naccess is denied")
                case 404:
                    self.display_error("Not found:\ncity not found")
                case 500:
                    self.display_error("Internal server error: \nplease try again later")
                case 502:
                    self.display_error("Bad gateway: \nInvalid response from the server")
                case 503:
                    self.display_error("Service unavailable: \nserver is down")
                case 504:
                    self.display_error("Gateway timeout: \nno response from the server")
                case _:
                    self.display_error("HTTPError occured:\n{http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout error:\nThe request timeout error")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects:\nCheck the url")
        except requests.exceptions.RequestException:
            self.display_error("request error:\n{req_error}")
            
        
    def display_error(self,message):
        self.temperature_Label.setStyleSheet("font-size:30px;")
        self.temperature_Label.setText(message)
        self.emoji_label.clear()
        self.description.clear()
    def display_weather(self,data):
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_k * 9/5) - 459.67
        self.temperature_Label.setStyleSheet("font-size:75px;")
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]
        self.temperature_Label.setText(f"{temperature_f:.0f}°F")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description.setText(weather_description)
    @staticmethod
    def get_weather_emoji(weather_id):
        if  weather_id >= 200 and weather_id <=232:
            return "⛈️"
        elif 300<= weather_id<=323:
            return "🌨️"
        elif 500<=weather_id<=531:
            return "🌧️"
        elif 600<=weather_id<=622:
            return "⛄"
        elif 701<=weather_id<=741:
            return "🌫️"
        elif weather_id == 762:
            return "🔥"
        elif weather_id == 771:
            return "💨"
        
        elif weather_id==781:
            return "🌪️"
        elif weather_id==800:
            return "😎"
        elif 801<=weather_id<=804:
            return "😶‍🌫️"
        else:
            return ""
        
if __name__ == "__main__":
        app = QApplication(sys.argv)
        weatherapp = WeatherApp()
        weatherapp.show()
        sys.exit(app.exec_())
