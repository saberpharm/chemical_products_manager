from PyQt5.QtWidgets import QMainWindow
from fbs_runtime.application_context import ApplicationContext, cached_property

import sys

from main_window import Ui_MainWindow
from search import SearchDialog


class AppContext(ApplicationContext):  # 1. Subclass ApplicationContext
    def run(self):  # 2. Implement run()
        window = self.window
        window.show()
        return self.app.exec_()  # 3. End run() with this line

    @cached_property
    def window(self):
        return MainWindow()


class MainWindow(QMainWindow):
    # noinspection PyArgumentList
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.search_dialog = None
        self.ui.search_button.clicked.connect(self.search_button_clicked)

    def search_button_clicked(self):
        self.search_dialog = SearchDialog()
        self.search_dialog.show()


if __name__ == '__main__':
    app_context = AppContext()  # 4. Instantiate the subclass
    exit_code = app_context.run()  # 5. Invoke run()
    sys.exit(exit_code)
