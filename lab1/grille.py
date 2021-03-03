import math
import copy

def set_rang(matrix, rang, x, y):
    size = len(matrix)
    matrix[x][y] = rang
    matrix[y][size - 1 - x] = rang
    matrix[size - 1 - x][size - 1 - y] = rang
    matrix[size - 1 - y][x] = rang

def matrix_numerate(matrix):
    size = len(matrix)
    rang = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (matrix[i][j] == 0):
                rang += 1
                set_rang(matrix, rang, i, j)

    return rang

def rotate_matrix(matrix):
    size = len(matrix)
    for i in range(0, int(size / 2)): 
        for j in range(i, size - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[size - 1 - j][i]
            matrix[size - 1 - j][i] = matrix[size - 1 - i][size - 1 - j]
            matrix[size - 1 - i][size - 1 - j] = matrix[j][size - 1 - i]
            matrix[j][size - 1 - i] = temp

# Fill the matrix with substring next characters on ciphering step
def fill_matrix(str, index, matrix, key):
    center_is_empty = True
    for i in range(len(key)):
        for j in range(len(key[i])):
            if (key[i][j]):
                if (matrix[i][j] != "_"):
                    center_is_empty = False
                else:
                    matrix[i][j] = str[index]
                    index += 1

    return index

# Create cipher from string <href=str> to matrix
def create_cipher(str, matrix, key):
    index = 0
    for i in range(4):
        index = fill_matrix(str, index, matrix, key)
        rotate_matrix(key)

def get_key(classes_matrix, num_classes):
    size = len(classes_matrix)
    matrix_class_fill = [False for i in range(num_classes)]
    key = [[False for i in range(size)] for j in range(size)]
    classes_left = num_classes
    while (classes_left != 0):
        i = int(input("Enter the row: "))
        j = int(input("Enter the column: "))
        if (not matrix_class_fill[classes_matrix[i][j] - 1]):
            matrix_class_fill[classes_matrix[i][j] - 1] = True
            key[i][j] = True
            classes_left -= 1
        else:
            print("Incorrect element\n")

    return key

def get_str_from_matrix(key, matrix):
    size = len(matrix)
    str = ""
    for i in range(size):
        for j in range(size):
            if (matrix[i][j] == ""):
                continue
            if (key[i][j]):
                str += matrix[i][j]
                matrix[i][j] = ""

    return str

def decrypt_grille(str, key):
    size = math.ceil(math.sqrt(len(str)))
    decode_matrix = [list(str)[i: i + size] for i in range(0, len(str), size)]

    original_string = ""
    classes_matrix = [[0 for i in range(size)] for j in range(size)]
    rang = matrix_numerate(classes_matrix)
    for i in range(4):
        original_string += get_str_from_matrix(key, decode_matrix)
        rotate_matrix(key)

    return original_string.rstrip("_")

def generate_key(str):
    min_size = math.ceil(math.sqrt(len(str)))
    size = int(input("Enter key size: "))
    while (size < min_size):
        size = int(input("Enter key size: "))

    classes_matrix = [[0 for i in range(size)]
                      for j in range(size)]
    num_classes = matrix_numerate(classes_matrix)
    key = get_key(classes_matrix, num_classes)
    return key

def encrypt_grille(str, key):
    size = len(key)
    str += "_" * ((size * size) - len(str))
    result_matrix = [["_" for i in range(size)] for j in range(size)]
    create_cipher(str, result_matrix, key)
    result = ""
    for i in result_matrix:
        for j in i:
            result += j

    return result