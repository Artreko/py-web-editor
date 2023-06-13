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
from .insert_link_dialog import LinkDialog

class Plugin:
    NAME = 'createTablePlugin'
    AUTHOR = 'Artik'
    VERSION = '0.1'
    TITLE = 'Вставка ссылок'
    CAPTION = 'Вставить ссылку'

    def __init__(self, main_window):

        self.main_window = main_window
        self.insertLinkPluginsAction = QAction()
        self.insertLinkPluginsAction.setObjectName('insertLinkPluginsAction')
        self.insertLinkPluginsAction.setText(self.TITLE)
        self.insertLinkPluginsAction.setCheckable(True)
        self.insertLinkPluginsAction.setChecked(True)

        self.insertLinkToolsAction = QAction()
        self.insertLinkToolsAction.setIcon(QIcon(':insert-link'))
        self.insertLinkToolsAction.setObjectName('insertLinkToolsAction')
        self.insertLinkToolsAction.setText('Вставить ссылку')
        self.insertLinkPluginsAction.changed.connect(self.check_changed)
        self.insertLinkToolsAction.triggered.connect(self.create_table)

    def check_changed(self):
        check = self.insertLinkPluginsAction.isChecked()
        self.insertLinkToolsAction.setVisible(check)

    def create_table(self):
        if link := LinkDialog.get_link(self.main_window):
            self.main_window.write_mode(link)

    def get_description(self):
        d = {
            'pluginsAction': self.insertLinkPluginsAction,
            'toolsActions': {
                'insertLinkToolsAction': self.insertLinkToolsAction
            }
        }
        return d
