import sys
import os
from PySide6 import QtCore, QtWidgets, QtGui

class NewWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('New Widget')
        self.text = QtWidgets.QLabel(os.getcwd(),
                                     alignment=QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = NewWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())