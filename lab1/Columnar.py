import math;

def find_unused(vals, c):
    for i in range(len(vals)):
        if (vals[i][0] == c) and (not vals[i][1]):
            return i

def encrypt_columnar(str, key):
    result = ""
    str_len = len(str)
    str_list = list(str)
    key_list = sorted(list(key))
    key_dict = [[v, False] for v in key]
    num_col = len(key)
    index = 0
    row = int(math.ceil(float(str_len) / num_col))
    str_list.extend([None] * int((row * num_col) - str_len))
    matrix = [str_list[i: i + num_col] for i in range(0, len(str), num_col)]
    for i in range(num_col):
        index = find_unused(key_dict, key_list[i])
        key_dict[index][1] = True
        result += ''.join([row[index] if row[index] != None else ''
                           for row in matrix])
  
    return result

def decrypt_columnar(str, key):
    origin_string = ""
    str_index = 0
    str_len = len(str)
    str_list = list(str)
    key_dict = [[v, False] for v in key]
    col = len(key)
      
    row = int(math.ceil(float(str_len) / col))
    num_pad = (row * col) - str_len
   
    key_list = sorted(list(key))
  
    str_list.extend([None] * ((col * row) - str_len))
    decrypt_list = []
    for i in range(row):
        decrypt_list += [[None] * col]
   
    for i in range(col):
        curr_index = find_unused(key_dict, key_list[i])
        key_dict[curr_index][1] = True
        for j in range(row - 1 if curr_index >= (col - num_pad) else row):
            decrypt_list[j][curr_index] = str_list[str_index]
            str_index += 1
  
    for i in range(len(decrypt_list)):
        decrypt_list[i] = list(filter(None, decrypt_list[i]))

    origin_string = ''.join(sum(decrypt_list, []))

    return origin_string
