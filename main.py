from ui_dashboard import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Modern Dashboard")

        # Hide / Show Sidebar
        self.ui.sidebar.hide()
        self.ui.button_sidebar.clicked.connect(self.hide_sidebar)

        # Change graph tab
        self.ui.button_electricity_consumption.setStyleSheet("border-bottom: 2px solid #E60540;")
        self.ui.button_electricity_consumption.clicked.connect(self.style_tab_electricity_consumption)
        self.ui.button_devices.clicked.connect(self.style_tab_devices)

    def hide_sidebar(self):
        sidebar_container = self.ui.sidebar
        if sidebar_container.isVisible():
            sidebar_container.hide()
            self.ui.button_sidebar.setIcon(QIcon("icons/align-justify.svg"))
        else:
            sidebar_container.show()
            self.ui.button_sidebar.setIcon(QIcon("icons/chevron-left.svg"))

    def style_tab_electricity_consumption(self):
        style_button_electricity_consumption = "border-bottom: 2px solid #E60540;"
        style_button_devices = "border: none;"
        self.ui.button_electricity_consumption.setStyleSheet(style_button_electricity_consumption)
        self.ui.button_devices.setStyleSheet(style_button_devices)

    def style_tab_devices(self):
        style_button_electricity_consumption = "border: none;"
        style_button_devices = "border-bottom: 2px solid #E60540;"
        self.ui.button_electricity_consumption.setStyleSheet(style_button_electricity_consumption)
        self.ui.button_devices.setStyleSheet(style_button_devices)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
