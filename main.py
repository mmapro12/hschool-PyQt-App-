from PyQt5.QtWidgets import QApplication
from login_app import LoginApp
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    app.exec_()
