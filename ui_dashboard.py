# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardImtffK.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import icons_rc
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1178, 679)
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
        self.logo_frame = QFrame(self.slide_menu)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setFrameShape(QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.logo_frame)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 6, 6)
        self.label_app_name = QLabel(self.logo_frame)
        self.label_app_name.setObjectName(u"label_app_name")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_app_name.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_app_name)

        self.icon_app = QLabel(self.logo_frame)
        self.icon_app.setObjectName(u"icon_app")
        self.icon_app.setPixmap(QPixmap(u":/icons/icons/github.svg"))

        self.horizontalLayout_2.addWidget(self.icon_app)


        self.verticalLayout.addWidget(self.logo_frame, 0, Qt.AlignTop)

        self.sidebar_content_frame = QFrame(self.slide_menu)
        self.sidebar_content_frame.setObjectName(u"sidebar_content_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar_content_frame.sizePolicy().hasHeightForWidth())
        self.sidebar_content_frame.setSizePolicy(sizePolicy)
        self.sidebar_content_frame.setStyleSheet(u"QPushButton {\n"
"	text-align: left;\n"
"	margin-left: 4px;\n"
"	padding: 9px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(19, 15, 23);\n"
"}")
        self.sidebar_content_frame.setFrameShape(QFrame.StyledPanel)
        self.sidebar_content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.sidebar_content_frame)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 50, 0, -1)
        self.button_dashboard = QPushButton(self.sidebar_content_frame)
        self.button_dashboard.setObjectName(u"button_dashboard")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_dashboard.sizePolicy().hasHeightForWidth())
        self.button_dashboard.setSizePolicy(sizePolicy1)
        self.button_dashboard.setMinimumSize(QSize(0, 0))
        self.button_dashboard.setMaximumSize(QSize(300, 16777215))
        self.button_dashboard.setFont(font)
        self.button_dashboard.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_dashboard.setLayoutDirection(Qt.LeftToRight)
        self.button_dashboard.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/airplay.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_dashboard.setIcon(icon)
        self.button_dashboard.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.button_dashboard)

        self.button_employees = QPushButton(self.sidebar_content_frame)
        self.button_employees.setObjectName(u"button_employees")
        self.button_employees.setMaximumSize(QSize(300, 16777215))
        self.button_employees.setFont(font)
        self.button_employees.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_employees.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_employees.setIcon(icon1)
        self.button_employees.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.button_employees)

        self.button_orders = QPushButton(self.sidebar_content_frame)
        self.button_orders.setObjectName(u"button_orders")
        self.button_orders.setFont(font)
        self.button_orders.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_orders.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/credit-card.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_orders.setIcon(icon2)
        self.button_orders.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.button_orders)

        self.button_sales = QPushButton(self.sidebar_content_frame)
        self.button_sales.setObjectName(u"button_sales")
        self.button_sales.setFont(font)
        self.button_sales.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_sales.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/dollar-sign.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_sales.setIcon(icon3)
        self.button_sales.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.button_sales)

        self.button_profit = QPushButton(self.sidebar_content_frame)
        self.button_profit.setObjectName(u"button_profit")
        self.button_profit.setFont(font)
        self.button_profit.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_profit.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/trending-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_profit.setIcon(icon4)
        self.button_profit.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.button_profit)

        self.button_permissions = QPushButton(self.sidebar_content_frame)
        self.button_permissions.setObjectName(u"button_permissions")
        self.button_permissions.setFont(font)
        self.button_permissions.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_permissions.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/key.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_permissions.setIcon(icon5)
        self.button_permissions.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.button_permissions)

        self.button_management = QPushButton(self.sidebar_content_frame)
        self.button_management.setObjectName(u"button_management")
        self.button_management.setFont(font)
        self.button_management.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_management.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/briefcase.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_management.setIcon(icon6)
        self.button_management.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.button_management)


        self.verticalLayout.addWidget(self.sidebar_content_frame)


        self.verticalLayout_2.addWidget(self.slide_menu, 0, Qt.AlignTop)


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
        self.sidebar_button_container = QFrame(self.header)
        self.sidebar_button_container.setObjectName(u"sidebar_button_container")
        self.sidebar_button_container.setFrameShape(QFrame.StyledPanel)
        self.sidebar_button_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.sidebar_button_container)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.button_sidebar = QPushButton(self.sidebar_button_container)
        self.button_sidebar.setObjectName(u"button_sidebar")
        self.button_sidebar.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_sidebar.setIcon(icon7)
        self.button_sidebar.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.button_sidebar)


        self.horizontalLayout_4.addWidget(self.sidebar_button_container, 0, Qt.AlignLeft|Qt.AlignTop)

        self.navbar_container = QFrame(self.header)
        self.navbar_container.setObjectName(u"navbar_container")
        self.navbar_container.setFrameShape(QFrame.StyledPanel)
        self.navbar_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.navbar_container)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.navbar_tools = QFrame(self.navbar_container)
        self.navbar_tools.setObjectName(u"navbar_tools")
        self.navbar_tools.setFrameShape(QFrame.StyledPanel)
        self.navbar_tools.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.navbar_tools)
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.button_search = QPushButton(self.navbar_tools)
        self.button_search.setObjectName(u"button_search")
        self.button_search.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_search.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_search.setIcon(icon8)

        self.horizontalLayout_12.addWidget(self.button_search)

        self.button_messages = QPushButton(self.navbar_tools)
        self.button_messages.setObjectName(u"button_messages")
        self.button_messages.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/mail.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_messages.setIcon(icon9)

        self.horizontalLayout_12.addWidget(self.button_messages)

        self.button_notifications = QPushButton(self.navbar_tools)
        self.button_notifications.setObjectName(u"button_notifications")
        self.button_notifications.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_notifications.setIcon(icon10)

        self.horizontalLayout_12.addWidget(self.button_notifications)


        self.horizontalLayout_6.addWidget(self.navbar_tools)

        self.button_user = QPushButton(self.navbar_container)
        self.button_user.setObjectName(u"button_user")
        self.button_user.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_user.setIcon(icon11)
        self.button_user.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.button_user)

        self.label_username = QLabel(self.navbar_container)
        self.label_username.setObjectName(u"label_username")
        font1 = QFont()
        font1.setBold(True)
        self.label_username.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_username)


        self.horizontalLayout_4.addWidget(self.navbar_container, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.header, 0, Qt.AlignTop)

        self.main_body = QFrame(self.main_content)
        self.main_body.setObjectName(u"main_body")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy2)
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.main_body)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.information_group_1 = QFrame(self.main_body)
        self.information_group_1.setObjectName(u"information_group_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.information_group_1.sizePolicy().hasHeightForWidth())
        self.information_group_1.setSizePolicy(sizePolicy3)
        self.information_group_1.setStyleSheet(u"/*background-color: white;*/")
        self.information_group_1.setFrameShape(QFrame.StyledPanel)
        self.information_group_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.information_group_1)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.information_cards_frame_1 = QFrame(self.information_group_1)
        self.information_cards_frame_1.setObjectName(u"information_cards_frame_1")
        self.information_cards_frame_1.setMinimumSize(QSize(0, 240))
        self.information_cards_frame_1.setMaximumSize(QSize(16777213, 240))
        self.information_cards_frame_1.setStyleSheet(u"")
        self.information_cards_frame_1.setFrameShape(QFrame.StyledPanel)
        self.information_cards_frame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.information_cards_frame_1)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.primary_card_frame_1 = QFrame(self.information_cards_frame_1)
        self.primary_card_frame_1.setObjectName(u"primary_card_frame_1")
        self.primary_card_frame_1.setMaximumSize(QSize(16777215, 200))
        self.primary_card_frame_1.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.primary_card_frame_1.setFrameShape(QFrame.StyledPanel)
        self.primary_card_frame_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.primary_card_frame_1)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.primary_card_left_content_1 = QFrame(self.primary_card_frame_1)
        self.primary_card_left_content_1.setObjectName(u"primary_card_left_content_1")
        self.primary_card_left_content_1.setStyleSheet(u"")
        self.primary_card_left_content_1.setFrameShape(QFrame.StyledPanel)
        self.primary_card_left_content_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.primary_card_left_content_1)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.icon_primary_card_1 = QLabel(self.primary_card_left_content_1)
        self.icon_primary_card_1.setObjectName(u"icon_primary_card_1")
        self.icon_primary_card_1.setMinimumSize(QSize(60, 50))
        self.icon_primary_card_1.setStyleSheet(u"background-color: rgb(24, 24, 36);\n"
"border-radius: 5px;")
        self.icon_primary_card_1.setPixmap(QPixmap(u":/icons/icons/cpu.svg"))
        self.icon_primary_card_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.icon_primary_card_1)

        self.label_primary_card_1 = QLabel(self.primary_card_left_content_1)
        self.label_primary_card_1.setObjectName(u"label_primary_card_1")
        self.label_primary_card_1.setFont(font1)

        self.horizontalLayout_18.addWidget(self.label_primary_card_1)


        self.horizontalLayout_17.addWidget(self.primary_card_left_content_1, 0, Qt.AlignLeft)

        self.button_support = QPushButton(self.primary_card_frame_1)
        self.button_support.setObjectName(u"button_support")
        self.button_support.setMinimumSize(QSize(100, 35))
        self.button_support.setFont(font1)
        self.button_support.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_support.setStyleSheet(u"QPushButton {\n"
"	background-color: #E60540;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #C50332;\n"
"}")

        self.horizontalLayout_17.addWidget(self.button_support, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.primary_card_frame_1)

        self.secondary_card_frame_1 = QFrame(self.information_cards_frame_1)
        self.secondary_card_frame_1.setObjectName(u"secondary_card_frame_1")
        self.secondary_card_frame_1.setMaximumSize(QSize(16777215, 16777215))
        self.secondary_card_frame_1.setStyleSheet(u"")
        self.secondary_card_frame_1.setFrameShape(QFrame.StyledPanel)
        self.secondary_card_frame_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.secondary_card_frame_1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.secondary_card_left_frame_1 = QFrame(self.secondary_card_frame_1)
        self.secondary_card_left_frame_1.setObjectName(u"secondary_card_left_frame_1")
        self.secondary_card_left_frame_1.setStyleSheet(u"")
        self.secondary_card_left_frame_1.setFrameShape(QFrame.StyledPanel)
        self.secondary_card_left_frame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.secondary_card_left_frame_1)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 9, 0, 0)
        self.secondary_card_left_content_1 = QFrame(self.secondary_card_left_frame_1)
        self.secondary_card_left_content_1.setObjectName(u"secondary_card_left_content_1")
        self.secondary_card_left_content_1.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.secondary_card_left_content_1.setFrameShape(QFrame.StyledPanel)
        self.secondary_card_left_content_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.secondary_card_left_content_1)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.icon_secondary_card_left_1 = QLabel(self.secondary_card_left_content_1)
        self.icon_secondary_card_left_1.setObjectName(u"icon_secondary_card_left_1")
        self.icon_secondary_card_left_1.setMinimumSize(QSize(40, 40))
        self.icon_secondary_card_left_1.setFont(font1)
        self.icon_secondary_card_left_1.setLayoutDirection(Qt.LeftToRight)
        self.icon_secondary_card_left_1.setStyleSheet(u"background-color: rgb(24, 24, 36);\n"
"border-radius: 5px;")
        self.icon_secondary_card_left_1.setPixmap(QPixmap(u":/icons/icons/anchor.svg"))
        self.icon_secondary_card_left_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.icon_secondary_card_left_1)

        self.label_secondary_card_left_1 = QLabel(self.secondary_card_left_content_1)
        self.label_secondary_card_left_1.setObjectName(u"label_secondary_card_left_1")
        self.label_secondary_card_left_1.setFont(font1)

        self.horizontalLayout_19.addWidget(self.label_secondary_card_left_1, 0, Qt.AlignHCenter)


        self.verticalLayout_16.addWidget(self.secondary_card_left_content_1)


        self.horizontalLayout_10.addWidget(self.secondary_card_left_frame_1)

        self.secondary_card_right_frame_1 = QFrame(self.secondary_card_frame_1)
        self.secondary_card_right_frame_1.setObjectName(u"secondary_card_right_frame_1")
        self.secondary_card_right_frame_1.setStyleSheet(u"")
        self.secondary_card_right_frame_1.setFrameShape(QFrame.StyledPanel)
        self.secondary_card_right_frame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.secondary_card_right_frame_1)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, -1, 0, 0)
        self.secondary_card_right_content_1 = QFrame(self.secondary_card_right_frame_1)
        self.secondary_card_right_content_1.setObjectName(u"secondary_card_right_content_1")
        self.secondary_card_right_content_1.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.secondary_card_right_content_1.setFrameShape(QFrame.StyledPanel)
        self.secondary_card_right_content_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.secondary_card_right_content_1)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.icon_secondary_card_right_1 = QLabel(self.secondary_card_right_content_1)
        self.icon_secondary_card_right_1.setObjectName(u"icon_secondary_card_right_1")
        self.icon_secondary_card_right_1.setMinimumSize(QSize(40, 40))
        self.icon_secondary_card_right_1.setFont(font1)
        self.icon_secondary_card_right_1.setStyleSheet(u"background-color: rgb(24, 24, 36);\n"
"border-radius: 5px;")
        self.icon_secondary_card_right_1.setPixmap(QPixmap(u":/icons/icons/loader.svg"))
        self.icon_secondary_card_right_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.icon_secondary_card_right_1)

        self.label_secondary_card_right_1 = QLabel(self.secondary_card_right_content_1)
        self.label_secondary_card_right_1.setObjectName(u"label_secondary_card_right_1")
        self.label_secondary_card_right_1.setFont(font1)

        self.horizontalLayout_20.addWidget(self.label_secondary_card_right_1, 0, Qt.AlignHCenter)


        self.verticalLayout_17.addWidget(self.secondary_card_right_content_1)


        self.horizontalLayout_10.addWidget(self.secondary_card_right_frame_1)


        self.verticalLayout_12.addWidget(self.secondary_card_frame_1)


        self.verticalLayout_10.addWidget(self.information_cards_frame_1)

        self.data_frame_1 = QFrame(self.information_group_1)
        self.data_frame_1.setObjectName(u"data_frame_1")
        self.data_frame_1.setMinimumSize(QSize(0, 300))
        self.data_frame_1.setMaximumSize(QSize(16777215, 16777215))
        self.data_frame_1.setStyleSheet(u"")
        self.data_frame_1.setFrameShape(QFrame.StyledPanel)
        self.data_frame_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.data_frame_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.main_graph_frame_1 = QFrame(self.data_frame_1)
        self.main_graph_frame_1.setObjectName(u"main_graph_frame_1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.main_graph_frame_1.sizePolicy().hasHeightForWidth())
        self.main_graph_frame_1.setSizePolicy(sizePolicy4)
        self.main_graph_frame_1.setMinimumSize(QSize(300, 0))
        self.main_graph_frame_1.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.main_graph_frame_1.setFrameShape(QFrame.StyledPanel)
        self.main_graph_frame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.main_graph_frame_1)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(-1, 9, -1, 9)
        self.tab_container_1 = QFrame(self.main_graph_frame_1)
        self.tab_container_1.setObjectName(u"tab_container_1")
        self.tab_container_1.setFrameShape(QFrame.StyledPanel)
        self.tab_container_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.tab_container_1)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(2, -1, 2, -1)
        self.button_temperature = QPushButton(self.tab_container_1)
        self.button_temperature.setObjectName(u"button_temperature")
        self.button_temperature.setFont(font1)

        self.horizontalLayout_23.addWidget(self.button_temperature)

        self.button_humidity = QPushButton(self.tab_container_1)
        self.button_humidity.setObjectName(u"button_humidity")
        self.button_humidity.setFont(font1)

        self.horizontalLayout_23.addWidget(self.button_humidity)


        self.verticalLayout_24.addWidget(self.tab_container_1, 0, Qt.AlignTop)

        self.alternative_graph_frame_1 = QFrame(self.main_graph_frame_1)
        self.alternative_graph_frame_1.setObjectName(u"alternative_graph_frame_1")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.alternative_graph_frame_1.sizePolicy().hasHeightForWidth())
        self.alternative_graph_frame_1.setSizePolicy(sizePolicy5)
        self.alternative_graph_frame_1.setFrameShape(QFrame.StyledPanel)
        self.alternative_graph_frame_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.alternative_graph_frame_1)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.main_information = QFrame(self.alternative_graph_frame_1)
        self.main_information.setObjectName(u"main_information")
        font2 = QFont()
        font2.setBold(False)
        self.main_information.setFont(font2)
        self.main_information.setFrameShape(QFrame.StyledPanel)
        self.main_information.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.main_information)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_temperature = QLabel(self.main_information)
        self.label_temperature.setObjectName(u"label_temperature")
        font3 = QFont()
        font3.setPointSize(24)
        font3.setBold(True)
        self.label_temperature.setFont(font3)

        self.horizontalLayout_25.addWidget(self.label_temperature, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_24.addWidget(self.main_information, 0, Qt.AlignVCenter)

        self.additional_information = QFrame(self.alternative_graph_frame_1)
        self.additional_information.setObjectName(u"additional_information")
        self.additional_information.setFrameShape(QFrame.StyledPanel)
        self.additional_information.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.additional_information)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_wind = QFrame(self.additional_information)
        self.frame_wind.setObjectName(u"frame_wind")
        self.frame_wind.setFrameShape(QFrame.StyledPanel)
        self.frame_wind.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_wind)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_label_wind = QFrame(self.frame_wind)
        self.frame_label_wind.setObjectName(u"frame_label_wind")
        self.frame_label_wind.setMaximumSize(QSize(16777215, 16777215))
        self.frame_label_wind.setFrameShape(QFrame.StyledPanel)
        self.frame_label_wind.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_label_wind)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.icon_wind = QLabel(self.frame_label_wind)
        self.icon_wind.setObjectName(u"icon_wind")
        self.icon_wind.setPixmap(QPixmap(u":/icons/icons/wind.svg"))
        self.icon_wind.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.icon_wind)

        self.label_wind = QLabel(self.frame_label_wind)
        self.label_wind.setObjectName(u"label_wind")
        self.label_wind.setFont(font1)
        self.label_wind.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_wind)


        self.horizontalLayout_26.addWidget(self.frame_label_wind)


        self.verticalLayout_6.addWidget(self.frame_wind)

        self.frame_rain = QFrame(self.additional_information)
        self.frame_rain.setObjectName(u"frame_rain")
        self.frame_rain.setFrameShape(QFrame.StyledPanel)
        self.frame_rain.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_rain)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_labe_rain = QFrame(self.frame_rain)
        self.frame_labe_rain.setObjectName(u"frame_labe_rain")
        self.frame_labe_rain.setFrameShape(QFrame.StyledPanel)
        self.frame_labe_rain.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_labe_rain)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.icon_rain = QLabel(self.frame_labe_rain)
        self.icon_rain.setObjectName(u"icon_rain")
        self.icon_rain.setPixmap(QPixmap(u":/icons/icons/cloud-rain.svg"))
        self.icon_rain.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.icon_rain)

        self.label_rain = QLabel(self.frame_labe_rain)
        self.label_rain.setObjectName(u"label_rain")
        self.label_rain.setFont(font1)
        self.label_rain.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_rain)


        self.horizontalLayout_28.addWidget(self.frame_labe_rain)


        self.verticalLayout_6.addWidget(self.frame_rain)

        self.frame_weather = QFrame(self.additional_information)
        self.frame_weather.setObjectName(u"frame_weather")
        self.frame_weather.setFrameShape(QFrame.StyledPanel)
        self.frame_weather.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_weather)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_label_weather = QFrame(self.frame_weather)
        self.frame_label_weather.setObjectName(u"frame_label_weather")
        self.frame_label_weather.setFrameShape(QFrame.StyledPanel)
        self.frame_label_weather.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_label_weather)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.icon_weather = QLabel(self.frame_label_weather)
        self.icon_weather.setObjectName(u"icon_weather")
        self.icon_weather.setPixmap(QPixmap(u":/icons/icons/sun.svg"))
        self.icon_weather.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.icon_weather)

        self.label_weather = QLabel(self.frame_label_weather)
        self.label_weather.setObjectName(u"label_weather")
        self.label_weather.setFont(font1)
        self.label_weather.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.label_weather)


        self.horizontalLayout_27.addWidget(self.frame_label_weather)


        self.verticalLayout_6.addWidget(self.frame_weather)


        self.horizontalLayout_24.addWidget(self.additional_information)


        self.verticalLayout_24.addWidget(self.alternative_graph_frame_1)


        self.horizontalLayout_9.addWidget(self.main_graph_frame_1)

        self.data_frame_right_content = QFrame(self.data_frame_1)
        self.data_frame_right_content.setObjectName(u"data_frame_right_content")
        self.data_frame_right_content.setStyleSheet(u"")
        self.data_frame_right_content.setFrameShape(QFrame.StyledPanel)
        self.data_frame_right_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.data_frame_right_content)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.solar_energy_consumption_content = QFrame(self.data_frame_right_content)
        self.solar_energy_consumption_content.setObjectName(u"solar_energy_consumption_content")
        sizePolicy2.setHeightForWidth(self.solar_energy_consumption_content.sizePolicy().hasHeightForWidth())
        self.solar_energy_consumption_content.setSizePolicy(sizePolicy2)
        self.solar_energy_consumption_content.setStyleSheet(u"")
        self.solar_energy_consumption_content.setFrameShape(QFrame.StyledPanel)
        self.solar_energy_consumption_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.solar_energy_consumption_content)
        self.verticalLayout_18.setSpacing(2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.solar_energy_consumption_title_frame = QFrame(self.solar_energy_consumption_content)
        self.solar_energy_consumption_title_frame.setObjectName(u"solar_energy_consumption_title_frame")
        self.solar_energy_consumption_title_frame.setMaximumSize(QSize(16777215, 40))
        self.solar_energy_consumption_title_frame.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.solar_energy_consumption_title_frame.setFrameShape(QFrame.StyledPanel)
        self.solar_energy_consumption_title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.solar_energy_consumption_title_frame)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_solar_energy_consumption = QLabel(self.solar_energy_consumption_title_frame)
        self.label_solar_energy_consumption.setObjectName(u"label_solar_energy_consumption")
        self.label_solar_energy_consumption.setFont(font1)

        self.verticalLayout_20.addWidget(self.label_solar_energy_consumption)


        self.verticalLayout_18.addWidget(self.solar_energy_consumption_title_frame)

        self.solar_energy_graph_content = QFrame(self.solar_energy_consumption_content)
        self.solar_energy_graph_content.setObjectName(u"solar_energy_graph_content")
        self.solar_energy_graph_content.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.solar_energy_graph_content.setFrameShape(QFrame.StyledPanel)
        self.solar_energy_graph_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.solar_energy_graph_content)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.solar_energy_consumption_graph_frame = QFrame(self.solar_energy_graph_content)
        self.solar_energy_consumption_graph_frame.setObjectName(u"solar_energy_consumption_graph_frame")
        self.solar_energy_consumption_graph_frame.setStyleSheet(u"")
        self.solar_energy_consumption_graph_frame.setFrameShape(QFrame.StyledPanel)
        self.solar_energy_consumption_graph_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.solar_energy_consumption_graph_frame)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_total_consumed = QLabel(self.solar_energy_consumption_graph_frame)
        self.label_total_consumed.setObjectName(u"label_total_consumed")
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(True)
        self.label_total_consumed.setFont(font4)
        self.label_total_consumed.setStyleSheet(u"color: #E60540;")
        self.label_total_consumed.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_total_consumed)


        self.horizontalLayout_21.addWidget(self.solar_energy_consumption_graph_frame)

        self.solar_energy_consumed_frame = QFrame(self.solar_energy_graph_content)
        self.solar_energy_consumed_frame.setObjectName(u"solar_energy_consumed_frame")
        self.solar_energy_consumed_frame.setStyleSheet(u"")
        self.solar_energy_consumed_frame.setFrameShape(QFrame.StyledPanel)
        self.solar_energy_consumed_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.solar_energy_consumed_frame)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_current_solar_energy_consumption = QLabel(self.solar_energy_consumed_frame)
        self.label_current_solar_energy_consumption.setObjectName(u"label_current_solar_energy_consumption")
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        self.label_current_solar_energy_consumption.setFont(font5)

        self.verticalLayout_23.addWidget(self.label_current_solar_energy_consumption, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_solar_energy_consumption_limit = QLabel(self.solar_energy_consumed_frame)
        self.label_solar_energy_consumption_limit.setObjectName(u"label_solar_energy_consumption_limit")
        font6 = QFont()
        font6.setPointSize(9)
        font6.setBold(False)
        self.label_solar_energy_consumption_limit.setFont(font6)

        self.verticalLayout_23.addWidget(self.label_solar_energy_consumption_limit, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_21.addWidget(self.solar_energy_consumed_frame)


        self.verticalLayout_18.addWidget(self.solar_energy_graph_content)


        self.verticalLayout_11.addWidget(self.solar_energy_consumption_content)

        self.traffic_consumption_content = QFrame(self.data_frame_right_content)
        self.traffic_consumption_content.setObjectName(u"traffic_consumption_content")
        self.traffic_consumption_content.setStyleSheet(u"")
        self.traffic_consumption_content.setFrameShape(QFrame.StyledPanel)
        self.traffic_consumption_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.traffic_consumption_content)
        self.verticalLayout_19.setSpacing(2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.traffic_consumption_title_frame = QFrame(self.traffic_consumption_content)
        self.traffic_consumption_title_frame.setObjectName(u"traffic_consumption_title_frame")
        self.traffic_consumption_title_frame.setMaximumSize(QSize(16777215, 40))
        self.traffic_consumption_title_frame.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.traffic_consumption_title_frame.setFrameShape(QFrame.StyledPanel)
        self.traffic_consumption_title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.traffic_consumption_title_frame)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_traffic_consumption = QLabel(self.traffic_consumption_title_frame)
        self.label_traffic_consumption.setObjectName(u"label_traffic_consumption")
        self.label_traffic_consumption.setFont(font1)

        self.verticalLayout_21.addWidget(self.label_traffic_consumption)


        self.verticalLayout_19.addWidget(self.traffic_consumption_title_frame)

        self.traffic_graph_content = QFrame(self.traffic_consumption_content)
        self.traffic_graph_content.setObjectName(u"traffic_graph_content")
        sizePolicy2.setHeightForWidth(self.traffic_graph_content.sizePolicy().hasHeightForWidth())
        self.traffic_graph_content.setSizePolicy(sizePolicy2)
        self.traffic_graph_content.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.traffic_graph_content.setFrameShape(QFrame.StyledPanel)
        self.traffic_graph_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.traffic_graph_content)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 0, 6, 6)

        self.verticalLayout_19.addWidget(self.traffic_graph_content)


        self.verticalLayout_11.addWidget(self.traffic_consumption_content)


        self.horizontalLayout_9.addWidget(self.data_frame_right_content)


        self.verticalLayout_10.addWidget(self.data_frame_1)


        self.horizontalLayout_3.addWidget(self.information_group_1)

        self.information_group_2 = QFrame(self.main_body)
        self.information_group_2.setObjectName(u"information_group_2")
        sizePolicy3.setHeightForWidth(self.information_group_2.sizePolicy().hasHeightForWidth())
        self.information_group_2.setSizePolicy(sizePolicy3)
        self.information_group_2.setMinimumSize(QSize(0, 0))
        self.information_group_2.setMaximumSize(QSize(16777215, 16777215))
        self.information_group_2.setStyleSheet(u"/*background-color: grey;*/")
        self.information_group_2.setFrameShape(QFrame.StyledPanel)
        self.information_group_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.information_group_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.information_cards_frame_2 = QFrame(self.information_group_2)
        self.information_cards_frame_2.setObjectName(u"information_cards_frame_2")
        self.information_cards_frame_2.setMinimumSize(QSize(0, 240))
        self.information_cards_frame_2.setMaximumSize(QSize(16777215, 240))
        self.information_cards_frame_2.setStyleSheet(u"")
        self.information_cards_frame_2.setFrameShape(QFrame.StyledPanel)
        self.information_cards_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.information_cards_frame_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.primary_card_frame_2 = QFrame(self.information_cards_frame_2)
        self.primary_card_frame_2.setObjectName(u"primary_card_frame_2")
        self.primary_card_frame_2.setMaximumSize(QSize(16777215, 200))
        self.primary_card_frame_2.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.primary_card_frame_2.setFrameShape(QFrame.StyledPanel)
        self.primary_card_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.primary_card_frame_2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.primary_card_left_content_2 = QFrame(self.primary_card_frame_2)
        self.primary_card_left_content_2.setObjectName(u"primary_card_left_content_2")
        self.primary_card_left_content_2.setStyleSheet(u"")
        self.primary_card_left_content_2.setFrameShape(QFrame.StyledPanel)
        self.primary_card_left_content_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.primary_card_left_content_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.icon_primary_card_2 = QLabel(self.primary_card_left_content_2)
        self.icon_primary_card_2.setObjectName(u"icon_primary_card_2")
        self.icon_primary_card_2.setMinimumSize(QSize(60, 50))
        self.icon_primary_card_2.setStyleSheet(u"background-color: rgb(24, 24, 36);\n"
"border-radius: 5px;")
        self.icon_primary_card_2.setPixmap(QPixmap(u":/icons/icons/briefcase.svg"))
        self.icon_primary_card_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.icon_primary_card_2)

        self.label_primary_card_2 = QLabel(self.primary_card_left_content_2)
        self.label_primary_card_2.setObjectName(u"label_primary_card_2")
        self.label_primary_card_2.setFont(font1)

        self.horizontalLayout_13.addWidget(self.label_primary_card_2)


        self.horizontalLayout_14.addWidget(self.primary_card_left_content_2, 0, Qt.AlignLeft)

        self.button_documentation = QPushButton(self.primary_card_frame_2)
        self.button_documentation.setObjectName(u"button_documentation")
        self.button_documentation.setMinimumSize(QSize(120, 35))
        self.button_documentation.setFont(font1)
        self.button_documentation.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_documentation.setMouseTracking(True)
        self.button_documentation.setStyleSheet(u"QPushButton {\n"
"	background-color: #E60540;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #C50332;\n"
"}")

        self.horizontalLayout_14.addWidget(self.button_documentation, 0, Qt.AlignRight)


        self.verticalLayout_13.addWidget(self.primary_card_frame_2)

        self.secondary_card_frame_2 = QFrame(self.information_cards_frame_2)
        self.secondary_card_frame_2.setObjectName(u"secondary_card_frame_2")
        self.secondary_card_frame_2.setStyleSheet(u"")
        self.secondary_card_frame_2.setFrameShape(QFrame.StyledPanel)
        self.secondary_card_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.secondary_card_frame_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.secondary_card_left_frame_2 = QFrame(self.secondary_card_frame_2)
        self.secondary_card_left_frame_2.setObjectName(u"secondary_card_left_frame_2")
        self.secondary_card_left_frame_2.setStyleSheet(u"")
        self.secondary_card_left_frame_2.setFrameShape(QFrame.StyledPanel)
        self.secondary_card_left_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.secondary_card_left_frame_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, -1, 0, 0)
        self.secondary_card_left_content_2 = QFrame(self.secondary_card_left_frame_2)
        self.secondary_card_left_content_2.setObjectName(u"secondary_card_left_content_2")
        self.secondary_card_left_content_2.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.secondary_card_left_content_2.setFrameShape(QFrame.StyledPanel)
        self.secondary_card_left_content_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.secondary_card_left_content_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, -1, -1, 9)
        self.icon_secondary_card_left_2 = QLabel(self.secondary_card_left_content_2)
        self.icon_secondary_card_left_2.setObjectName(u"icon_secondary_card_left_2")
        self.icon_secondary_card_left_2.setMinimumSize(QSize(40, 40))
        self.icon_secondary_card_left_2.setStyleSheet(u"background-color: rgb(24, 24, 36);\n"
"border-radius: 5px;")
        self.icon_secondary_card_left_2.setPixmap(QPixmap(u":/icons/icons/speaker.svg"))
        self.icon_secondary_card_left_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.icon_secondary_card_left_2)

        self.label_secondary_card_left_2 = QLabel(self.secondary_card_left_content_2)
        self.label_secondary_card_left_2.setObjectName(u"label_secondary_card_left_2")
        self.label_secondary_card_left_2.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label_secondary_card_left_2, 0, Qt.AlignHCenter)


        self.verticalLayout_14.addWidget(self.secondary_card_left_content_2)


        self.horizontalLayout_11.addWidget(self.secondary_card_left_frame_2)

        self.secondary_card_right_frame_2 = QFrame(self.secondary_card_frame_2)
        self.secondary_card_right_frame_2.setObjectName(u"secondary_card_right_frame_2")
        self.secondary_card_right_frame_2.setStyleSheet(u"")
        self.secondary_card_right_frame_2.setFrameShape(QFrame.StyledPanel)
        self.secondary_card_right_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.secondary_card_right_frame_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, -1, 0, 0)
        self.secondary_card_right_content_2 = QFrame(self.secondary_card_right_frame_2)
        self.secondary_card_right_content_2.setObjectName(u"secondary_card_right_content_2")
        self.secondary_card_right_content_2.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.secondary_card_right_content_2.setFrameShape(QFrame.StyledPanel)
        self.secondary_card_right_content_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.secondary_card_right_content_2)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.icon_secondary_card_right_2 = QLabel(self.secondary_card_right_content_2)
        self.icon_secondary_card_right_2.setObjectName(u"icon_secondary_card_right_2")
        self.icon_secondary_card_right_2.setMinimumSize(QSize(40, 40))
        self.icon_secondary_card_right_2.setStyleSheet(u"background-color: rgb(24, 24, 36);\n"
"border-radius: 5px;")
        self.icon_secondary_card_right_2.setPixmap(QPixmap(u":/icons/icons/mic.svg"))
        self.icon_secondary_card_right_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.icon_secondary_card_right_2)

        self.label_secondary_card_right_2 = QLabel(self.secondary_card_right_content_2)
        self.label_secondary_card_right_2.setObjectName(u"label_secondary_card_right_2")
        self.label_secondary_card_right_2.setFont(font1)

        self.horizontalLayout_16.addWidget(self.label_secondary_card_right_2, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.secondary_card_right_content_2)


        self.horizontalLayout_11.addWidget(self.secondary_card_right_frame_2)


        self.verticalLayout_13.addWidget(self.secondary_card_frame_2)


        self.verticalLayout_9.addWidget(self.information_cards_frame_2)

        self.data_frame_2 = QFrame(self.information_group_2)
        self.data_frame_2.setObjectName(u"data_frame_2")
        self.data_frame_2.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.data_frame_2.setFrameShape(QFrame.StyledPanel)
        self.data_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.data_frame_2)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, -1, 0, 0)
        self.tab_container_2 = QFrame(self.data_frame_2)
        self.tab_container_2.setObjectName(u"tab_container_2")
        self.tab_container_2.setStyleSheet(u"")
        self.tab_container_2.setFrameShape(QFrame.StyledPanel)
        self.tab_container_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.tab_container_2)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(2, 9, 2, 9)
        self.button_electricity_consumption = QPushButton(self.tab_container_2)
        self.button_electricity_consumption.setObjectName(u"button_electricity_consumption")
        self.button_electricity_consumption.setFont(font1)
        self.button_electricity_consumption.setStyleSheet(u"")

        self.horizontalLayout_22.addWidget(self.button_electricity_consumption)

        self.button_devices = QPushButton(self.tab_container_2)
        self.button_devices.setObjectName(u"button_devices")
        self.button_devices.setFont(font1)

        self.horizontalLayout_22.addWidget(self.button_devices)


        self.verticalLayout_25.addWidget(self.tab_container_2, 0, Qt.AlignTop)

        self.alternative_graph_frame_2 = QFrame(self.data_frame_2)
        self.alternative_graph_frame_2.setObjectName(u"alternative_graph_frame_2")
        sizePolicy5.setHeightForWidth(self.alternative_graph_frame_2.sizePolicy().hasHeightForWidth())
        self.alternative_graph_frame_2.setSizePolicy(sizePolicy5)
        self.alternative_graph_frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.alternative_graph_frame_2.setFrameShape(QFrame.StyledPanel)
        self.alternative_graph_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.alternative_graph_frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, 0, 6, 6)

        self.verticalLayout_25.addWidget(self.alternative_graph_frame_2)


        self.verticalLayout_9.addWidget(self.data_frame_2)


        self.horizontalLayout_3.addWidget(self.information_group_2)


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
        self.size_grip_container = QFrame(self.footer)
        self.size_grip_container.setObjectName(u"size_grip_container")
        self.size_grip_container.setFrameShape(QFrame.StyledPanel)
        self.size_grip_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.size_grip_container)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.size_grip = QFrame(self.size_grip_container)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.size_grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.horizontalLayout_7.addWidget(self.size_grip_container)


        self.verticalLayout_7.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.main_content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_app_name.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.icon_app.setText("")
        self.button_dashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.button_employees.setText(QCoreApplication.translate("MainWindow", u"Employees", None))
        self.button_orders.setText(QCoreApplication.translate("MainWindow", u"Orders", None))
        self.button_sales.setText(QCoreApplication.translate("MainWindow", u"Sales", None))
        self.button_profit.setText(QCoreApplication.translate("MainWindow", u"Profit", None))
        self.button_permissions.setText(QCoreApplication.translate("MainWindow", u"Permissions", None))
        self.button_management.setText(QCoreApplication.translate("MainWindow", u"Management", None))
        self.button_sidebar.setText("")
        self.button_search.setText("")
        self.button_messages.setText("")
        self.button_notifications.setText("")
        self.button_user.setText("")
        self.label_username.setText(QCoreApplication.translate("MainWindow", u"User 1", None))
        self.icon_primary_card_1.setText("")
        self.label_primary_card_1.setText(QCoreApplication.translate("MainWindow", u"Title of label card", None))
        self.button_support.setText(QCoreApplication.translate("MainWindow", u"Support", None))
        self.icon_secondary_card_left_1.setText("")
        self.label_secondary_card_left_1.setText(QCoreApplication.translate("MainWindow", u"Title of label card", None))
        self.icon_secondary_card_right_1.setText("")
        self.label_secondary_card_right_1.setText(QCoreApplication.translate("MainWindow", u"Title of label card 2", None))
        self.button_temperature.setText(QCoreApplication.translate("MainWindow", u"TEMPERATURE", None))
        self.button_humidity.setText(QCoreApplication.translate("MainWindow", u"HUMIDITY", None))
        self.label_temperature.setText(QCoreApplication.translate("MainWindow", u"75\u00ba F", None))
        self.icon_wind.setText("")
        self.label_wind.setText(QCoreApplication.translate("MainWindow", u"Wind: 3mph", None))
        self.icon_rain.setText("")
        self.label_rain.setText(QCoreApplication.translate("MainWindow", u"Rain: 0%", None))
        self.icon_weather.setText("")
        self.label_weather.setText(QCoreApplication.translate("MainWindow", u"Sunny", None))
        self.label_solar_energy_consumption.setText(QCoreApplication.translate("MainWindow", u"Solar Energy Consumption", None))
        self.label_total_consumed.setText(QCoreApplication.translate("MainWindow", u"76.34%", None))
        self.label_current_solar_energy_consumption.setText(QCoreApplication.translate("MainWindow", u"6.421 kWh", None))
        self.label_solar_energy_consumption_limit.setText(QCoreApplication.translate("MainWindow", u"out of 8.421 kWh", None))
        self.label_traffic_consumption.setText(QCoreApplication.translate("MainWindow", u"Traffic Consumption", None))
        self.icon_primary_card_2.setText("")
        self.label_primary_card_2.setText(QCoreApplication.translate("MainWindow", u"Title of label card 2", None))
        self.button_documentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.icon_secondary_card_left_2.setText("")
        self.label_secondary_card_left_2.setText(QCoreApplication.translate("MainWindow", u"Title of label card 3", None))
        self.icon_secondary_card_right_2.setText("")
        self.label_secondary_card_right_2.setText(QCoreApplication.translate("MainWindow", u"Title of label card 4", None))
        self.button_electricity_consumption.setText(QCoreApplication.translate("MainWindow", u"ELECTRICITY CONSUMPTION", None))
        self.button_devices.setText(QCoreApplication.translate("MainWindow", u"DEVICES", None))
    # retranslateUi

