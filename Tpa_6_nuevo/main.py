import sys
from PyQt6.QtWidgets import QApplication
from mainWindow import MainWindow,LoginWindow
from desvincularWindow import DesvincularWindow
from horarioWindow import HorarioWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
