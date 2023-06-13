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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFontComboBox, QFormLayout, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_TableDialog(object):
    def setupUi(self, TableDialog):
        if not TableDialog.objectName():
            TableDialog.setObjectName(u"TableDialog")
        TableDialog.setWindowModality(Qt.WindowModal)
        TableDialog.resize(405, 593)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TableDialog.sizePolicy().hasHeightForWidth())
        TableDialog.setSizePolicy(sizePolicy)
        TableDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(TableDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(TableDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.rowSpin = QSpinBox(self.frame)
        self.rowSpin.setObjectName(u"rowSpin")
        self.rowSpin.setMinimum(1)
        self.rowSpin.setValue(2)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.rowSpin)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.colSpin = QSpinBox(self.frame)
        self.colSpin.setObjectName(u"colSpin")
        self.colSpin.setMinimum(1)
        self.colSpin.setValue(3)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.colSpin)

        self.acceptButton = QPushButton(self.frame)
        self.acceptButton.setObjectName(u"acceptButton")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.acceptButton)

        self.borderFrame = QFrame(self.frame)
        self.borderFrame.setObjectName(u"borderFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.borderFrame.sizePolicy().hasHeightForWidth())
        self.borderFrame.setSizePolicy(sizePolicy1)
        self.borderFrame.setFrameShape(QFrame.StyledPanel)
        self.borderFrame.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.borderFrame)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_6 = QLabel(self.borderFrame)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.borderWidth = QSpinBox(self.borderFrame)
        self.borderWidth.setObjectName(u"borderWidth")
        self.borderWidth.setMinimum(1)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.borderWidth)

        self.label_7 = QLabel(self.borderFrame)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.label_8 = QLabel(self.borderFrame)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.borderType = QComboBox(self.borderFrame)
        self.borderType.addItem("")
        self.borderType.addItem("")
        self.borderType.addItem("")
        self.borderType.addItem("")
        self.borderType.addItem("")
        self.borderType.addItem("")
        self.borderType.addItem("")
        self.borderType.addItem("")
        self.borderType.addItem("")
        self.borderType.addItem("")
        self.borderType.setObjectName(u"borderType")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.borderType)

        self.collapceCheck = QCheckBox(self.borderFrame)
        self.collapceCheck.setObjectName(u"collapceCheck")

        self.formLayout_3.setWidget(3, QFormLayout.SpanningRole, self.collapceCheck)


        self.formLayout.setWidget(11, QFormLayout.SpanningRole, self.borderFrame)

        self.headerFrame = QFrame(self.frame)
        self.headerFrame.setObjectName(u"headerFrame")
        sizePolicy1.setHeightForWidth(self.headerFrame.sizePolicy().hasHeightForWidth())
        self.headerFrame.setSizePolicy(sizePolicy1)
        self.headerFrame.setMinimumSize(QSize(0, 0))
        self.headerFrame.setFrameShape(QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.headerFrame)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.headerFont = QFontComboBox(self.headerFrame)
        self.headerFont.setObjectName(u"headerFont")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.headerFont)

        self.label_3 = QLabel(self.headerFrame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.headerFrame)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.headerFrame)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.headerSpin = QSpinBox(self.headerFrame)
        self.headerSpin.setObjectName(u"headerSpin")
        self.headerSpin.setMinimum(1)
        self.headerSpin.setValue(10)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.headerSpin)

        self.label_25 = QLabel(self.headerFrame)
        self.label_25.setObjectName(u"label_25")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_25)


        self.formLayout.setWidget(9, QFormLayout.SpanningRole, self.headerFrame)

        self.borderCheck = QCheckBox(self.frame)
        self.borderCheck.setObjectName(u"borderCheck")

        self.formLayout.setWidget(10, QFormLayout.SpanningRole, self.borderCheck)

        self.headerCheck = QCheckBox(self.frame)
        self.headerCheck.setObjectName(u"headerCheck")

        self.formLayout.setWidget(8, QFormLayout.SpanningRole, self.headerCheck)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_9)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_10)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_11)

        self.mainFont = QFontComboBox(self.frame)
        self.mainFont.setObjectName(u"mainFont")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.mainFont)

        self.label_23 = QLabel(self.frame)
        self.label_23.setObjectName(u"label_23")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_23)

        self.captionEdit = QLineEdit(self.frame)
        self.captionEdit.setObjectName(u"captionEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.captionEdit)

        self.label_24 = QLabel(self.frame)
        self.label_24.setObjectName(u"label_24")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_24)

        self.mainSpin = QSpinBox(self.frame)
        self.mainSpin.setObjectName(u"mainSpin")
        self.mainSpin.setMinimum(1)
        self.mainSpin.setValue(12)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.mainSpin)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(TableDialog)

        QMetaObject.connectSlotsByName(TableDialog)
    # setupUi

    def retranslateUi(self, TableDialog):
        TableDialog.setWindowTitle(QCoreApplication.translate("TableDialog", u"\u0412\u0441\u0442\u0430\u0432\u043a\u0430 \u0442\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.label.setText(QCoreApplication.translate("TableDialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u0440\u043e\u043a", None))
        self.label_2.setText(QCoreApplication.translate("TableDialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u043e\u043b\u0431\u0446\u043e\u0432", None))
        self.acceptButton.setText(QCoreApplication.translate("TableDialog", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("TableDialog", u"\u0422\u043e\u043b\u0449\u0438\u043d\u0430", None))
        self.label_7.setText(QCoreApplication.translate("TableDialog", u"\u0426\u0432\u0435\u0442", None))
        self.label_8.setText(QCoreApplication.translate("TableDialog", u"\u0422\u0438\u043f", None))
        self.borderType.setItemText(0, QCoreApplication.translate("TableDialog", u"solid", None))
        self.borderType.setItemText(1, QCoreApplication.translate("TableDialog", u"dotted", None))
        self.borderType.setItemText(2, QCoreApplication.translate("TableDialog", u"dashed", None))
        self.borderType.setItemText(3, QCoreApplication.translate("TableDialog", u"double", None))
        self.borderType.setItemText(4, QCoreApplication.translate("TableDialog", u"groove", None))
        self.borderType.setItemText(5, QCoreApplication.translate("TableDialog", u"ridje", None))
        self.borderType.setItemText(6, QCoreApplication.translate("TableDialog", u"inset", None))
        self.borderType.setItemText(7, QCoreApplication.translate("TableDialog", u"outset", None))
        self.borderType.setItemText(8, QCoreApplication.translate("TableDialog", u"none", None))
        self.borderType.setItemText(9, QCoreApplication.translate("TableDialog", u"hidden", None))

        self.collapceCheck.setText(QCoreApplication.translate("TableDialog", u"collapce", None))
        self.headerFont.setCurrentText("")
        self.label_3.setText(QCoreApplication.translate("TableDialog", u"\u0428\u0440\u0438\u0444\u0442", None))
        self.label_4.setText(QCoreApplication.translate("TableDialog", u"\u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430", None))
        self.label_5.setText(QCoreApplication.translate("TableDialog", u"\u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430", None))
        self.label_25.setText(QCoreApplication.translate("TableDialog", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430", None))
        self.borderCheck.setText(QCoreApplication.translate("TableDialog", u"\u0420\u0430\u043c\u043a\u0430", None))
        self.headerCheck.setText(QCoreApplication.translate("TableDialog", u"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a", None))
        self.label_9.setText(QCoreApplication.translate("TableDialog", u"\u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430", None))
        self.label_10.setText(QCoreApplication.translate("TableDialog", u"\u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430", None))
        self.label_11.setText(QCoreApplication.translate("TableDialog", u"\u0428\u0440\u0438\u0444\u0442", None))
        self.mainFont.setCurrentText("")
        self.label_23.setText(QCoreApplication.translate("TableDialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.label_24.setText(QCoreApplication.translate("TableDialog", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430", None))
    # retranslateUi

