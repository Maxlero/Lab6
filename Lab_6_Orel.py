"""
    Автор: Орел Максим
    Группа: КБ-161
    Вариант: 11
    Дата создания: 18/04/2018
    Python Version: 3.6
"""
import math
import sys
import warnings
import numpy as np
import matplotlib.pyplot as plt

# Constants
accuracy = 0.00001
START_X = -1
END_X = 6
START_Y = -1
END_Y = 20

x = [1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5]
y = [7.19, 7.466, 7.912, 8.495, 8.727, 8.842, 9.673, 9.622, 10.09, 10.744, 10.988, 11.028, 11.897, 12.311, 12.737,
     13.054, 13.166, 13.956, 13.949, 14.562, 15.312]


def whence_differences(y_array):
    return_array = []
    for i in range(0, len(y_array) - 1):
        return_array.append(y_array[i + 1] - y_array[i])
    return return_array


def witchcraft_start(y_array, h):
    part_y = [y_array[0]]
    y = y_array
    for i in range(0, len(y_array) - 1):
        y = whence_differences(y)
        part_y.append(y[0] / math.factorial(i + 1) / (h ** (i + 1)))

    return part_y


def tragic_magic(coefficients_y, point, x_array):
    value = coefficients_y[0]
    for i in range(1, len(coefficients_y)):
        q = 1
        for j in range(0, i):
            q *= (point - x_array[j])

        value += coefficients_y[i] * q
    return value


def build_points(x_array, y_array):
    for i in range(0, len(x_array)):
        plt.scatter(x_array[i], y_array[i])


# def build_function(x_array, y_array, x_from=START_X, x_to=END_X, y_from=START_Y,
#                    y_to=END_Y):
#     plt.plot(x_array, y_array)
#     plt.axis([x_from, x_to, y_from, y_to])
#     plt.grid(True)
#     plt.axhline(y=0, color='k')
#     plt.axvline(x=0, color='k')


def show_plot():
    plt.show()


def newton_there(x_array, y_array):
    # setting up
    x0 = x_array[0]
    h = x_array[1] - x_array[0]
    build_points(x_array, y_array)

    # returns part_y = delta ^ n * y0 / (n! * h ^ n)
    part_y = witchcraft_start(y_array, h)

    print('Коэффициенты прямого полинома')
    print(part_y)

    x = np.linspace(x_array[0], x_array[len(x_array) - 1], 228)
    # x = np.arange(1.5, 4.5, 0.005)
    #
    # y = []
    # for i in range(0, len(x)):
    #     y.append(tragic_magic(part_y, x[i], x_array))
    #
    # plt.plot(x, y)
    plt.plot(x, tragic_magic(part_y, x, x_array))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    show_plot()


def witchcraft_continue(y_array, h):
    part_y = [y_array[len(y_array) - 1]]
    y = y_array
    for i in range(0, len(y_array) - 1):
        y = whence_differences(y)
        part_y.append(y[len(y) - 1] / math.factorial(i + 1) / (h ** (i + 1)))
    return part_y


def ecstatic_magic(coefficients_y, point, x_array):
    value = coefficients_y[0]
    for i in range(1, len(coefficients_y)):
        q = 1
        for j in range(0, i):
            q *= (point - x_array[len(x_array) - j - 1])

        value += coefficients_y[i] * q
    return value


def newton_here_the_boss(x_array, y_array):
    # setting up
    x0 = x_array[0]
    h = x_array[1] - x_array[0]
    build_points(x_array, y_array)

    # returns part_y = delta ^ n * y_n / (n! * h ^ n)
    part_y = witchcraft_continue(y_array, h)

    print('Коэффициенты обратного полинома')
    print(part_y)

    x = np.linspace(x_array[0], x_array[len(x_array) - 1], 228)
    plt.plot(x, ecstatic_magic(part_y, x, x_array))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    show_plot()


if __name__ == "__main__":
    # # Отключение вывода некоторых уведомлений
    # if not sys.warnoptions:
    #     warnings.simplefilter("ignore")
    #
    # # Устанавливает максимальную глубину рекурсии на 2000
    # sys.setrecursionlimit(2000)

    try:
        newton_there(x, y)
    except Exception as e:
        print(e)

    try:
        newton_here_the_boss(x, y)
    except Exception as e:
        print(e)
