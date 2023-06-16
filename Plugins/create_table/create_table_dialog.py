from PySide6.QtWidgets import QDialog, QFormLayout
from PySide6.QtGui import QColor, QIcon
from .create_table_ui import Ui_TableDialog
from color_button import ColorButton
import qrc_resources


class CreateTableUI(Ui_TableDialog):
    def setupUi(self, TableDialog):
        super().setupUi(TableDialog)
        self.main_color = ColorButton(color='#000')
        self.main_back_color = ColorButton(color='#fff')
        self.border_color = ColorButton(color='#000')
        self.header_color = ColorButton(color='#000')
        self.header_back_color = ColorButton(color='#fff')

        self.formLayout.setWidget(6, QFormLayout.ItemRole.SpanningRole, self.main_color)
        self.formLayout.setWidget(7, QFormLayout.ItemRole.SpanningRole, self.main_back_color)
        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.header_color)
        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.SpanningRole, self.header_back_color)
        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.border_color)

    def retranslateUi(self, TableDialog):
        super().retranslateUi(TableDialog)
class CreateTableDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = CreateTableUI()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon.fromTheme(':insert-table.png'))

        self.border_check()
        self.header_check()

        self.ui.acceptButton.clicked.connect(self.accept_button_clicked)
        self.ui.borderCheck.stateChanged.connect(self.border_check)
        self.ui.headerCheck.stateChanged.connect(self.header_check)

    def border_check(self):
        self.ui.borderFrame.setEnabled(self.ui.borderCheck.isChecked())

    def header_check(self):
        self.ui.headerFrame.setEnabled(self.ui.headerCheck.isChecked())

    def accept_button_clicked(self):
        self.accept()
        self.close()

    def back_button_clicked(self):
        self.ui.frame.show()

    def next_button_clicked(self):
        rows = self.ui.rowSpin.value()
        cols = self.ui.colSpin.value()

    @staticmethod
    def get_table():
        dialog = CreateTableDialog()
        if dialog.exec():
            rows = dialog.ui.rowSpin.value()
            cols = dialog.ui.colSpin.value()
            if dialog.ui.borderCheck.isChecked():
                result = '<style>\n'
                result += f'table, th, td {"{"} \n border: {dialog.ui.borderWidth.value()}px ' \
                          f'{dialog.ui.borderType.currentText()} ' \
                          f'{dialog.ui.border_color.color()}'
                if dialog.ui.collapceCheck.isChecked():
                    result += ';\n border-collapse: collapse;'
                result += '}</style>\n'
            result += '<table>\n'
            if cap := dialog.ui.captionEdit.text():
                result += '\t<caption>\n'+cap+'\n\t</caption>\n'
            if dialog.ui.headerCheck.isChecked():
                result += f'\t<thead style="' \
                          f'background-color: {dialog.ui.header_back_color.color()};' \
                          f'color: {dialog.ui.header_color.color()};' \
                          f'font: {dialog.ui.headerSpin.value()}px ' \
                          f'\'{dialog.ui.mainFont.currentFont().family()}\'">\n\t\t<tr>\n'
                for col in range(cols):
                    result += '\t\t\t<th></th>\n'
                result += '\t\t</tr>\n</thead>\n'
            result += f'\t<tbody style="color: {dialog.ui.main_color.color()};' \
                      f'background-color: {dialog.ui.main_back_color.color()};' \
                      f'font: {dialog.ui.mainSpin.value()}px ' \
                      f'\'{dialog.ui.mainFont.currentFont().family()}\'">\n'
            for row in range(rows):
                result += '\t\t<tr>\n'
                for col in range(cols):
                    result += '\t\t\t<td></td>\n'
                result += '\t\t</tr>\n'
            result += '\t</tbody>\n'
            result += '</table>\n'
            return result

