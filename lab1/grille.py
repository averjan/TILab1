import math
import copy

matrix_rang = []
rang_list = []
matrix_class_fill = []
bool_matrix = []
rang_matrix = []
result_matrix = []

def rotate(N, k):
    return ((j,N - 1 - i) for i,j in k)
 
def round_key(N, k, r):
    for _ in range(r):
        k = rotate(N, k)
    return  sorted(k)
 
def set_rang(matrix, rang, x, y):
    size = len(matrix)
    matrix[x][y] = rang
    matrix[y][size - 1 - x] = rang
    matrix[size - 1 - x][size - 1 - y] = rang
    matrix[size - 1 - y][x] = rang
    rang_list.append([(x, y), (y, size - 1 - x),
                      (size - 1 - x, size - 1 - y), (size - 1 - y, x)])
    return matrix

def matrix_numerate(matrix):
    size = len(matrix)
    rang = 1
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (matrix[i][j] == 0):
                matrix = set_rang(matrix, rang, i, j)
                rang += 1

    return rang - 1, matrix

def create_key(str):
    matrix_rang = math.ceil(math.sqrt(len(str)))
    N = range(matrix_rang)
    matrix = [[0 for i in range(matrix_rang)] for j in range(matrix_rang)]
    result_matrix = [["_" for i in range(matrix_rang)] for j in range(matrix_rang)]
    global bool_matrix
    bool_matrix = [[False for i in N] for j in N]
    rang = 1
    str += "_" * ((matrix_rang * matrix_rang) - len(str))
    matrix_class_fill = [False for i in range(matrix_rang)]
    rang, matrix = matrix_numerate(matrix)
    return matrix, result_matrix, str

def add_to_matrix(str, index, matrix):
    for j in key:
        if (matrix[j[0]][j[1]] == "_"):
            matrix[j[0]][j[1]] = str[str_index]
            index += 1
    return index, matrix

def rotate_matrix(matrix):
    N = len(matrix)
    for i in range(0, int(N / 2)): 
        for j in range(i, N-i-1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[N - 1 - j][i]
            matrix[N - 1 - j][i] = matrix[N - 1 - i][N - 1 - j]
            matrix[N - 1 - i][N - 1 - j] = matrix[j][N - 1 - i]
            matrix[j][N - 1 - i] = temp
    return matrix

# Fill the matrix with substring next characters on ciphering step
def fill_matrix(str, index, matrix, key, rang_matrix):
    center_is_empty = True
    for i in range(len(key)):
        for j in range(len(key[i])):
            if (key[i][j]):
                if (matrix[i][j] != "_"):
                    center_is_empty = False
                else:
                    matrix[i][j] = str[index]
                    index += 1
                    #matrix[i][j] = str[index - 1 + rang_matrix[i][j]]

    #if (not center_is_empty):
    #    index -= 1
    #return index + len(matrix), matrix;
    return index

# Create cipher from string <href=str> to matrix
def create_cipher(str, matrix, key, rang_matrix):
    index = 0
    key_matrix = copy.deepcopy(key)
    for i in range(5):
        #matrix = 
        index = fill_matrix(str, index, matrix, key_matrix, rang_matrix)
        key_matrix = rotate_matrix(key_matrix)

    return matrix

def get_key(rang_matrix):
    N = len(rang_matrix)
    matrix_class_fill = [False for i in N]
    key = [[False for i in N] for j in N]
    classes_left = len(rang_matrix)
    while (classes_left != 0):
        i = int(input("Enter the row: "))
        j = int(input("Enter the column: "))
        if (not matrix_class_fill[rang_matrix[i][j] - 1]):
            matrix_class_fill[rang_matrix[i][j] - 1] = True
            key[i][j] = True
            classes_left -= 1
        else:
            print("Incorrect element\n")

    return key

def get_str_from_matrix(key_matrix, matrix, rangs, rang_matrix):
    N = len(matrix)
    #str = [" " for i in range(rangs)]
    str = ""
    for i in range(N):
        for j in range(N):
            if (matrix[i][j] == ""):
                #str.pop
                continue
            if (key_matrix[i][j]):
                #str[rang_matrix[i][j] - 1] = matrix[i][j]
                str += matrix[i][j]
                matrix[i][j] = ""

    return str

def decrypt_grille(str, key_matrix):
    N = math.ceil(math.sqrt(len(str)))
    decode_matrix = [["" for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            decode_matrix[i][j] = str[(i * N) + j]

    original_str = ""
    rang_matrix = [[0 for i in range(N)] for j in range(N)]
    rang, rang_matrix = matrix_numerate(rang_matrix)
    for i in range(5):
        original_str += get_str_from_matrix(key_matrix, decode_matrix, rang, rang_matrix)
        rotate_matrix(key_matrix)

    return original_str.rstrip("_")

def encrypt_grille(str):
    rang_matrix, result_matrix, str = create_key(str)
    get_key(rang_matrix)
    result_matrix = create_cipher(str, result_matrix, bool_matrix, rang_matrix)
    result_string = ""
    for i in result_matrix:
        for j in i:
            result_string += j

    return result_string, bool_matrix