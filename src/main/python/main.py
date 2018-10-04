from PyQt5.QtWidgets import QMainWindow
from fbs_runtime.application_context import ApplicationContext, cached_property

import sys

from main_window import Ui_MainWindow


class AppContext(ApplicationContext):  # 1. Subclass ApplicationContext
    def run(self):  # 2. Implement run()
        window = self.window

        window.show()
        return self.app.exec_()  # 3. End run() with this line

    @cached_property
    def window(self):
        return AppWindow()


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


if __name__ == '__main__':
    appctxt = AppContext()  # 4. Instantiate the subclass
    exit_code = appctxt.run()  # 5. Invoke run()
    sys.exit(exit_code)
