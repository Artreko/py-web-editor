from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QAction)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGridLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget, QAbstractItemView)
import qrc_resources
from .create_table_dialog import CreateTableDialog


class Plugin:
    NAME = 'createTablePlugin'
    AUTHOR = 'Artik'
    VERSION = '0.1'
    TITLE = 'Создание таблиц'
    CAPTION = 'Создание таблиц'

    def __init__(self, main_window):

        self.main_window = main_window
        self.createTablePluginsAction = QAction()
        self.createTablePluginsAction.setObjectName('createTablePluginsAction')
        self.createTablePluginsAction.setText(self.TITLE)
        self.createTablePluginsAction.setCheckable(True)
        self.createTablePluginsAction.setChecked(True)

        self.createTableToolsAction = QAction()
        self.createTableToolsAction.setIcon(QIcon(':insert-table'))
        self.createTableToolsAction.setObjectName('createTableToolsAction')
        self.createTableToolsAction.setText('Создать таблицу')
        self.createTablePluginsAction.changed.connect(self.check_changed)
        self.createTableToolsAction.triggered.connect(self.create_table)

    def check_changed(self):
        check = self.createTablePluginsAction.isChecked()
        self.createTableToolsAction.setVisible(check)

    def create_table(self):
        self.main_window.write_mode(CreateTableDialog.get_table())

    def get_description(self):
        d = {
            'pluginsAction': self.createTablePluginsAction,
            'toolsActions': {
                'createTableToolsAction': self.createTableToolsAction
            }
        }
        return d
