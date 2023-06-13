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
    QWidget, QFileDialog, QMessageBox, QDialog, QFormLayout)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEnginePage
from UI.font_form_ui import Ui_FontDialog
import qrc_resources
from color_button import ColorButton
class FontDialogUI(Ui_FontDialog):
    def setupUi(self, FontDialog):
        super().setupUi(FontDialog)
        FontDialog.setWindowIcon(QIcon.fromTheme(':font.png'))
        self.colorButton = ColorButton(color='#000000')
        self.formLayout.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.colorButton)

    def retranslateUi(self, linkDialog):
        super().retranslateUi(linkDialog)


class FontDialog(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.ui = FontDialogUI()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon.fromTheme(':font.png'))
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
    def get_font(parent=None):
        d = FontDialog(parent)
        if d.exec():
            result = '<span '
            result += f'style="' \
                      f'font: {d.ui.sizeSpin.value()}px ' \
                      f'\'{d.ui.fontBox.currentFont().family()}\'; ' \
                      f'color: {d.ui.colorButton.color()};"'
            result += '>' + d.value + '</span>'
            return result
