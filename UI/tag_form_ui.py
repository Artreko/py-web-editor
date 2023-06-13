# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tag_form.ui'
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
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_tagDialog(object):
    def setupUi(self, tagDialog):
        if not tagDialog.objectName():
            tagDialog.setObjectName(u"tagDialog")
        tagDialog.resize(449, 164)
        tagDialog.setModal(True)
        tagDialog.setWindowIcon(QIcon.fromTheme(':tag.png'))
        self.formLayout = QFormLayout(tagDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(tagDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.tagEdit = QLineEdit(tagDialog)
        self.tagEdit.setObjectName(u"tagEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.tagEdit)

        self.pairTagButton = QRadioButton(tagDialog)
        self.pairTagButton.setObjectName(u"pairTagButton")
        self.pairTagButton.setChecked(True)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.pairTagButton)

        self.singleTagButton = QRadioButton(tagDialog)
        self.singleTagButton.setObjectName(u"singleTagButton")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.singleTagButton)

        self.label_2 = QLabel(tagDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.idEdit = QLineEdit(tagDialog)
        self.idEdit.setObjectName(u"idEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.idEdit)

        self.label_3 = QLabel(tagDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.classEdit = QLineEdit(tagDialog)
        self.classEdit.setObjectName(u"classEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.classEdit)

        self.acceptButton = QPushButton(tagDialog)
        self.acceptButton.setObjectName(u"acceptButton")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.acceptButton)


        self.retranslateUi(tagDialog)

        QMetaObject.connectSlotsByName(tagDialog)
    # setupUi

    def retranslateUi(self, tagDialog):
        tagDialog.setWindowTitle(QCoreApplication.translate("tagDialog", u"\u0412\u0441\u0442\u0430\u0432\u043a\u0430 \u0442\u0435\u0433\u0430", None))
        self.label.setText(QCoreApplication.translate("tagDialog", u"\u0422\u0435\u0433", None))
        self.pairTagButton.setText(QCoreApplication.translate("tagDialog", u"\u041f\u0430\u0440\u043d\u044b\u0439", None))
        self.singleTagButton.setText(QCoreApplication.translate("tagDialog", u"\u041e\u0434\u0438\u043d\u0430\u0440\u043d\u044b\u0439", None))
        self.label_2.setText(QCoreApplication.translate("tagDialog", u"id", None))
        self.label_3.setText(QCoreApplication.translate("tagDialog", u"class", None))
        self.acceptButton.setText(QCoreApplication.translate("tagDialog", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
    # retranslateUi

