# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend_1.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
import numpy.core.multiarray
import cv2
import pikepdf
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap, QImage, QPainter
from PySide2.QtPrintSupport import QPrinter, QPrintPreviewDialog, QPrintDialog,QPageSetupDialog
from PySide2.QtWidgets import QMessageBox, QFileDialog, QDialog
import fitz
import os
from images import logo
import tempfile
BASE_URL = 'http://127.0.0.1:8000'

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1024, 590)
                MainWindow.setMinimumSize(QtCore.QSize(1024, 590))
                MainWindow.setMaximumSize(QtCore.QSize(1024, 590))
                MainWindow.setStyleSheet("background-color: rgb(220, 220, 220);")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(10, 10, 161, 31))
                self.label.setStyleSheet("border-image: url(:/newPrefix/WhatsApp Image 2020-09-11 at 12.46.25 AM.jpeg);")
                self.label.setText("")
                self.label.setObjectName("label")
                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(950, 10, 31, 31))
                self.pushButton.setStyleSheet("border-image: url(:/newPrefix/help.png);")
                self.pushButton.setText("")
                self.pushButton.setObjectName("pushButton")
                self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_2.setGeometry(QtCore.QRect(910, 10, 31, 31))
                self.pushButton_2.setStyleSheet("border-image: url(:/newPrefix/contact.jpg);")
                self.pushButton_2.setText("")
                self.pushButton_2.setObjectName("pushButton_2")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(180, 50, 341, 91))
                self.label_2.setStyleSheet("border: 2px solid black;\n"
        "background-color: rgb(255, 255, 255);")
                self.label_2.setText("")
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(540, 50, 341, 91))
                self.label_3.setStyleSheet("border: 2px solid black;\n"
        "background-color: rgb(255, 255, 255);")
                self.label_3.setText("")
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(200, 70, 81, 16))
                self.label_4.setStyleSheet("font: 87 11pt \"Arial Black\";\n"
        "background-color: rgb(255, 255, 255);")
                self.label_4.setScaledContents(True)
                self.label_4.setIndent(-1)
                self.label_4.setObjectName("label_4")
                self.label_6 = QtWidgets.QLabel(self.centralwidget)
                self.label_6.setGeometry(QtCore.QRect(200, 100, 91, 16))
                self.label_6.setStyleSheet("font: 87 11pt \"Arial Black\";\n"
        "background-color: rgb(255, 255, 255);")
                self.label_6.setScaledContents(True)
                self.label_6.setIndent(-1)
                self.label_6.setObjectName("label_6")
                self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit.setGeometry(QtCore.QRect(300, 70, 161, 21))
                self.lineEdit.setObjectName("lineEdit")
                self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit_2.setGeometry(QtCore.QRect(300, 100, 161, 21))
                self.lineEdit_2.setObjectName("lineEdit_2")
                self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_4.setGeometry(QtCore.QRect(470, 100, 31, 21))
                self.pushButton_4.setStyleSheet("border-image: url(:/newPrefix/submit.png);")
                self.pushButton_4.setText("")
                self.pushButton_4.setObjectName("pushButton_4")
                self.pushButton_4.clicked.connect(self.password)
                self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_3.setGeometry(QtCore.QRect(470, 70, 31, 21))
                self.pushButton_3.setAutoFillBackground(False)
                self.pushButton_3.setStyleSheet("border-image: url(:/newPrefix/file.jpg);")
                self.pushButton_3.setText("")
                self.pushButton_3.setIconSize(QtCore.QSize(11, 11))
                self.pushButton_3.setObjectName("pushButton_3")
                self.pushButton_3.clicked.connect(self.browseImage)
                self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_5.setGeometry(QtCore.QRect(550, 60, 101, 31))
                self.pushButton_5.setStyleSheet("font: 87 8pt \"Arial Black\";")
                self.pushButton_5.setObjectName("pushButton_5")
                self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_6.setGeometry(QtCore.QRect(770, 60, 101, 31))
                self.pushButton_6.setStyleSheet("font: 87 8pt \"Arial Black\";")
                self.pushButton_6.setObjectName("pushButton_6")
                self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_7.setGeometry(QtCore.QRect(660, 60, 101, 31))
                self.pushButton_7.setStyleSheet("font: 87 8pt \"Arial Black\";")
                self.pushButton_7.setObjectName("pushButton_7")
                self.pushButton_7.clicked.connect(self.printpreviewDialog)
                self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_8.setGeometry(QtCore.QRect(660, 100, 101, 31))
                self.pushButton_8.setStyleSheet("font: 87 8pt \"Arial Black\";")
                self.pushButton_8.setObjectName("pushButton_8")
                self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_9.setGeometry(QtCore.QRect(550, 100, 101, 31))
                self.pushButton_9.setStyleSheet("font: 87 8pt \"Arial Black\";")
                self.pushButton_9.setObjectName("pushButton_9")
                self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_10.setGeometry(QtCore.QRect(770, 100, 101, 31))
                self.pushButton_10.setStyleSheet("font: 87 8pt \"Arial Black\";")
                self.pushButton_10.setObjectName("pushButton_10")
                self.line = QtWidgets.QFrame(self.centralwidget)
                self.line.setGeometry(QtCore.QRect(0, 160, 1021, 31))
                self.line.setFrameShape(QtWidgets.QFrame.HLine)
                self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line.setObjectName("line")
                self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
                self.checkBox.setGeometry(QtCore.QRect(20, 540, 121, 21))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.checkBox.setFont(font)
                self.checkBox.setObjectName("checkBox")
                self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
                self.checkBox_2.setGeometry(QtCore.QRect(880, 540, 121, 21))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.checkBox_2.setFont(font)
                self.checkBox_2.setObjectName("checkBox_2")
                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(10, 210, 1001, 311))
                self.label_5.setStyleSheet("background-color: rgb(239, 239, 239);")
                self.label_5.setText("")
                self.label_5.setObjectName("label_5")
                self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
                self.groupBox.setGeometry(QtCore.QRect(18, 215, 490, 300))
                self.groupBox.setTitle("")
                self.groupBox.setObjectName("groupBox")
                self.label_7 = QtWidgets.QLabel(self.groupBox)
                self.label_7.setGeometry(QtCore.QRect(0, 0, 491, 51))
                self.label_7.setStyleSheet("")
                self.label_7.setText("")
                self.label_7.setObjectName("label_7")
                self.label_9 = QtWidgets.QLabel(self.groupBox)
                self.label_9.setGeometry(QtCore.QRect(40, 60, 120, 152))
                self.label_9.setStyleSheet("")
                self.label_9.setText("")
                self.label_9.setObjectName("label_9")
                self.label_10 = QtWidgets.QLabel(self.groupBox)
                self.label_10.setGeometry(QtCore.QRect(170, 70, 251, 25))
                self.label_10.setStyleSheet("")
                self.label_10.setText("")
                self.label_10.setObjectName("label_10")
                self.label_11 = QtWidgets.QLabel(self.groupBox)
                self.label_11.setGeometry(QtCore.QRect(170, 90, 251, 25))
                self.label_11.setStyleSheet("")
                self.label_11.setText("")
                self.label_11.setObjectName("label_11")
                self.label_12 = QtWidgets.QLabel(self.groupBox)
                self.label_12.setGeometry(QtCore.QRect(170, 110, 251, 25))
                self.label_12.setStyleSheet("")
                self.label_12.setText("")
                self.label_12.setObjectName("label_12")
                self.label_13 = QtWidgets.QLabel(self.groupBox)
                self.label_13.setGeometry(QtCore.QRect(170, 130, 251, 21))
                self.label_13.setStyleSheet("")
                self.label_13.setText("")
                self.label_13.setObjectName("label_13")
                self.label_14 = QtWidgets.QLabel(self.groupBox)
                self.label_14.setGeometry(QtCore.QRect(170, 170, 251, 25))
                self.label_14.setStyleSheet("")
                self.label_14.setText("")
                self.label_14.setObjectName("label_14")
                self.label_15 = QtWidgets.QLabel(self.groupBox)
                self.label_15.setGeometry(QtCore.QRect(0, 270, 491, 30))
                self.label_15.setStyleSheet("")
                self.label_15.setText("")
                self.label_15.setObjectName("label_15")
                self.label_16 = QtWidgets.QLabel(self.groupBox)
                self.label_16.setGeometry(QtCore.QRect(0, 270, 491, 5))
                self.label_16.setStyleSheet("")
                self.label_16.setText("")
                self.label_16.setObjectName("label_16")
                self.label_20 = QtWidgets.QLabel(self.groupBox)
                self.label_20.setGeometry(QtCore.QRect(10, 60, 16, 141))
                self.label_20.setText("")
                self.label_20.setObjectName("label_20")
                self.label_21 = QtWidgets.QLabel(self.groupBox)
                self.label_21.setGeometry(QtCore.QRect(460, 70, 16, 171))
                self.label_21.setText("")
                self.label_21.setObjectName("label_21")
                self.label_23 = QtWidgets.QLabel(self.groupBox)
                self.label_23.setGeometry(QtCore.QRect(90, 250, 311, 21))
                self.label_23.setStyleSheet("")
                self.label_23.setText("")
                self.label_23.setObjectName("label_23")
                self.label_24 = QtWidgets.QLabel(self.groupBox)
                self.label_24.setGeometry(QtCore.QRect(90, 230, 311, 21))
                self.label_24.setStyleSheet("")
                self.label_24.setText("")
                self.label_24.setObjectName("label_24")
                self.label_31 = QtWidgets.QLabel(self.groupBox)
                self.label_31.setGeometry(QtCore.QRect(10, 60, 21, 141))
                self.label_31.setStyleSheet("")
                self.label_31.setText("")
                self.label_31.setObjectName("label_31")
                self.label_32 = QtWidgets.QLabel(self.groupBox)
                self.label_32.setGeometry(QtCore.QRect(450, 70, 31, 171))
                self.label_32.setStyleSheet("")
                self.label_32.setText("")
                self.label_32.setObjectName("label_32")
                self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
                self.groupBox_2.setGeometry(QtCore.QRect(515, 215, 490, 300))
                self.groupBox_2.setTitle("")
                self.groupBox_2.setObjectName("groupBox_2")
                self.label_8 = QtWidgets.QLabel(self.groupBox_2)
                self.label_8.setGeometry(QtCore.QRect(0, 0, 491, 51))
                self.label_8.setText("")
                self.label_8.setObjectName("label_8")
                self.label_17 = QtWidgets.QLabel(self.groupBox_2)
                self.label_17.setGeometry(QtCore.QRect(0, 0, 491, 51))
                self.label_17.setStyleSheet("")
                self.label_17.setText("")
                self.label_17.setObjectName("label_17")
                self.label_19 = QtWidgets.QLabel(self.groupBox_2)
                self.label_19.setGeometry(QtCore.QRect(0, 269, 491, 31))
                self.label_19.setStyleSheet("")
                self.label_19.setText("")
                self.label_19.setObjectName("label_19")
                self.label_18 = QtWidgets.QLabel(self.groupBox_2)
                self.label_18.setGeometry(QtCore.QRect(0, 262, 491, 8))
                self.label_18.setStyleSheet("")
                self.label_18.setText("")
                self.label_18.setObjectName("label_18")
                self.label_22 = QtWidgets.QLabel(self.groupBox_2)
                self.label_22.setGeometry(QtCore.QRect(330, 70, 143, 143))
                self.label_22.setText("")
                self.label_22.setObjectName("label_22")
                self.label_25 = QtWidgets.QLabel(self.groupBox_2)
                self.label_25.setGeometry(QtCore.QRect(330, 60, 143, 143))
                self.label_25.setStyleSheet("")
                self.label_25.setText("")
                self.label_25.setObjectName("label_25")
                self.label_26 = QtWidgets.QLabel(self.groupBox_2)
                self.label_26.setGeometry(QtCore.QRect(330, 210, 141, 31))
                self.label_26.setStyleSheet("")
                self.label_26.setText("")
                self.label_26.setObjectName("label_26")
                self.label_27 = QtWidgets.QLabel(self.groupBox_2)
                self.label_27.setGeometry(QtCore.QRect(70, 220, 261, 21))
                self.label_27.setStyleSheet("")
                self.label_27.setText("")
                self.label_27.setObjectName("label_27")
                self.label_28 = QtWidgets.QLabel(self.groupBox_2)
                self.label_28.setGeometry(QtCore.QRect(70, 240, 261, 21))
                self.label_28.setStyleSheet("")
                self.label_28.setText("")
                self.label_28.setObjectName("label_28")
                self.label_29 = QtWidgets.QLabel(self.groupBox_2)
                self.label_29.setGeometry(QtCore.QRect(10, 60, 301, 71))
                self.label_29.setStyleSheet("")
                self.label_29.setText("")
                self.label_29.setObjectName("label_29")
                self.label_30 = QtWidgets.QLabel(self.groupBox_2)
                self.label_30.setGeometry(QtCore.QRect(10, 140, 301, 71))
                self.label_30.setStyleSheet("")
                self.label_30.setText("")
                self.label_30.setObjectName("label_30")
                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

                #create temp folder
                self.path = tempfile.mkdtemp()

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "TECHIDENTITY"))
                self.label_4.setText(_translate("MainWindow", "Filename:"))
                self.label_6.setText(_translate("MainWindow", "Password:"))
                self.pushButton_5.setText(_translate("MainWindow", "Settings"))
                self.pushButton_6.setText(_translate("MainWindow", "Font"))
                self.pushButton_7.setText(_translate("MainWindow", "Print"))
                self.pushButton_8.setText(_translate("MainWindow", "Image Editor"))
                self.pushButton_9.setText(_translate("MainWindow", "Report"))
                self.pushButton_10.setText(_translate("MainWindow", "License"))
                self.checkBox.setText(_translate("MainWindow", "PRINT FRONT"))
                self.checkBox_2.setText(_translate("MainWindow", "PRINT BACK"))

        def topimage(self):
                pixmap = QPixmap(r'images\Aadhar Back Side Top.jpg')
                self.label_7.setPixmap(pixmap)
                self.label_7.setScaledContents(True)

        def nextpagebottomimage(self):
                pixmap = QPixmap('assets/rearpagefooter.jpeg')
                self.label_33.setPixmap(pixmap)
                self.label_33.setScaledContents(True)

        def nextpagetop(self):
                pixmap = QPixmap('assets/rearheader.png')
                self.label_31.setPixmap(pixmap)
                self.label_31.setScaledContents(True)

        def photoextraction(self, doc):

                for i in range(len(doc)):
                        for img in doc.getPageImageList(i):
                                xref = img[0]
                                pix = fitz.Pixmap(doc, xref)
                                if pix.n < 1:
                                        pix.writePNG(os.path.join(self.path, "p%s-%s.png" % (i, xref)))
                                else:
                                        pix1 = fitz.Pixmap(fitz.csRGB, pix)
                                        pix1.writePNG(os.path.join(self.path, "p%s-%s.png" % (i, xref)))

                                if (pix.width == 160 and pix.height == 200):
                                        pixmap = QPixmap(os.path.join(self.path, "p%s-%s.png" % (i, xref)))
                                        self.label_9.setPixmap(pixmap)
                                        self.label_9.setScaledContents(True)

                                elif (pix.width == 1000 and pix.height == 1000):
                                        pixmap = QPixmap(os.path.join(self.path, "p%s-%s.png" % (i, xref)))
                                        self.label_25.setPixmap(pixmap)
                                        self.label_25.setScaledContents(True)

        def setText_to_elements(self):

                self.label_13.setText(self.text_ex['DOB'])
                self.label_27.adjustSize()
                self.label_10.setText(self.text_ex['namehindi'])
                self.label_10.adjustSize()
                self.label_12.setText(self.text_ex['gender string'])
                self.label_12.adjustSize()
                self.label_29.setText(self.text_ex['hindiAddress'])
                self.label_30.setText("Address: " + "\n" + self.text_ex['engAddress'])
                self.label_30.adjustSize()
                self.label_27.setText(self.text_ex['Adhaar no'])
                self.label_27.adjustSize()
                if (self.text_ex['VID'] != None):
                        self.label_23.setText("VID: " + self.text_ex['VID'])
                        self.label_28.setText("VID: " + self.text_ex['VID'])
                        self.label_28.adjustSize()
                        self.label_28.setStyleSheet("border-top:0.5px solid rgb(220, 220, 220);")
                self.label_22.adjustSize()
                self.label_22.setStyleSheet("border-top:0.5px solid rgb(220, 220, 220);")
                self.label_24.setText(self.text_ex['Adhaar no'])
                self.label_24.adjustSize()

        def password(self):
                r = self.lineEdit.text()
                pwd = self.lineEdit_2.text()

                if pwd != "":
                        try:
                                mypdf = pikepdf.open(r, pwd)
                                r = os.path.join(self.path ,"/pdffile",r ,"unlocked.pdf")
                                mypdf.save(r)
                        except pikepdf._qpdf.PasswordError:
                                print("hi")
                                self.showdialog()
                                #         print('cannot decrypt %s with password %s' % (r, pwd))
                else:
                        pikepdf.open(r)


                print(r)
                # Hit fast api endpoint with PDF file

                doc = fitz.open(r)
                page = doc.loadPage(0)
                mat = fitz.Matrix(2, 2)
                pix = page.getPixmap(matrix=mat)

                output = os.path.join(self.path, "outfile.png")
                output = pix.writePNG(output)

                image_full = cv2.imread("outfile.png")
                path = os.path.join(self.path, "image_full.png")
                # cv2.imwrite(path,image_full)



                # self.paintEvent()
                import requests
                # try:
                res = requests.post(BASE_URL + '/uploadfile/', files={
                        'pdf': open(r, 'rb')
                })
                data = res.json()
                self.text_ex = data["text"]
                print(self.text_ex)


                # name = self.name_ex(r, path)
                # self.text_ex["Name"] = name
                # print("name", name)
                # self.label_27.setText(self.text_ex["Name"])
                try:
                        self.groupBox.setStyleSheet("background-color:rgb(255,255,255")
                        self.groupBox_2.setStyleSheet("background-color:rgb(255,255,255")
                        self.photoextraction(doc)
                        self.setText_to_elements()
                except:
                        print("Sorry!response invalid")

                # filename = "img02.png"
                # fnt = ImageFont.truetype('arial.ttf', 15)
                # # create new image
                # image = Image.new(mode="RGB", size=(170, 90), color="white")
                # draw = ImageDraw.Draw(image)
                # #self.text_ex["Issuedate"]
                # draw.text((10, 10), "qwertyui", font=fnt, fill=(0, 0, 0))
                # image.save(filename)
                #
                # # os.system(filename)
                # angle = 270  # What angle would you like to rotate
                # self.pixmap = QPixmap("img02.png")  # image for your label
                # pixmap_rotated = self.pixmap.transformed(QTransform().rotate(angle), QtCore.Qt.SmoothTransformation)
                # self.label_24.setPixmap(pixmap_rotated)  # set rotated pixmap into your QLabel
                # self.label_24.setScaledContents(True)
                # self.label_24.setAlignment(Qt.AlignCenter)
                self.topimage()
                self.nextpagetop()
                #self.bottomimage()
                #self.nextpagebottomimage()
                #self.issuedate()
                # self.downloaddate()
                print("take ss")
                self.take_screenshot()
                print("Restart your server!!")

        def showdialog(self):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("file extension not supported")
                msg.setWindowTitle("ERROR!")

                retval = msg.exec_()
                print("value of pressed message box button:", retval)

        def browseImage(self):
                """
                    this function opens the dialog box.
                """
                foldername = QFileDialog.getOpenFileName()
                ext = os.path.splitext(foldername[0])[1]
                valid_extensions = '.pdf'
                if ext != valid_extensions:
                        print(u'File not supported!')
                        self.showdialog()
                        print("hi")

                pdffile = foldername[0]
                self.lineEdit.setText(pdffile)
                self.take_screenshot()

        def printpreviewDialog(self):
                printer = QPrinter(QPrinter.HighResolution)
                previewDialog = QPrintPreviewDialog(printer, parent=None)
                # previewDialog.paintRequested.connect(self.printPreview)
                previewDialog.paintRequested.connect(self.printImage)
                previewDialog.exec_()

        def printImage(self, printer):
                "Prints the current diagram"
                self.image = QImage('test1.png')

                # Create the printer
                printerobject = QPrinter()
                # Set the settings
                printdialog = QPrintDialog(printerobject)
                if printdialog.exec_() == QDialog.Accepted:
                        painter = QPainter(printer)
                        rect = painter.viewport()
                        size = self.image.size()
                        size.scale(rect.size(), Qt.KeepAspectRatio)
                        painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
                        painter.setWindow(self.image.rect())
                        painter.drawImage(0, 0, self.image)

        def take_screenshot(self):
                from PySide2 import QtCore as pyqt5c
                from PySide2 import QtWidgets as pyqt5w

                screen = pyqt5w.QApplication.primaryScreen()
                pixmap = screen.grabWindow(self.groupBox.winId())

                ba = pyqt5c.QByteArray()
                buff = pyqt5c.QBuffer(ba)
                pixmap = pixmap.scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                pixmap.save('test1.png', 'PNG')
                return ba.data()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
