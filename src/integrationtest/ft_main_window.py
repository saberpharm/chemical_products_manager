from time import sleep

from PyQt5 import QtCore

from src.main.python.main import AppContext


def test_main_window(qtbot):
    # If a user want to use the program
    window = AppContext().window
    qtbot.addWidget(window)

    ui = window.ui

    assert ui.search_button.text() == 'Research'
    assert ui.weight_button.text() == 'Weight'
    assert ui.aliquot_button.text() == 'Aliquot'

    window.show()
    qtbot.waitForWindowShown(window)
    sleep(3)


def test_search_button(qtbot):
    # if a user want to search for a product
    window = AppContext().window

    qtbot.addWidget(window)

    search_button = window.ui.search_button

    qtbot.mouseClick(search_button, QtCore.Qt.LeftButton)

    # a new dialog must show
    # TODO

    sleep(3)
