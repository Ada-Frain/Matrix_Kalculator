# Импортируем нужные библиотеки
import sys      # sys нужен для передачи argv в QApplication
import gui      # Конвертированный файл дизайна приложения
import instr    # Конвертированный файл дизайна окна инструкции
import errorW   # Конвертированный файл дизайна окна ошибки
from calcul import det_matrix, tran_matrix, mult_scalar_matrix, add_matrix, sub_matrix, mult_matrix
import numpy as np
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Создаем класс для взаимодействия с элементами интерфейса
class App(QMainWindow, gui.Ui_MatrixCalcul):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.instruct.clicked.connect(self.instructionButnClicked)
        self.addButn.clicked.connect(self.addMatrixButn)
        self.subButn.clicked.connect(self.subMatrixButn)
        self.multButn.clicked.connect(self.multMatrixButn)
        self.detButn.clicked.connect(self.detMatrixButn)
        self.transButn.clicked.connect(self.transMatrixButn)
        self.multOnScalar.clicked.connect(self.multOnScalarMatrixButn)


    # Сбор данных матриц
    def sborDataA(self):
        a = [[int(self.m11.text()),int(self.m12.text()),int(self.m13.text()),int(self.m14.text()),int(self.m15.text())],
            [int(self.m21.text()),int(self.m22.text()),int(self.m23.text()),int(self.m24.text()),int(self.m25.text())],
            [int(self.m31.text()),int(self.m32.text()),int(self.m33.text()),int(self.m34.text()),int(self.m35.text())],
            [int(self.m41.text()),int(self.m42.text()),int(self.m43.text()),int(self.m44.text()),int(self.m45.text())],
            [int(self.m51.text()),int(self.m52.text()),int(self.m53.text()),int(self.m54.text()),int(self.m55.text())]]

        return a

    def sborDataB(self):
        b = [[int(self.n11.text()),int(self.n12.text()),int(self.n13.text()),int(self.n14.text()),int(self.n15.text())],
            [int(self.n21.text()),int(self.n22.text()),int(self.n23.text()),int(self.n24.text()),int(self.n25.text())],
            [int(self.n31.text()),int(self.n32.text()),int(self.n33.text()),int(self.n34.text()),int(self.n35.text())],
            [int(self.n41.text()),int(self.n42.text()),int(self.n43.text()),int(self.n44.text()),int(self.n45.text())],
            [int(self.n51.text()),int(self.n52.text()),int(self.n53.text()),int(self.n54.text()),int(self.n55.text())]]

        return b

    
    # Реализуемые операции над матрицами
    # сложение
    def addMatrixButn(self):
        try:
            a = np.matrix(self.sborDataA())
            b = np.matrix(self.sborDataB())
            self.label_3.setText(str(add_matrix(a,b)))
        except Exception:
            self.errorWindow = ErrorWind()
            self.errorWindow.show()

    # вычиталиние
    def subMatrixButn(self):
        try:
            a = np.matrix(self.sborDataA())
            b = np.matrix(self.sborDataB())
            self.label_3.setText(str(sub_matrix(a,b)))
        except Exception:
            self.errorWindow = ErrorWind()
            self.errorWindow.show()
        
    # умножение
    def multMatrixButn(self):
        try:
            a = np.matrix(self.sborDataA())
            b = np.matrix(self.sborDataB())
            self.label_3.setText(str(mult_matrix(a,b)))
        except Exception:
            self.errorWindow = ErrorWind()
            self.errorWindow.show()

    # определитель
    def detMatrixButn(self):
        try:
            a = np.matrix(self.sborDataA())
            self.label_3.setText(str(det_matrix(a)))
        except Exception:
            self.errorWindow = ErrorWind()
            self.errorWindow.show()

    # транспонирование
    def transMatrixButn(self):
        try:
            a = np.matrix(self.sborDataA())
            self.label_3.setText(str(tran_matrix(a)))
        except Exception:
            self.errorWindow = ErrorWind()
            self.errorWindow.show()

    # умножение на скаляр
    def multOnScalarMatrixButn(self):
        try:
            a = np.matrix(self.sborDataA())
            x = int(self.scalar.text())
            self.label_3.setText(str(mult_scalar_matrix(a,x)))
        except Exception:
            self.errorWindow = ErrorWind()
            self.errorWindow.show()

    # инструкция
    def instructionButnClicked(self):
        self.instWindow = Window2()
        self.instWindow.show()

# Класс для окна инструкции
class Window2(QDialog, instr.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# Класс для окна ошибки
class ErrorWind(QDialog, errorW.Ui_errorWind):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = App()
    form.show()
    sys.exit(app.exec_())