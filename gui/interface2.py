import dotenv
import os
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QFileDialog
from threading import Thread

from running.main import getting_started
from running.main import points


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(857, 579)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/bonk.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAccessibleName("")
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgb(0, 0, 0), stop:1 rgb(69, 152, 190),);\n"
            "font: ;\n"
            "font: 16pt \"Arial\";\n"
            "color: rgb(208, 208, 208);"
        )
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 210, 842, 361))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fileButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.fileButton.setStyleSheet(
            "QPushButton {\n"
            "color: rgb(45, 45, 45);\n"
            "font-weight: bold;\n"
            "font-size: 17pt;\n"
            "background-color: rgba(255, 255, 255, 60%);\n"
            "border: 1px solid rgba(255,255,255, 70%);\n"
            "border-radius: 7px;\n"
            "width: 120px;\n"
            "height: 50px\n"
            "}\n"
            "QPushButton:hover {\n"
            "background-color: rgba(255, 255, 255, 70%);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "background-color: rgba(255, 255, 255, 90%);\n"
            "}"
        )
        self.fileButton.setObjectName("fileButton")
        self.horizontalLayout_2.addWidget(self.fileButton)
        self.setFileDirectory = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.setFileDirectory.setStyleSheet(
            "height: 40px\n"
            ""
        )
        self.setFileDirectory.setObjectName("setFileDirectory")
        self.horizontalLayout_2.addWidget(self.setFileDirectory)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tg_id_input = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.tg_id_input.setStyleSheet("font: 700 13pt \"Malgun Gothic\";")
        self.tg_id_input.setText("")
        self.tg_id_input.setObjectName("tg_id_input")
        self.verticalLayout.addWidget(self.tg_id_input)
        self.bot_token_input = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.bot_token_input.setStyleSheet("font: 700 13pt \"Malgun Gothic\";")
        self.bot_token_input.setText("")
        self.bot_token_input.setObjectName("bot_token_input")
        self.verticalLayout.addWidget(self.bot_token_input)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.threads_input_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.threads_input_label.setStyleSheet(
            "color: white;\n"
            "font-weight: bold;\n"
            "font-size: 12pt;\n"
            "background-color: none;\n"
            "border-radius: 7px;\n"
            "border: none;"
        )
        self.threads_input_label.setObjectName("threads_input_label")
        self.horizontalLayout.addWidget(self.threads_input_label)
        self.threads_input = QtWidgets.QSpinBox(parent=self.layoutWidget)
        self.threads_input.setStyleSheet(
            "QSpinBox {\n"
            "color: white;\n"
            "font-weight: bold;\n"
            "font-size: 25pt;\n"
            "background-color: rgba(255, 255, 255, 30%);\n"
            "border: 1px solid rgba(255,255,255, 40%);\n"
            "border-radius: 7px;\n"
            "width: 100px;\n"
            "height: 50px\n"
            "}\n"
            ""
        )
        self.threads_input.setWrapping(False)
        self.threads_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.threads_input.setSuffix("")
        self.threads_input.setPrefix("")
        self.threads_input.setMinimum(1)
        self.threads_input.setObjectName("threads_input")
        self.horizontalLayout.addWidget(self.threads_input)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.send_test = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.send_test.setStyleSheet(
            "QPushButton {\n"
            "color: rgb(45, 45, 45);\n"
            "font-weight: bold;\n"
            "font-size: 17pt;\n"
            "background-color: rgba(255, 255, 255, 60%);\n"
            "border: 1px solid rgba(255,255,255, 70%);\n"
            "border-radius: 7px;\n"
            "width: 420px;\n"
            "height: 50px\n"
            "}\n"
            "QPushButton:hover {\n"
            "background-color: rgba(255, 255, 255, 70%);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "background-color: rgba(255, 255, 255, 90%);\n"
            "}"
        )
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icons/fingerprint_FILL0_wght400_GRAD0_opsz24.svg"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.send_test.setIcon(icon1)
        self.send_test.setIconSize(QtCore.QSize(25, 25))
        self.send_test.setObjectName("send_test")
        self.horizontalLayout_3.addWidget(self.send_test)
        self.start = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.start.setStyleSheet(
            "QPushButton {\n"
            "color: rgb(208, 208, 208);\n"
            "font-weight: bold;\n"
            "font-size: 25pt;\n"
            "background-color: rgba(18, 181, 18, 60%);\n"
            "border: 1px solid rgba(255,255,255, 70%);\n"
            "border-radius: 7px;\n"
            "width: 200px;\n"
            "height: 50px\n"
            "}\n"
            "QPushButton:hover {\n"
            "background-color: rgba(18, 181, 18, 70%);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "background-color: rgba(18, 181, 18, 90%);\n"
            "}"
        )
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icons/rocket_launch_FILL1_wght400_GRAD0_opsz24.svg"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.start.setIcon(icon2)
        self.start.setIconSize(QtCore.QSize(32, 32))
        self.start.setObjectName("start")
        self.horizontalLayout_3.addWidget(self.start)
        self.stop = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.stop.setStyleSheet(
            "QPushButton {\n"
            "color: rgb(208, 208, 208);\n"
            "font-weight: bold;\n"
            "font-size: 25pt;\n"
            "background-color: rgba(189, 0, 0, 60%);\n"
            "border: 1px solid rgba(255,255,255, 70%);\n"
            "border-radius: 7px;\n"
            "width: 200px;\n"
            "height: 50px\n"
            "}\n"
            "QPushButton:hover {\n"
            "background-color: rgba(189, 0, 0, 70%);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "background-color: rgba(189, 0, 0, 90%);\n"
            "}"
        )
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icons/disabled_by_default_FILL0_wght400_GRAD0_opsz24.svg"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.stop.setIcon(icon3)
        self.stop.setIconSize(QtCore.QSize(32, 32))
        self.stop.setObjectName("stop")
        self.horizontalLayout_3.addWidget(self.stop)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.earned_money_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.earned_money_label.setStyleSheet(
            "color: white;\n"
            "font-weight: bold;\n"
            "font-size: 34pt;\n"
            "background-color: none;\n"
            "border-radius: 7px;\n"
            "border: none;"
        )
        self.earned_money_label.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.earned_money_label.setScaledContents(False)
        self.earned_money_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.earned_money_label.setWordWrap(False)
        self.earned_money_label.setIndent(0)
        self.earned_money_label.setOpenExternalLinks(False)
        self.earned_money_label.setObjectName("earned_money_label")
        self.verticalLayout_4.addWidget(self.earned_money_label)
        self.earned_money = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.earned_money.setEnabled(True)
        self.earned_money.setAcceptDrops(False)
        self.earned_money.setStyleSheet(
            "background-color: rgba(255,255,255,30%);\n"
            "border: 1px solid rgba(255,255,255,40%);\n"
            "border-radius: 7px;\n"
            "font: 700 56pt \"Malgun Gothic\";"
        )
        self.earned_money.setReadOnly(True)
        self.earned_money.setObjectName("earned_money")
        self.verticalLayout_4.addWidget(self.earned_money)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_function()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Howk"))
        self.fileButton.setText(_translate("MainWindow", "Открыть"))
        self.setFileDirectory.setPlaceholderText(_translate("MainWindow", "Выберите расположение файла key-phrases:"))
        self.tg_id_input.setPlaceholderText(_translate("MainWindow", "Введите Telegram-id:"))
        self.bot_token_input.setPlaceholderText(_translate("MainWindow", "Введите token бота:"))
        self.threads_input_label.setText(_translate("MainWindow", "Кол-во потоков:"))
        self.threads_input.setAccessibleDescription(_translate("MainWindow", "asdasdasdsadsa"))
        self.send_test.setText(_translate("MainWindow", "Отправить тестовое уведомление"))
        self.start.setText(_translate("MainWindow", "Пуск"))
        self.stop.setText(_translate("MainWindow", "Стоп"))
        self.earned_money_label.setText(_translate("MainWindow", "Заработано:"))

    def add_function(self):
        self.send_test.clicked.connect(
            lambda: self.test_notif(user_id=self.tg_id_input.text(), bot_token=self.bot_token_input.text()))
        self.fileButton.clicked.connect(self.open_directory)
        self.start.clicked.connect(lambda: self.main_start())

    def open_directory(self):
        self.setFileDirectory.setText(str(f"{QFileDialog.getOpenFileName()}")[2:-19])
        dotenv.load_dotenv(r'../.env')
        os.environ["MNEMO_PATH"] = str(f"{self.setFileDirectory.text()}")
        dotenv.set_key(r'../.env', 'MNEMO_PATH', os.environ["MNEMO_PATH"])

    def main_start(self):
        dotenv.load_dotenv(r'../.env')
        os.environ["THREADS"] = str(f"{self.threads_input.text()}")
        dotenv.set_key(r'../.env', 'THREADS', os.environ["THREADS"])
        t1 = Thread(target=lambda: os.system(r'python C:\Users\nikit\PycharmProjects\IMSO\running\main.py'))
        t1.start()
        t1.join()

    def money_amount(self, bonks):
        self.earned_money.setText(f"{int(bonks)}$")

    def test_notif(self, user_id, bot_token):
        try:
            req = requests.get(
                f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={user_id}&text=Тестовое сообщение!").json()
            if req["ok"] == True:
                self.send_test.setStyleSheet(
                    "QPushButton {\n"
                    "color: rgb(45, 45, 45);\n"
                    "font-weight: bold;\n"
                    "font-size: 17pt;\n"
                    "background-color: rgba(38, 255, 71, 60%);\n"
                    "border: 1px solid rgba(255,255,255, 70%);\n"
                    "border-radius: 7px;\n"
                    "width: 420px;\n"
                    "height: 50px\n"
                    "}\n"
                    "QPushButton:hover {\n"
                    "background-color: rgba(255, 255, 255, 70%);\n"
                    "}\n"
                    "QPushButton:pressed {\n"
                    "background-color: rgba(255, 255, 255, 90%);\n"
                    "}"
                )
                self.send_test.setText("Данные корректны!")
                dotenv.load_dotenv(r'../.env')
                os.environ["TOKEN"] = str(f"{bot_token}")
                os.environ["ID"] = str(f"{user_id}")
                dotenv.set_key(r'../.env', 'TOKEN', os.environ["TOKEN"])
                dotenv.set_key(r'../.env', 'ID', os.environ["ID"])
                return True
            elif req["ok"] == False:
                self.send_test.setStyleSheet(
                    "QPushButton {\n"
                    "color: rgb(45, 45, 45);\n"
                    "font-weight: bold;\n"
                    "font-size: 17pt;\n"
                    "background-color: rgba(255, 41, 41, 60%);\n"
                    "border: 1px solid rgba(255,255,255, 70%);\n"
                    "border-radius: 7px;\n"
                    "width: 420px;\n"
                    "height: 50px\n"
                    "}\n"
                    "QPushButton:hover {\n"
                    "background-color: rgba(255, 255, 255, 70%);\n"
                    "}\n"
                    "QPushButton:pressed {\n"
                    "background-color: rgba(255, 255, 255, 90%);\n"
                    "}"
                )
                self.send_test.setText("Некорректные данные!")
                return False
        except Exception:
            return False

    def save_params(self, user_id, bot_token, mnemo_path):
        print(user_id, bot_token, mnemo_path)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
