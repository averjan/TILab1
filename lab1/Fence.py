def encrypt_fence(str, key):
    period = 2 * (key - 1)
    result = [""] * len(str)
    for i in range(len(str)):
        remainder = i % period
        row = key - 1 - abs(key - 1 - remainder)
        result[row] += str[i]

    return "".join(result);

def decrypt_fence(str, key): 
    matrix = [[None for i in range(len(str))] for j in range(key)]
    decrease = False
    row, col = 0, 0
    result = []
    index = 0
      
    for i in range(len(str)):
        if row == 0:
            decrease = True
        if row == key - 1:
            decrease = False
          
        matrix[row][col] = 0
        col += 1
        if decrease:
            row += 1
        else:
            row -= 1
              
    for i in range(key):
        for j in range(len(str)):
            if ((matrix[i][j] == 0) and (index < len(str))):
                matrix[i][j] = str[index]
                index += 1
      
    row, col = 0, 0
    for i in range(len(str)):
        if row == 0:
            decrease = True
        if row == key-1:
            decrease = False
               
        result.append(matrix[row][col])
        col += 1
              
        if decrease:
            row += 1
        else:
            row -= 1

    return "".join(result)

