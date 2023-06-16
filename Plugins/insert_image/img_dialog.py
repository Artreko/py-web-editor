from PySide6.QtWidgets import (QDialog, QFileDialog)
from PySide6.QtGui import QIcon
from PySide6.QtCore import QDir
from .img_dialog_ui import Ui_ImageDialog
import os
import qrc_resources

class InsertImageDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ImageDialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(':insert-image.png'))
        self.ui.acceptButton.clicked.connect(self.accept_button_clicked)
        self.ui.searchButton.clicked.connect(self.search_button_clicked)
        self.ui.label_5.setVisible(False)
        self.ui.label_2.setVisible(False)
        self.ui.classEdit.setVisible(False)


    def accept_button_clicked(self):
        self.accept()
        self.close()

    def search_button_clicked(self):
        file, filter = QFileDialog.getOpenFileName(self,
                                    dir=os.path.join(QDir.homePath(), 'Pictures'),
                                    filter='Image (*.jpg *.png)')
        if filter:
            self.ui.srcEdit.setText(file)

    @staticmethod
    def get_img():
        dialog = InsertImageDialog()
        if dialog.exec():
            src = dialog.ui.srcEdit.text()
            alt = dialog.ui.altEdit.text()
            class_ = dialog.ui.classEdit.text()
            height = dialog.ui.hSpin.value()
            width = dialog.ui.wSpin.value()
            result = f'<img src="{src}" alt="{alt}"'
            if class_:
                result += f' class="{class_}"'
            if height:
                result += f' height="{height}"'
            if width:
                result += f' width="{width}"'
            result += '>'
            return result

