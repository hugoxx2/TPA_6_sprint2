import csv
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QMainWindow, QApplication, QFormLayout, QDateEdit
from PyQt6.QtCore import Qt, QDate
from desvincularWindow import DesvincularWindow
from horarioWindow import HorarioWindow

class RegisterWindow(QWidget):
    #def constructor de la clase registerwindow que recibe una ventana de inicio de sesion como argumento
    def __init__(self, login_window):
        super().__init__()
        self.setWindowTitle("Registro")
        self.setGeometry(200, 200, 400, 300)

        self.login_window = login_window

        self.register_label = QLabel("Registro")
        self.register_label.setStyleSheet("font-size: 24px; margin-bottom: 20px;")

        self.username_label = QLabel("Usuario:")
        self.password_label = QLabel("Contraseña:")
        self.rut_label = QLabel("Rut:")
        self.codigo_label = QLabel("Codigo empleado: ")
        self.birthdate_label = QLabel("Fecha de nacimiento:")
        self.occupation_label = QLabel("Ocupación:")

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.rut_input = QLineEdit()
        self.codigo_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.birthdate_input = QDateEdit()
        self.occupation_input = QLineEdit()

        self.register_button = QPushButton("Registrarse")
        self.register_button.clicked.connect(self.register)
        self.register_button.setStyleSheet("font-size: 18px; padding: 10px 20px;")

        self.back_button = QPushButton("Volver")
        self.back_button.clicked.connect(self.back)
        self.back_button.setStyleSheet("font-size: 18px; padding: 10px 20px;")

        self.form_layout = QFormLayout()
        self.form_layout.addRow(self.username_label, self.username_input)
        self.form_layout.addRow(self.password_label, self.password_input)
        self.form_layout.addRow(self.rut_label, self.rut_input)
        self.form_layout.addRow(self.codigo_label, self.codigo_input)
        self.form_layout.addRow(self.birthdate_label, self.birthdate_input)
        self.form_layout.addRow(self.occupation_label, self.occupation_input)
        self.form_layout.addRow(self.register_button, self.back_button)

        layout = QVBoxLayout()
        layout.addWidget(self.register_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(self.form_layout)
        layout.addStretch()

        self.setLayout(layout)
#en este def, se puede modificar la ventana de registrarse
#se puede modificar que se muestra en la ventana, como el nombre de usuario, la contraseña y la ocupacion en el hotel
#tambien verifica si se cumplen ciertas condiciones como la longitud de la contraseña
#y guarda la informacion en un csv "registro_de_cuentas.csv" y si hay algun error lo muestra en pantalla
    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        rut = self.rut_input.text()
        codigo = self.codigo_input.text()
        birthdate = self.birthdate_input.date().toString(Qt.DateFormat.ISODate)
        occupation = self.occupation_input.text()

        if len(password) > 8:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Icon.Critical)
            error_dialog.setWindowTitle("Error de registro")
            error_dialog.setText("La contraseña no puede tener más de 8 caracteres.")
            error_dialog.exec()
            return

        if username and password and rut and codigo and birthdate and occupation:
            try:
                with open('registro_de_cuentas.csv','a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([username, password, rut, codigo, birthdate, occupation])
            except OSError as e:
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Icon.Critical)
                error_dialog.setWindowTitle("Error de registro")
                error_dialog.setText("Error al escribir en el archivo CSV.")
                error_dialog.exec()
                print(f"Error al escribir en el archivo CSV: {e}")
                return

            print("Registro exitoso")
            self.close()
            self.login_window.show()
        else:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Icon.Critical)
            error_dialog.setWindowTitle("Error de registro")
            error_dialog.setText("Por favor, ingresa todos los campos requeridos.")
            error_dialog.exec()

        

    def back(self):
        #metodo de la clase registerwindow, que se llama cuando se le hace click en volver
        #cerrando la ventana actual y volviendo a la ventana de inicio de sesion
        self.close()
        self.login_window.show()

class LoginWindow(QWidget):
#define una clase llamada loginwindow que hereda de Qwidget, representa la ventana de inicio de sesion
    def __init__(self):
        #constructor de loginwindow,pudiendose configurar la apariencia y tambien los widgets de la ventana de inicio de sesion
        super().__init__()
        self.setWindowTitle("Inicio de sesión")
        self.setGeometry(200, 200, 400, 300)

        self.login_label = QLabel("Inicio de sesión")
        self.login_label.setStyleSheet("font-size: 24px; margin-bottom: 20px;")

        self.username_label = QLabel("Usuario:")
        self.password_label = QLabel("Contraseña:")

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Iniciar sesión")
        self.login_button.clicked.connect(self.login)
        self.login_button.setStyleSheet("font-size: 18px; padding: 10px 20px;")

        layout = QVBoxLayout()
        layout.addWidget(self.login_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addStretch()

        self.setLayout(layout)

        self.main_window = None

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        with open('registro_de_cuentas.csv',newline='') as cuentas:
            reader = csv.DictReader(cuentas)
            for row in reader:
                if username == row['Usuario'] and password == row['Contrasenha']:
                    print("Inicio de sesión exitoso")
                    self.login_successful()
                    break
            else:
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Icon.Critical)
                error_dialog.setWindowTitle("Error de inicio de sesión")
                error_dialog.setText("Usuario o contraseña incorrectos.")
                print("Inicio de sesión fallido")
                error_dialog.exec()

    def login_successful(self):
        if self.main_window is None:
            self.main_window = MainWindow()
        self.main_window.show()
        self.hide()

class MainWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("Sistema de Personal")
        self.setGeometry(200, 200, 800, 600)

        self.label = QLabel("¿Qué desea hacer?")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("font-size: 24px;")

        self.horario_button = QPushButton("Gestionar de Horarios")
        self.horario_button.clicked.connect(self.open_gestionar_horario)
        self.horario_button.setStyleSheet("font-size: 18px; padding: 10px 20px;")

        self.desvincular_button = QPushButton("Desvincular Personal")
        self.desvincular_button.clicked.connect(self.open_desvincular_window)
        self.desvincular_button.setStyleSheet("font-size: 18px; padding: 10px 20px;")

        self.register_button = QPushButton("Contratar")
        self.register_button.clicked.connect(self.open_register_window)
        self.register_button.setStyleSheet("font-size: 18px; padding: 10px 20px;")

        layout = QVBoxLayout()
        layout.addSpacing(80)
        layout.addWidget(self.label)
        layout.addStretch()
        layout.addWidget(self.horario_button)
        layout.addWidget(self.desvincular_button)
        layout.addWidget(self.register_button)
        layout.addStretch()

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.horario_window = None
        self.desvincular_window = None
        self.register_window = None

    def login_successful(self):
        self.label.setText("¿Qué desea hacer?")
        self.horario_button.setEnabled(True)
        self.desvincular_button.setEnabled(True)
        self.register_button.setEnabled(True)

    def open_gestionar_horario(self):
        self.horario_window = HorarioWindow(self)
        self.horario_window.show()
        self.hide()

    def open_desvincular_window(self):
        self.desvincular_window = DesvincularWindow(self)
        self.hide()
        self.desvincular_window.show()

    def open_register_window(self):
        self.register_window = RegisterWindow(self)
        self.hide()
        self.register_window.show()

