# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerKTqTUw.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from backend import *
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                         QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                         QRadialGradient, QStandardItemModel, QStandardItem)
import messagebox
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(794, 599)
        icon = QIcon()
        icon.addFile(u"./images/library.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color:#a2e4eb")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 771, 161))
        self.frame.setStyleSheet(u"border: 1px solid gray;\n"
"background-color: rgb(235, 235, 235,0.9);\n"
"border-radius: 5px;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(400, 19, 261, 31))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(Qt.RightToLeft)
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding-right: 5px;\n"
"padding-left: 5px;")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(30, 20, 261, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding-right: 5px;\n"
"padding-left: 5px;")
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(400, 80, 261, 31))
        self.lineEdit_3.setFont(font1)
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding-right: 5px;\n"
"padding-left: 5px;")
        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(30, 80, 261, 31))
        self.lineEdit_4.setFont(font1)
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding-right: 5px;\n"
"padding-left: 5px;")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(680, 20, 81, 31))
        self.label.setStyleSheet(u"border:none;\n"
"font-size:14px;\n"
"font-weight: bold;background:transparent;")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 20, 71, 31))
        self.label_2.setStyleSheet(u"border:none;\n"
"font-size:14px;\n"
"font-weight: bold;background:transparent;")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(680, 80, 81, 31))
        self.label_3.setStyleSheet(u"border:none;\n"
"font-size:14px;\n"
"font-weight: bold;background:transparent;")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(300, 80, 81, 31))
        self.label_4.setStyleSheet(u"border:none;\n"
"font-size:14px;\n"
"font-weight: bold;background:transparent;")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(580, 179, 201, 371))
        self.frame_2.setStyleSheet(u"border: 1px solid gray;\n"
"background-color: rgb(235, 235, 235 , 0.9);\n"
" border-radius: 5px;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 30, 181, 41))
        self.pushButton.setStyleSheet(u"font-size:13px;\n"
"font-weight: bold;\n"
"background-color: rgb(17, 173, 0);\n"
"color:#fff;")
        icon1 = QIcon()
        icon1.addFile(u"./images/add-symbol .png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(22, 22))
        self.pushButton.setCheckable(True)
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 90, 181, 41))
        self.pushButton_2.setStyleSheet(u"font-size:13px;\n"
"font-weight: bold;\n"
"background-color: rgb(51, 0, 255);\n"
"color:#fff;")
        icon2 = QIcon()
        icon2.addFile(u"./images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 150, 181, 41))
        self.pushButton_3.setStyleSheet(u"font-size:11px;\n"
"font-weight: bold;\n"
"background-color: rgb(217, 192, 0);\n"
"color:#fff;")
        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 210, 181, 41))
        self.pushButton_4.setStyleSheet(u"font-size:13px;\n"
"background-color: rgb(0, 166, 175);\n"
"font-weight: bold;\n"
"\n"
"color:#fff;")
        self.pushButton_4.setText('قرض دادن')
        icon3 = QIcon()
        icon3.addFile(u"./images/editing.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 270, 181, 41))
        self.pushButton_5.setStyleSheet(u"font-size:13px;\n"
"font-weight: bold;\n"
"background-color: rgb(186, 0, 0);\n"
"color:#fff;")
        self.pushButton_5.setText('گزارش ها')
        icon4 = QIcon()
        icon4.addFile(u"./images/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(9, 179, 561, 371))
        self.frame_3.setStyleSheet(u"border: 1px solid gray;\n"
"background-color: rgb(235, 235, 235 , 0.9);\n"
"border-radius: 5px;\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.scrollArea = QScrollArea(self.frame_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(9, 9, 541, 351))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollAreaWidgetContents = QWidget()
        self.scroll_layout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scroll_layout.setAlignment(Qt.AlignTop)
        # self.scroll_layout.set
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 794, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.add_book)
        self.pushButton_2.clicked.connect(self.search_book)
        self.pushButton_3.clicked.connect(self.search_category)
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    def add_book(self):
        title = self.lineEdit.text()
        author = self.lineEdit_2.text()
        isnb = self.lineEdit_3.text()
        category = self.lineEdit_4.text()
        if len(title.strip()) > 2 and len(author.strip()) > 2 and len(isnb.strip()) > 3 and len(category.strip()) > 2:
            res = add_book(title=title , author=author , isnb=isnb , category=category)
            if res =="success":
                messagebox.showinfo('Success' , f'کتاب {title}  با موفقیت اضافه شد')
                self.lineEdit.setText('')
                self.lineEdit_2.setText('')
                self.lineEdit_3.setText('')
                self.lineEdit_4.setText('')
        else:
            messagebox.showerror('Error' , 'تمامی موارد را با دقت وارد کنید')
    def search_book(self):
        self.clear_layout()
        title = self.lineEdit.text()
        res = search_for_title(title)
        for item in res:
            title_label = item[1]
            book_label = QLabel(title_label)
            book_label.setText(title_label)
            book_label.setFixedHeight(50)
            book_label.setFixedWidth(450)
            book_label.setGeometry(QRect(20, 20, 501, 41))
            book_label.setStyleSheet(u"background-color: lightgreen;\n"
                                       "font-size:14px;\n"
                                       "padding-right:20px;\n"
                                       "font-weight: bold;margin:2px;")
            edit_button = QPushButton(self.scrollAreaWidgetContents)
            edit_button.setIcon(QIcon('./images/editing.png'))
            edit_button.setStyleSheet(u"border:none;")
            delete_button =QPushButton(self.scrollAreaWidgetContents)
            delete_button.setIcon(QIcon('./images/delete.png'))
            delete_button.setStyleSheet(u"border:none")
            sub_layout = QHBoxLayout()
            sub_layout.addWidget(delete_button)
            sub_layout.addWidget(edit_button)
            sub_layout.addWidget(book_label)
            self.scroll_layout.addLayout(sub_layout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

    def clear_layout(self):
        self.scrollAreaWidgetContents = QWidget()
        self.scroll_layout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scroll_layout.setAlignment(Qt.AlignTop)
    def search_category(self):
        self.clear_layout()
        category = self.lineEdit_4.text()
        res = search_for_category(category=category)
        for item in res:
            title_label = item[1]
            book_label = QLabel(title_label)
            book_label.setText(title_label)
            book_label.setFixedHeight(50)
            book_label.setGeometry(QRect(20, 20, 501, 41))
            book_label.setStyleSheet(u"background-color: lightgreen;\n"
                                     "font-size:14px;\n"
                                     "padding-right:20px;\n"
                                     "font-weight: bold;margin:2px;")

            self.scroll_layout.addWidget(book_label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Library App", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0646\u0648\u0627\u0646 \u06a9\u062a\u0627\u0628 :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0648\u06cc\u0633\u0646\u062f\u0647 :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u": isnb \u0634\u0627\u0628\u06a9", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0633\u062a\u0647 \u0628\u0646\u062f\u06cc :", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u" \u062b\u0628\u062a \u06a9\u062a\u0627\u0628 \u062c\u062f\u06cc\u062f", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0633\u062a\u062c\u0648\u06cc \u0639\u0646\u0648\u0627\u0646", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0633\u062a\u062c\u0648\u06cc \u0628\u0631 \u0627\u0633\u0627\u0633 \u062f\u0633\u062a\u0647 \u0628\u0646\u062f\u06cc", None))
        # self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0648\u06cc\u0631\u0627\u06cc\u0634  \u06a9\u062a\u0627\u0628", None))
        # self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641 \u06a9\u062a\u0627\u0628", None))
        # self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0646\u0648\u0627\u0646 \u06a9\u062a\u0627\u0628", None))
    # retranslateUi

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)
window.show()
sys.exit(app.exec())
