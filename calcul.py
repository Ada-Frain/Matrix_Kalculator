# Импортируем библиотеку Numpy.
import numpy as np


# Функция поиска определителя матрицы.
def det_matrix(a):
    c = np.linalg.det(a)
    return c

# Функция транспонирования матрицы.
def tran_matrix(a):
    c = np.transpose(a)
    return c

# Функция умножения матрицы на скаляр.
def mult_scalar_matrix(a, x):
    c = a * x
    return c

# Функция сложения двух матриц.
def add_matrix(a, b):
    c = a + b
    return c

# Функция вычитания двух матриц.
def sub_matrix(a, b):
    c = a - b
    return c

# Функция умножения двух матриц.
def mult_matrix(a, b):
    c = np.dot(a, b)
    return c

# a = [[8, 7, 5],[7, 8, 9],[5, 9, 12]]
# b = [[1, 2, 3],[2, 2, 3],[4, 3, 2]]
# a = np.matrix(a)
# b = np.matrix(b)
# print(a, b)
# mult_matrix(a, b)
# sub_matrix(a, b)

# while(True):
#     # Выбор операции над матрицами.
#     print("Выбор операции над матрицами:")
#     print("\n1) Поиск определителя матрицы\n2) Транспонирование матрицы\n3) Умножение матрицы на скаляр\n4) Сложение\n5) Вычитание\n6) Умножение\n")
#     oper = input("Для выбора введите номер операции ")

#     '''
#     Ниже представлен ввод одной или двух матриц,
#     а также ввод числа (для умножения матрицы на число)
#     с обработчиком ошибок при некорректном вводе данных.
#     '''

#     try:
#         a = np.matrix(input("Введите матрицу A: "))
#     except Exception:
#         print("Некорректный ввод, повторите попытку")
#         break

#     if oper == "3":
#         try:
#             x = int(input("Введите число: "))
#         except Exception:
#             print("Некорректный ввод, повторите попытку\n")
#             break
    
#     elif oper == "4" or oper == "5" or oper == "6":
#         try:
#             b = np.matrix(input("Введите матрицу B: "))
#         except Exception:
#             print("Некорректный ввод, повторите попытку")
#             break

#     # Далее в зависимости от выбранной операции происходит вызов соответствующей функции и вывод результата
#     if oper == "1":
#         print("A = \n", a, "\nDeterminant = ", det_matrix(a))
        
#     elif oper == "2":
#         print("A = \n", a, "\nTransposed matrix = \n", tran_matrix(a))
        
#     elif oper == "3":
#         print("A = \n", a, "\nX = ", x, "\nA * X = \n", mult_scalar_matrix(a, x))
        
#     elif oper == "4":
#         print("A = \n", a, "\nB = \n", b, "\nA + B = \n", add_matrix(a, b))
        
#     elif oper == "5":
#         print("A = \n", a, "\nB = \n", b, "\nA - B = \n", sub_matrix(a, b))
        
#     elif oper == "6":
#         print("A = \n", a, "\nB = \n", b, "\nA * B = \n", mult_matrix(a, b))

#     else:
#         print("Что-то пошло не так. Попробуйте еще раз.\n")

    
#     print("\nВведите цифру 0, чтобы попробывать ещё")
#     if input() != "0":
#         break