from mainwindow_ui import Ui_MainWindow

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, qDebug, Slot, QLocale)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform, QFontMetricsF)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QSizePolicy, QStatusBar,
    QWidget, QFileDialog, QMessageBox, QToolBar)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEnginePage

import qrc_resources

class MainWindow(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.web = QWebEngineView(MainWindow)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.web.setSizePolicy(sizePolicy)
        self.web.settings().setDefaultTextEncoding('utf-8')
        self.web.setEnabled(False)
        self.horizontalLayout.addWidget(self.web)

        self.plainTextEdit.setTabStopDistance(
        QFontMetricsF(self.plainTextEdit.font()).horizontalAdvance(' ') * 4)



        self.openFileAction.setIcon(QIcon(':open-file.png'))
        self.createFileAction.setIcon(QIcon(':new-file.png'))
        self.saveFileAction.setIcon(QIcon(':save.png'))
        self.saveAsFileAction.setIcon(QIcon(':save-as.png'))
        self.exitFileAction.setIcon(QIcon(':close.png'))
        self.fontEditAction.setIcon(QIcon(':font.png'))
        self.tagEditAction.setIcon(QIcon(':tag.png'))
        self.updateEditAction.setIcon(QIcon(':update.png'))
        self.boldEditAction.setIcon(QIcon(':bold.png'))
        self.underlineEditAction.setIcon(QIcon(':underline.png'))
        self.italicEditAction.setIcon(QIcon(':italic.png'))


    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)
