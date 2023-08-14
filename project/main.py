from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import sys


# main window
class MainWindow(QMainWindow):

    # constructor
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.tabs = QTabWidget()

        # making document mode true
        self.tabs.setDocumentMode(True)

        self.tabs.currentChanged.connect(self.current_tab_changed)

        self.tabs.setTabsClosable(True)

        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        self.setCentralWidget(self.tabs)

        self.status = QStatusBar()

        navtb = QToolBar("Navigation")

        self.addToolBar(navtb)



        # creating back action
        back_btn = QAction('', self)
        back_btn.setIcon(QIcon(r".\img\arrow.png"))

        # setting status tip
        back_btn.setStatusTip("Back to previous page")

        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())

        navtb.addAction(back_btn)

        next_btn = QAction("", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.setIcon(QIcon(r".\img\arrows.png"))
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        navtb.addAction(next_btn)

        reload_btn = QAction("", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.setIcon(QIcon(r'.\img\reload.png'))
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        navtb.addAction(reload_btn)

        home_btn = QAction("", self)
        home_btn.setStatusTip("Go home")
        home_btn.setIcon(QIcon('.\img\home.png'))

        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        self.urlbar = QLineEdit()

        # adding action to line edit when return key is pressed
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        self.urlbar.setPlaceholderText('URL или Название Сайта')

        navtb.addWidget(self.urlbar)

        stop_btn = QAction("", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.setIcon(QIcon('close.png'))
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        navtb.addAction(stop_btn)

        help = QAction("", self)
        help.setStatusTip("Q")
        help.setIcon(QIcon('.\img\doubts-button.png'))
        help.triggered.connect(self.help)
        navtb.addAction(help)


        logo = QAction("", self)
        logo.setIcon(QIcon(".\img\logo.png"))
        navtb.addAction(logo)

        # creating first tab
        self.add_new_tab(QUrl('https://duckduckgo.com/'), 'Homepage')

        self.showMaximized()

        # setting window title
        self.setWindowTitle("DI2")
        self.setWindowIcon(QIcon('.\img\logo.png'))

        _add = QAction("", self)
        _add.triggered.connect(self.tab_open_doubleclick)
        _add.setIcon(QIcon(r'.\img\add-button.png'))

        navtb.addAction(_add)

        self.setStyleSheet("""
				        QWidget{
							background-color: white;
						}
						QLineEdit{
							color: white;
							background-color: #202124;
							border-radius: 8px;
							height: 25px !important;
							font-size: 14px;
							font-weight: bold;
						}

						QHBoxLayout{
							background-color: black;
						}

						QToolButton{
							border-radius: 16px;
							background-color: #35363A;
							color: white;
							padding: 5px;
							margin: 5px;
							width: 19px !important;
    						height: 19px !important;
    						cursor: pointer;
						}

						QToolButton:hover{
							background-color: grey;
						}

						QToolBar#logo{
							border-radius: 16px;
							background-color: white;
							color: white;
							padding: 5px;
							margin: 5px;
							width: 19px !important;
    						height: 19px !important;
    						cursor: pointer;
						}

						QTabBar{
							border: none;
							background: #202124;
						}
						QTabBar::tab{
							background-color: #606164;
							border-radius: 5px;
							padding: 6px;
							margin: 5px;
							font-weight: bold;
							font-size: 12px;
							width: 90px;
						}
						QTabWidget{
							background-color: #35363A;
							border-radius: 8px;
						}
						QToolBar{
							background-color: #35363A;
						}
						QTabBar::close-button{
                            image: url(close.png);
                            padding-right: 5px;
                        }
                        QTabBar::close-button:hover{
                            image: url(cancel.png);
                            subcontrol-position: left;
                            padding-right: 5px;
                        }
				        """)

    def help(self):
        self.urlbar.setText('http://di2-proj-of.tilda.ws/help')
        self.navigate_to_url()

    def on_pushButton_clicked(self):
        self.dialog.show()


    def open_settings_dw(self):
        qa = QMainWindow()
        tb = QToolBar('settings')
        qa.addToolBar(tb)
        while not self.add_new_tab():
            qa.show()
            qa.setWindowTitle("DI2-Settings")

    def add_new_tab(self, qurl=None, label="Blank"):
        if qurl is None:
            qurl = QUrl('https://duckduckgo.com/')

        browser = QWebEngineView()
        browser.settings().setAttribute(
            QWebEngineSettings.FullScreenSupportEnabled, True
        )

        browser.setUrl(qurl)

        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        browser.urlChanged.connect(lambda qurl, browser=browser:
                                   self.update_urlbar(qurl, browser))

        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.tabs.setTabText(i, browser.page().title()))

        browser.page().fullScreenRequested.connect(
            lambda request, browser=browser: self.handle_fullscreen_requested(
                request, browser
            )
        )

    def handle_fullscreen_requested(self, request, browser):
        request.accept()

    def tab_open_doubleclick(self, i):
        self.add_new_tab()

    def current_tab_changed(self, i):
        qurl = self.tabs.currentWidget().url()
        self.update_urlbar(qurl, self.tabs.currentWidget())
        self.update_title(self.tabs.currentWidget())

    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            sys.exit(app.exec())

        page = self.tabs.widget(i)
        self.tabs.removeTab(i)
        page.deleteLater()

    def update_title(self, browser):
        if browser != self.tabs.currentWidget():
            return

        title = self.tabs.currentWidget().page().title()
        self.setWindowTitle("DI2 - " + title)

    def navigate_home(self):
        self.tabs.currentWidget().setUrl(QUrl("https://duckduckgo.com/"))

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")

        self.tabs.currentWidget().setUrl(q)

    def update_urlbar(self, q, browser=None):
        if browser != self.tabs.currentWidget():
            return

        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

        def _downloadRequested(item):
            print("downloading to", item)
            item.accept()

        browser.page().profile().downloadRequested.connect(_downloadRequested)


app = QApplication(sys.argv)

app.setApplicationName("DI2")

window = MainWindow()

app.exec_()
