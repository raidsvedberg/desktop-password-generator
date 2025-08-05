import sys
import random
import requests
import webbrowser
import os
from PyQt5 import QtWidgets
import design_password


class ExampleApp(QtWidgets.QMainWindow, design_password.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ButtonGenerate.clicked.connect(self.on_click)
        self.ButtonGenerate.clicked.connect(self.btn_clicked)
        self.ButtonExit.clicked.connect(self.close)
        self.ButtonBored.clicked.connect(get_bored)
        self.ButtonHard.clicked.connect(complaints)

    def btn_clicked(self):
        if not self.password():
            self.label.setText("Passwords are null")
            self.label.setStyleSheet("color: rgb(255, 0, 0);")
            self.label.adjustSize()
        else:
            self.label.setText("Passwords are generated")
            self.label.setStyleSheet("color: rgb(30, 50, 255);")
            self.label.adjustSize()

    def password(self):
        p = self.number_password.text()
        n = self.number_symbols.text()
        chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        passwords = []
        try:
            for r in range(int(p)):
                password = ''
                for m in range(int(n)):
                    password += random.choice(chars)
                passwords.append(password)
            return "\n".join(passwords)
        except ValueError:
            pass


    def on_click(self):
        self.textPassword.setText(self.password())

def toggle_fullscreen(self):
    if self.isFullScreen():
        self.showNormal()
    else:
        self.showMaximized()

def get_bored():
    url = "https://en.wikipedia.org/wiki/Special:Random"
    article_page = requests.get(url)
    webbrowser.open(article_page.url)
    return True

def complaints():
    r = random.randint(0, 100)
    try:
        f = open(f"complaints_number_{r}.txt", "x")
        f.write("Tell me about it here. Safe space\n")
        file_path = f'complaints_number_{r}.txt'
        os.startfile(file_path)
    except FileExistsError:
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    toggle_fullscreen(window)
    app.exec()


if __name__ == '__main__':
    main()
