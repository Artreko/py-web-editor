from PySide6.QtCore import (QDir)
from PySide6.QtGui import (QIcon,
                           QAction)
from PySide6.QtWidgets import (QDialog, QFileDialog)

import os
from .img_dialog import InsertImageDialog


class Plugin:
    NAME = 'insertImagePlugin'
    AUTHOR = 'Artik'
    VERSION = '0.1'
    TITLE = 'Втавка картинок'
    CAPTION = 'Вставка картинок'

    def __init__(self, main_window):

        self.main_window = main_window
        self.insertImagePluginsAction = QAction()
        self.insertImagePluginsAction.setObjectName('createTablePluginsAction')
        self.insertImagePluginsAction.setText(self.TITLE)
        self.insertImagePluginsAction.setCheckable(True)
        self.insertImagePluginsAction.setChecked(True)

        self.insertImageToolsAction = QAction()
        self.insertImageToolsAction.setIcon(QIcon(':insert-image.png'))
        self.insertImageToolsAction.setObjectName('insertImageToolsAction')
        self.insertImageToolsAction.setText('Вставить картинку')
        self.insertImagePluginsAction.changed.connect(self.check_changed)
        self.insertImageToolsAction.triggered.connect(self.create_table)

    def check_changed(self):
        check = self.insertImagePluginsAction.isChecked()
        self.insertImageToolsAction.setVisible(check)

    def create_table(self):
        self.main_window.write_mode(InsertImageDialog.get_img())

    def get_description(self):
        d = {
            'pluginsAction': self.insertImagePluginsAction,
            'toolsActions': {
                'insertImageToolsAction': self.insertImageToolsAction
            }
        }
        return d
