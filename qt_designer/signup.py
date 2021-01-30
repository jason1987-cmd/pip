# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet("background-color: rgb(0, 63, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 111, 41))
        self.label.setStyleSheet("color:white;\n"
"font-family:Calibri;\n"
"font-size:26px;\n"
"font-weight:bold;")
        self.label.setObjectName("label")
        self.fullnamelabel = QtWidgets.QLabel(self.centralwidget)
        self.fullnamelabel.setGeometry(QtCore.QRect(50, 70, 111, 41))
        self.fullnamelabel.setStyleSheet("color:white;\n"
"font-family:Calibri;\n"
"font-size:22px;\n"
"font-weight:bold;")
        self.fullnamelabel.setObjectName("fullnamelabel")
        self.fullnamefield = QtWidgets.QLineEdit(self.centralwidget)
        self.fullnamefield.setGeometry(QtCore.QRect(190, 69, 391, 41))
        self.fullnamefield.setObjectName("fullnamefield")
        self.emaillabel = QtWidgets.QLabel(self.centralwidget)
        self.emaillabel.setGeometry(QtCore.QRect(50, 140, 111, 41))
        self.emaillabel.setStyleSheet("color:white;\n"
"font-family:Calibri;\n"
"font-size:22px;\n"
"font-weight:bold;")
        self.emaillabel.setObjectName("emaillabel")
        self.emailfield = QtWidgets.QLineEdit(self.centralwidget)
        self.emailfield.setGeometry(QtCore.QRect(190, 140, 391, 41))
        self.emailfield.setObjectName("emailfield")
        self.phonenolabel = QtWidgets.QLabel(self.centralwidget)
        self.phonenolabel.setGeometry(QtCore.QRect(50, 210, 111, 41))
        self.phonenolabel.setStyleSheet("color:white;\n"
"font-family:Calibri;\n"
"font-size:22px;\n"
"font-weight:bold;")
        self.phonenolabel.setObjectName("phonenolabel")
        self.phonenofiled = QtWidgets.QLineEdit(self.centralwidget)
        self.phonenofiled.setGeometry(QtCore.QRect(190, 210, 391, 41))
        self.phonenofiled.setObjectName("phonenofiled")
        self.passwordlabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordlabel.setGeometry(QtCore.QRect(50, 290, 111, 41))
        self.passwordlabel.setStyleSheet("color:white;\n"
"font-family:Calibri;\n"
"font-size:22px;\n"
"font-weight:bold;")
        self.passwordlabel.setObjectName("passwordlabel")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(190, 290, 391, 41))
        self.password.setObjectName("password")
        self.signupbtn = QtWidgets.QPushButton(self.centralwidget)
        self.signupbtn.setGeometry(QtCore.QRect(190, 380, 391, 41))
        self.signupbtn.setStyleSheet("background-color:orange;\n"
"font-family:Calibri;\n"
"font-size:22px;\n"
"font-weight:bold;\n"
"color:white;")
        self.signupbtn.setObjectName("signupbtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sign Up window"))
        self.label.setText(_translate("MainWindow", "Sign Up"))
        self.fullnamelabel.setText(_translate("MainWindow", "Full name :"))
        self.emaillabel.setText(_translate("MainWindow", "Email :"))
        self.phonenolabel.setText(_translate("MainWindow", "Phone no :"))
        self.passwordlabel.setText(_translate("MainWindow", "Password :"))
        self.signupbtn.setText(_translate("MainWindow", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
