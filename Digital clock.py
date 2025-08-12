#python PyQt5 Digital clock
import sys 
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import QTimer,QTime,Qt
from PyQt5.QtGui import QFont,QFontDatabase
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Digital clock")
        self.setGeometry(600,400,300,100)
        vbox = QVBoxLayout()
        vbox.addWidget(self.time)
        self.setLayout(vbox)
        self.time.setAlignment(Qt.AlignCenter)
        self.time.setStyleSheet("font-size:150px;"
                                "font-family:Arial;"
                                "color : hsl(111,100%,50%);")
        self.setStyleSheet("background-color:black;")
        font_id = QFontDatabase.addApplicationFont("C:\\Users\\vasan\\OneDrive\\Desktop\\DigitalClockProgram\\DS-DIGII.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family,150)
        self.time.setFont(my_font)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time.setText(current_time)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
