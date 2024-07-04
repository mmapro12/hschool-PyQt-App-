from PyQt5.QtWidgets import *
from designs.home_page_ui import Ui_MainWindow
import sys


class HomepageApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui_design = Ui_MainWindow()
        self.ui_design.setupUi(self)

        self.CreateConnects()

    def CreateConnects(self):
        self.ui_design.create_button.clicked.connect(self.create_clicked)
    
    def create_clicked(self):
        username = self.ui_design.username_lineedit.text()
        password = self.ui_design.password_lineedit.text()

        print(f"Account Created ['name': '{username}', 'password': '{password}']")

        self.ui_design.username_lineedit.clear()
        self.ui_design.password_lineedit.clear()

        self.add_person(username, password)
    
    def add_person(self, username, password):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomepageApp()
    window.show()
    app.exec_()
