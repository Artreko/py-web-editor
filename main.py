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
from tag_dialog import TagDialog

sys.path.extend(['UI', 'Plugins'])

from UI.mainwindow import MainWindow
from tag_dialog import TagDialog

class NewWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MainWindow()
        self.ui.setupUi(self)
        self.init_signals()

        self.filename = ''
        self.is_new = True
        self.file_open_dialog = QFileDialog(self)
        self.file_save_dialog = QFileDialog(self)
        self.file_dialog_config()

        self.load_page('index.html')

        self.write_mode = [self.ui.plainTextEdit.appendPlainText]
        self.set_write_mode()

        self.PATH_WITH_PLUGINS = 'Plugins'
        self.REQUIRED_FIELDS = ['NAME', 'VERSION', 'AUTHOR', 'TITLE', 'CAPTION', 'get_description']
        files = self.get_py_files()
        modules = self.get_modules(files)
        self.plugins = list(self.check_plugins(modules))
        for plugin in self.plugins:
            d = plugin.get_description()
            self.ui.pluginsMenu.addAction(d['pluginsAction'])
            for key, action in d['toolsActions'].items():
                self.ui.toolsMenu.addAction(action)

    def file_dialog_config(self):
        file_filter = 'HTML (*.html)'
        base_dir = os.path.join(QDir.homePath(), 'Documents')

        self.file_open_dialog.setNameFilter(file_filter)
        self.file_open_dialog.setDirectory(base_dir)

        self.file_save_dialog.setDirectory(base_dir)
        self.file_save_dialog.setNameFilter(file_filter)
        self.file_save_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)

    def init_signals(self):
        self.ui.saveFileAction.triggered.connect(self.save_file)
        self.ui.saveAsFileAction.triggered.connect(self.save_as_file)
        self.ui.openFileAction.triggered.connect(self.open_file)        
        self.ui.createFileAction.triggered.connect(self.create_file)
        self.ui.updateEditAction.triggered.connect(self.update_page)
        self.ui.exitFileAction.triggered.connect(self.close)

        self.ui.tagEditAction.triggered.connect(self.insert_tag)

        self.ui.insertSettingsAction.changed.connect(self.insert_changed)
        self.ui.appendSettingsAction.changed.connect(self.append_changed)

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

    def insert_changed(self):
        self.ui.appendSettingsAction.setChecked(not self.ui.insertSettingsAction.isChecked())

    def set_write_mode(self):
        write_mode = self.ui.plainTextEdit.appendPlainText \
            if self.ui.appendSettingsAction.isChecked() \
            else self.ui.plainTextEdit.insertPlainText
        self.write_mode.pop()
        self.write_mode.append(write_mode)

    def append_changed(self):
        self.ui.insertSettingsAction.setChecked(not self.ui.appendSettingsAction.isChecked())
        self.set_write_mode()

    def insert_tag(self):
        self.write_mode[0](TagDialog.get_tag())


    def get_py_files(self) -> Generator[str, None, None]:
        """Получаем все файлы из папки"""
        for file in os.listdir(self.PATH_WITH_PLUGINS):
            # Отбрасываем все файлы, которые заканчиваются не на .py
            if file[-3:] != '.py':
                continue
            yield file[:-3]

    def get_modules(self, files: Iterable[str]) -> Generator[object, None, None]:
        """Получаем модули из файлов"""
        for file in files:
            module = __import__(f'{self.PATH_WITH_PLUGINS}.{file}')
            module = getattr(module, file)
            # Если в модуле нет класса Plugin, пропускаем
            if not hasattr(module, 'Plugin'):
                print(file, 'Модуль не имеет класса Plugin')
                continue
            yield getattr(module, 'Plugin')(self.write_mode)

    def check_plugins(self, modules: Iterable[object]):
        """Проверяем, чтоб в модуле были нужные переменные и функции"""
        for module in modules:
            # Если хоть какого-то эллемента из массива REQUIRED_FIELDS нет - пропускаем
            if not all([hasattr(module, field) for field in self.REQUIRED_FIELDS]):
                print(module, 'Модуль не имеет нужных полей')
                continue
            yield module


if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, '')
    app = QApplication([])

    widget = NewWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
