# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardgDVTlL.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QToolBox,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1357, 722)
        MainWindow.setStyleSheet(u"* {\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(24, 24, 36);\n"
"	")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QFrame(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMinimumSize(QSize(0, 0))
        self.sidebar.setMaximumSize(QSize(200, 16777215))
        self.sidebar.setStyleSheet(u"background-color: rgb(9, 5, 13);")
        self.sidebar.setFrameShape(QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sidebar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.slide_menu = QFrame(self.sidebar)
        self.slide_menu.setObjectName(u"slide_menu")
        self.slide_menu.setFrameShape(QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.slide_menu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.slide_menu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/icons/icons/github.svg"))

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.slide_menu)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.frame_3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton_8.setFont(font1)
        self.pushButton_8.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_8.setStyleSheet(u"margin-left: 4px;\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/airplay.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon)

        self.verticalLayout_8.addWidget(self.pushButton_8, 0, Qt.AlignLeft)

        self.toolBox = QToolBox(self.frame_3)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setFont(font1)
        self.toolBox.setStyleSheet(u"QToolBox {\n"
"	text-align: left;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"	border-radius: 5px;\n"
"	text-align: left;\n"
"}")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 200, 594))
        self.verticalLayout_4 = QVBoxLayout(self.page_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.page_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(25)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/briefcase.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/dollar-sign.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.pushButton_2, 0, Qt.AlignHCenter)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/key.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.pushButton_3, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_4, 0, Qt.AlignTop)

        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_3, icon4, u"Employees")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 200, 594))
        self.verticalLayout_3 = QVBoxLayout(self.page_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.page_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setSpacing(25)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon5)
        self.pushButton_4.setIconSize(QSize(25, 25))

        self.verticalLayout_6.addWidget(self.pushButton_4, 0, Qt.AlignHCenter)

        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/trending-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon6)
        self.pushButton_5.setIconSize(QSize(25, 25))

        self.verticalLayout_6.addWidget(self.pushButton_5, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame_5, 0, Qt.AlignTop)

        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/eye.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_4, icon7, u"Sales Overview")

        self.verticalLayout_8.addWidget(self.toolBox)


        self.verticalLayout.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.slide_menu)


        self.horizontalLayout.addWidget(self.sidebar)

        self.main_content = QFrame(self.centralwidget)
        self.main_content.setObjectName(u"main_content")
        self.main_content.setFrameShape(QFrame.StyledPanel)
        self.main_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.main_content)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.main_content)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"background-color: rgb(9, 5, 13);")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon8)
        self.pushButton_6.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.pushButton_6)


        self.horizontalLayout_4.addWidget(self.frame, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_6 = QFrame(self.header)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_27 = QFrame(self.frame_6)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_10 = QPushButton(self.frame_27)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon9)

        self.horizontalLayout_12.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.frame_27)
        self.pushButton_11.setObjectName(u"pushButton_11")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/mail.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon10)

        self.horizontalLayout_12.addWidget(self.pushButton_11)

        self.pushButton_9 = QPushButton(self.frame_27)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon11)

        self.horizontalLayout_12.addWidget(self.pushButton_9)


        self.horizontalLayout_6.addWidget(self.frame_27)

        self.pushButton_7 = QPushButton(self.frame_6)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon12)
        self.pushButton_7.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.pushButton_7)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setBold(True)
        self.label_3.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_3)


        self.horizontalLayout_4.addWidget(self.frame_6, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.header, 0, Qt.AlignTop)

        self.main_body = QFrame(self.main_content)
        self.main_body.setObjectName(u"main_body")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy1)
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.main_body)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_9 = QFrame(self.main_body)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"/*background-color: white;*/")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 240))
        self.frame_14.setMaximumSize(QSize(16777213, 240))
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_14)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_20 = QFrame(self.frame_14)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 200))
        self.frame_20.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.frame_31 = QFrame(self.frame_20)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_11 = QLabel(self.frame_31)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(60, 50))
        self.label_11.setStyleSheet(u"background-color: rgb(24, 24, 36);\n"
"border-radius: 5px;")
        self.label_11.setPixmap(QPixmap(u":/icons/icons/cpu.svg"))
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_31)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.horizontalLayout_18.addWidget(self.label_12)


        self.horizontalLayout_17.addWidget(self.frame_31, 0, Qt.AlignLeft)

        self.pushButton_13 = QPushButton(self.frame_20)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(100, 35))
        self.pushButton_13.setFont(font2)
        self.pushButton_13.setStyleSheet(u"background-color: #E60540;\n"
"border-radius: 5px;")

        self.horizontalLayout_17.addWidget(self.pushButton_13, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_20)

        self.frame_19 = QFrame(self.frame_14)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 16777215))
        self.frame_19.setStyleSheet(u"")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_21)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, -1, 0, 0)
        self.frame_32 = QFrame(self.frame_21)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_13 = QLabel(self.frame_32)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(40, 40))
        self.label_13.setFont(font2)
        self.label_13.setLayoutDirection(Qt.LeftToRight)
        self.label_13.setStyleSheet(u"background-color: rgb(24, 24, 36);\n"
"border-radius: 5px;")
        self.label_13.setPixmap(QPixmap(u":/icons/icons/anchor.svg"))
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_13, 0, Qt.AlignVCenter)

        self.label_14 = QLabel(self.frame_32)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)

        self.horizontalLayout_19.addWidget(self.label_14, 0, Qt.AlignHCenter)


        self.verticalLayout_16.addWidget(self.frame_32)


        self.horizontalLayout_10.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_22)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, -1, 0, 0)
        self.frame_33 = QFrame(self.frame_22)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_15 = QLabel(self.frame_33)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(40, 40))
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"background-color: rgb(24, 24, 36);\n"
"border-radius: 5px;")
        self.label_15.setPixmap(QPixmap(u":/icons/icons/loader.svg"))
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_15, 0, Qt.AlignVCenter)

        self.label_16 = QLabel(self.frame_33)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)

        self.horizontalLayout_20.addWidget(self.label_16, 0, Qt.AlignHCenter)


        self.verticalLayout_17.addWidget(self.frame_33)


        self.horizontalLayout_10.addWidget(self.frame_22)


        self.verticalLayout_12.addWidget(self.frame_19)


        self.verticalLayout_10.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 300))
        self.frame_13.setMaximumSize(QSize(16777215, 16777215))
        self.frame_13.setStyleSheet(u"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_16)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(-1, 9, -1, 9)

        self.horizontalLayout_9.addWidget(self.frame_16)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_15)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_17)
        self.verticalLayout_18.setSpacing(2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_34 = QFrame(self.frame_17)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMaximumSize(QSize(16777215, 40))
        self.frame_34.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_34)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_18 = QLabel(self.frame_34)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)

        self.verticalLayout_20.addWidget(self.label_18)


        self.verticalLayout_18.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.frame_17)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.frame_38 = QFrame(self.frame_35)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"background-color: rgb(24, 24, 36);")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_38)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_19 = QLabel(self.frame_38)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)

        self.verticalLayout_22.addWidget(self.label_19, 0, Qt.AlignHCenter)


        self.horizontalLayout_21.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frame_35)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_39)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_20 = QLabel(self.frame_39)
        self.label_20.setObjectName(u"label_20")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.label_20.setFont(font3)

        self.verticalLayout_23.addWidget(self.label_20, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_21 = QLabel(self.frame_39)
        self.label_21.setObjectName(u"label_21")
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(False)
        self.label_21.setFont(font4)

        self.verticalLayout_23.addWidget(self.label_21, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_21.addWidget(self.frame_39)


        self.verticalLayout_18.addWidget(self.frame_35)


        self.verticalLayout_11.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_18)
        self.verticalLayout_19.setSpacing(2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_36 = QFrame(self.frame_18)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMaximumSize(QSize(16777215, 40))
        self.frame_36.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_36)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_17 = QLabel(self.frame_36)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)

        self.verticalLayout_21.addWidget(self.label_17)


        self.verticalLayout_19.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.frame_18)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)

        self.verticalLayout_19.addWidget(self.frame_37)


        self.verticalLayout_11.addWidget(self.frame_18)


        self.horizontalLayout_9.addWidget(self.frame_15)


        self.verticalLayout_10.addWidget(self.frame_13)


        self.horizontalLayout_3.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.main_body)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 0))
        self.frame_10.setMaximumSize(QSize(16777215, 16777215))
        self.frame_10.setStyleSheet(u"/*background-color: grey;*/")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 240))
        self.frame_12.setMaximumSize(QSize(16777215, 240))
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_12)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_23 = QFrame(self.frame_12)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(16777215, 200))
        self.frame_23.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_28 = QFrame(self.frame_23)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_5 = QLabel(self.frame_28)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(60, 50))
        self.label_5.setStyleSheet(u"background-color: rgb(24, 24, 36);\n"
"border-radius: 5px;")
        self.label_5.setPixmap(QPixmap(u":/icons/icons/briefcase.svg"))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_5)

        self.label_4 = QLabel(self.frame_28)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.horizontalLayout_13.addWidget(self.label_4)


        self.horizontalLayout_14.addWidget(self.frame_28, 0, Qt.AlignLeft)

        self.pushButton_12 = QPushButton(self.frame_23)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(100, 35))
        font5 = QFont()
        font5.setPointSize(9)
        font5.setBold(True)
        self.pushButton_12.setFont(font5)
        self.pushButton_12.setStyleSheet(u"background-color: #E60540;\n"
"border-radius: 5px;")

        self.horizontalLayout_14.addWidget(self.pushButton_12, 0, Qt.AlignRight)


        self.verticalLayout_13.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_12)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_25)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, -1, 0, 0)
        self.frame_29 = QFrame(self.frame_25)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, -1, -1, 9)
        self.label_7 = QLabel(self.frame_29)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(40, 40))
        self.label_7.setStyleSheet(u"background-color: rgb(24, 24, 36);\n"
"border-radius: 5px;")
        self.label_7.setPixmap(QPixmap(u":/icons/icons/speaker.svg"))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_7, 0, Qt.AlignVCenter)

        self.label_6 = QLabel(self.frame_29)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.horizontalLayout_15.addWidget(self.label_6, 0, Qt.AlignHCenter)


        self.verticalLayout_14.addWidget(self.frame_29)


        self.horizontalLayout_11.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_24)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_26)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, -1, 0, 0)
        self.frame_30 = QFrame(self.frame_26)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_8 = QLabel(self.frame_30)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(40, 40))
        self.label_8.setStyleSheet(u"background-color: rgb(24, 24, 36);\n"
"border-radius: 5px;")
        self.label_8.setPixmap(QPixmap(u":/icons/icons/mic.svg"))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_30)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.horizontalLayout_16.addWidget(self.label_9, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.frame_30)


        self.horizontalLayout_11.addWidget(self.frame_26)


        self.verticalLayout_13.addWidget(self.frame_24)


        self.verticalLayout_9.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_11)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, -1, 0, -1)
        self.frame_41 = QFrame(self.frame_11)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(2, -1, 2, -1)
        self.pushButton_14 = QPushButton(self.frame_41)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setFont(font2)
        self.pushButton_14.setStyleSheet(u"")

        self.horizontalLayout_22.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.frame_41)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setFont(font2)

        self.horizontalLayout_22.addWidget(self.pushButton_15)


        self.verticalLayout_25.addWidget(self.frame_41, 0, Qt.AlignTop)

        self.frame_40 = QFrame(self.frame_11)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy1.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy1)
        self.frame_40.setStyleSheet(u"")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.label_10 = QLabel(self.frame_40)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(160, 90, 81, 16))
        self.label_10.setFont(font2)

        self.verticalLayout_25.addWidget(self.frame_40)


        self.verticalLayout_9.addWidget(self.frame_11)


        self.horizontalLayout_3.addWidget(self.frame_10)


        self.verticalLayout_7.addWidget(self.main_body)

        self.footer = QFrame(self.main_content)
        self.footer.setObjectName(u"footer")
        self.footer.setStyleSheet(u"")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.footer)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.footer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(10, 10))
        self.frame_8.setMaximumSize(QSize(10, 10))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_8, 0, Qt.AlignRight|Qt.AlignBottom)


        self.horizontalLayout_7.addWidget(self.frame_7)


        self.verticalLayout_7.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.main_content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.label_2.setText("")
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Management", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Sales", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Permissions", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"Employees", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Total Sales", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Profit", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"Sales Overview", None))
        self.pushButton_6.setText("")
        self.pushButton_10.setText("")
        self.pushButton_11.setText("")
        self.pushButton_9.setText("")
        self.pushButton_7.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"User 1", None))
        self.label_11.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Title of label card", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Support", None))
        self.label_13.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Title of label card", None))
        self.label_15.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Title of label card 2", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Solar Energy Consumption", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"GRAPH HERE", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"6.421 kWh", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"out of 8.421 kWh", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Traffic Consumption", None))
        self.label_5.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Title of label card 2", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.label_7.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Title of label card 3", None))
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Title of label card 4", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"ELECTRICITY CONSUMPTION", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"DEVICES", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"GRAPH HERE", None))
    # retranslateUi

