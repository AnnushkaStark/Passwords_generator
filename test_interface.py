from PyQt6.QtWidgets import *
from my_interface import *
import sys
from PyQt6 import *

import random






class Window(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.my_password = []
        self.chars = ''
        self.passwords = ''
        self.Password_counter.valueChanged.connect(self.value_changed)
        self.password_lenght.valueChanged.connect(self.lenght_changed) 
        self.pushButton.clicked.connect(self.upper_case)
        self.pushButton_2.clicked.connect(self.lower_case)
        self.pushButton_3.clicked.connect(self.add_digits)
        self.pushButton_4.clicked.connect(self.add_punc)
        self.pushButton_5.clicked.connect(self.del_uncorrect)
        self.pushButton_6.clicked.connect(self.gen_password)
        self.pushButton_7.clicked.connect(self.submit)
        self.label_10.setText('')



    def value_changed(self,value):
        self.value = value
        return(self.value)
        

    def lenght_changed(self,lenght):
        self.lenght = lenght
        return(self.lenght)
    
    

    def upper_case(self):
        self.chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return self.chars

    def lower_case(self):
        self.chars += 'abcdefghijklmnopqrstuvwxyz'
        return self.chars
    

    def add_digits(self):
        self.chars += '0123456789'
        return self.chars

    
    def add_punc(self):
        self.chars +='!#$%&*+-=?@^'
        return self.chars

    def del_uncorrect(self):
        for c in 'il1Lo0O':
            self.chars = self.chars.replace(c, '')
        return self.chars

        
    def submit(self):

        for _ in range(self.lenght):
            self.passwords += random.choice(self.chars)
        print(self.passwords, end = ' ')
        print()
            

    def gen_password(self):
        pass     


        
    
    
            
           





app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())












digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^'
chars = ''
password_count =  int(input('Введите количесво паролей для генерации '))
password_lenght = int(input('Введите длину одного парля '))
add_digits = (input("Включать ли цифры 0123456789? (д /н ) "))
add_lowercase_letters = input(('Включать буквы нижнего регистра abcdefghijklmnopqrstuvwxyz ?  ( д / н) ' ))
add_uppercase_letters = input(('Включать буквы верхнего регистра ABCDEFGHIJKLMNOPQRSTUVWXYZ ? ( д / н) '))
add_punctuation  = input(('Включать знаки пунктуации !#$%&*+-=?@^ ? (д / н) '))
add_incorrect_chars = input(('Исключать ли неоднозначные символы il1Lo0O ?  (д/ н) '))



if  add_uppercase_letters == 'д': 
    chars += '0123456789'
if add_lowercase_letters == 'д':
    chars += 'abcdefghijklmnopqrstuvwxyz'
if add_uppercase_letters  == 'д':
    chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if add_punctuation  == 'д':
    chars += '!#$%&*+-=?@^'
if add_incorrect_chars == 'д':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')
         


def generate_password(password_lenght, chars):
    password = ''
    for j in range(password_lenght):
        password += random.choice(chars)
    return password

my_passwords = []
for _ in range(password_count):
    my_passwords.append(generate_password(password_lenght,chars))
for password in my_passwords:
    print(password)

finally_question = input(("Перед тем как ответить на вопрос сохраните сгенерированные пароли!!! Вам удобно исползование генератора паролей (д\н)? "))


