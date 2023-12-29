from ui_dashboard import *
from graphs import Graphs
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("InsightFlow Manager")

        # Hide / Show Sidebar
        self.ui.sidebar.hide()
        self.ui.button_sidebar.clicked.connect(self.hide_sidebar)

        # Change temperature / humidity graph tab
        self.ui.button_temperature.setStyleSheet("border-bottom: 2px solid #E60540;")
        self.ui.button_temperature.clicked.connect(self.style_tab_temperature)
        self.ui.button_humidity.clicked.connect(self.style_tab_humidity)

        # Change electricity / devices graph tab
        self.ui.button_electricity_consumption.setStyleSheet("border-bottom: 2px solid #E60540;")
        self.ui.button_electricity_consumption.clicked.connect(self.style_tab_electricity_consumption)
        self.ui.button_devices.clicked.connect(self.style_tab_devices)

        # Plot Traffic Consumption Graph
        traffic_consumption_graph = Graphs.traffic_consumption()
        self.ui.verticalLayout_5.addWidget(traffic_consumption_graph)

        # Plot Energy Consumption Graph
        electricity_consumption_graph = Graphs.energy_consumption()
        self.ui.verticalLayout_4.addWidget(electricity_consumption_graph)

        # ================ PAGES
        self.ui.button_dashboard.clicked.connect(self.set_dashboard_layout)
        self.ui.button_employees.clicked.connect(self.set_employees_layout)
        self.ui.button_orders.clicked.connect(self.set_orders_layout)
        self.ui.button_sales.clicked.connect(self.set_sales_layout)
        self.ui.button_profit.clicked.connect(self.set_profit_layout)
        self.ui.button_permissions.clicked.connect(self.set_permissions_layout)
        self.ui.button_management.clicked.connect(self.set_management_layout)

    def hide_sidebar(self):
        sidebar_container = self.ui.sidebar
        if sidebar_container.isVisible():
            sidebar_container.hide()
            self.ui.button_sidebar.setIcon(QIcon("icons/align-justify.svg"))
        else:
            sidebar_container.show()
            self.ui.button_sidebar.setIcon(QIcon("icons/chevron-left.svg"))

    def style_tab_temperature(self):
        style_button_temperature = "border-bottom: 2px solid #E60540;"
        style_button_humidity = "border: none"

        self.ui.button_temperature.setStyleSheet(style_button_temperature)
        self.ui.button_humidity.setStyleSheet(style_button_humidity)

        temperature_label = "75º F"

        icon_wind = QPixmap("icons/wind.svg")
        label_wind = "Wind: 3mph"

        icon_rain = QPixmap("icons/cloud-rain.svg")
        label_rain = "Rain: 0%"

        icon_weather = QPixmap("icons/sun.svg")
        label_weather = "Sunny"""

        self.ui.label_temperature.setText(temperature_label)

        self.ui.icon_wind.setPixmap(icon_wind)
        self.ui.label_wind.setText(label_wind)

        self.ui.icon_rain.setPixmap(icon_rain)
        self.ui.label_rain.setText(label_rain)

        self.ui.icon_weather.setPixmap(icon_weather)
        self.ui.label_weather.setText(label_weather)

    def style_tab_humidity(self):
        style_button_temperature = "border: none"
        style_button_humidity = "border-bottom: 2px solid #E60540;"

        self.ui.button_temperature.setStyleSheet(style_button_temperature)
        self.ui.button_humidity.setStyleSheet(style_button_humidity)

        temperature_label = "95%"

        icon_visibility = QPixmap("icons/eye.svg")
        label_visibility = "Visibility: Excellent"

        icon_sunrise = QPixmap("icons/sunrise.svg")
        label_sunrise = "Sunrise: 6am"

        icon_sunset = QPixmap("icons/sunset.svg")
        label_sunset = "Sunset: 6pm"

        self.ui.label_temperature.setText(temperature_label)

        self.ui.icon_wind.setPixmap(icon_visibility)
        self.ui.label_wind.setText(label_visibility)

        self.ui.icon_rain.setPixmap(icon_sunrise)
        self.ui.label_rain.setText(label_sunrise)

        self.ui.icon_weather.setPixmap(icon_sunset)
        self.ui.label_weather.setText(label_sunset)

    def style_tab_electricity_consumption(self):
        style_button_electricity_consumption = "border-bottom: 2px solid #E60540;"
        style_button_devices = "border: none;"
        electricity_consumption_graph = Graphs.energy_consumption()

        # Clear layout to plot a new graph
        for i in reversed(range(self.ui.verticalLayout_4.count())):
            self.ui.verticalLayout_4.itemAt(i).widget().setParent(None)
        self.ui.button_electricity_consumption.setStyleSheet(style_button_electricity_consumption)
        self.ui.button_devices.setStyleSheet(style_button_devices)
        self.ui.verticalLayout_4.addWidget(electricity_consumption_graph)

    def style_tab_devices(self):
        style_button_electricity_consumption = "border: none;"
        style_button_devices = "border-bottom: 2px solid #E60540;"
        devices_graph = Graphs.devices()

        # Clear layout to plot a new graph
        for i in reversed(range(self.ui.verticalLayout_4.count())):
            self.ui.verticalLayout_4.itemAt(i).widget().setParent(None)
        self.ui.button_electricity_consumption.setStyleSheet(style_button_electricity_consumption)
        self.ui.button_devices.setStyleSheet(style_button_devices)
        self.ui.verticalLayout_4.addWidget(devices_graph)

    # =============== PAGES
    def set_dashboard_layout(self):
        self.ui.main_body.setCurrentWidget(self.ui.page_dashboard)

    def set_employees_layout(self):
        self.ui.main_body.setCurrentWidget(self.ui.page_employees)

    def set_orders_layout(self):
        self.ui.main_body.setCurrentWidget(self.ui.page_orders)

    def set_sales_layout(self):
        self.ui.main_body.setCurrentWidget(self.ui.page_sales)

    def set_profit_layout(self):
        self.ui.main_body.setCurrentWidget(self.ui.page_profit)

    def set_permissions_layout(self):
        self.ui.main_body.setCurrentWidget(self.ui.page_permissions)

    def set_management_layout(self):
        self.ui.main_body.setCurrentWidget(self.ui.page_management)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
