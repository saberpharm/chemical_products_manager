from PyQt5.QtCore import QStringListModel, Qt
from PyQt5.QtWidgets import QDialog, QCompleter, QTableWidgetItem
from openpyxl import load_workbook

from search_dialog import Ui_search_dialog


class SearchDialog(QDialog):
    # noinspection PyArgumentList
    def __init__(self):
        super().__init__()
        self.ui = Ui_search_dialog()
        self.ui.setupUi(self)

        self.ui.search_button.clicked.connect(self.search_button_clicked)

        # "G:\07 Informatique\03 Softwares\01 Script\Chemical Products Manager"
        # "C:\Users\saber.graf\PycharmProjects\chemical_products_manager\src\main\resources"
        wb = load_workbook(r"C:\Users\saber.graf\PycharmProjects\chemical_products_manager\src\main\resources"
                           r"\DR-PNS 35-N°67.xlsx", data_only=True)

        self.db_ws = wb['Database']

        compounds = sorted(set([x.value for x in self.db_ws['F'] if x.value is not None]))

        edit = self.ui.search_lineEdit

        completer = QCompleter()
        completer.setCaseSensitivity(Qt.CaseInsensitive)

        edit.setCompleter(completer)

        model = QStringListModel()
        model.setStringList(compounds)

        completer.setModel(model)

    def search_button_clicked(self):

        search_text = self.ui.search_lineEdit.text()
        results_table = self.ui.results_table

        ns_id_list = list([x.value for x in self.db_ws['A']])
        names_list = list([x.value for x in self.db_ws['F']])
        storage_list = list([x.value for x in self.db_ws['J']])

        row_num = 0
        for i, name in enumerate(names_list):
            if name == search_text:
                row_num += 1
                results_table.setRowCount(row_num)
                ns_id = ns_id_list[i]
                results_table.setItem(row_num - 1, 0, QTableWidgetItem(ns_id))
                results_table.setItem(row_num - 1, 1, QTableWidgetItem(name))
                storage = storage_list[i]
                results_table.setItem(row_num - 1, 2, QTableWidgetItem(storage))
