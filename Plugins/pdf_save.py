from PySide6.QtCore import (QDir)
from PySide6.QtGui import (QIcon,
                           QAction)
from PySide6.QtWidgets import (QFileDialog)

import os


class Plugin:
    NAME = 'pdfPlugin'
    AUTHOR = 'Artik'
    VERSION = '0.1'
    TITLE = 'Сохранение в PDF'
    CAPTION = 'Сохранить в PDF'

    def __init__(self, main_window):
        self.main_window = main_window
        self.savePdfPluginsAction = QAction()
        self.savePdfPluginsAction.setObjectName('createTablePluginsAction')
        self.savePdfPluginsAction.setText(self.TITLE)
        self.savePdfPluginsAction.setCheckable(True)
        self.savePdfPluginsAction.setChecked(True)

        self.savePdfToolsAction = QAction()
        self.savePdfToolsAction.setIcon(QIcon(':pdf-2.png'))
        self.savePdfToolsAction.setObjectName('createTableToolsAction')
        self.savePdfToolsAction.setText(self.CAPTION)
        self.savePdfPluginsAction.changed.connect(self.check_changed)
        self.savePdfToolsAction.triggered.connect(self.save_pdf)

    def check_changed(self):
        check = self.savePdfPluginsAction.isChecked()
        self.savePdfToolsAction.setVisible(check)

    def save_pdf(self):
        self.main_window.update_page()
        file, _ = QFileDialog.getSaveFileName(parent=self.main_window,
                                              caption='Сохранить в pdf',
                                              dir=os.path.join(QDir.homePath(), 'Documents'),
                                              filter="PDF (*.pdf)")
        if file:
            self.main_window.ui.web.page().printToPdf(file)

    def get_description(self):
        d = {
            'pluginsAction': self.savePdfPluginsAction,
            'toolsActions': {
                'savePdfToolsAction': self.savePdfToolsAction
            }
        }
        return d
