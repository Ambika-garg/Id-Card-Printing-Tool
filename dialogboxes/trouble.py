import smtplib as s

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QMessageBox
import requests

BASE_URL = 'https://techidentity.herokuapp.com'


class Ui_MainWindow3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 300, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 40pt \"Arial\";")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 601, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setKerning(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: 0.5px solid black;")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 180, 581, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 220, 91, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 250, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, 220, 91, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(280, 250, 341, 20))
        self.label_6.setStyleSheet("border: 0.5px solid black;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 290, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 320, 561, 111))
        self.lineEdit_3.setStyleSheet("border: 0.5px solid black;")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 440, 231, 31))
        self.pushButton.setStyleSheet("background-color:rgb(151,154,154)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 440, 251, 31))
        self.pushButton_2.setStyleSheet("background-color:rgb(151,154,154)")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Report"))
        self.label.setText(_translate("MainWindow", "Report Issue"))
        self.label_2.setText(_translate("MainWindow",
                                        "Please Note - Your Information will be kept strictly confidential. We will update you over E-Mail once we fix the issue"))
        self.label_3.setText(_translate("MainWindow", " File"))
        self.label_4.setText(_translate("MainWindow", "  Password"))
        self.label_5.setText(_translate("MainWindow", "  Email ID"))
        self.label_7.setText(_translate("MainWindow", "  Message"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.pushButton.clicked.connect(self.body)
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))

    def showdialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Your credentials are invalid!")
        msg.setWindowTitle("ERROR!")

        retval = msg.exec_()
        print("value of pressed message box button:", retval)

    def body(self):
        try:
            ob = s.SMTP('smtp.gmail.com', 587)
            password = self.lineEdit_2.text()
            email = self.label_6.text()
            # ob.starttls()
            # ob.login(email, password)
            subject = "sending email using python"
            body = self.lineEdit_3.text()
            message = "Subject:{}\n\n{}".format(subject, body)
            myobj = {"email": email, "message": message}
            res = requests.post(BASE_URL + '/Customer_issues/', data=myobj)
            print(res.text)

            # ob.sendmail("ambika.garg3@aiesec.net", 'techidentity1234@gmail.com', message)
            # print("send successfully...")
            # ob.quit()
        except Exception as e:
            print(e)
            self.showdialog()


if __name__ == "_main_":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
