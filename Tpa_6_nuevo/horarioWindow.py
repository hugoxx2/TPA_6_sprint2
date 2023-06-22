import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QPushButton


class HorarioWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Calendario")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout(self)

        # Calendario
        self.calendar = QCalendarWidget()
        layout.addWidget(self.calendar)

        # Botón de asignación
        assign_button = QPushButton("Asignar")
        assign_button.clicked.connect(self.assign_date)
        layout.addWidget(assign_button)

        # Botón de volver
        back_button = QPushButton("Volver")
        back_button.clicked.connect(self.close)
        layout.addWidget(back_button)

    def close(self):
        self.main_window.show()
        self.hide()

    def assign_date(self):
        selected_date = self.calendar.selectedDate()
        print("Fecha seleccionada:", selected_date.toString())
