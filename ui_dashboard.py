# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardDwWwsh.ui'
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
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import icons_rc
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1185, 679)
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

        self.main_body = QStackedWidget(self.main_content)
        self.main_body.setObjectName(u"main_body")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy2)
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.page_dashboard = QWidget()
        self.page_dashboard.setObjectName(u"page_dashboard")
        self.horizontalLayout_3 = QHBoxLayout(self.page_dashboard)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.information_group_1 = QFrame(self.page_dashboard)
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
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
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
        self.button_temperature.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_23.addWidget(self.button_temperature)

        self.button_humidity = QPushButton(self.tab_container_1)
        self.button_humidity.setObjectName(u"button_humidity")
        self.button_humidity.setFont(font1)
        self.button_humidity.setCursor(QCursor(Qt.PointingHandCursor))

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
        self.label_wind.setWordWrap(True)

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
        self.label_rain.setWordWrap(True)

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
        self.label_weather.setWordWrap(True)

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

        self.information_group_2 = QFrame(self.page_dashboard)
        self.information_group_2.setObjectName(u"information_group_2")
        sizePolicy3.setHeightForWidth(self.information_group_2.sizePolicy().hasHeightForWidth())
        self.information_group_2.setSizePolicy(sizePolicy3)
        self.information_group_2.setMinimumSize(QSize(0, 0))
        self.information_group_2.setMaximumSize(QSize(16777215, 16777215))
        self.information_group_2.setStyleSheet(u"/*background-color: grey;*/")
        self.information_group_2.setFrameShape(QFrame.StyledPanel)
        self.information_group_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.information_group_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
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
        self.data_frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.data_frame_2.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.data_frame_2.setFrameShape(QFrame.StyledPanel)
        self.data_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.data_frame_2)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, -1, 0, 0)
        self.tab_container_2 = QFrame(self.data_frame_2)
        self.tab_container_2.setObjectName(u"tab_container_2")
        self.tab_container_2.setCursor(QCursor(Qt.ArrowCursor))
        self.tab_container_2.setStyleSheet(u"")
        self.tab_container_2.setFrameShape(QFrame.StyledPanel)
        self.tab_container_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.tab_container_2)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(2, 9, 2, 9)
        self.button_electricity_consumption = QPushButton(self.tab_container_2)
        self.button_electricity_consumption.setObjectName(u"button_electricity_consumption")
        self.button_electricity_consumption.setFont(font1)
        self.button_electricity_consumption.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_electricity_consumption.setStyleSheet(u"")

        self.horizontalLayout_22.addWidget(self.button_electricity_consumption)

        self.button_devices = QPushButton(self.tab_container_2)
        self.button_devices.setObjectName(u"button_devices")
        self.button_devices.setFont(font1)
        self.button_devices.setCursor(QCursor(Qt.PointingHandCursor))

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

        self.main_body.addWidget(self.page_dashboard)
        self.page_sales = QWidget()
        self.page_sales.setObjectName(u"page_sales")
        self.horizontalLayout_35 = QHBoxLayout(self.page_sales)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_6 = QLabel(self.page_sales)
        self.label_6.setObjectName(u"label_6")
        font7 = QFont()
        font7.setPointSize(32)
        font7.setBold(True)
        self.label_6.setFont(font7)

        self.horizontalLayout_35.addWidget(self.label_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.main_body.addWidget(self.page_sales)
        self.page_profit = QWidget()
        self.page_profit.setObjectName(u"page_profit")
        self.horizontalLayout_34 = QHBoxLayout(self.page_profit)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_4 = QLabel(self.page_profit)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font7)

        self.horizontalLayout_34.addWidget(self.label_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.main_body.addWidget(self.page_profit)
        self.page_permissions = QWidget()
        self.page_permissions.setObjectName(u"page_permissions")
        self.horizontalLayout_37 = QHBoxLayout(self.page_permissions)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_5 = QLabel(self.page_permissions)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font7)

        self.horizontalLayout_37.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.main_body.addWidget(self.page_permissions)
        self.page_management = QWidget()
        self.page_management.setObjectName(u"page_management")
        self.horizontalLayout_33 = QHBoxLayout(self.page_management)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_3 = QLabel(self.page_management)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font7)

        self.horizontalLayout_33.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.main_body.addWidget(self.page_management)
        self.page_orders = QWidget()
        self.page_orders.setObjectName(u"page_orders")
        self.horizontalLayout_36 = QHBoxLayout(self.page_orders)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.main_body_orders = QFrame(self.page_orders)
        self.main_body_orders.setObjectName(u"main_body_orders")
        self.main_body_orders.setFrameShape(QFrame.StyledPanel)
        self.main_body_orders.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.main_body_orders)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.orders_information_group_1 = QFrame(self.main_body_orders)
        self.orders_information_group_1.setObjectName(u"orders_information_group_1")
        sizePolicy3.setHeightForWidth(self.orders_information_group_1.sizePolicy().hasHeightForWidth())
        self.orders_information_group_1.setSizePolicy(sizePolicy3)
        self.orders_information_group_1.setMaximumSize(QSize(16777215, 16777215))
        self.orders_information_group_1.setStyleSheet(u"")
        self.orders_information_group_1.setFrameShape(QFrame.StyledPanel)
        self.orders_information_group_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.orders_information_group_1)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.credit_card_frame = QFrame(self.orders_information_group_1)
        self.credit_card_frame.setObjectName(u"credit_card_frame")
        self.credit_card_frame.setStyleSheet(u"")
        self.credit_card_frame.setFrameShape(QFrame.StyledPanel)
        self.credit_card_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.credit_card_frame)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.credit_card_container = QFrame(self.credit_card_frame)
        self.credit_card_container.setObjectName(u"credit_card_container")
        self.credit_card_container.setStyleSheet(u"")
        self.credit_card_container.setFrameShape(QFrame.StyledPanel)
        self.credit_card_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.credit_card_container)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.credit_card_label_container = QFrame(self.credit_card_container)
        self.credit_card_label_container.setObjectName(u"credit_card_label_container")
        self.credit_card_label_container.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.credit_card_label_container.setFrameShape(QFrame.StyledPanel)
        self.credit_card_label_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.credit_card_label_container)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.icon_credit_card = QLabel(self.credit_card_label_container)
        self.icon_credit_card.setObjectName(u"icon_credit_card")
        self.icon_credit_card.setMinimumSize(QSize(60, 50))
        self.icon_credit_card.setFont(font1)
        self.icon_credit_card.setStyleSheet(u"background-color: rgb(24, 24, 36);\n"
"border-radius: 5px;")
        self.icon_credit_card.setPixmap(QPixmap(u":/icons/icons/credit-card.svg"))
        self.icon_credit_card.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_46.addWidget(self.icon_credit_card, 0, Qt.AlignLeft)

        self.label_credit_card = QLabel(self.credit_card_label_container)
        self.label_credit_card.setObjectName(u"label_credit_card")
        self.label_credit_card.setFont(font5)
        self.label_credit_card.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_46.addWidget(self.label_credit_card, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_30.addWidget(self.credit_card_label_container, 0, Qt.AlignHCenter)


        self.verticalLayout_29.addWidget(self.credit_card_container)


        self.verticalLayout_28.addWidget(self.credit_card_frame, 0, Qt.AlignTop)

        self.credit_cards_orders_frame = QFrame(self.orders_information_group_1)
        self.credit_cards_orders_frame.setObjectName(u"credit_cards_orders_frame")
        sizePolicy4.setHeightForWidth(self.credit_cards_orders_frame.sizePolicy().hasHeightForWidth())
        self.credit_cards_orders_frame.setSizePolicy(sizePolicy4)
        self.credit_cards_orders_frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(9, 5, 13);\n"
"	border-radius: 5px;\n"
"	margin: 10px;\n"
"}")
        self.credit_cards_orders_frame.setFrameShape(QFrame.StyledPanel)
        self.credit_cards_orders_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.credit_cards_orders_frame)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_total_credit_card_orders = QLabel(self.credit_cards_orders_frame)
        self.label_total_credit_card_orders.setObjectName(u"label_total_credit_card_orders")
        font8 = QFont()
        font8.setPointSize(16)
        font8.setBold(True)
        self.label_total_credit_card_orders.setFont(font8)

        self.verticalLayout_33.addWidget(self.label_total_credit_card_orders, 0, Qt.AlignLeft)

        self.scrollArea_credit_card = QScrollArea(self.credit_cards_orders_frame)
        self.scrollArea_credit_card.setObjectName(u"scrollArea_credit_card")
        self.scrollArea_credit_card.setStyleSheet(u"background-color: #09050D;")
        self.scrollArea_credit_card.setWidgetResizable(True)
        self.scrollAreaWidget_credit_card = QWidget()
        self.scrollAreaWidget_credit_card.setObjectName(u"scrollAreaWidget_credit_card")
        self.scrollAreaWidget_credit_card.setGeometry(QRect(0, 0, 435, 389))
        self.scrollAreaWidget_credit_card.setStyleSheet(u"QFrame {\n"
"	margin: 0px;\n"
"}")
        self.verticalLayout_32 = QVBoxLayout(self.scrollAreaWidget_credit_card)
        self.verticalLayout_32.setSpacing(6)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(-1, 9, -1, -1)
        self.template_order_1 = QFrame(self.scrollAreaWidget_credit_card)
        self.template_order_1.setObjectName(u"template_order_1")
        self.template_order_1.setStyleSheet(u"")
        self.template_order_1.setFrameShape(QFrame.StyledPanel)
        self.template_order_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.template_order_1)
        self.verticalLayout_31.setSpacing(6)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.container_order_information_1 = QFrame(self.template_order_1)
        self.container_order_information_1.setObjectName(u"container_order_information_1")
        self.container_order_information_1.setStyleSheet(u"")
        self.container_order_information_1.setFrameShape(QFrame.StyledPanel)
        self.container_order_information_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.container_order_information_1)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_order_product_1 = QLabel(self.container_order_information_1)
        self.label_order_product_1.setObjectName(u"label_order_product_1")
        self.label_order_product_1.setFont(font)

        self.horizontalLayout_48.addWidget(self.label_order_product_1, 0, Qt.AlignLeft)

        self.label_order_price_1 = QLabel(self.container_order_information_1)
        self.label_order_price_1.setObjectName(u"label_order_price_1")
        self.label_order_price_1.setFont(font)
        self.label_order_price_1.setStyleSheet(u"color: lime;")

        self.horizontalLayout_48.addWidget(self.label_order_price_1, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_31.addWidget(self.container_order_information_1, 0, Qt.AlignBottom)

        self.container_order_id_1 = QFrame(self.template_order_1)
        self.container_order_id_1.setObjectName(u"container_order_id_1")
        self.container_order_id_1.setStyleSheet(u"")
        self.container_order_id_1.setFrameShape(QFrame.StyledPanel)
        self.container_order_id_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.container_order_id_1)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_order_id_1 = QLabel(self.container_order_id_1)
        self.label_order_id_1.setObjectName(u"label_order_id_1")
        font9 = QFont()
        font9.setPointSize(10)
        font9.setBold(True)
        self.label_order_id_1.setFont(font9)
        self.label_order_id_1.setStyleSheet(u"color: #5B5B5B;")

        self.horizontalLayout_47.addWidget(self.label_order_id_1, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_31.addWidget(self.container_order_id_1, 0, Qt.AlignTop)

        self.divider1 = QLineEdit(self.template_order_1)
        self.divider1.setObjectName(u"divider1")
        self.divider1.setMaximumSize(QSize(16777215, 2))
        self.divider1.setStyleSheet(u"background-color: #E60540;")

        self.verticalLayout_31.addWidget(self.divider1)


        self.verticalLayout_32.addWidget(self.template_order_1, 0, Qt.AlignTop)

        self.template_order_2 = QFrame(self.scrollAreaWidget_credit_card)
        self.template_order_2.setObjectName(u"template_order_2")
        self.template_order_2.setFrameShape(QFrame.StyledPanel)
        self.template_order_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.template_order_2)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.container_order_information_2 = QFrame(self.template_order_2)
        self.container_order_information_2.setObjectName(u"container_order_information_2")
        self.container_order_information_2.setStyleSheet(u"")
        self.container_order_information_2.setFrameShape(QFrame.StyledPanel)
        self.container_order_information_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.container_order_information_2)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.label_order_product_2 = QLabel(self.container_order_information_2)
        self.label_order_product_2.setObjectName(u"label_order_product_2")
        self.label_order_product_2.setFont(font)

        self.horizontalLayout_49.addWidget(self.label_order_product_2, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.label_order_price_2 = QLabel(self.container_order_information_2)
        self.label_order_price_2.setObjectName(u"label_order_price_2")
        self.label_order_price_2.setFont(font)
        self.label_order_price_2.setStyleSheet(u"color: lime;")

        self.horizontalLayout_49.addWidget(self.label_order_price_2, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_34.addWidget(self.container_order_information_2, 0, Qt.AlignTop)

        self.container_order_id_2 = QFrame(self.template_order_2)
        self.container_order_id_2.setObjectName(u"container_order_id_2")
        self.container_order_id_2.setStyleSheet(u"")
        self.container_order_id_2.setFrameShape(QFrame.StyledPanel)
        self.container_order_id_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.container_order_id_2)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_order_id_2 = QLabel(self.container_order_id_2)
        self.label_order_id_2.setObjectName(u"label_order_id_2")
        self.label_order_id_2.setFont(font9)
        self.label_order_id_2.setStyleSheet(u"color: #5B5B5B;")

        self.horizontalLayout_50.addWidget(self.label_order_id_2, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_34.addWidget(self.container_order_id_2, 0, Qt.AlignTop)

        self.divider2 = QLineEdit(self.template_order_2)
        self.divider2.setObjectName(u"divider2")
        self.divider2.setMaximumSize(QSize(16777215, 2))
        self.divider2.setStyleSheet(u"background-color: #E60540;")

        self.verticalLayout_34.addWidget(self.divider2)


        self.verticalLayout_32.addWidget(self.template_order_2, 0, Qt.AlignTop)

        self.scrollArea_credit_card.setWidget(self.scrollAreaWidget_credit_card)

        self.verticalLayout_33.addWidget(self.scrollArea_credit_card)


        self.verticalLayout_28.addWidget(self.credit_cards_orders_frame)


        self.horizontalLayout_38.addWidget(self.orders_information_group_1)

        self.orders_information_group_2 = QFrame(self.main_body_orders)
        self.orders_information_group_2.setObjectName(u"orders_information_group_2")
        sizePolicy3.setHeightForWidth(self.orders_information_group_2.sizePolicy().hasHeightForWidth())
        self.orders_information_group_2.setSizePolicy(sizePolicy3)
        self.orders_information_group_2.setStyleSheet(u"")
        self.orders_information_group_2.setFrameShape(QFrame.StyledPanel)
        self.orders_information_group_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.orders_information_group_2)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.money_frame = QFrame(self.orders_information_group_2)
        self.money_frame.setObjectName(u"money_frame")
        self.money_frame.setFrameShape(QFrame.StyledPanel)
        self.money_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.money_frame)
        self.verticalLayout_36.setSpacing(6)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(9, 9, 9, 9)
        self.money_container = QFrame(self.money_frame)
        self.money_container.setObjectName(u"money_container")
        self.money_container.setStyleSheet(u"")
        self.money_container.setFrameShape(QFrame.StyledPanel)
        self.money_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.money_container)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.money_label_container = QFrame(self.money_container)
        self.money_label_container.setObjectName(u"money_label_container")
        self.money_label_container.setStyleSheet(u"background-color: rgb(9, 5, 13);\n"
"border-radius: 5px;")
        self.money_label_container.setFrameShape(QFrame.StyledPanel)
        self.money_label_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.money_label_container)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.icon_money = QLabel(self.money_label_container)
        self.icon_money.setObjectName(u"icon_money")
        self.icon_money.setMinimumSize(QSize(60, 50))
        self.icon_money.setFont(font1)
        self.icon_money.setStyleSheet(u"background-color: rgb(24, 24, 36);\n"
"border-radius: 5px;")
        self.icon_money.setPixmap(QPixmap(u":/icons/icons/dollar-sign.svg"))
        self.icon_money.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_51.addWidget(self.icon_money)

        self.label_money = QLabel(self.money_label_container)
        self.label_money.setObjectName(u"label_money")
        self.label_money.setFont(font5)
        self.label_money.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_51.addWidget(self.label_money)


        self.verticalLayout_37.addWidget(self.money_label_container, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_36.addWidget(self.money_container)


        self.verticalLayout_35.addWidget(self.money_frame, 0, Qt.AlignTop)

        self.money_orders_frame = QFrame(self.orders_information_group_2)
        self.money_orders_frame.setObjectName(u"money_orders_frame")
        sizePolicy4.setHeightForWidth(self.money_orders_frame.sizePolicy().hasHeightForWidth())
        self.money_orders_frame.setSizePolicy(sizePolicy4)
        self.money_orders_frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(9, 5, 13);\n"
"	border-radius: 5px;\n"
"	margin: 10px;\n"
"}")
        self.money_orders_frame.setFrameShape(QFrame.StyledPanel)
        self.money_orders_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.money_orders_frame)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_total_money_orders = QLabel(self.money_orders_frame)
        self.label_total_money_orders.setObjectName(u"label_total_money_orders")
        self.label_total_money_orders.setFont(font8)

        self.verticalLayout_38.addWidget(self.label_total_money_orders, 0, Qt.AlignLeft)

        self.scrollArea_money = QScrollArea(self.money_orders_frame)
        self.scrollArea_money.setObjectName(u"scrollArea_money")
        self.scrollArea_money.setStyleSheet(u"background-color: #09050D;")
        self.scrollArea_money.setWidgetResizable(True)
        self.scrollAreaWidget_money = QWidget()
        self.scrollAreaWidget_money.setObjectName(u"scrollAreaWidget_money")
        self.scrollAreaWidget_money.setGeometry(QRect(0, 0, 434, 389))
        self.scrollAreaWidget_money.setStyleSheet(u"QFrame {\n"
"	margin: 0px;\n"
"}")
        self.verticalLayout_41 = QVBoxLayout(self.scrollAreaWidget_money)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.template_order_3 = QFrame(self.scrollAreaWidget_money)
        self.template_order_3.setObjectName(u"template_order_3")
        self.template_order_3.setFrameShape(QFrame.StyledPanel)
        self.template_order_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.template_order_3)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.container_order_information_3 = QFrame(self.template_order_3)
        self.container_order_information_3.setObjectName(u"container_order_information_3")
        self.container_order_information_3.setStyleSheet(u"")
        self.container_order_information_3.setFrameShape(QFrame.StyledPanel)
        self.container_order_information_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.container_order_information_3)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_order_product_3 = QLabel(self.container_order_information_3)
        self.label_order_product_3.setObjectName(u"label_order_product_3")
        self.label_order_product_3.setFont(font)

        self.horizontalLayout_53.addWidget(self.label_order_product_3, 0, Qt.AlignLeft)

        self.label_order_price_3 = QLabel(self.container_order_information_3)
        self.label_order_price_3.setObjectName(u"label_order_price_3")
        self.label_order_price_3.setFont(font)
        self.label_order_price_3.setStyleSheet(u"color: lime;")

        self.horizontalLayout_53.addWidget(self.label_order_price_3, 0, Qt.AlignRight)


        self.verticalLayout_39.addWidget(self.container_order_information_3, 0, Qt.AlignBottom)

        self.container_order_id_3 = QFrame(self.template_order_3)
        self.container_order_id_3.setObjectName(u"container_order_id_3")
        self.container_order_id_3.setStyleSheet(u"")
        self.container_order_id_3.setFrameShape(QFrame.StyledPanel)
        self.container_order_id_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.container_order_id_3)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_order_id_3 = QLabel(self.container_order_id_3)
        self.label_order_id_3.setObjectName(u"label_order_id_3")
        self.label_order_id_3.setFont(font9)
        self.label_order_id_3.setStyleSheet(u"color: #5B5B5B;")

        self.horizontalLayout_52.addWidget(self.label_order_id_3, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_39.addWidget(self.container_order_id_3, 0, Qt.AlignTop)

        self.divider3 = QLineEdit(self.template_order_3)
        self.divider3.setObjectName(u"divider3")
        self.divider3.setMaximumSize(QSize(16777215, 2))
        self.divider3.setStyleSheet(u"background-color: #E60540;")

        self.verticalLayout_39.addWidget(self.divider3)


        self.verticalLayout_41.addWidget(self.template_order_3, 0, Qt.AlignTop)

        self.template_order_4 = QFrame(self.scrollAreaWidget_money)
        self.template_order_4.setObjectName(u"template_order_4")
        self.template_order_4.setStyleSheet(u"")
        self.template_order_4.setFrameShape(QFrame.StyledPanel)
        self.template_order_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.template_order_4)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.container_order_information_4 = QFrame(self.template_order_4)
        self.container_order_information_4.setObjectName(u"container_order_information_4")
        self.container_order_information_4.setStyleSheet(u"")
        self.container_order_information_4.setFrameShape(QFrame.StyledPanel)
        self.container_order_information_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.container_order_information_4)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_order_product_4 = QLabel(self.container_order_information_4)
        self.label_order_product_4.setObjectName(u"label_order_product_4")
        self.label_order_product_4.setFont(font)

        self.horizontalLayout_54.addWidget(self.label_order_product_4, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.label_order_price_4 = QLabel(self.container_order_information_4)
        self.label_order_price_4.setObjectName(u"label_order_price_4")
        self.label_order_price_4.setFont(font)
        self.label_order_price_4.setStyleSheet(u"color: #E60540;")

        self.horizontalLayout_54.addWidget(self.label_order_price_4, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_40.addWidget(self.container_order_information_4, 0, Qt.AlignTop)

        self.container_order_id_4 = QFrame(self.template_order_4)
        self.container_order_id_4.setObjectName(u"container_order_id_4")
        self.container_order_id_4.setStyleSheet(u"")
        self.container_order_id_4.setFrameShape(QFrame.StyledPanel)
        self.container_order_id_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.container_order_id_4)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label_order_id_4 = QLabel(self.container_order_id_4)
        self.label_order_id_4.setObjectName(u"label_order_id_4")
        self.label_order_id_4.setFont(font9)
        self.label_order_id_4.setStyleSheet(u"color: #5B5B5B;")

        self.horizontalLayout_55.addWidget(self.label_order_id_4, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_40.addWidget(self.container_order_id_4, 0, Qt.AlignTop)

        self.divider4 = QLineEdit(self.template_order_4)
        self.divider4.setObjectName(u"divider4")
        self.divider4.setMaximumSize(QSize(16777215, 2))
        self.divider4.setStyleSheet(u"background-color: #E60540;")

        self.verticalLayout_40.addWidget(self.divider4)


        self.verticalLayout_41.addWidget(self.template_order_4, 0, Qt.AlignTop)

        self.scrollArea_money.setWidget(self.scrollAreaWidget_money)

        self.verticalLayout_38.addWidget(self.scrollArea_money)


        self.verticalLayout_35.addWidget(self.money_orders_frame)


        self.horizontalLayout_38.addWidget(self.orders_information_group_2)


        self.horizontalLayout_36.addWidget(self.main_body_orders)

        self.main_body.addWidget(self.page_orders)
        self.page_employees = QWidget()
        self.page_employees.setObjectName(u"page_employees")
        self.horizontalLayout_32 = QHBoxLayout(self.page_employees)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.main_body_employees = QFrame(self.page_employees)
        self.main_body_employees.setObjectName(u"main_body_employees")
        self.main_body_employees.setFrameShape(QFrame.StyledPanel)
        self.main_body_employees.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.main_body_employees)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.main_employee_content_frame = QFrame(self.main_body_employees)
        self.main_employee_content_frame.setObjectName(u"main_employee_content_frame")
        self.main_employee_content_frame.setMinimumSize(QSize(0, 0))
        self.main_employee_content_frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(9, 5, 13);\n"
"	border-radius: 5px;\n"
"	margin: 10px;\n"
"}")
        self.main_employee_content_frame.setFrameShape(QFrame.StyledPanel)
        self.main_employee_content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.main_employee_content_frame)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(12, 12, 12, 12)
        self.header_employee_list = QFrame(self.main_employee_content_frame)
        self.header_employee_list.setObjectName(u"header_employee_list")
        self.header_employee_list.setMinimumSize(QSize(0, 0))
        self.header_employee_list.setFrameShape(QFrame.StyledPanel)
        self.header_employee_list.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.header_employee_list)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_list_title = QLabel(self.header_employee_list)
        self.label_list_title.setObjectName(u"label_list_title")
        self.label_list_title.setFont(font8)

        self.horizontalLayout_45.addWidget(self.label_list_title, 0, Qt.AlignLeft)

        self.button_add_employee = QPushButton(self.header_employee_list)
        self.button_add_employee.setObjectName(u"button_add_employee")
        self.button_add_employee.setMinimumSize(QSize(120, 35))
        self.button_add_employee.setFont(font1)
        self.button_add_employee.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_add_employee.setStyleSheet(u"QPushButton {\n"
"	background-color: #E60540;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #C50332;\n"
"}")

        self.horizontalLayout_45.addWidget(self.button_add_employee, 0, Qt.AlignRight)


        self.verticalLayout_26.addWidget(self.header_employee_list)

        self.separator_employees = QFrame(self.main_employee_content_frame)
        self.separator_employees.setObjectName(u"separator_employees")
        self.separator_employees.setMaximumSize(QSize(16777215, 2))
        self.separator_employees.setStyleSheet(u"background-color: #FFFFFF;")
        self.separator_employees.setFrameShadow(QFrame.Sunken)
        self.separator_employees.setFrameShape(QFrame.HLine)

        self.verticalLayout_26.addWidget(self.separator_employees)

        self.scrollArea_employees = QScrollArea(self.main_employee_content_frame)
        self.scrollArea_employees.setObjectName(u"scrollArea_employees")
        self.scrollArea_employees.setMinimumSize(QSize(600, 0))
        self.scrollArea_employees.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea_employees.setStyleSheet(u"QScrollArea {\n"
"	margin: 0px;\n"
"	padding: 0px;\n"
"}\n"
"")
        self.scrollArea_employees.setWidgetResizable(True)
        self.scrollAreaWidgets_employees = QWidget()
        self.scrollAreaWidgets_employees.setObjectName(u"scrollAreaWidgets_employees")
        self.scrollAreaWidgets_employees.setGeometry(QRect(0, 0, 600, 473))
        self.scrollAreaWidgets_employees.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(9, 5, 13);\n"
