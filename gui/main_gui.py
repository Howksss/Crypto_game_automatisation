import os
import requests
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from dotenv import load_dotenv

load_dotenv(r"..\.env")


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("IMSO")
        self.setGeometry(750, 350, 500, 600)

        self.new_text = QtWidgets.QLabel(self)

        threads_input = QtWidgets.QPlainTextEdit(self)
        threads_input.move(10, 30)

        main_text = QtWidgets.QLabel(self)
        main_text.setText("Введите свой Telegram-id")
        main_text.move(10, 10)
        main_text.adjustSize()

        btn = QtWidgets.QPushButton(self)
        btn.move(10, 60)
        btn.setText("Отправить тестовое сообщение")
        btn.setFixedWidth(200)
        btn.clicked.connect(self.check_tg)

    def check_tg(self):
        self.new_text.setText("Отправлено")
        self.new_text.move()
        url = f"https://api.telegram.org/bot{os.getenv('TOKEN')}/sendMessage?chat_id={os.getenv('ID')}&text=Обнаружен запуск софта\n\nПользователь: {os.getlogin()}\nПотоков запущено:"
        requests.get(url).json()


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
