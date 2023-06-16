from .insert_link_ui import Ui_linkDialog
import sys
import locale
import importlib
import os
from typing import Generator, Iterable
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QDir,
    QSize, QTime, QUrl, Qt, qDebug, Slot, QLocale)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QSizePolicy, QStatusBar,
    QWidget, QFileDialog, QMessageBox, QDialog)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEnginePage
class LinkDialogUI(Ui_linkDialog):
    def setupUi(self, linkDialog):
        super().setupUi(linkDialog)

    def retranslateUi(self, linkDialog):
        super().retranslateUi(linkDialog)


class LinkDialog(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.ui = LinkDialogUI()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(':insert-link.png'))
        self.parent = parent
        self.value = ''
        if parent.ui.insertSettingsAction.isChecked():
            if parent.ui.plainTextEdit.textCursor().hasSelection():
                self.ui.valueEdit.setText(parent.ui.plainTextEdit.textCursor().selectedText())
        self.ui.acceptButton.clicked.connect(self.accept_button_clicked)

    def accept_button_clicked(self):
        self.accept()
        self.close()

    def get_link(parent=None):
        dialog = LinkDialog(parent)
        if dialog.exec():
            result = f'<a href="{dialog.ui.linkEdit.text()}"'
            if dialog.ui.blankCheck.isChecked():
                result += ' target="blank_"'
            result += '>' + dialog.ui.valueEdit.text() + '</a>'
            return result