"	margin: 0px;\n"
"	padding: 0px;\n"
"}")
        self.verticalLayout_27 = QVBoxLayout(self.scrollAreaWidgets_employees)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(-1, -1, -1, 9)
        self.employee_management_frame_1 = QFrame(self.scrollAreaWidgets_employees)
        self.employee_management_frame_1.setObjectName(u"employee_management_frame_1")
        self.employee_management_frame_1.setMaximumSize(QSize(16777215, 80))
        self.employee_management_frame_1.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(9, 5, 13);\n"
"	border-radius: 10px;\n"
"}")
        self.employee_management_frame_1.setFrameShape(QFrame.StyledPanel)
        self.employee_management_frame_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.employee_management_frame_1)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.employee_information_frame_1 = QFrame(self.employee_management_frame_1)
        self.employee_information_frame_1.setObjectName(u"employee_information_frame_1")
        self.employee_information_frame_1.setFrameShape(QFrame.StyledPanel)
        self.employee_information_frame_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.employee_information_frame_1)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(-1, -1, 0, 0)
        self.icon_employee_picture_1 = QLabel(self.employee_information_frame_1)
        self.icon_employee_picture_1.setObjectName(u"icon_employee_picture_1")
        self.icon_employee_picture_1.setFont(font1)
        self.icon_employee_picture_1.setPixmap(QPixmap(u":/icons/icons/user.svg"))
        self.icon_employee_picture_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_43.addWidget(self.icon_employee_picture_1, 0, Qt.AlignLeft)

        self.label_employee_name_1 = QLabel(self.employee_information_frame_1)
        self.label_employee_name_1.setObjectName(u"label_employee_name_1")
        self.label_employee_name_1.setFont(font1)
        self.label_employee_name_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_43.addWidget(self.label_employee_name_1, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer)

        self.label_employee_permission_1 = QLabel(self.employee_information_frame_1)
        self.label_employee_permission_1.setObjectName(u"label_employee_permission_1")
        self.label_employee_permission_1.setFont(font1)
        self.label_employee_permission_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_43.addWidget(self.label_employee_permission_1, 0, Qt.AlignLeft)


        self.horizontalLayout_39.addWidget(self.employee_information_frame_1, 0, Qt.AlignLeft)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_2)

        self.button_manage_employee_1 = QPushButton(self.employee_management_frame_1)
        self.button_manage_employee_1.setObjectName(u"button_manage_employee_1")
        self.button_manage_employee_1.setMinimumSize(QSize(120, 35))
        self.button_manage_employee_1.setFont(font1)
        self.button_manage_employee_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_manage_employee_1.setStyleSheet(u"QPushButton {\n"
"	background-color: #E60540;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #C50332;\n"
"}")

        self.horizontalLayout_39.addWidget(self.button_manage_employee_1, 0, Qt.AlignRight)


        self.verticalLayout_27.addWidget(self.employee_management_frame_1)

        self.employee_management_frame_2 = QFrame(self.scrollAreaWidgets_employees)
        self.employee_management_frame_2.setObjectName(u"employee_management_frame_2")
        self.employee_management_frame_2.setMaximumSize(QSize(16777215, 80))
        self.employee_management_frame_2.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(9, 5, 13);\n"
