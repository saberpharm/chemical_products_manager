# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_search_dialog(object):
    def setupUi(self, search_dialog):
        search_dialog.setObjectName("search_dialog")
        search_dialog.resize(473, 342)
        self.verticalLayoutWidget = QtWidgets.QWidget(search_dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 471, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(100, -1, 100, -1)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.search_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.horizontalLayout.addWidget(self.search_lineEdit)
        self.search_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.search_button.setMinimumSize(QtCore.QSize(0, 30))
        self.search_button.setObjectName("search_button")
        self.horizontalLayout.addWidget(self.search_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.results_table = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.results_table.setShowGrid(True)
        self.results_table.setGridStyle(QtCore.Qt.SolidLine)
        self.results_table.setObjectName("results_table")
        self.results_table.setColumnCount(3)
        self.results_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.results_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.results_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.results_table.setHorizontalHeaderItem(2, item)
        self.results_table.horizontalHeader().setVisible(True)
        self.results_table.horizontalHeader().setCascadingSectionResizes(False)
        self.results_table.horizontalHeader().setDefaultSectionSize(155)
        self.results_table.verticalHeader().setCascadingSectionResizes(False)
        self.results_table.verticalHeader().setSortIndicatorShown(False)
        self.results_table.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.results_table)

        self.retranslateUi(search_dialog)
        QtCore.QMetaObject.connectSlotsByName(search_dialog)

    def retranslateUi(self, search_dialog):
        _translate = QtCore.QCoreApplication.translate
        search_dialog.setWindowTitle(_translate("search_dialog", "Dialog"))
        self.label.setText(_translate("search_dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Product Search</span></p></body></html>"))
        self.search_button.setText(_translate("search_dialog", "Search"))
        item = self.results_table.horizontalHeaderItem(0)
        item.setText(_translate("search_dialog", "NS ID"))
        item = self.results_table.horizontalHeaderItem(1)
        item.setText(_translate("search_dialog", "Name"))
        item = self.results_table.horizontalHeaderItem(2)
        item.setText(_translate("search_dialog", "Storage"))

