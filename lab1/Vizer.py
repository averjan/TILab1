def generate_key(str, key):
    key = list(key)
    if len(str) == len(key):
        return(key)
    else:
        key.append(str[0: len(str) - len(key)])
    return "".join(key).upper()
       
def encrypt_vizer(str, key):
    encrypted_str = []
    for i in range(len(str)):
        x = (ord(str[i]) +
             ord(key[i])) % 26
        x += ord('A')
        encrypted_str.append(chr(x))
    return "".join(encrypted_str)

def dercrypt_vizer(encrypted_str, key):
    original_string = []
    for i in range(len(encrypted_str)):
        x = (ord(encrypted_str[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        original_string.append(chr(x))
    return "".join(original_string)
