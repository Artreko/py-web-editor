# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'font_form.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFontComboBox, QFormLayout,
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_FontDialog(object):
    def setupUi(self, FontDialog):
        if not FontDialog.objectName():
            FontDialog.setObjectName(u"FontDialog")
        FontDialog.resize(348, 131)
        self.formLayout = QFormLayout(FontDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(FontDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.acceptButton = QPushButton(FontDialog)
        self.acceptButton.setObjectName(u"acceptButton")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.acceptButton)

        self.label_2 = QLabel(FontDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(FontDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.fontBox = QFontComboBox(FontDialog)
        self.fontBox.setObjectName(u"fontBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.fontBox)

        self.sizeSpin = QSpinBox(FontDialog)
        self.sizeSpin.setObjectName(u"sizeSpin")
        self.sizeSpin.setMinimum(1)
        self.sizeSpin.setValue(10)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.sizeSpin)


        self.retranslateUi(FontDialog)

        QMetaObject.connectSlotsByName(FontDialog)
    # setupUi

    def retranslateUi(self, FontDialog):
        FontDialog.setWindowTitle(QCoreApplication.translate("FontDialog", u"\u0412\u0441\u0442\u0430\u0432\u043a\u0430 \u0448\u0440\u0438\u0444\u0442\u0430", None))
        self.label.setText(QCoreApplication.translate("FontDialog", u"\u0420\u0430\u0437\u043c\u0435\u0440", None))
        self.acceptButton.setText(QCoreApplication.translate("FontDialog", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("FontDialog", u"\u0428\u0440\u0438\u0444\u0442", None))
        self.label_3.setText(QCoreApplication.translate("FontDialog", u"\u0426\u0432\u0435\u0442", None))
    # retranslateUi

