import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QColorDialog, QDialog, QDialogButtonBox, QHBoxLayout
)
from PyQt5.QtGui import QFont, QPalette, QColor, QLinearGradient, QBrush
from PyQt5.QtCore import Qt, QTimer, QDateTime


class BeautifulApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Красивое PyQt5-приложение")
        self.setGeometry(200, 200, 400, 350)
        self.setup_ui()
        self.apply_styles()

    def setup_ui(self):
        # Шрифты
        title_font = QFont("Arial", 18, QFont.Bold)
        text_font = QFont("Arial", 12)

        # Виджеты
        self.label_title = QLabel("Добро пожаловать!", self)
        self.label_title.setFont(title_font)
        self.label_title.setAlignment(Qt.AlignCenter)

        self.input = QLineEdit(self)
        self.input.setPlaceholderText("Введите ваше имя")
        self.input.setFont(text_font)

        self.button_hello = QPushButton("Сказать привет", self)
        self.button_hello.setFont(text_font)
        self.button_hello.clicked.connect(self.say_hello)

        self.button_change_bg = QPushButton("Изменить фон", self)
        self.button_change_bg.setFont(text_font)
        self.button_change_bg.clicked.connect(self.change_background)

        self.button_info = QPushButton("Информация о приложении", self)
        self.button_info.setFont(text_font)
        self.button_info.clicked.connect(self.show_info)

        self.output = QLabel("", self)
        self.output.setFont(text_font)
        self.output.setAlignment(Qt.AlignCenter)

        # Текущее время
        self.time_label = QLabel("", self)
        self.time_label.setFont(text_font)
        self.time_label.setAlignment(Qt.AlignCenter)

        # Обновление времени каждую секунду
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_title)
        layout.addWidget(self.input)
        layout.addWidget(self.button_hello)
        layout.addWidget(self.button_change_bg)
        layout.addWidget(self.button_info)
        layout.addWidget(self.output)
        layout.addWidget(self.time_label)
        self.setLayout(layout)

    def say_hello(self):
        name = self.input.text().strip()
        if name:
            self.output.setText(f"🌸 Привет, {name}! 🌸")
        else:
            self.output.setText("Пожалуйста, введите имя 🌿")

    def change_background(self):
        color = QColorDialog.getColor()
        if color.isValid():
            palette = QPalette()
            palette.setColor(QPalette.Window, color)
            self.setPalette(palette)

    def update_time(self):
        current_time = QDateTime.currentDateTime().toString('hh:mm:ss')
        self.time_label.setText(f"Текущее время: {current_time}")

    def show_info(self):
        info_dialog = QDialog(self)
        info_dialog.setWindowTitle("Информация")

        info_label = QLabel("Это простое PyQt5-приложение, демонстрирующее\n"
                            "работу с графическим интерфейсом, цветами,\n"
                            "временем и взаимодействием с пользователем.", info_dialog)
        info_label.setFont(QFont("Arial", 12))

        buttons = QDialogButtonBox(QDialogButtonBox.Ok)
        buttons.rejected.connect(info_dialog.reject)

        layout = QVBoxLayout()
        layout.addWidget(info_label)
        layout.addWidget(buttons)
        info_dialog.setLayout(layout)

        info_dialog.exec_()

    def apply_styles(self):
        # Градиент фона
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor("#ffecd2"))
        gradient.setColorAt(1.0, QColor("#fcb69f"))
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(palette)

        # Стили для кнопки и поля ввода
        self.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #f8cdda;
                border-radius: 10px;
                background-color: #fffaf0;
            }
            QPushButton {
                background-color: #f6d365;
                border: none;
                padding: 10px;
                border-radius: 15px;
                color: #4b3832;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #fda085;
            }
            QLabel {
                color: #4b3832;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BeautifulApp()
    window.show()
    sys.exit(app.exec_())
