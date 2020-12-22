# -*- coding: utf-8 -*-

import os
import re
import tempfile
# Form implementation generated from reading ui file 'frontend_1.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
from difflib import get_close_matches

import webbrowser
import cv2
import fitz
import pikepdf
import pytesseract
import requests
from PIL import Image, ImageFont, ImageDraw
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap, QImage, QPainter, QFont, QTransform, QIcon
from PySide2.QtPrintSupport import QPrinter, QPrintPreviewDialog, QPrintDialog
from PySide2.QtWidgets import QMessageBox, QFileDialog, QDialog, QFontDialog

from dialogboxes.resize import Ui_MainWindow9
from dialogboxes.settingsbox import Ui_MainWindow1
from dialogboxes.trouble1 import Ui_MainWindow3

BINARY_THREHOLD = 180
IMAGE_SIZE = 1800
BASE_URL = 'https://techidentity.herokuapp.com'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 590)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 590))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 590))
        MainWindow.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.switch = 0
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 166, 41))
        self.label.setStyleSheet("border-image: url(:/newPrefix/WhatsApp Image 2020-09-11 at 12.46.25 AM.jpeg);")
        pixmap = QPixmap(r"D:\finalapp\images\applogo.jpeg")
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(950, 10, 31, 31))
        self.pushButton.setStyleSheet("Background-color:rgb(255,251,549)")
        self.pushButton.setIcon(QIcon('images\help.png'))
        self.pushButton.setText("")

        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(910, 10, 31, 31))
        self.pushButton_2.setStyleSheet('Background-color:rgb(0,10,5)')
        self.pushButton_2.setText("")
        self.pushButton_2.setIcon(QIcon('images\contact.png'))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.contact)
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
        self.pushButton_4.setStyleSheet("")
        icon1 = QtGui.QPixmap(r'D:\finalapp\images\submit.png')
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(11, 11))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.password)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 70, 31, 21))
        self.pushButton_3.setAutoFillBackground(True)
        icon = QtGui.QPixmap(r'D:\finalapp\images\file.jpg')
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(11, 11))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.browseImage)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(550, 60, 101, 31))
        self.pushButton_5.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.open_settings)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(770, 60, 101, 31))
        self.pushButton_6.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.openFontDialog)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(660, 60, 101, 31))
        self.pushButton_7.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.printpreviewDialog)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(660, 100, 101, 31))
        self.pushButton_8.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.resizeimage)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(550, 100, 101, 31))
        self.pushButton_9.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.trouble)
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(770, 100, 101, 31))
        self.pushButton_10.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.pushButton_10.setObjectName("pushButton_10")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 160, 1021, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.checkBox = QtWidgets.QRadioButton(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 540, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.toggled.connect(self.clickBox)
        self.checkBox_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(880, 540, 121, 21))
        self.checkBox_2.toggled.connect(self.clickBox2)
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
        self.label_7.setGeometry(QtCore.QRect(30, 0, 451, 61))
        self.label_7.setStyleSheet("")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(40, 50, 120, 152))
        self.label_9.setStyleSheet("")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(170, 63, 251, 25))
        self.label_10.setStyleSheet("")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(170, 89, 251, 25))
        self.label_11.setStyleSheet("")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(170, 115, 251, 25))
        self.label_12.setStyleSheet("")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(170, 140, 251, 21))
        self.label_13.setStyleSheet("")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(170, 170, 251, 25))
        self.label_14.setStyleSheet("")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(0, 270, 491, 32))
        self.label_15.setStyleSheet("")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(0, 265, 491, 5))
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
        self.label_23.setGeometry(QtCore.QRect(90, 242, 311, 23))
        self.label_23.setStyleSheet("font-size:12")
        self.label_23.setFont(QFont('Arial', 12, weight=QtGui.QFont.Bold))
        self.label_23.setObjectName("label_23")
        self.label_23.setAlignment(Qt.AlignAbsolute)
        self.label_24 = QtWidgets.QLabel(self.groupBox)
        self.label_24.setGeometry(QtCore.QRect(110, 219, 311, 23))
        self.label_24.setStyleSheet("font-size:15")
        self.label_24.setFont(QFont('Arial', 12, weight=QtGui.QFont.Bold))
        self.label_24.setObjectName("label_24")
        self.label_24.setAlignment(Qt.AlignBottom)
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
        self.label_19.setGeometry(QtCore.QRect(10, 269, 471, 31))
        self.label_19.setStyleSheet("")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setGeometry(QtCore.QRect(0, 262, 491, 5))
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
        self.label_26.setGeometry(QtCore.QRect(330, 220, 161, 31))
        self.label_26.setStyleSheet("")
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox_2)
        self.label_27.setGeometry(QtCore.QRect(70, 220, 261, 21))
        self.label_27.setStyleSheet("font-size:15")
        self.label_27.setText("")
        self.label_27.setFont(QFont('Arial', 12, weight=QtGui.QFont.Bold))
        self.label_27.setObjectName("label_27")
        self.label_27.setAlignment(Qt.AlignAbsolute)
        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        self.label_28.setGeometry(QtCore.QRect(30, 240, 281, 22))
        self.label_28.setStyleSheet("")
        self.label_28.setStyleSheet("font-size:12")
        self.label_28.setText("")
        self.label_28.setFont(QFont('Arial', 12, weight=QtGui.QFont.Bold))
        self.label_28.setObjectName("label_28")
        self.label_28.setAlignment(Qt.AlignAbsolute | Qt.AlignJustify)
        self.label_29 = QtWidgets.QLabel(self.groupBox_2)
        self.label_29.setGeometry(QtCore.QRect(10, 60, 321, 75))
        self.label_29.setStyleSheet("")
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.groupBox_2)
        self.label_30.setGeometry(QtCore.QRect(10, 140, 341, 75))
        self.label_30.setStyleSheet("")
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # create temp folder
        self.path = tempfile.mkdtemp()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aapki Pehchaan"))
        self.label_4.setText(_translate("MainWindow", "Filename:"))
        self.label_4.adjustSize()
        self.label_6.setText(_translate("MainWindow", "Password:"))
        self.label_6.adjustSize()
        self.pushButton_5.setText(_translate("MainWindow", "SETTINGS"))
        self.pushButton_6.setText(_translate("MainWindow", "FONT"))
        self.pushButton_7.setText(_translate("MainWindow", "PRINT"))
        self.pushButton_8.setText(_translate("MainWindow", "RESIZE"))
        self.pushButton_9.setText(_translate("MainWindow", "REPORT"))
        self.pushButton_10.setText(_translate("MainWindow", "LICENSE"))
        self.checkBox.setText(_translate("MainWindow", "PRINT FRONT"))
        self.checkBox.adjustSize()
        self.checkBox_2.setText(_translate("MainWindow", "PRINT BACK"))
        self.checkBox_2.adjustSize()

    def clickBox(self, state):
        if state:
            print('Checked')
            self.take_screenshot()
        else:
            print('Unchecked')

    def clickBox2(self, state):
        if state:
            print('Checked')
            self.take_screenshot2()
        else:
            print('Unchecked')

    def contact(self):
        webbrowser.open("https://mltool.in/contact")

    def topimage(self):
        pixmap = QPixmap(r'D:\finalapp\images\Ashok Stambh Front.png')
        self.label_7.setPixmap(pixmap)
        self.label_7.setScaledContents(True)

    def nextpagebottomimage(self):
        pixmap = QPixmap(r'D:\finalapp\images\Back side Symbol.png')
        self.label_19.setPixmap(pixmap)
        self.label_19.setScaledContents(True)

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
                try:
                    # HUMAN IMAGE IN ADHAR
                    if pix.width == float(0.8) * pix.height or pix.width == 0.75 * pix.height:
                        self.human_image = os.path.join(self.path, "p%s-%s.png" % (i, xref))
                        pixmap = QPixmap(self.human_image)
                        self.label_9.setPixmap(pixmap)
                        self.label_9.setScaledContents(True)

                    # SCANNER CODE IN ADHAR
                    elif pix.width == pix.height:
                        pixmap = QPixmap(os.path.join(self.path, "p%s-%s.png" % (i, xref)))
                        self.label_25.setPixmap(pixmap)
                        self.label_25.setScaledContents(True)
                except Exception as e:
                    print(e)
                    print("fault in human and scanner image")

    def setText_to_elements(self, a):

        self.label_13.setText(self.text_ex['DOB'])
        self.label_10.setText(self.text_ex['namehindi'])
        self.label_11.setText(self.text_ex['englishname'])
        self.label_12.setText(self.text_ex['gender string'])
        self.label_29.setText(self.text_ex['hindiAddress'])
        self.label_30.setText("Address: " + "\n" + self.text_ex['engAddress'])
        self.label_30.adjustSize()
        self.label_27.setText(self.text_ex['Adhaar no'])
        if (self.text_ex['VID'] != None):
            self.label_23.setText("VID: " + self.text_ex['VID'])
            self.label_23.adjustSize()
            self.label_23.setStyleSheet("border-top:0.5px solid rgb(220, 220, 220);")

            self.label_28.setText("VID: " + self.text_ex['VID'])
            self.label_28.adjustSize()
            self.label_28.setStyleSheet("border-top:0.5px solid rgb(220, 220, 220);")

        self.label_24.setText(self.text_ex['Adhaar no'])

    def password(self):
        self.switch = 1
        r = self.lineEdit.text()
        pwd = self.lineEdit_2.text()

        if pwd != "":
            try:
                mypdf = pikepdf.open(r, pwd)
                r = os.path.join(self.path, "unlocked.pdf")
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
        # # try:
        res = requests.post(BASE_URL + '/uploadfile/', files={
            'pdf': open(r, 'rb')
        })
        data = res.json()
        self.text_ex = data["text"]
        name = self.name_ex(doc)
        self.text_ex["englishname"] = name

        try:

            self.groupBox.setStyleSheet("background-color:rgb(255,255,255)")
            self.groupBox_2.setStyleSheet("background-color:rgb(255,255,255)")
            self.photoextraction(doc)
            self.setText_to_elements(self.text_ex)
            self.nextpagetop()
            self.topimage()
            self.redline()
            self.nextpagetop()
            self.defaultfooter()
            self.nextpagebottomimage()
            self.label_26.clear()

        except Exception as e:
            print(e)
            print("Sorry!response invalid")

    def image_smoothening(self, img):
        ret1, th1 = cv2.threshold(img, BINARY_THREHOLD, 255, cv2.THRESH_BINARY)
        ret2, th2 = cv2.threshold(th1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        blur = cv2.GaussianBlur(th2, (1, 1), 0)
        ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return th3

    def remove_noise_and_smooth(self, file_name):
        img = cv2.imread(file_name, 0)
        img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        gaus = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 25)
        img = self.image_smoothening(gaus)
        return img

    def name_ex(self, doc):

        page = doc.loadPage(0)
        mat = fitz.Matrix(2, 2)
        pix = page.getPixmap(matrix=mat)

        outfile = os.path.join(self.path, "outfile.png")
        output = pix.writePNG(outfile)
        image_full = cv2.imread(outfile)

        path = os.path.join(self.path, "image_full.png")
        cv2.imwrite(path, image_full)

        image_front = image_full[1140:1475, 120:500]
        a = os.path.join(self.path, "image_front.png")
        cv2.imwrite(a, image_front)

        image_front1 = self.remove_noise_and_smooth(a)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        text = pytesseract.image_to_string(image_front1, lang="eng")

        try:
            newlist1 = []
            for xx in text.split('\n'):
                newlist1.append(xx)
                newlist1 = list(filter(lambda x: len(x) > 1, newlist1))
            a = 0
            str2 = "Government"
            str1 = "of"
            for no in newlist1:
                if str2 in no or str1 in no:
                    b = a
                a = a + 1
            name = newlist1[b + 2]
            name = name.split(" ")
            print(name)
            if len(name) == 2:
                print(name)
                name = " ".join(name)
                print(name)
                return name
            else:
                name = " ".join(name)
                name = re.sub(r'[(' ')]', '', name)
                name = re.sub(r'[0-9]+', '', name)
                # name = re.sub(r'[;'';;!@#!@#!#!$!=()|:><~~' '__-]+','',name)

                wordlist = self.text_ex['raw'].split("\n")
                name = get_close_matches(name, wordlist)
                print(name)
                return name[0]

        except Exception as e:
            print(e)
            pass

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

        pdffile = foldername[0]
        self.lineEdit.setText(pdffile)

    def printpreviewDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, parent=None, flags=Qt.WindowFlags())

        previewDialog.paintRequested.connect(self.printImage)
        previewDialog.exec_()

    def printImage(self, printer):
        "Prints the current diagram"
        self.image = QImage('test1.tif')

        # # Create the printer
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

    def take_screenshot2(self):
        from PySide2 import QtCore as pyqt5c
        from PySide2 import QtWidgets as pyqt5w

        screen = pyqt5w.QApplication.primaryScreen()
        pixmap = screen.grabWindow(self.groupBox_2.winId())

        ba = pyqt5c.QByteArray()
        buff = pyqt5c.QBuffer(ba)
        pixmap = pixmap.scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        pixmap.save('test1.tif', 'TIF')
        return ba.data()

    def take_screenshot(self):
        from PySide2 import QtCore as pyqt5c
        from PySide2 import QtWidgets as pyqt5w

        screen = pyqt5w.QApplication.primaryScreen()
        pixmap = screen.grabWindow(self.groupBox.winId())

        ba = pyqt5c.QByteArray()
        buff = pyqt5c.QBuffer(ba)
        pixmap = pixmap.scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        pixmap.save('test1.tif', 'TIF')
        return ba.data()

    def openFontDialog(self):
        ok, font = QFontDialog.getFont()
        if ok:
            self.label_10.setFont(font)
            self.label_11.setFont(font)
            self.label_12.setFont(font)
            self.label_13.setFont(font)
            self.label_14.setFont(font)
            self.label_30.setFont(font)
            self.label_29.setFont(font)
            self.label_10.adjustSize()
            self.label_11.adjustSize()
            self.label_12.adjustSize()
            self.label_13.adjustSize()
            self.label_14.adjustSize()
            self.label_30.adjustSize()
            self.label_29.adjustSize()

    def trouble(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self.window)
        self.window.show()

    def photoframe(self):
        if self.ui.checkBox_10.isChecked() == True:
            self.label_9.setStyleSheet("border: 2px solid black;")
        else:
            self.label_9.setStyleSheet("border: 0px solid black;")

    def redline(self):
        pixmap = QPixmap(r'D:\finalapp\images\redline.jpeg')
        self.label_16.setPixmap(pixmap)
        self.label_16.setScaledContents(True)

        self.label_18.setPixmap(pixmap)
        self.label_18.setScaledContents(True)

    def frontpageheader(self):
        if self.ui.checkBox.isChecked() == True:
            self.topimage()
        else:
            self.label_7.clear()

    def rearpagefooter(self):
        if self.ui.checkBox_6.isChecked() == True:
            self.nextpagebottomimage()
        else:
            self.label_19.clear()

    def phnno(self):
        if self.ui.checkBox_14.isChecked() == True:
            self.label_14.setText("Mobile No:" + self.text_ex['mobile no'])

        else:
            self.label_14.clear()

    def put_uid(self):
        sentence = self.text_ex['Adhaar no']
        space = sentence.replace(" ", "")
        number = space

        import barcode
        from barcode.writer import ImageWriter
        ITF = barcode.get_barcode_class('itf')
        itf = ITF(number, writer=ImageWriter())
        fullname = itf.save('itf_barcode', options={"write_text": False})
        print(fullname)
        pixmap = QPixmap('itf_barcode.png')
        self.label_26.setPixmap(pixmap)
        self.label_26.setScaledContents(True)

    def barcode(self):

        try:

            if self.ui.checkBox_7.isChecked() == True:
                self.put_uid()
                self.label_28.clear()
                self.label_27.clear()


            else:
                self.label_26.clear()
                self.label_28.setText("VID: " + self.text_ex['VID'])
                self.label_27.setText(self.text_ex['Adhaar no'])
        except:
            self.label_26.clear()
            self.label_28.setText("VID: " + self.text_ex['VID'])
            self.label_27.setText(self.text_ex['Adhaar no'])

    def vid(self):

        if self.ui.checkBox_15.isChecked() == True:
            if (self.text_ex['VID'] != None):
                self.label_23.setText("VID: " + self.text_ex['VID'])
                self.label_28.setText("VID: " + self.text_ex['VID'])
                # self.label_23.setAlignment(Qt.AlignCenter)
                # self.label_28.setAlignment(Qt.AlignCenter)
        else:
            self.label_23.clear()
            self.label_28.clear()

    def frontpageheadermargin(self):

        if self.ui.checkBox_2.isChecked() == True:
            pixmap = QPixmap(r'D:\finalapp\images\redline.jpeg')
            self.label_16.setPixmap(pixmap)
            self.label_16.setScaledContents(True)

        else:
            self.label_16.clear()

    def RearPageFooterMargin(self):

        if self.ui.checkBox_5.isChecked() == True:
            pixmap = QPixmap(r'D:\finalapp\images\redline.jpeg')
            self.label_18.setPixmap(pixmap)
            self.label_18.setScaledContents(True)

        else:
            self.label_18.clear()

    def rearpageheader(self):
        if self.ui.checkBox_4.isChecked() == True:
            self.nextpagetop()
        else:
            pixmap = QPixmap(None)
            self.label_17.setPixmap(pixmap)
            self.label_17.setScaledContents(True)

    def nextpagetop(self):
        pixmap = QPixmap('images/Aadhar Back Side Top.jpg')
        self.label_17.setPixmap(pixmap)
        self.label_17.setScaledContents(True)

    def defaultfooter(self):
        pixmap1 = QPixmap('images/footertext/hinditext.jpg')
        self.label_15.setPixmap(pixmap1)
        self.label_15.setScaledContents(True)
        # self.label_15.adjustSize()

    def hindifooter(self):
        if self.ui.checkBox_16.isChecked() == True:
            pixmap1 = QPixmap('images/footertext/hinditext.jpg')
            self.label_15.setPixmap(pixmap1)
            self.label_15.setScaledContents(True)

        else:
            pixmap = QPixmap(None)
            self.label_15.setPixmap(pixmap)
            self.label_15.setScaledContents(True)

    def Tamilfooter(self):
        if self.ui.checkBox_17.isChecked() == True:
            pixmap1 = QPixmap('images/footertext/Tamiltext.png')
            self.label_15.setPixmap(pixmap1)
            self.label_15.setScaledContents(True)
        else:
            pixmap = QPixmap(None)
            self.label_15.setPixmap(pixmap)
            self.label_15.setScaledContents(True)

    def Marathifooter(self):
        if self.ui.checkBox_19.isChecked() == True:
            pixmap1 = QPixmap('images/footertext/Marathitext.png')
            self.label_15.setPixmap(pixmap1)
            self.label_15.setScaledContents(True)
        else:
            pixmap = QPixmap(None)
            self.label_15.setPixmap(pixmap)
            self.label_15.setScaledContents(True)

    def Punjabifooter(self):
        if self.ui.checkBox_18.isChecked() == True:
            pixmap1 = QPixmap('images/footertext/Punjabitext.png')
            self.label_15.setPixmap(pixmap1)
            self.label_15.setScaledContents(True)
        else:
            pixmap = QPixmap(None)
            self.label_15.setPixmap(pixmap)
            self.label_15.setScaledContents(True)

    def FrontPageFooter(self):
        if self.ui.checkBox_3.isChecked() == True:
            if self.ui.checkBox_16.isChecked():
                self.hindifooter()
            elif self.ui.checkBox_17.isChecked():
                self.Tamilfooter()
            elif self.ui.checkBox_19.isChecked():
                self.Marathifooter()
            else:
                pixmap = QPixmap(None)
                self.label_15.setPixmap(pixmap)
                self.label_15.setScaledContents(True)

        else:
            pixmap = QPixmap(None)
            self.label_15.setPixmap(pixmap)
            self.label_15.setScaledContents(True)

    def put_dd(self):
        filename = os.path.join(self.path, "img01.png")
        fnt = ImageFont.truetype('arial.ttf', 37)
        # create new image
        a = self.text_ex["Downloaddate"]
        image = Image.new(mode="RGB", size=(440, 100), color="white")
        draw = ImageDraw.Draw(image)
        draw.text((18, 18), a, font=fnt, fill=(0, 0, 0))
        image.save(filename)

        # os.system(filename)
        angle = 90  # What angle would you like to rotate
        self.pixmap = QPixmap(filename)  # image for your label
        pixmap_rotated = self.pixmap.transformed(QTransform().rotate(angle), QtCore.Qt.SmoothTransformation)
        self.label_31.setPixmap(pixmap_rotated)  # set rotated pixmap into your QLabel
        self.label_31.setScaledContents(True)
        self.label_31.setAlignment(Qt.AlignCenter)
        self.label_31.setStyleSheet("QLabel {background-color: white;}")

    def put_id(self):
        filename = os.path.join(self.path, "img02.png")
        fnt = ImageFont.truetype('arial.ttf', 37)
        # create new image
        image = Image.new(mode="RGB", size=(440, 100), color="white")
        draw = ImageDraw.Draw(image)
        a = self.text_ex["Issuedate"]
        draw.text((0, 0), a, font=fnt, fill=(0, 0, 0))
        image.save(filename)

        # os.system(filename)
        angle = 270 + 180  # What angle would you like to rotate
        self.pixmap = QPixmap(filename)  # image for your label
        pixmap_rotated = self.pixmap.transformed(QTransform().rotate(angle), QtCore.Qt.SmoothTransformation)
        self.label_32.setPixmap(pixmap_rotated)  # set rotated pixmap into your QLabel
        self.label_32.setScaledContents(True)
        self.label_32.setAlignment(Qt.AlignCenter)

    def dd(self):
        if self.ui.checkBox_11.isChecked() == True:
            self.put_dd()
        else:
            pixmap = QPixmap(None)
            self.label_31.setPixmap(pixmap)
            self.label_31.setScaledContents(True)

    def id(self):
        if self.ui.checkBox_12.isChecked() == True:
            self.put_id()
        else:
            pixmap = QPixmap(None)
            self.label_32.setPixmap(pixmap)
            self.label_32.setScaledContents(True)

    def uid(self):
        if self.ui.checkBox_8.isChecked() == True:
            self.put_uid()
        else:
            pixmap = QPixmap(None)
            self.label_26.setPixmap(pixmap)
            self.label_26.setScaledContents(True)

    def open_settings(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui.setup(self.window)
        self.ui.checkBox_15.setChecked(True)
        self.ui.checkBox_15.toggled.connect(self.vid)
        self.ui.checkBox_14.toggled.connect(self.phnno)
        self.ui.checkBox_7.toggled.connect(self.barcode)
        self.ui.checkBox_2.setChecked(True)
        self.ui.checkBox_2.toggled.connect(self.frontpageheadermargin)
        self.ui.checkBox_5.setChecked(True)
        self.ui.checkBox_5.toggled.connect(self.RearPageFooterMargin)
        self.ui.checkBox.setChecked(True)
        self.ui.checkBox.toggled.connect(self.frontpageheader)
        self.ui.checkBox_6.setChecked(True)
        self.ui.checkBox_6.toggled.connect(self.rearpagefooter)
        # self.ui.checkBox_10.setChecked(True)
        self.ui.checkBox_10.toggled.connect(self.photoframe)
        self.ui.checkBox_4.setChecked(True)
        self.ui.checkBox_4.toggled.connect(self.rearpageheader)
        self.ui.checkBox_16.setChecked(True)
        self.ui.checkBox_16.toggled.connect(self.hindifooter)
        self.ui.checkBox_17.toggled.connect(self.Tamilfooter)
        self.ui.checkBox_18.toggled.connect(self.Punjabifooter)
        self.ui.checkBox_19.toggled.connect(self.Marathifooter)
        self.ui.checkBox_3.setChecked(True)
        self.ui.checkBox_3.toggled.connect(self.FrontPageFooter)
        self.ui.checkBox_11.toggled.connect(self.dd)
        self.ui.checkBox_12.toggled.connect(self.id)
        self.ui.checkBox_8.toggled.connect(self.uid)

        self.window.show()

    def resizeimage(self):
        self.Resize = QtWidgets.QMainWindow()
        self.ui2 = Ui_MainWindow9()
        self.ui2.setupUi(self.Resize)
        self.ui2.horizontalSlider_11.valueChanged[int].connect(self.height)
        self.ui2.horizontalSlider_10.valueChanged[int].connect(self.Width)
        self.ui2.horizontalSlider_9.valueChanged[int].connect(self.side)
        self.Resize.show()

    def side(self, value):
        w = self.ui2.horizontalSlider_9.value()
        self.label_25.resize(w, w)

    def height(self, value):
        w = self.ui2.horizontalSlider_10.value()
        self.label_9.resize(w, value)

    def Width(self, value):
        h = self.ui2.horizontalSlider_11.value()
        self.label_9.resize(value, h)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
