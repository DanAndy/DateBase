import sys 
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QWidget, QApplication
import viborbd
import service

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("handler\\viborbd.ui", self)
        self.pushButton.clicked.connect(self.gotoScreen2)
        self.pushButton_2.clicked.connect(self.gotoScreen3)
        self.pushButton_3.clicked.connect(self.gotoScreen4)
        self.pushButton_4.clicked.connect(self.gotoScreen5)

    def gotoScreen2(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoScreen3(self):
        widget.setCurrentIndex(widget.currentIndex()+2)

    def gotoScreen4(self):
        widget.setCurrentIndex(widget.currentIndex()+3)

    
    def gotoScreen5(self):
        widget.setCurrentIndex(widget.currentIndex()+4)


class Screen2(QWidget):
    def __init__(self):
        super(Screen2, self).__init__()
        loadUi("handler\\service.ui", self)

class Screen3(QWidget):
    def __init__(self):
        super(Screen3, self).__init__()
        loadUi("handler\\xexexex.ui", self)


class Screen4(QWidget):
    def __init__(self):
        super(Screen4, self).__init__()
        loadUi("handler\\client.ui", self)


class Screen5(QWidget):
    def __init__(self):
        super(Screen5, self).__init__()
        loadUi("handler\\zakazi.ui", self)


# class Screen4(QWidget):
#     def __init__(self):
#         super(Screen2, self).__init__()
#         loadUi("handler\\service.ui", self)

# class Screen5(QWidget):
#     def __init__(self):
#         super(Screen2, self).__init__()
#         loadUi("handler\\service.ui", self)


#main 
app = QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
mainwindow=MainWindow()
screen2=Screen2()
screen3=Screen3()
screen4=Screen4()
screen5=Screen5()
widget.addWidget(mainwindow)
widget.addWidget(screen2)
widget.addWidget(screen3)
widget.addWidget(screen4)
widget.addWidget(screen5)
widget.setFixedHeight(1000)
widget.setFixedWidth(1000)
#widget.colorCount("#212121")
widget.show()


try:
    sys.exit(app.exec_())
except:
    print("exeting")