"	border-radius: 10px;\n"
"}")
        self.employee_management_frame_2.setFrameShape(QFrame.StyledPanel)
        self.employee_management_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.employee_management_frame_2)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.employee_information_frame_2 = QFrame(self.employee_management_frame_2)
        self.employee_information_frame_2.setObjectName(u"employee_information_frame_2")
        self.employee_information_frame_2.setFrameShape(QFrame.StyledPanel)
        self.employee_information_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.employee_information_frame_2)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.icon_employee_picture_2 = QLabel(self.employee_information_frame_2)
        self.icon_employee_picture_2.setObjectName(u"icon_employee_picture_2")
        self.icon_employee_picture_2.setFont(font1)
        self.icon_employee_picture_2.setPixmap(QPixmap(u":/icons/icons/user.svg"))
        self.icon_employee_picture_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.icon_employee_picture_2, 0, Qt.AlignLeft)

        self.label_employee_name_2 = QLabel(self.employee_information_frame_2)
        self.label_employee_name_2.setObjectName(u"label_employee_name_2")
        self.label_employee_name_2.setFont(font1)
        self.label_employee_name_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.label_employee_name_2, 0, Qt.AlignLeft)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_3)

        self.label_employee_permission_2 = QLabel(self.employee_information_frame_2)
        self.label_employee_permission_2.setObjectName(u"label_employee_permission_2")
        self.label_employee_permission_2.setFont(font1)
        self.label_employee_permission_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.label_employee_permission_2, 0, Qt.AlignLeft)


        self.horizontalLayout_40.addWidget(self.employee_information_frame_2, 0, Qt.AlignLeft)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_4)

        self.button_manage_employee_2 = QPushButton(self.employee_management_frame_2)
        self.button_manage_employee_2.setObjectName(u"button_manage_employee_2")
        self.button_manage_employee_2.setMinimumSize(QSize(120, 35))
        self.button_manage_employee_2.setFont(font1)
        self.button_manage_employee_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_manage_employee_2.setStyleSheet(u"QPushButton {\n"
"	background-color: #E60540;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #C50332;\n"
"}")

        self.horizontalLayout_40.addWidget(self.button_manage_employee_2, 0, Qt.AlignRight)


        self.verticalLayout_27.addWidget(self.employee_management_frame_2)

        self.employee_management_frame_3 = QFrame(self.scrollAreaWidgets_employees)
        self.employee_management_frame_3.setObjectName(u"employee_management_frame_3")
        self.employee_management_frame_3.setMaximumSize(QSize(16777215, 80))
        self.employee_management_frame_3.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(9, 5, 13);\n"
