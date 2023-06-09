from PySide6.QtWidgets import QDialog
from .create_table_ui import Ui_Dialog


class CreateTableDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.frame_2.hide()

        self.ui.backButton.clicked.connect(self.back_button_clicked)
        self.ui.acceptButton.clicked.connect(self.accept_button_clicked)
        self.ui.nextButton.clicked.connect(self.next_button_clicked)

    def accept_button_clicked(self):
        self.accept()
        self.close()

    def back_button_clicked(self):
        self.ui.frame_2.hide()
        self.ui.frame.show()

    def next_button_clicked(self):
        rows = self.ui.rowSpin.value()
        cols = self.ui.colSpin.value()
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setColumnCount(cols)
        self.ui.tableWidget.setRowCount(rows)
        for col in range(cols):
            for row in range(rows):
                row_item = QTableWidgetItem()
                self.ui.tableWidget.setItem(row, col, row_item)
        self.ui.frame.hide()
        self.ui.frame_2.show()


    @staticmethod
    def get_table():
        dialog = CreateTableDialog()
        if dialog.exec():
            rows = dialog.ui.rowSpin.value()
            cols = dialog.ui.colSpin.value()
            result = '<table>\n'
            for row in range(rows):
                result += '  <tr>\n'
                for col in range(cols):
                    result += f'    <td>{dialog.ui.tableWidget.item(row, col).text()}</td>\n'
                result += '  </tr>\n'
            result += '</table>\n'
            return result

