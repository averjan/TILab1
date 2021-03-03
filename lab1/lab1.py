import Vizer;
import Fence;
import grille;
import Columnar;

str = input("Print string to encrype: ")

# Fence encrption
key = int(input("Print key: "))
res = Fence.encrypt_fence(str, key)
print(res)
print(Fence.decrypt_fence(res, key))

# Columnar
str_key = input("Enter the key for Columnar: ")
res = Columnar.encrypt_columnar(str, str_key)
print(res)
print(Columnar.decrypt_columnar(res, str_key))

# Vizer
str_key = Vizer.generateKey(str, str_key)
print(Vizer.cipherText(str, str_key))
print(Vizer.originalText(str, str_key))

# Grille
#grille_key = grille.get_key()
res, grille_key = grille.encrypt_grille(str)
print(res)
print(grille.decrypt_grille(res, grille_key))
