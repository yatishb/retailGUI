# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddNewPerishable.ui'
#
# Created: Fri Dec 06 17:05:11 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AddNewPerishable(object):
    def setupUi(self, AddNewPerishable):
        AddNewPerishable.setObjectName(_fromUtf8("AddNewPerishable"))
        AddNewPerishable.resize(391, 351)
        self.label_Heading = QtGui.QLabel(AddNewPerishable)
        self.label_Heading.setGeometry(QtCore.QRect(20, 20, 151, 16))
        self.label_Heading.setObjectName(_fromUtf8("label_Heading"))
        self.widget = QtGui.QWidget(AddNewPerishable)
        self.widget.setGeometry(QtCore.QRect(20, 50, 341, 241))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_Name = QtGui.QLabel(self.widget)
        self.label_Name.setObjectName(_fromUtf8("label_Name"))
        self.gridLayout.addWidget(self.label_Name, 1, 0, 1, 1)
        self.label_Category = QtGui.QLabel(self.widget)
        self.label_Category.setObjectName(_fromUtf8("label_Category"))
        self.gridLayout.addWidget(self.label_Category, 2, 0, 1, 1)
        self.lineEdit_Name = QtGui.QLineEdit(self.widget)
        self.lineEdit_Name.setObjectName(_fromUtf8("lineEdit_Name"))
        self.gridLayout.addWidget(self.lineEdit_Name, 1, 1, 1, 1)
        self.lineEdit_Manu = QtGui.QLineEdit(self.widget)
        self.lineEdit_Manu.setObjectName(_fromUtf8("lineEdit_Manu"))
        self.gridLayout.addWidget(self.lineEdit_Manu, 3, 1, 1, 1)
        self.label_Price = QtGui.QLabel(self.widget)
        self.label_Price.setObjectName(_fromUtf8("label_Price"))
        self.gridLayout.addWidget(self.label_Price, 4, 0, 1, 1)
        self.lineEdit_Category = QtGui.QLineEdit(self.widget)
        self.lineEdit_Category.setObjectName(_fromUtf8("lineEdit_Category"))
        self.gridLayout.addWidget(self.lineEdit_Category, 2, 1, 1, 1)
        self.label_Manufacturer = QtGui.QLabel(self.widget)
        self.label_Manufacturer.setObjectName(_fromUtf8("label_Manufacturer"))
        self.gridLayout.addWidget(self.label_Manufacturer, 3, 0, 1, 1)
        self.lineEdit_Price = QtGui.QLineEdit(self.widget)
        self.lineEdit_Price.setObjectName(_fromUtf8("lineEdit_Price"))
        self.gridLayout.addWidget(self.lineEdit_Price, 4, 1, 1, 1)
        self.label_Stock = QtGui.QLabel(self.widget)
        self.label_Stock.setObjectName(_fromUtf8("label_Stock"))
        self.gridLayout.addWidget(self.label_Stock, 5, 0, 1, 1)
        self.label_Barcode = QtGui.QLabel(self.widget)
        self.label_Barcode.setObjectName(_fromUtf8("label_Barcode"))
        self.gridLayout.addWidget(self.label_Barcode, 0, 0, 1, 1)
        self.label_Expiry = QtGui.QLabel(self.widget)
        self.label_Expiry.setObjectName(_fromUtf8("label_Expiry"))
        self.gridLayout.addWidget(self.label_Expiry, 6, 0, 1, 1)
        self.lineEdit_Expiry = QtGui.QLineEdit(self.widget)
        self.lineEdit_Expiry.setText(_fromUtf8(""))
        self.lineEdit_Expiry.setObjectName(_fromUtf8("lineEdit_Expiry"))
        self.gridLayout.addWidget(self.lineEdit_Expiry, 6, 1, 1, 1)
        self.lineEdit_Stock = QtGui.QLineEdit(self.widget)
        self.lineEdit_Stock.setObjectName(_fromUtf8("lineEdit_Stock"))
        self.gridLayout.addWidget(self.lineEdit_Stock, 5, 1, 1, 1)
        self.lineEdit_Barcode = QtGui.QLineEdit(self.widget)
        self.lineEdit_Barcode.setObjectName(_fromUtf8("lineEdit_Barcode"))
        self.gridLayout.addWidget(self.lineEdit_Barcode, 0, 1, 1, 1)
        self.error_Name = QtGui.QLabel(self.widget)
        self.error_Name.setText(_fromUtf8(""))
        self.error_Name.setObjectName(_fromUtf8("error_Name"))
        self.gridLayout.addWidget(self.error_Name, 1, 2, 1, 1)
        self.error_Barcode = QtGui.QLabel(self.widget)
        self.error_Barcode.setText(_fromUtf8(""))
        self.error_Barcode.setObjectName(_fromUtf8("error_Barcode"))
        self.gridLayout.addWidget(self.error_Barcode, 0, 2, 1, 1)
        self.error_Category = QtGui.QLabel(self.widget)
        self.error_Category.setText(_fromUtf8(""))
        self.error_Category.setObjectName(_fromUtf8("error_Category"))
        self.gridLayout.addWidget(self.error_Category, 2, 2, 1, 1)
        self.error_Manu = QtGui.QLabel(self.widget)
        self.error_Manu.setText(_fromUtf8(""))
        self.error_Manu.setObjectName(_fromUtf8("error_Manu"))
        self.gridLayout.addWidget(self.error_Manu, 3, 2, 1, 1)
        self.error_Price = QtGui.QLabel(self.widget)
        self.error_Price.setText(_fromUtf8(""))
        self.error_Price.setObjectName(_fromUtf8("error_Price"))
        self.gridLayout.addWidget(self.error_Price, 4, 2, 1, 1)
        self.error_Stock = QtGui.QLabel(self.widget)
        self.error_Stock.setText(_fromUtf8(""))
        self.error_Stock.setObjectName(_fromUtf8("error_Stock"))
        self.gridLayout.addWidget(self.error_Stock, 5, 2, 1, 1)
        self.error_Expiry = QtGui.QLabel(self.widget)
        self.error_Expiry.setText(_fromUtf8(""))
        self.error_Expiry.setObjectName(_fromUtf8("error_Expiry"))
        self.gridLayout.addWidget(self.error_Expiry, 6, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 50)
        self.gridLayout.setColumnStretch(1, 100)
        self.gridLayout.setColumnStretch(2, 50)
        self.widget1 = QtGui.QWidget(AddNewPerishable)
        self.widget1.setGeometry(QtCore.QRect(190, 310, 182, 25))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.create = QtGui.QPushButton(self.widget1)
        self.create.setObjectName(_fromUtf8("create"))
        self.horizontalLayout.addWidget(self.create)
        self.cancel = QtGui.QPushButton(self.widget1)
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.horizontalLayout.addWidget(self.cancel)

        self.retranslateUi(AddNewPerishable)
        QtCore.QObject.connect(self.cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), AddNewPerishable.close)
        QtCore.QMetaObject.connectSlotsByName(AddNewPerishable)

    def retranslateUi(self, AddNewPerishable):
        AddNewPerishable.setWindowTitle(_translate("AddNewPerishable", "New Perishable Product", None))
        self.label_Heading.setText(_translate("AddNewPerishable", "Add A New Perishable Product", None))
        self.label_Name.setText(_translate("AddNewPerishable", "Name", None))
        self.label_Category.setText(_translate("AddNewPerishable", "Category", None))
        self.label_Price.setText(_translate("AddNewPerishable", "Unit Price", None))
        self.label_Manufacturer.setText(_translate("AddNewPerishable", "Manufacturer", None))
        self.label_Stock.setText(_translate("AddNewPerishable", "Initial Stock", None))
        self.label_Barcode.setText(_translate("AddNewPerishable", "Barcode", None))
        self.label_Expiry.setText(_translate("AddNewPerishable", "Expiry Date", None))
        self.lineEdit_Expiry.setPlaceholderText(_translate("AddNewPerishable", "yyyy-mm-dd", None))
        self.create.setText(_translate("AddNewPerishable", "Create New", None))
        self.cancel.setText(_translate("AddNewPerishable", "Cancel", None))

