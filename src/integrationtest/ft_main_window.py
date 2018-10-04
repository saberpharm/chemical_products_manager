from time import sleep

from src.main.python.main import AppContext


def test_main_window(qtbot):
    # If a user want to use the program
    window = AppContext().window
    qtbot.addWidget(window)

    assert window.ui.pushButton.text() == 'Research'

    # qtbot.keyClicks(window.directoryComboBox, str('some text'))

    # qtbot.mouseClick(window.findButton, QtCore.Qt.LeftButton)

    window.show()
    qtbot.waitForWindowShown(window)
    sleep(3)
