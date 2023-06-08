# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(890, 706)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.openFileAction = QAction(MainWindow)
        self.openFileAction.setObjectName(u"openFileAction")
        self.createFileAction = QAction(MainWindow)
        self.createFileAction.setObjectName(u"createFileAction")
        self.saveFileAction = QAction(MainWindow)
        self.saveFileAction.setObjectName(u"saveFileAction")
        self.saveAsFileAction = QAction(MainWindow)
        self.saveAsFileAction.setObjectName(u"saveAsFileAction")
        self.reloadPluginsAction = QAction(MainWindow)
        self.reloadPluginsAction.setObjectName(u"reloadPluginsAction")
        self.loadPluginsAction = QAction(MainWindow)
        self.loadPluginsAction.setObjectName(u"loadPluginsAction")
        self.insertSettingsAction = QAction(MainWindow)
        self.insertSettingsAction.setObjectName(u"insertSettingsAction")
        self.insertSettingsAction.setCheckable(True)
        self.insertSettingsAction.setChecked(True)
        self.appendSettingsAction = QAction(MainWindow)
        self.appendSettingsAction.setObjectName(u"appendSettingsAction")
        self.appendSettingsAction.setCheckable(True)
        self.settingsAction = QAction(MainWindow)
        self.settingsAction.setObjectName(u"settingsAction")
        self.exitFileAction = QAction(MainWindow)
        self.exitFileAction.setObjectName(u"exitFileAction")
        self.updateEditAction = QAction(MainWindow)
        self.updateEditAction.setObjectName(u"updateEditAction")
        self.tagEditAction = QAction(MainWindow)
        self.tagEditAction.setObjectName(u"tagEditAction")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.horizontalLayout.addWidget(self.plainTextEdit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 890, 26))
        self.fileMenu = QMenu(self.menubar)
        self.fileMenu.setObjectName(u"fileMenu")
        self.toolsMenu = QMenu(self.menubar)
        self.toolsMenu.setObjectName(u"toolsMenu")
        self.pluginsMenu = QMenu(self.menubar)
        self.pluginsMenu.setObjectName(u"pluginsMenu")
        self.pluginsLoadMenu = QMenu(self.pluginsMenu)
        self.pluginsLoadMenu.setObjectName(u"pluginsLoadMenu")
        self.pluginsLoadMenu.setEnabled(True)
        self.settingsMenu = QMenu(self.menubar)
        self.settingsMenu.setObjectName(u"settingsMenu")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.fileMenu.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.toolsMenu.menuAction())
        self.menubar.addAction(self.pluginsMenu.menuAction())
        self.menubar.addAction(self.settingsMenu.menuAction())
        self.fileMenu.addAction(self.openFileAction)
        self.fileMenu.addAction(self.createFileAction)
        self.fileMenu.addAction(self.saveFileAction)
        self.fileMenu.addAction(self.saveAsFileAction)
        self.fileMenu.addAction(self.exitFileAction)
        self.pluginsMenu.addAction(self.pluginsLoadMenu.menuAction())
        self.pluginsMenu.addSeparator()
        self.pluginsLoadMenu.addAction(self.reloadPluginsAction)
        self.pluginsLoadMenu.addAction(self.loadPluginsAction)
        self.settingsMenu.addAction(self.insertSettingsAction)
        self.settingsMenu.addAction(self.appendSettingsAction)
        self.settingsMenu.addSeparator()
        self.settingsMenu.addAction(self.settingsAction)
        self.menu.addAction(self.updateEditAction)
        self.menu.addAction(self.tagEditAction)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyWebEditor", None))
        self.openFileAction.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.openFileAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.createFileAction.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.createFileAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.saveFileAction.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.saveFileAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.saveAsFileAction.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a", None))
        self.reloadPluginsAction.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.loadPluginsAction.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c", None))
        self.insertSettingsAction.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0430\u0432\u043a\u0430", None))
        self.appendSettingsAction.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435", None))
        self.settingsAction.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.exitFileAction.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.updateEditAction.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.updateEditAction.setShortcut(QCoreApplication.translate("MainWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.tagEditAction.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0442\u0435\u0433", None))
        self.fileMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.toolsMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b", None))
        self.pluginsMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u0433\u0438\u043d\u044b", None))
        self.pluginsLoadMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.settingsMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440", None))
    # retranslateUi

