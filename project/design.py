
################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(606, 298)
        icon = QIcon()
        icon.addFile(u":/logo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget{\n"
"	background-color: white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: white;\n"
"	background-color: black;\n"
"	border-radius: 8px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	border-radius: 7px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/logo/Dive in 2-logos_transparent.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(64, 64))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.send_2 = QPushButton(self.centralwidget)
        self.send_2.setObjectName(u"send_2")
        self.send_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.send_2.setStyleSheet(u"QPushButton{\n"
"	border-radius: 4px;\n"
"	background-color: black;\n"
"	color: white;\n"
"	padding: 5px;\n"
"}")

        self.horizontalLayout.addWidget(self.send_2)

        self.send_3 = QPushButton(self.centralwidget)
        self.send_3.setObjectName(u"send_3")
        self.send_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.send_3.setStyleSheet(u"QPushButton{\n"
"	border-radius: 4px;\n"
"	background-color: black;\n"
"	color: white;\n"
"	padding: 5px;\n"
"}")

        self.horizontalLayout.addWidget(self.send_3)

        self.url = QLineEdit(self.centralwidget)
        self.url.setObjectName(u"url")
        self.url.setMinimumSize(QSize(0, 23))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.url.setFont(font)

        self.horizontalLayout.addWidget(self.url)

        self.send = QPushButton(self.centralwidget)
        self.send.setObjectName(u"send")
        self.send.setCursor(QCursor(Qt.PointingHandCursor))
        self.send.setStyleSheet(u"QPushButton{\n"
"	border-radius: 4px;\n"
"	background-color: black;\n"
"	color: white;\n"
"	padding: 5px;\n"
"}")

        self.horizontalLayout.addWidget(self.send)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.webEngineView = QWebEngineView(self.centralwidget)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setUrl(QUrl(u"https://www.google.com/"))

        self.verticalLayout_3.addWidget(self.webEngineView)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DiveIn2", None))
        self.pushButton_2.setText("")
        self.send_2.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.send_3.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.url.setPlaceholderText(QCoreApplication.translate("MainWindow", u"URL \u0438\u043b\u0438 \u041d\u0430\u0437\u0432\u0430\u043d\u0438\u044f \u0421\u0430\u0439\u0442\u0430", None))
        self.send.setText(QCoreApplication.translate("MainWindow", u"Search", None))
#if QT_CONFIG(shortcut)
        self.send.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

