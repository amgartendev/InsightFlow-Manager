from PySide6.QtWidgets import QApplication, QMainWindow
from ui_dashboard import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Modern Dashboard")
        self.ui.pushButton_14.clicked.connect(self.test)
        self.ui.pushButton_15.clicked.connect(self.test2)
        self.ui.pushButton_14.setStyleSheet("border-bottom: 2px solid #E60540;")

    def test(self):
        new_style_button_14 = "border-bottom: 2px solid #E60540;"
        new_style_button_15 = "border: none;"
        self.ui.pushButton_14.setStyleSheet(new_style_button_14)
        self.ui.pushButton_15.setStyleSheet(new_style_button_15)

    def test2(self):
        new_style_button_14 = "border: none;"
        new_style_button_15 = "border-bottom: 2px solid #E60540;"
        self.ui.pushButton_14.setStyleSheet(new_style_button_14)
        self.ui.pushButton_15.setStyleSheet(new_style_button_15)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
