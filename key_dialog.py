from UI.key_dialog_ui import Ui_Dialog
from check_key.check_key import read_file
from datetime import datetime, timedelta
import wmi
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
    QWidget, QFileDialog, QMessageBox, QDialog, QTableWidgetItem)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEnginePage
import qrc_resources


class KeyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon.fromTheme(':key.png'))
        self.ui.searchButton.clicked.connect(self.search_button_clicked)
        self.ui.reSearchButton.clicked.connect(self.search_button_clicked)
        self.ui.diskChooseButton.clicked.connect(self.disc_choose_button_clicked)

        self.ui.searchFailureLabel.hide()
        self.ui.diskTableFrame.hide()

        self.filename = 'secret.key'
        self.table_columns = ['id', 'name', 'status', 'owner', 'end_time']
        self.statuses = ('Нет доступа', 'Доступ истек', 'Есть доступ')
        self.drives = [dict]

    def get_drives(self) -> bool:
        w = wmi.WMI()
        self.drives = [{'id': drive.Name,
                        'name': drive.VolumeName or 'USB-накопитель',
                        'status': self.statuses[0],
                        'owner': None,
                        'level': 0,
                        'end_time': None,
                        'serial_number': drive.VolumeSerialNumber,
                        'access': False,
                        'access_by_time': False,
                        }
                       for drive in w.Win32_LogicalDisk()
                       if drive.DriveType == 2]
        if not self.drives:
            return False
        return True

    def get_drives_statuses(self):
        for drive in self.drives:
            try:
                if self.filename in os.listdir(drive['id']):
                    drive['access'] = True
                    key = read_file(fr'{drive["id"]}\{self.filename}',
                                    drive['serial_number'])
                    drive['owner'] = key['owner']
                    drive['level'] = key['level']
                    drive['end_time'] = \
                        datetime.strptime(key['date_creation'], '%Y-%m-%d %H:%M:%S.%f') + \
                        timedelta(minutes=key['lifetime'])
                    if drive['end_time'] > datetime.now():
                        drive['access_by_time'] = True
                    drive['status'] = \
                        self.statuses[int(drive['access']) << int(drive['access_by_time'])]
            except PermissionError:
                continue

    def search_button_clicked(self):
        self.ui.searchFailureLabel.hide()
        if not self.get_drives():
            self.ui.searchFailureLabel.show()
            self.ui.startFrame.show()
            return None
        self.get_drives_statuses()
        # print(*self.drives, sep='\n')
        self.ui.diskTable.clearContents()
        self.ui.diskTable.setRowCount(len(self.drives))
        for row, drive in enumerate(self.drives):
            for col, key in enumerate(self.table_columns):
                value = drive[key] or ''
                value = value if type(value) == str else value.strftime('%X %x')
                item = QTableWidgetItem(value)
                self.ui.diskTable.setItem(row, col, item)
        self.ui.diskTable.resizeColumnsToContents()
        self.ui.diskTableFrame.show()
        self.ui.startFrame.hide()

    def disc_choose_button_clicked(self):
        drive = self.drives[self.ui.diskTable.currentRow()]
        if not drive['access_by_time']:
            QMessageBox.critical(self, 'Отказано в доступе', 'Вы не можете получить доступ к программе!')
            return None
        self.selected_drive = drive
        self.accept()
        self.close()

    def cancel_button_clicked(self):
        self.search_button_clicked()


    @staticmethod
    def get_drive():
        dialog = KeyDialog()
        if dialog.exec():
            return dialog.selected_drive['owner'], dialog.selected_drive['end_time']