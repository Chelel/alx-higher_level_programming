#!/usr/bin/python3
# function that divides all elements of a matrix.


def validate_col(matrix):
    for list in matrix:
        for item in list:
            if not(isinstance(item, int) or isinstance(item, float)):
                raise TypeError('matrix must be a matrix\
                                (list of lists)of integers/floats')


def validate_rows(matrix):
    initial_length = len(matrix[0])
    for list in matrix:
        if len(list) != initial_length:
            raise TypeError('Each row of the matrix\
           must have the same size')


def matrix_divided(matrix, div):
    result = []
    for i in range(len(matrix)):
        result.append([])
        for j in range(len(matrix[i])):
            result[i].append(None)

    validate_rows(matrix)

    # check for validate_col
    validate_col(matrix)

    if div == 0:
        raise ZeroDivisionError('division by zero')

    # matrix col division
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            col_answer = round((matrix[i][j] / div), 2)
            result[i][j] = col_answer

    return result
