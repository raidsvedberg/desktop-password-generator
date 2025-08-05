import sys
import glob

import project
from PyQt5 import QtWidgets


class TestGenerator :
    def test_on_click(self):
        test_app = QtWidgets.QApplication(sys.argv)
        window = project.ExampleApp()
        self.ButtonGenerate = QtWidgets.QPushButton()
        window.show()
        window.ButtonGenerate.click()
        self.label = QtWidgets.QLabel()
        assert window.label.text() == "Passwords are null"

    def test_btn_clicked(self):
        test_app = QtWidgets.QApplication(sys.argv)
        window = project.ExampleApp()
        self.ButtonGenerate = QtWidgets.QPushButton()
        window.show()
        window.ButtonExit.click()
        assert window.ButtonExit.close()

    def test_toggle_fullscreen(self):
        test_app = QtWidgets.QApplication(sys.argv)
        window = project.ExampleApp()
        window.show()
        project.toggle_fullscreen(window)
        assert window.isMaximized()

    def test_get_bored(self):
        test_app = QtWidgets.QApplication(sys.argv)
        window = project.ExampleApp()
        self.ButtonBored = QtWidgets.QPushButton()
        window.ButtonBored.click()
        assert project.get_bored() == True

    def test_complaints(self):
        test_app = QtWidgets.QApplication(sys.argv)
        window = project.ExampleApp()
        self.ButtonComplaints = QtWidgets.QPushButton()
        window.ButtonHard.click()
        name = glob.glob('complaints_number_*')
        if name:
            assert True
        else:
            assert False

