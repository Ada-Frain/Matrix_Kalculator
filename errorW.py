# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Зарета\Documents\codeprojects\PP\qt_Project\errorW.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_errorWind(object):
    def setupUi(self, errorWind):
        errorWind.setObjectName("errorWind")
        errorWind.resize(437, 173)
        self.buttonBox = QtWidgets.QDialogButtonBox(errorWind)
        self.buttonBox.setGeometry(QtCore.QRect(180, 110, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(errorWind)
        self.label.setGeometry(QtCore.QRect(10, 10, 411, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.retranslateUi(errorWind)
        self.buttonBox.accepted.connect(errorWind.accept)
        self.buttonBox.rejected.connect(errorWind.reject)
        QtCore.QMetaObject.connectSlotsByName(errorWind)

    def retranslateUi(self, errorWind):
        _translate = QtCore.QCoreApplication.translate
        errorWind.setWindowTitle(_translate("errorWind", "Ошибка"))
        self.label.setText(_translate("errorWind", "Вы ввели некорректные данные либо оставили пустые ячейки. Попробуйте еще раз."))
