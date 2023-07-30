from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit
import random
class PasswordGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('Генератор паролей')
        self.setGeometry(100,100,200,300)
        self.password_count_input = QLineEdit(self)
        self.password_count_input.setPlaceholderText('Введите количество паролей')
        self.password_length_input = QLineEdit(self)
        self.password_length_input.setPlaceholderText('Введите длину пароля')
        self.generate_button = QPushButton('Сгенерировать',self)
        self.generate_button.clicked.connect(self.handle_input)
        self.passwords_label= QLabel(self)

        layout = QVBoxLayout()

        layout.addWidget(self.password_count_input)
        layout.addWidget(self.password_length_input)
        layout.addWidget(self.passwords_label)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def handle_input(self):
        digits ='0123456789'
        lowercase_latter = 'abcdefghijklnopqrstuvwxyz'
        uppercase_latter =  'ABCDEFGHIJKLMNOPQSTUVWXYZ'
        punctuation = '!@#%$&*+=^?'
        chars = ''
        password_count = int(self.password_count_input.txt())
        password_lenght = int(self.password_length_input.txt())
        add_digits = True
        add_lowercase_letter = True
        add_uppercase_letter = True
        add_punctuation = True
        add_incorrect_chars = True

        if add_digits:
            chars += digits
        if add_lowercase_letter:
            chars += lowercase_latter
        if  add_uppercase_letter:
            chars += uppercase_latter
        if add_punctuation:
            chars += punctuation
        if add_incorrect_chars:
            for c in 'ilL1o0O':
                chars = chars.replace(c,'')
           

        my_password = []
        for _ in range(password_count):
            my_password.append(self.generate_password(password_lenght,chars))

            password_text ='\n'.join(my_password)
        
            self.passwords_label.setText(password_text)
        
    def generate_password(self,password_lenght,chars):
        password = ''
        for j in range(password_lenght):
            password += random.choice(chars)
        return password
if __name__ =='__main__':
    app = QApplication([])
    window = PasswordGenerator()
    window.show()
    app.exec()




        