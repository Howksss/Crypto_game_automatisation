import dotenv
import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 579)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgb(0, 0, 0), stop:1 rgb(69, 152, 190),);\n"
            "font: 700 16pt \"Malgun Gothic\";\n"
            "color: rgb(208, 208, 208);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(13, 169, 781, 191))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.mnemo_input = QtWidgets.QLineEdit(self.widget)
        self.mnemo_input.setMinimumSize(QtCore.QSize(0, 29))
        self.mnemo_input.setMaximumSize(QtCore.QSize(737, 29))
        self.mnemo_input.setStyleSheet("font: 700 13pt \"Malgun Gothic\";")
        self.mnemo_input.setText("")
        self.mnemo_input.setClearButtonEnabled(False)
        self.mnemo_input.setObjectName("mnemo_input")
        self.verticalLayout.addWidget(self.mnemo_input)
        self.tg_id_input = QtWidgets.QLineEdit(self.widget)
        self.tg_id_input.setStyleSheet("font: 700 13pt \"Malgun Gothic\";")
        self.tg_id_input.setText("")
        self.tg_id_input.setObjectName("tg_id_input")
        self.verticalLayout.addWidget(self.tg_id_input)
        self.bot_token_input = QtWidgets.QLineEdit(self.widget)
        self.bot_token_input.setStyleSheet("font: 700 13pt \"Malgun Gothic\";")
        self.bot_token_input.setText("")
        self.bot_token_input.setObjectName("bot_token_input")
        self.verticalLayout.addWidget(self.bot_token_input)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.threads_input = QtWidgets.QSpinBox(self.widget)
        self.threads_input.setMinimum(1)
        self.threads_input.setObjectName("threads_input")
        self.verticalLayout_2.addWidget(self.threads_input)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.send_test = QtWidgets.QPushButton(self.widget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/fingerprint_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.send_test.setIcon(icon)
        self.send_test.setIconSize(QtCore.QSize(25, 25))
        self.send_test.setObjectName("send_test")
        self.horizontalLayout.addWidget(self.send_test)
        self.start = QtWidgets.QPushButton(self.widget)
        self.start.setStyleSheet("background-color: rgb(18, 181, 18);\n"
                                 "color: rgb(0, 0, 0)")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icons/rocket_launch_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.start.setIcon(icon1)
        self.start.setIconSize(QtCore.QSize(25, 25))
        self.start.setObjectName("start")
        self.horizontalLayout.addWidget(self.start)
        self.stop = QtWidgets.QPushButton(self.widget)
        self.stop.setStyleSheet("background-color: rgb(189, 0, 0);\n"
                                "color: rgb(0, 0, 0)")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icons/disabled_by_default_FILL0_wght400_GRAD0_opsz24.svg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop.setIcon(icon2)
        self.stop.setIconSize(QtCore.QSize(25, 25))
        self.stop.setObjectName("stop")
        self.horizontalLayout.addWidget(self.stop)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 370, 781, 151))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setStyleSheet("background-color:rgb(80, 80, 80);\n"
                                 "font: 700 25pt \"Malgun Gothic\";")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setIndent(0)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.earned_money = QtWidgets.QLabel(self.widget1)
        self.earned_money.setStyleSheet("font: 700 56pt \"Malgun Gothic\";")
        self.earned_money.setScaledContents(False)
        self.earned_money.setAlignment(QtCore.Qt.AlignCenter)
        self.earned_money.setObjectName("earned_money")
        self.verticalLayout_4.addWidget(self.earned_money)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Howk"))
        self.mnemo_input.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.mnemo_input.setPlaceholderText(_translate("MainWindow", "Введите ключ-фразу:"))
        self.tg_id_input.setPlaceholderText(_translate("MainWindow", "Введите Telegram-id:"))
        self.bot_token_input.setPlaceholderText(_translate("MainWindow", "Введите token бота:"))
        self.threads_input.setPrefix(_translate("MainWindow", "Количество потоков: "))
        self.send_test.setText(_translate("MainWindow", "Отправить тестовое уведомление"))
        self.start.setText(_translate("MainWindow", "Пуск"))
        self.stop.setText(_translate("MainWindow", "Стоп"))
        self.label.setText(_translate("MainWindow", "Заработано:"))
        self.earned_money.setText(_translate("MainWindow", "16.74$"))

    def save_mnemo(self):
        mnemo = self.mnemo_input.text()
        dotenv.load_dotenv(r'../.env')
        os.environ["MNEMO"] = str(f"{mnemo}")
        dotenv.set_key(r'../.env', 'MNEMO', os.environ["MNEMO"])


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = YesMainWindow()
    YesMainWindow.show()
    sys.exit(app.exec_())
