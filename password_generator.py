from typing import Self
from PyQt6.QtWidgets import *
from new_interface import *
import sys
from PyQt6 import *
from PyQt6 import QtCore, QtGui, QtWidgets
import random


class Window(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.password_lenght.valueChanged.connect(self.lenght)
        self.password_count.valueChanged.connect(self.count)
        self.pushButton_add_upper.clicked.connect(self.upper_case)
        self.pushButton_add_small.clicked.connect(self.lower_case)
        self.pushButton_add_digitts.clicked.connect(self.add_digits)
        self.pushButton_add_punct.clicked.connect(self.add_punct)
        self.pushButton_add_del_chars.clicked.connect(self.del_chars)
        self.pushButton_generate.clicked.connect(self.generate)
        self.pushButtonSubmit.clicked.connect(self.submit)

        self.listWidget.addItems([])
        self.password = []
        self.chars = ''
        self.passwords = ''


    def lenght(self,lenght):
        try:
            self.lenght  = lenght
            return self.lenght
        except ValueError:
            print('Error')

    def count(self,count):
        try:
            self.count  = count
            return self.count
        except ValueError:
            print('Error')
            
    def upper_case(self):
        self.chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return self.chars

    def lower_case(self):
        self.chars += 'abcdefghijklmnopqrstuvwxyz'
        return self.chars
    
    def add_digits(self):
        self.chars += '0123456789'
        return self.chars

    def add_punct(self):
        self.chars +='!#$%&*+-=?@^'
        return self.chars


    def del_chars(self):
        for c in 'il1Lo0O':
            self.chars = self.chars.replace(c, '')
        return self.chars

    def submit(self):
        for _ in range(self.count * self.lenght):
            self.passwords += random.choice(self.chars)

           
        return self.passwords

    def generate(self):
        row = ''
        for _ in range(self.count):
            row += self.passwords[:self.lenght]
            self.passwords = self.passwords[self.lenght:]
            self.listWidget.addItems([row])
            row = ''
      

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())

        