"	border-radius: 10px;\n"
"}")
        self.employee_management_frame_3.setFrameShape(QFrame.StyledPanel)
        self.employee_management_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.employee_management_frame_3)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.employee_information_frame_3 = QFrame(self.employee_management_frame_3)
        self.employee_information_frame_3.setObjectName(u"employee_information_frame_3")
        self.employee_information_frame_3.setFrameShape(QFrame.StyledPanel)
        self.employee_information_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.employee_information_frame_3)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.icon_employee_picture_3 = QLabel(self.employee_information_frame_3)
        self.icon_employee_picture_3.setObjectName(u"icon_employee_picture_3")
        self.icon_employee_picture_3.setFont(font1)
        self.icon_employee_picture_3.setPixmap(QPixmap(u":/icons/icons/user.svg"))
        self.icon_employee_picture_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_44.addWidget(self.icon_employee_picture_3, 0, Qt.AlignLeft)

        self.label_employee_name_3 = QLabel(self.employee_information_frame_3)
        self.label_employee_name_3.setObjectName(u"label_employee_name_3")
        self.label_employee_name_3.setFont(font1)
        self.label_employee_name_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_44.addWidget(self.label_employee_name_3, 0, Qt.AlignLeft)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_5)

        self.label_employee_permission_3 = QLabel(self.employee_information_frame_3)
        self.label_employee_permission_3.setObjectName(u"label_employee_permission_3")
        self.label_employee_permission_3.setFont(font1)
        self.label_employee_permission_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_44.addWidget(self.label_employee_permission_3, 0, Qt.AlignLeft)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_6)


        self.horizontalLayout_41.addWidget(self.employee_information_frame_3, 0, Qt.AlignLeft)

        self.button_manage_employee_3 = QPushButton(self.employee_management_frame_3)
        self.button_manage_employee_3.setObjectName(u"button_manage_employee_3")
        self.button_manage_employee_3.setMinimumSize(QSize(120, 35))
        self.button_manage_employee_3.setFont(font1)
        self.button_manage_employee_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_manage_employee_3.setStyleSheet(u"QPushButton {\n"
"	background-color: #E60540;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #C50332;\n"
"}")

        self.horizontalLayout_41.addWidget(self.button_manage_employee_3, 0, Qt.AlignRight)


        self.verticalLayout_27.addWidget(self.employee_management_frame_3)

        self.scrollArea_employees.setWidget(self.scrollAreaWidgets_employees)

        self.verticalLayout_26.addWidget(self.scrollArea_employees)


        self.verticalLayout_8.addWidget(self.main_employee_content_frame, 0, Qt.AlignHCenter)


        self.horizontalLayout_32.addWidget(self.main_body_employees)

        self.main_body.addWidget(self.page_employees)

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

        self.main_body.setCurrentIndex(0)


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
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"SALES", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"PROFIT", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PERMISSIONS", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MANAGEMENT", None))
        self.icon_credit_card.setText("")
        self.label_credit_card.setText(QCoreApplication.translate("MainWindow", u"CREDIT CARD", None))
        self.label_total_credit_card_orders.setText(QCoreApplication.translate("MainWindow", u"Total: 0", None))
        self.label_order_product_1.setText(QCoreApplication.translate("MainWindow", u"Purchased Product 1", None))
        self.label_order_price_1.setText(QCoreApplication.translate("MainWindow", u"+$20", None))
        self.label_order_id_1.setText(QCoreApplication.translate("MainWindow", u"Order ID: #487129", None))
        self.label_order_product_2.setText(QCoreApplication.translate("MainWindow", u"Purchased Product 2", None))
        self.label_order_price_2.setText(QCoreApplication.translate("MainWindow", u"+$45", None))
        self.label_order_id_2.setText(QCoreApplication.translate("MainWindow", u"Order ID: #091283", None))
        self.icon_money.setText("")
        self.label_money.setText(QCoreApplication.translate("MainWindow", u"MONEY", None))
        self.label_total_money_orders.setText(QCoreApplication.translate("MainWindow", u"Total: 0", None))
        self.label_order_product_3.setText(QCoreApplication.translate("MainWindow", u"Purchased Product 2", None))
        self.label_order_price_3.setText(QCoreApplication.translate("MainWindow", u"+$45", None))
        self.label_order_id_3.setText(QCoreApplication.translate("MainWindow", u"Order ID: #751987", None))
        self.label_order_product_4.setText(QCoreApplication.translate("MainWindow", u"Refund Product 1", None))
        self.label_order_price_4.setText(QCoreApplication.translate("MainWindow", u"-$20", None))
        self.label_order_id_4.setText(QCoreApplication.translate("MainWindow", u"Order ID: #051548", None))
        self.label_list_title.setText(QCoreApplication.translate("MainWindow", u"Employees list", None))
        self.button_add_employee.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.icon_employee_picture_1.setText("")
        self.label_employee_name_1.setText(QCoreApplication.translate("MainWindow", u"Employee 1", None))
        self.label_employee_permission_1.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.button_manage_employee_1.setText(QCoreApplication.translate("MainWindow", u"Manage", None))
        self.icon_employee_picture_2.setText("")
        self.label_employee_name_2.setText(QCoreApplication.translate("MainWindow", u"Employee 2", None))
        self.label_employee_permission_2.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.button_manage_employee_2.setText(QCoreApplication.translate("MainWindow", u"Manage", None))
        self.icon_employee_picture_3.setText("")
        self.label_employee_name_3.setText(QCoreApplication.translate("MainWindow", u"Employee 3", None))
        self.label_employee_permission_3.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.button_manage_employee_3.setText(QCoreApplication.translate("MainWindow", u"Manage", None))
    # retranslateUi

