from PySide6.QtWidgets import QApplication
from dashboard import Dashboard
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    app.exec()
