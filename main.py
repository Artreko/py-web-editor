import datetime
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
    QTransform, QTextCursor)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QSizePolicy, QStatusBar,
    QWidget, QFileDialog, QMessageBox, QDialog, QToolBar)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEnginePage
from tag_dialog import TagDialog

sys.path.extend(['UI', 'Plugins'])

from UI.mainwindow import MainWindow
from tag_dialog import TagDialog
from key_dialog import KeyDialog


class NewWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MainWindow()
        self.ui.setupUi(self)
        self.init_signals()

        self.is_auth = True
        self.user_data = ('unauthenticated user', datetime.datetime.now())

        self.ui.pluginsMenu.setEnabled(self.is_auth)
        self.ui.toolsMenu.setEnabled(self.is_auth)

        self.filename = ''
        self.is_new = True
        self.file_open_dialog = QFileDialog(self)
        self.file_save_dialog = QFileDialog(self)
        self.file_dialog_config()

        self.load_page('index.html')

        self.write_mode = self.ui.plainTextEdit.insertPlainText
        self.set_write_mode()

        self.PATHS_WITH_PLUGINS = ['Plugins']
        self.REQUIRED_FIELDS = ['NAME', 'VERSION', 'AUTHOR', 'TITLE', 'CAPTION', 'get_description']
        self.plugins = []

        self.load_plugins()

        # self.ui.plainTextEdit.find()

        self.fileToolBar = QToolBar(self)
        for action in self.ui.fileMenu.actions()[:-1]:
            self.fileToolBar.addAction(action)
        self.addToolBar(self.fileToolBar)
        self.editToolBar = QToolBar(self)
        for action in self.ui.editMenu.actions():
            if action.icon():
                self.editToolBar.addAction(action)
        self.addToolBar(self.editToolBar)
        self.toolsToolBar = QToolBar(self)
        for action in self.ui.toolsMenu.actions():
            if action.icon():
                self.toolsToolBar.addAction(action)
        self.addToolBar(self.toolsToolBar)

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

        self.ui.authSettingsAction.triggered.connect(self.get_auth)
        self.ui.viewSettingsAction.changed.connect(self.view_setting_changed)

        self.ui.ction.triggered.connect(self.move_cursor_to_end)

    def load_page(self, filename: str):
        self.load_text(filename)
        self.update_page()

    def update_page(self):
        html = self.ui.plainTextEdit.toPlainText()
        self.ui.web.setHtml(html, baseUrl='C:/')

    def load_text(self, filename: str):
        with open(filename, encoding='utf-8') as f:
            text = f.read()
            self.ui.plainTextEdit.setPlainText(text)
    
    def open_file(self):
        if self.file_open_dialog.exec():
            filenames = self.file_open_dialog.selectedFiles()
            self.filename = filenames[0]
            self.load_page(self.filename)
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
        self.write_mode = self.insert_to_end \
            if self.ui.appendSettingsAction.isChecked() \
            else self.ui.plainTextEdit.insertPlainText

    def append_changed(self):
        self.ui.insertSettingsAction.setChecked(not self.ui.appendSettingsAction.isChecked())
        self.set_write_mode()

    def insert_tag(self):
        self.write_mode(TagDialog.get_tag())

    def load_plugins(self):
        files = self.get_py_files()
        modules = self.get_modules(files)
        self.plugins = [*self.check_plugins(modules)]
        for plugin in self.plugins:
            d = plugin.get_description()
            self.ui.pluginsMenu.addAction(d['pluginsAction'])
            for key, action in d['toolsActions'].items():
                self.ui.toolsMenu.addAction(action)

    def get_py_files(self) -> Generator[tuple[str], None, None]:
        """Получаем все файлы из папки"""
        for path in self.PATHS_WITH_PLUGINS:
            for file in os.listdir(path):
                # Отбрасываем все файлы, которые заканчиваются не на .py
                if file.find('.') == -1:
                    yield path, file
                    continue
                if file[-3:] != '.py':
                    continue
                yield path, file[:-3]


    def get_modules(self, files: Iterable[tuple[str]]) -> Generator[object, None, None]:
        """Получаем модули из файлов"""
        # print(*files)
        for file in files:
            module = __import__(f'{file[0]}.{file[1]}')
            module = getattr(module, file[1])
            # Если в модуле нет класса Plugin, пропускаем
            if not hasattr(module, 'Plugin'):
                print(file, 'Модуль не имеет класса Plugin')
                continue
            yield getattr(module, 'Plugin')(self)

    def check_plugins(self, modules: Iterable[object]):
        """Проверяем, чтоб в модуле были нужные переменные и функции"""
        for module in modules:
            # Если хоть какого-то эллемента из массива REQUIRED_FIELDS нет - пропускаем
            if not all([hasattr(module, field) for field in self.REQUIRED_FIELDS]):
                print(module, 'Модуль не имеет нужных полей')
                continue
            yield module

    def get_auth(self):
        if not self.is_auth:
            if user_drive := KeyDialog.get_drive():
                self.user_data = user_drive
                self.is_auth = True
                self.ui.toolsMenu.setEnabled(True)
                self.ui.pluginsMenu.setEnabled(True)
        else:
            mbx = QMessageBox(self)
            mbx.setWindowTitle('Данные пользователя')
            mbx.setText(f'Пользователь {self.user_data[0]}\n'
                        f'Ключ действителен до {self.user_data[1].strftime("%X %x")}')
            mbx.show()

    def view_setting_changed(self):
        if self.ui.viewSettingsAction.isChecked():
            self.ui.web.show()
        else:
            self.ui.web.hide()

    def move_cursor_to_end(self):
        self.ui.plainTextEdit.find('</body>')
        self.ui.plainTextEdit.moveCursor(QTextCursor.MoveOperation.StartOfBlock)
        self.ui.plainTextEdit.textCursor().insertBlock()
        self.ui.plainTextEdit.moveCursor(QTextCursor.MoveOperation.PreviousBlock)

    def insert_to_end(self, text):
        self.move_cursor_to_end()
        self.ui.plainTextEdit.insertPlainText(text)

if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, '')
    app = QApplication([])

    widget = NewWidget()
    widget.resize(800, 600)
    widget.showMaximized()

    sys.exit(app.exec())
