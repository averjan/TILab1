def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else:
        key.append(string[0: len(string) - len(key)]) 
    return "".join(key).upper()
       
def cipherText(string, key): 
    cipher_text = []
    for i in range(len(string)): 
        x = (ord(string[i]) + 
             ord(key[i])) % 26
        x += ord('A') 
        cipher_text.append(chr(x)) 
    return "".join(cipher_text)

def originalText(cipher_text, key): 
    orig_text = [] 
    for i in range(len(cipher_text)): 
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A') 
        orig_text.append(chr(x)) 
    return "".join(orig_text)