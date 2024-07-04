from PyQt5.QtWidgets import *
from designs.login_form_ui import Ui_Form
from homepage_app import HomepageApp
import sys


class LoginApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui_design = Ui_Form()
        self.ui_design.setupUi(self)
        self.homepage = HomepageApp()

        self.CreateConnects()
    
    def CreateConnects(self):
        self.ui_design.login_button.clicked.connect(self.login_clicked)
        self.ui_design.sign_button.clicked.connect(self.sign_in_clicked)
    
    def login_clicked(self):
        username = self.ui_design.username_lineedit.text()
        password = self.ui_design.password_line.text()

        print(f"Username: {username}\nPassword: {password}\n")

        self.ui_design.username_lineedit.clear()
        self.ui_design.password_line.clear()

        self.show_homepage(username)
    
    def sign_in_clicked(self):
        username = self.ui_design.username_lineedit_sign.text()
        password = self.ui_design.password_line_sign.text()

        print(f"Account Created ['name': '{username}', 'password': '{password}']")

        self.ui_design.username_lineedit_sign.clear()
        self.ui_design.password_line_sign.clear()

        self.show_homepage(username)
    
    def show_homepage(self, username):
        self.homepage.show()
        self.homepage.ui_design.label.setText(username)

        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    app.exec_()
