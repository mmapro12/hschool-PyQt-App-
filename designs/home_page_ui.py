# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\designs\home_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("QWidget#frmLogin,QWidget#frmPopup,QWidget#frmHostInfo,QWidget#frmLogout,QWidget#frmConfig,QWidget#frmData,QWidget#frmDefence,QWidget#frmHost,QWidget#frmMain,QWidget#frmPwd,QWidget#frmSelect,QWidget#frmMessageBox{\n"
"    border:1px solid #1B89CA;\n"
"    border-radius:0px;    \n"
"}\n"
"\n"
".QFrame{\n"
"    border:1px solid #5CACEE;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QWidget#widget_title{\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5);\n"
"}\n"
"\n"
"QLabel#lab_Ico,QLabel#lab_Title{\n"
"    border-radius:0px;\n"
"    color: #F0F0F0;\n"
"    background-color:rgba(0,0,0,0);\n"
"    border-style:none;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #5CACEE;\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"    background: none;\n"
"    selection-background-color: #1B89CA;\n"
"}\n"
"\n"
"QLineEdit[echoMode=\"2\"] { \n"
"    lineedit-password-character: 9679; \n"
"}\n"
"\n"
".QGroupBox{\n"
"    border: 1px solid #5CACEE;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
".QPushButton{\n"
"    border-style: none;\n"
"    border: 0px;\n"
"    color: #F0F0F0;\n"
"    padding: 5px;    \n"
"    min-height: 20px;\n"
"    border-radius:5px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
".QPushButton[focusPolicy=\"0\"] {\n"
"    border-style: none;\n"
"    border: 0px;\n"
"    color: #F0F0F0;\n"
"    padding: 0px;    \n"
"    min-height: 10px;\n"
"    border-radius:3px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
".QPushButton:hover{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD);\n"
"}\n"
"\n"
".QPushButton:pressed{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5);\n"
"}\n"
"\n"
"QPushButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close{\n"
"    border-radius:0px;\n"
"    color: #F0F0F0;\n"
"    background-color:rgba(0,0,0,0);\n"
"    border-style:none;\n"
"}\n"
"\n"
"QPushButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(25, 134, 199, 0), stop:1 #5CACEE);\n"
"}\n"
"\n"
"QPushButton#btnMenu_Close:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(238, 0, 0, 128), stop:1 rgba(238, 44, 44, 255));\n"
"}\n"
"\n"
"QCheckBox {\n"
"    spacing: 2px; \n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/qss_icons/img_rc/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/qss_icons/img_rc/checkbox_checked.png); \n"
"}\n"
"\n"
"QRadioButton {\n"
"    spacing: 2px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 15px; \n"
"    height: 15px; \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"    image: url(:/qss_icons/img_rc/radio_normal.png); \n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"    image: url(:/qss_icons/img_rc/radio_selected.png); \n"
"}\n"
"\n"
"QComboBox,QDateEdit{\n"
"    border-radius: 3px;\n"
"    padding: 1px 10px 1px 5px;\n"
"    border: 1px solid #5CACEE;\n"
"}\n"
"\n"
"QComboBox::drop-down,QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px; \n"
"    border-left-width: 1px;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    border-left-color: #5CACEE;\n"
"}\n"
"\n"
"QComboBox::down-arrow,QDateEdit::down-arrow {\n"
"    image: url(:/qss_icons/img_rc/array_down.png); \n"
"}\n"
"\n"
"QMenu {\n"
"    background-color:#F0F0F0;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QMenu::item {    \n"
"    padding: 2px 12px 2px 12px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    color: #FFFFFF;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background: #5CACEE;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    border: 1px solid #5CACEE;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    width: 5px; \n"
"    margin: 0.5px;\n"
"    background-color: #1B89CA;\n"
"}\n"
"\n"
"QSlider::groove:horizontal,QSlider::add-page:horizontal { \n"
"    background: #808080; \n"
"    height: 8px; \n"
"    border-radius: 3px; \n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    height: 8px; \n"
"    border-radius: 3px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 13px; \n"
"    margin-top: -3px; \n"
"    margin-bottom: -3px; \n"
"    border-radius: 6px;\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,stop:0.6 #F0F0F0, stop:0.778409 #5CACEE);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread: pad, cx: 0.5, cy: 0.5, radius: 0.5, fx: 0.5, fy: 0.5, stop: 0.6 #F0F0F0,stop:0.778409 #1B89CA);\n"
"}\n"
"\n"
"QSlider::groove:vertical,QSlider::sub-page:vertical {\n"
"    background:#808080; \n"
"    width: 8px; \n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    width: 8px;\n"
"    border-radius: 3px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 14px; \n"
"    margin-left: -3px;\n"
"    margin-right: -3px;\n"
"    border-radius: 6px;\n"
"    background: qradialgradient(spread: pad, cx: 0.5, cy: 0.5, radius: 0.5, fx: 0.5, fy: 0.5, stop: 0.6 #F0F0F0, stop:0.778409 #5CACEE);\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"    background: qradialgradient(spread: pad, cx: 0.5, cy: 0.5, radius: 0.5, fx: 0.5, fy: 0.5, stop: 0.6 #F0F0F0,stop:0.778409 #1B89CA);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width:10px; \n"
"    background-color:rgba(0,0,0,0%); \n"
"    padding-top:10px; \n"
"    padding-bottom:10px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    height:10px; \n"
"    background-color:rgba(0,0,0,0%); \n"
"    padding-left:10px; padding-right:10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    width:10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD); \n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    height:10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD); \n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    width:10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    height:10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height:10px;\n"
"    width:10px;\n"
"    subcontrol-position: bottom; \n"
"    subcontrol-origin: margin;\n"
"    border-image:url(:/qss_icons/img_rc/add-line_vertical.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    height:10px;\n"
"    width:10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"    border-image:url(:/qss_icons/img_rc/add-line_horizontal.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    height:10px;\n"
"    width:10px;\n"
"    subcontrol-position: top; \n"
"    subcontrol-origin: margin;\n"
"    border-image:url(:/qss_icons/img_rc/sub-line_vertical.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    height:10px;\n"
"    width:10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"    border-image:url(:/qss_icons/img_rc/sub-line_horizontal.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical {\n"
"    width:10px;\n"
"    background: #C0C0C0;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal {\n"
"    height:10px;\n"
"    background: #C0C0C0;\n"
"}\n"
"\n"
"QScrollArea {\n"
"    border: 0px ; \n"
"}\n"
"\n"
"QTreeView,QListView,QTableView{\n"
"    border: 1px solid #5CACEE; \n"
"    selection-background-color: #1B89CA;\n"
"    selection-color: #F0F0F0;\n"
"}\n"
"\n"
"QTableView::item:selected, QListView::item:selected, QTreeView::item:selected {\n"
"    color: #F0F0F0;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
"QTableView::item:hover, QListView::item:hover, QTreeView::item:hover {\n"
"    color: #F0F0F0;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD); \n"
"}\n"
"\n"
"QTableView::item, QListView::item, QTreeView::item {\n"
"    padding: 5px; \n"
"    margin: 0px; \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    padding:3px;\n"
"    margin:0px;\n"
"    color:#F0F0F0;\n"
"    border: 1px solid #F0F0F0;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD);\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-bottom-left-radius:0px;\n"
"    border-bottom-right-radius:0px;\n"
"    color: #F0F0F0;\n"
"    min-width: 60px;\n"
"    min-height: 20px;\n"
"    padding: 3px 8px 3px 8px;\n"
"    margin:1px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD); \n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
"QStatusBar::item {\n"
"     border: 1px solid #5CACEE;\n"
"     border-radius: 3px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 100, 781, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.create_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_button.setGeometry(QtCore.QRect(690, 510, 93, 31))
        self.create_button.setObjectName("create_button")
        self.username_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.username_lineedit.setGeometry(QtCore.QRect(400, 510, 131, 31))
        self.username_lineedit.setObjectName("username_lineedit")
        self.password_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_lineedit.setGeometry(QtCore.QRect(542, 510, 131, 31))
        self.password_lineedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineedit.setObjectName("password_lineedit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "USERNAME"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "password"))
        self.create_button.setText(_translate("MainWindow", "Create"))
        self.username_lineedit.setPlaceholderText(_translate("MainWindow", "Enter username.."))
        self.password_lineedit.setPlaceholderText(_translate("MainWindow", "Enter password..."))
import style_blue_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
