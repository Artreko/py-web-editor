from UI.tag_form_ui import Ui_tagDialog

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


class TagDialog(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_tagDialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.value = ''
        if parent.ui.insertSettingsAction.isChecked():
            if parent.ui.plainTextEdit.textCursor().hasSelection():
                self.value = parent.ui.plainTextEdit.textCursor().selectedText()
        self.ui.acceptButton.clicked.connect(self.accept_button_clicked)

    def accept_button_clicked(self):
        self.accept()
        self.close()

    @staticmethod
    def get_tag(parent=None):
        tag_dialog = TagDialog(parent)
        if tag_dialog.exec():
            tag = tag_dialog.ui.tagEdit.text().strip()
            check = tag_dialog.ui.pairTagButton.isChecked()
            class_ = tag_dialog.ui.classEdit.text()
            id_ = tag_dialog.ui.idEdit.text()
            result = f'<{tag}'
            if id_:
                result += f' id="{id_}"'
            if class_:
                result += f' class="{class_}"'
            result += '>' + tag_dialog.value
            if check:
                result += f'</{tag}>'
            return result
