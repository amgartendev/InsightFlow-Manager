from ui_dashboard import *


class Pages(QMainWindow):
    def __init__(self, dashboard):
        super().__init__()
        self.dashboard = dashboard

    def set_dashboard_layout(self):
        self.dashboard.main_body.setCurrentWidget(self.dashboard.page_dashboard)

    def set_employees_layout(self):
        self.dashboard.main_body.setCurrentWidget(self.dashboard.page_employees)

    def set_orders_layout(self):
        self.dashboard.main_body.setCurrentWidget(self.dashboard.page_orders)

    def set_sales_layout(self):
        self.dashboard.main_body.setCurrentWidget(self.dashboard.page_sales)

    def set_profit_layout(self):
        self.dashboard.main_body.setCurrentWidget(self.dashboard.page_profit)

    def set_permissions_layout(self):
        self.dashboard.main_body.setCurrentWidget(self.dashboard.page_permissions)

    def set_management_layout(self):
        self.dashboard.main_body.setCurrentWidget(self.dashboard.page_management)
