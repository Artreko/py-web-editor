# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'key_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFormLayout,
    QFrame, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModal)
        Dialog.resize(640, 314)
        Dialog.setModal(True)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.startFrame = QFrame(Dialog)
        self.startFrame.setObjectName(u"startFrame")
        self.startFrame.setStyleSheet(u"")
        self.startFrame.setFrameShape(QFrame.StyledPanel)
        self.startFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.startFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.searchButton = QPushButton(self.startFrame)
        self.searchButton.setObjectName(u"searchButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchButton.setLayoutDirection(Qt.LeftToRight)
        self.searchButton.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.searchButton)

        self.searchFailureLabel = QLabel(self.startFrame)
        self.searchFailureLabel.setObjectName(u"searchFailureLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.searchFailureLabel.sizePolicy().hasHeightForWidth())
        self.searchFailureLabel.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Roboto Bk"])
        font.setPointSize(11)
        self.searchFailureLabel.setFont(font)
        self.searchFailureLabel.setLayoutDirection(Qt.LeftToRight)
        self.searchFailureLabel.setStyleSheet(u"color: brown;")
        self.searchFailureLabel.setFrameShape(QFrame.NoFrame)
        self.searchFailureLabel.setAlignment(Qt.AlignCenter)
        self.searchFailureLabel.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.searchFailureLabel)


        self.verticalLayout.addWidget(self.startFrame)

        self.diskTableFrame = QFrame(Dialog)
        self.diskTableFrame.setObjectName(u"diskTableFrame")
        self.diskTableFrame.setEnabled(True)
        self.diskTableFrame.setFrameShape(QFrame.StyledPanel)
        self.diskTableFrame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.diskTableFrame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.tableLabel = QLabel(self.diskTableFrame)
        self.tableLabel.setObjectName(u"tableLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableLabel.sizePolicy().hasHeightForWidth())
        self.tableLabel.setSizePolicy(sizePolicy2)
        self.tableLabel.setMinimumSize(QSize(0, 0))
        self.tableLabel.setStyleSheet(u"font-size: 18px;\n"
"font-weight: 600;")
        self.tableLabel.setFrameShape(QFrame.NoFrame)
        self.tableLabel.setFrameShadow(QFrame.Plain)
        self.tableLabel.setTextFormat(Qt.PlainText)
        self.tableLabel.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.tableLabel)

        self.diskTable = QTableWidget(self.diskTableFrame)
        if (self.diskTable.columnCount() < 5):
            self.diskTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.diskTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.diskTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.diskTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.diskTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.diskTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.diskTable.setObjectName(u"diskTable")
        self.diskTable.setAlternatingRowColors(False)
        self.diskTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.diskTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.diskTable.horizontalHeader().setCascadingSectionResizes(True)
        self.diskTable.horizontalHeader().setDefaultSectionSize(130)
        self.diskTable.horizontalHeader().setStretchLastSection(True)

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.diskTable)

        self.reSearchButton = QPushButton(self.diskTableFrame)
        self.reSearchButton.setObjectName(u"reSearchButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.reSearchButton.sizePolicy().hasHeightForWidth())
        self.reSearchButton.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.reSearchButton)

        self.diskChooseButton = QPushButton(self.diskTableFrame)
        self.diskChooseButton.setObjectName(u"diskChooseButton")
        sizePolicy3.setHeightForWidth(self.diskChooseButton.sizePolicy().hasHeightForWidth())
        self.diskChooseButton.setSizePolicy(sizePolicy3)
        self.diskChooseButton.setLayoutDirection(Qt.LeftToRight)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.diskChooseButton)


        self.verticalLayout.addWidget(self.diskTableFrame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.searchButton.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0438\u0441\u043a USB \u043d\u0430\u043a\u043e\u043f\u0438\u0442\u0435\u043b\u0435\u0439", None))
        self.searchFailureLabel.setText(QCoreApplication.translate("Dialog", u"USB \u043d\u0430\u043a\u043e\u043f\u0438\u0442\u0435\u043b\u0438 \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u044b!", None))
        self.tableLabel.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0435 \u0434\u0438\u0441\u043a\u0438", None))
        ___qtablewidgetitem = self.diskTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u0414\u0438\u0441\u043a", None));
        ___qtablewidgetitem1 = self.diskTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem2 = self.diskTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        ___qtablewidgetitem3 = self.diskTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"\u0412\u043b\u0430\u0434\u0435\u043b\u0435\u0446", None));
        ___qtablewidgetitem4 = self.diskTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u0435\u043d \u0434\u043e", None));
        self.reSearchButton.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u044c \u043f\u043e\u0438\u0441\u043a", None))
        self.diskChooseButton.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
    # retranslateUi

