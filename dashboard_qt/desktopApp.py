from PySide2 import QtWidgets, QtCore, QtWebEngineWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("QWidget{background-color: #343a40;}")

        self.main_layout = QtWidgets.QGridLayout(self)

        self.qline_edit = QtWidgets.QLineEdit(self)        
        self.qline_edit.setStyleSheet("color: white;")

        self.spin = QtWidgets.QSpinBox()
        self.spin.setValue(30)
        self.spin.setRange(7, 1200)

        self.btn_refresh = QtWidgets.QPushButton("Refresh")
        self.btn_refresh.clicked.connect(self.refresh)

        self.spin.setStyleSheet("color: white;")
        self.btn_refresh.setStyleSheet("color: white;")
        self.btn_refresh.setFlat(True)

        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view.load(QtCore.QUrl("http://127.0.0.1:8000"))

        self.setWindowTitle("Tableau de bord - Devise")

        self.main_layout.addWidget(self.spin, 0, 0, 1, 1)
        self.main_layout.addWidget(self.qline_edit, 0, 1, 1, 1)        
        self.main_layout.addWidget(self.btn_refresh, 0, 2, 1, 1)
        self.main_layout.addWidget(self.view, 2, 0, 1, 3)

    def refresh(self):
        days = self.spin.value()
        currencies = self.qline_edit.text().upper()
        self.view.load(QtCore.QUrl(f"http://127.0.0.1:8000/days={days}&currencies={currencies}"))


app = QtWidgets.QApplication([])
win = Window()
# win.showFullScreen()
win.show()
app.exec_()