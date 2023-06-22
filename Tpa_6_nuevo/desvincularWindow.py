import sys
import csv
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget


class DesvincularWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Desvincular Personal")
        self.setGeometry(100, 100, 600, 400)

        layout = QHBoxLayout(self)
        panel_layout = QVBoxLayout()

        # Panel izquierdo
        panel_label = QLabel("Lista de empleados:")
        self.employee_list = QListWidget()
        panel_layout.addWidget(panel_label)
        panel_layout.addWidget(self.employee_list)

        # Panel derecho
        right_panel_layout = QVBoxLayout()

        search_layout = QHBoxLayout()
        search_label = QLabel("Buscar:")
        self.search_input = QLineEdit()
        search_button = QPushButton("Buscar")
        search_button.clicked.connect(self.search_employee)
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_button)

        self.employee_info_label = QLabel("Información del empleado:")
        self.employee_info = QLabel()

        unbind_button = QPushButton("Desvincular Empleado")
        unbind_button.clicked.connect(self.unbind_employee)

        back_button = QPushButton("Volver")
        back_button.clicked.connect(self.close)

        right_panel_layout.addLayout(search_layout)
        right_panel_layout.addWidget(self.employee_info_label)
        right_panel_layout.addWidget(self.employee_info)
        right_panel_layout.addWidget(unbind_button)
        right_panel_layout.addWidget(back_button)

        layout.addLayout(panel_layout)
        layout.addLayout(right_panel_layout)

        self.load_employee_list()

    def close(self):
        self.main_window.show()
        self.hide()  

    def load_employee_list(self):
        with open("registro_de_cuentas.csv", newline='') as csvfile:
            reader = csv.reader(csvfile)
            employee_data = list(reader)
            for data in employee_data:
                self.employee_list.addItem(data[0])  # Assuming the employee name is in the first column

    def search_employee(self):
        search_text = self.search_input.text()
        with open("registro_de_cuentas.csv", newline='') as csvfile:
            reader = csv.reader(csvfile)
            employee_data = list(reader)
            for data in employee_data:
                if search_text in data:
                    self.employee_info.setText("\n".join(data))
                    break
            else:
                self.employee_info.setText("Empleado no encontrado")

    def unbind_employee(self):
        selected_employee = self.employee_list.currentItem().text()
        with open("registro_de_cuentas.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            employee_data = list(reader)
        with open("registro_de_cuentas.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            for data in employee_data:
                if data[0] != selected_employee:
                    writer.writerow(data)
        self.employee_info.setText("")
        self.employee_list.clear()
        self.load_employee_list()


