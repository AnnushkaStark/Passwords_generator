# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 794)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Password_counter = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.Password_counter.setGeometry(QtCore.QRect(0, 51, 101, 21))
        self.Password_counter.setObjectName("Password_counter")
        self.password_lenght = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.password_lenght.setGeometry(QtCore.QRect(0, 110, 101, 22))
        self.password_lenght.setObjectName("password_lenght")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 30, 281, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 90, 231, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 160, 271, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 173, 141, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 240, 141, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 220, 161, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 310, 141, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 290, 141, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 370, 141, 24))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 350, 181, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 430, 141, 24))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 410, 291, 16))
        self.label_7.setObjectName("label_7")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 550, 161, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 530, 191, 16))
        self.label_8.setObjectName("label_8")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 490, 151, 24))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 470, 141, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(0, 600, 581, 161))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Количество паролей?"))
        self.label_2.setText(_translate("MainWindow", "Длина пароля?"))
        self.label_3.setText(_translate("MainWindow", "Добавить заглавные буквы?"))
        self.pushButton.setText(_translate("MainWindow", "UpperCaseLatter"))
        self.pushButton_2.setText(_translate("MainWindow", "LowerCaseLatter"))
        self.label_4.setText(_translate("MainWindow", " Добавить строчные буквы?"))
        self.pushButton_3.setText(_translate("MainWindow", "Add_digits"))
        self.label_5.setText(_translate("MainWindow", "Добавить цифры?"))
        self.pushButton_4.setText(_translate("MainWindow", "Add_punctuation"))
        self.label_6.setText(_translate("MainWindow", "Добавить знаки пунктуации?"))
        self.pushButton_5.setText(_translate("MainWindow", "Del_incorrect_chars"))
        self.label_7.setText(_translate("MainWindow", "Убрать спорные символы (l0OI) ?"))
        self.pushButton_6.setText(_translate("MainWindow", "Generation"))
        self.label_8.setText(_translate("MainWindow", "Сгенерировать?"))
        self.pushButton_7.setText(_translate("MainWindow", "Submit"))
        self.label_9.setText(_translate("MainWindow", "применить настройки"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
