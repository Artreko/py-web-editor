# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'img_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_ImageDialog(object):
    def setupUi(self, ImageDialog):
        if not ImageDialog.objectName():
            ImageDialog.setObjectName(u"ImageDialog")
        ImageDialog.resize(402, 249)
        self.formLayout = QFormLayout(ImageDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.label_5 = QLabel(ImageDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font-size:16px;")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_5)

        self.label = QLabel(ImageDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.srcEdit = QLineEdit(ImageDialog)
        self.srcEdit.setObjectName(u"srcEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.srcEdit)

        self.searchButton = QPushButton(ImageDialog)
        self.searchButton.setObjectName(u"searchButton")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.searchButton)

        self.label_2 = QLabel(ImageDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.classEdit = QLineEdit(ImageDialog)
        self.classEdit.setObjectName(u"classEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.classEdit)

        self.label_3 = QLabel(ImageDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_3)

        self.hSpin = QSpinBox(ImageDialog)
        self.hSpin.setObjectName(u"hSpin")
        self.hSpin.setMaximum(1000)
        self.hSpin.setSingleStep(50)
        self.hSpin.setValue(50)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.hSpin)

        self.label_4 = QLabel(ImageDialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_4)

        self.wSpin = QSpinBox(ImageDialog)
        self.wSpin.setObjectName(u"wSpin")
        self.wSpin.setMaximum(1000)
        self.wSpin.setSingleStep(50)
        self.wSpin.setValue(50)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.wSpin)

        self.acceptButton = QPushButton(ImageDialog)
        self.acceptButton.setObjectName(u"acceptButton")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.acceptButton)

        self.label_6 = QLabel(ImageDialog)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.altEdit = QLineEdit(ImageDialog)
        self.altEdit.setObjectName(u"altEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.altEdit)


        self.retranslateUi(ImageDialog)

        QMetaObject.connectSlotsByName(ImageDialog)
    # setupUi

    def retranslateUi(self, ImageDialog):
        ImageDialog.setWindowTitle(QCoreApplication.translate("ImageDialog", u"\u0412\u0441\u0442\u0430\u0432\u043a\u0430 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438", None))
        self.label_5.setText(QCoreApplication.translate("ImageDialog", u"<html><head/><body><p>\u0410\u0442\u0440\u0438\u0431\u0443\u0442\u044b &lt;img&gt;</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("ImageDialog", u"src", None))
        self.searchButton.setText(QCoreApplication.translate("ImageDialog", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.label_2.setText(QCoreApplication.translate("ImageDialog", u"class", None))
        self.label_3.setText(QCoreApplication.translate("ImageDialog", u"height", None))
        self.label_4.setText(QCoreApplication.translate("ImageDialog", u"width", None))
        self.acceptButton.setText(QCoreApplication.translate("ImageDialog", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("ImageDialog", u"alt", None))
    # retranslateUi

