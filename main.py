from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = QApplication([])

wind_main = QWidget()
wind_main.resize(600,500)
wind_main.setWindowTitle("Memory Card")
wind_main.move(300,300)

wind_main.show()
app.exec()