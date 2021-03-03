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
    msg = "" 
  
    k_indx = 0
  
    msg_indx = 0
    msg_len = len(str)
    msg_lst = list(str) 
    key_dict = [[v, False] for v in key]
  
    col = len(key) 
      
    row = int(math.ceil(float(msg_len) / col)) 
    num_pad = (row * col) - msg_len
   
    key_lst = sorted(list(key)) 
  
    msg_lst.extend([None] * ((col * row) - msg_len))
    dec_cipher = [] 
    for _ in range(row): 
        dec_cipher += [[None] * col] 
   
    for i in range(col): 

        curr_idx = find_unused(key_dict, key_lst[i])
        key_dict[curr_idx][1] = True
  
        for j in range(row - 1 if curr_idx >= (col - num_pad) else row): 
            dec_cipher[j][curr_idx] = msg_lst[msg_indx] 
            msg_indx += 1
  
    for i in range(len(dec_cipher)):
        dec_cipher[i] = list(filter(None, dec_cipher[i]))
    msg = ''.join(sum(dec_cipher, [])) 

    return msg 
