from PyQt5.QtWidgets import *
from designs.menu_form_ui import Ui_Form
import sys

class MenuApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui_design = Ui_Form()
        self.ui_design.setupUi(self)

        self.CreateConnects()

    def CreateConnects(self):
        self.ui_design.radioButton.toggled.connect(self.menu_select)
        self.ui_design.radioButton_2.toggled.connect(self.menu_select)
        self.ui_design.radioButton_3.toggled.connect(self.menu_select)
        self.ui_design.radioButton_4.toggled.connect(self.menu_select)
        self.ui_design.radioButton_5.toggled.connect(self.menu_select)
    
    def menu_select(self):
        select = self.sender()

        if select.isChecked():
            selected = select.text()
            print(selected)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuApp()
    window.show()
    app.exec_()
