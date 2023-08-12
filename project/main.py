import sys
import datetime
from PySide6.QtWidgets import QApplication, QMainWindow
from pygame import mixer
from design import Ui_MainWindow
import PySide6
from PyQt6 import QtCore
from PyQt6 import QtTest
import mouse
from find_domains import find_domains


class DD(QMainWindow):
    def __init__(self):
        super(DD, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.send.clicked.connect(self.search)

        self.ui.send_2.clicked.connect(self.ui.webEngineView.back)
        self.ui.send_3.clicked.connect(self.ui.webEngineView.forward)
        self.ui.send_4.clicked.connect(self.reload)

    def search(self):
        if not self.ui.url.text().startswith('http') and len([i for i in find_domains(self.ui.url.text())]) == 0:
            link = f"{self.ui.url.text()}"
            self.ui.webEngineView.load(f"https://www.google.com/search?q={link}")

        else:
            link = 'http://' + self.ui.url.text()
            self.ui.webEngineView.load(link)

    def url_set(self):
        QtTest.QTest.qWait(1000)
        self.ui.url.setText(str(self.ui.webEngineView.url().url()))
        print('ep')

    def reload(self):
        self.ui.webEngineView.reload()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DD()
    window.showMaximized()
    sys.exit(app.exec())
