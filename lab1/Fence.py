def encrypt_fence(str, key):
    period = 2 * (key - 1)
    post = [""] * len(str)
    for e in range(len(str)):
        rem = e % period
        row = key - 1 - abs(key - 1 - rem)
        post[row] += str[e]

    return "".join(post);

def decrypt_fence(str, key): 

    matrix = [[None for i in range(len(str))]  
                  for j in range(key)] 
      
    direction = None
    row, col = 0, 0
    result = [] 
    index = 0
      
    for i in range(len(str)): 
        if row == 0: 
            direction = True
        if row == key - 1: 
            direction = False
          
        matrix[row][col] = 0
        col += 1

        if direction: 
            row += 1
        else: 
            row -= 1
              
    for i in range(key): 
        for j in range(len(str)): 
            if ((matrix[i][j] == 0) and
               (index < len(str))): 
                matrix[i][j] = str[index] 
                index += 1
      
    row, col = 0, 0
    for i in range(len(str)): 
        if row == 0: 
            direction = True
        if row == key-1: 
            direction = False
               
        result.append(matrix[row][col]) 
        col += 1
              
        if direction: 
            row += 1
        else: 
            row -= 1
    return("".join(result)) 

