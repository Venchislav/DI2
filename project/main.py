import sys
import datetime
from PySide6.QtWidgets import QApplication, QMainWindow
from pygame import mixer
from design import Ui_MainWindow
import PySide6
from PyQt6 import QtCore


class DD(QMainWindow):
    def __init__(self):
        super(DD, self).__init__()
        self.searchs = []
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.send.clicked.connect(self.search)

        self.ui.send_2.clicked.connect(self.backed)
        self.ui.send_3.clicked.connect(self.fwed)

    def search(self):
        link = f"{self.ui.url.text()}"
        self.ui.webEngineView.load(f"https://www.google.com/search?q={link}")
        self.searchs.append(link)
        self.back = self.searchs[:]
        self.fw = self.searchs[:]
        print(self.searchs)

    def backed(self):
        try:
            b = self.back.pop(-2)
            self.ui.webEngineView.load(f"https://www.google.com/search?q={b}")
            self.ui.url.setText(b)
            self.fw.append(b)
        except IndexError:
            pass

    def fwed(self):
        try:
            b1 = self.fw.pop(1)
            self.ui.webEngineView.load(f"https://www.google.com/search?q={b1}")
            self.ui.url.setText(b1)
        except IndexError:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DD()
    window.show()

    sys.exit(app.exec())
