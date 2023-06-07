import sys
import locale
import importlib
import os
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

sys.path.extend(['UI', 'Plugins'])

from UI.mainwindow import MainWindow


class NewWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MainWindow()
        self.ui.setupUi(self)
        self.init_actions()

        self.filename = ''
        self.is_new = True
        self.file_open_dialog = QFileDialog(self)
        self.file_save_dialog = QFileDialog(self)
        self.file_dialog_config()

        self.load_page('index.html')

    def file_dialog_config(self):
        file_filter = 'HTML (*.html)'
        base_dir = os.path.join(QDir.homePath(), 'Documents')

        self.file_open_dialog.setNameFilter(file_filter)
        self.file_open_dialog.setDirectory(base_dir)

        self.file_save_dialog.setDirectory(base_dir)
        self.file_save_dialog.setNameFilter(file_filter)
        self.file_save_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)

    def init_actions(self):
        self.ui.saveFileAction.triggered.connect(self.save_file)
        self.ui.saveAsFileAction.triggered.connect(self.save_as_file)
        self.ui.openFileAction.triggered.connect(self.open_file)        
        self.ui.createFileAction.triggered.connect(self.create_file)
        self.ui.updateEditAction.triggered.connect(self.update_page)

    def load_page(self, filename: str):
        self.load_text(filename)
        self.update_page()

    def update_page(self):
        html = self.ui.plainTextEdit.toPlainText()
        self.ui.web.setHtml(html)

    def load_text(self, filename: str):
        with open(filename, encoding='utf-8') as f:
            text = f.read()
            self.ui.plainTextEdit.setPlainText(text)
    
    def open_file(self):
        if self.file_open_dialog.exec():
            filenames = self.file_open_dialog.selectedFiles()
            filename = filenames[0]
            self.load_page(filename)
            self.is_new = False
    
    def create_file(self): 
        self.ui.plainTextEdit.setPlainText('')
        self.ui.web.setHtml('')
        self.filename = ''
        self.is_new = True
    
    def set_save_filename(self):
        if not self.filename:
            dir_path = (QDir.homePath(), 'Documents')
            dir_path = os.path.join(*dir_path)
            self.file_save_dialog.setDirectory(dir_path)
            self.file_save_dialog.selectFile('new.html')
            # print(self.file_save_dialog.directory())
        else:
            file_dir = os.path.dirname(self.filename)
            file_name = os.path.basename(self.filename)
            self.file_save_dialog.setDirectory(file_dir)
            self.file_save_dialog.selectFile(file_name)
        if self.file_save_dialog.exec() == QDialog.DialogCode.Accepted:
            self.filename = self.file_save_dialog.selectedFiles()[0]

    def save_(self):
        if self.filename:
            with open(self.filename, 'w', encoding='utf-8') as f:
                f.write(self.ui.plainTextEdit.toPlainText())
            self.load_page(self.filename)
        
    def save_file(self):
        if self.is_new:
            self.set_save_filename()
        self.save_()
        self.is_new = False

    def save_as_file(self):
        self.set_save_filename()
        self.save_()
        self.is_new = False
        

if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, '')
    app = QApplication([])

    widget = NewWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
