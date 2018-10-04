from PyQt5.QtWidgets import QDialog

from search_dialog import Ui_search_dialog


class SearchDialog(QDialog):
    # noinspection PyArgumentList
    def __init__(self):
        super().__init__()
        self.ui = Ui_search_dialog()
        self.ui.setupUi(self)

        self.ui.search_button.clicked.connect(self.search_button_clicked)

    def search_button_clicked(self):
        print(self.ui.search_lineEdit.text())
