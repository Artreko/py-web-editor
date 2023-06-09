# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_table.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFrame,
    QGridLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModal)
        Dialog.resize(494, 331)
        Dialog.setModal(True)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.rowSpin = QSpinBox(self.frame)
        self.rowSpin.setObjectName(u"rowSpin")

        self.verticalLayout_2.addWidget(self.rowSpin)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.colSpin = QSpinBox(self.frame)
        self.colSpin.setObjectName(u"colSpin")

        self.verticalLayout_2.addWidget(self.colSpin)

        self.nextButton = QPushButton(self.frame)
        self.nextButton.setObjectName(u"nextButton")

        self.verticalLayout_2.addWidget(self.nextButton)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.backButton = QPushButton(self.frame_2)
        self.backButton.setObjectName(u"backButton")

        self.gridLayout.addWidget(self.backButton, 1, 0, 1, 1)

        self.acceptButton = QPushButton(self.frame_2)
        self.acceptButton.setObjectName(u"acceptButton")

        self.gridLayout.addWidget(self.acceptButton, 1, 1, 1, 1)

        self.tableWidget = QTableWidget(self.frame_2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 2)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u0440\u043e\u043a", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u043e\u043b\u0431\u0446\u043e\u0432", None))
        self.nextButton.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.backButton.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.acceptButton.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
    # retranslateUi

