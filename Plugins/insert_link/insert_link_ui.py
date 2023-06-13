# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'insert_link.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFormLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)
import qrc_resources

class Ui_linkDialog(object):
    def setupUi(self, linkDialog):
        if not linkDialog.objectName():
            linkDialog.setObjectName(u"linkDialog")
        linkDialog.resize(452, 129)
        icon = QIcon(QIcon.fromTheme(u"insert-link.png"))
        linkDialog.setWindowIcon(icon)
        self.formLayout = QFormLayout(linkDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(linkDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.linkEdit = QLineEdit(linkDialog)
        self.linkEdit.setObjectName(u"linkEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.linkEdit)

        self.acceptButton = QPushButton(linkDialog)
        self.acceptButton.setObjectName(u"acceptButton")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.acceptButton)

        self.blankCheck = QCheckBox(linkDialog)
        self.blankCheck.setObjectName(u"blankCheck")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.blankCheck)

        self.label_2 = QLabel(linkDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.valueEdit = QLineEdit(linkDialog)
        self.valueEdit.setObjectName(u"valueEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.valueEdit)


        self.retranslateUi(linkDialog)

        QMetaObject.connectSlotsByName(linkDialog)
    # setupUi

    def retranslateUi(self, linkDialog):
        linkDialog.setWindowTitle(QCoreApplication.translate("linkDialog", u"\u0412\u0441\u0442\u0430\u0432\u043a\u0430 \u0441\u0441\u044b\u043b\u043a\u0438", None))
        self.label.setText(QCoreApplication.translate("linkDialog", u"\u0421\u0441\u044b\u043b\u043a\u0430", None))
        self.acceptButton.setText(QCoreApplication.translate("linkDialog", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.blankCheck.setText(QCoreApplication.translate("linkDialog", u"\u0412 \u043d\u043e\u0432\u043e\u043c \u043e\u043a\u043d\u0435", None))
        self.label_2.setText(QCoreApplication.translate("linkDialog", u"\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435", None))
    # retranslateUi

