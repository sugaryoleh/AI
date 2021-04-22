import numpy as np


def calculate_matrix(rates, values):
    cnt = len(values)

    matrix = [[0 for i in range(cnt)] for i in range(cnt)]

    temp_rates = list(rates)
    temp_rates.append(rates[len(rates) - 1])

    matrix[cnt-1] = temp_rates

    for i in range(0, cnt):
        for j in range(0, cnt):
            matrix[i][j] = temp_rates[j]/temp_rates[i]
    return matrix


def calc_appendix(matrix, dim):
    def calc_first_row(matrix):
        first_row = [0 for i in range(dim)]
        for i in range(0, dim):
            first_row[i] = sum([item[i] for item in matrix])
        return first_row
    def calc_second_row(matrix):
        first_row = calc_first_row(matrix)
        second_row = [1/x for x in first_row]
        return second_row
    def calc_third_row(matrix):
        max_el = max(calc_second_row(matrix))
        second_row = calc_second_row(matrix)
        third_row = [x/max_el for x in second_row]
        return third_row

    appendix = [[] for x in range(3)]
    appendix[0] = calc_first_row(matrix)
    appendix[1] = calc_second_row(matrix)
    appendix[2] = calc_third_row(matrix)
    return appendix

def get_values():
    values = [50, 60, 70, 80, 90, 100]
    return values

def get_appendix_values():
    return [1, 2, 'M(X)']

def get_rates():
    rates = (9., 7., 5., 3., 1.)
    return rates

def get_table():
    rates = get_rates()
    values = get_values()
    matrix = calculate_matrix(rates, values)
    a = calc_appendix(matrix, len(values))
    for row in a:
        matrix.append(row)
    for i, row in enumerate(matrix):
        for j, el in enumerate(row):
            matrix[i][j] = round(el, 2)
    for row in matrix:
        print(row)
    return matrix

