spisok=[chr(i) for i in range(32,126+1)] #len===95
def encrypt(plaintext: str, shift: int) -> str:
    result=""
    
    for element in plaintext:
        shifted_word=spisok[(spisok.index(element)+shift)%len(spisok)] #сдвиг строго внутри заданного алфавита(списка)
        # print(shifted_word,((ord(element)+shift)%len(spisok)),ord(element))
        result+=shifted_word
    return result
def decrypt(ciphertext: str, shift: int) -> str:
    result=""
    
    for i in ciphertext:
        idx=spisok.index(i)
        shifted_index=(idx-shift)%len(spisok)
        result+=spisok[shifted_index]
    return result
# shifting=-213
# encr=encrypt("Hello, World!", shifting)
# print(encr)
# print(decrypt(encr,shifting))
print(encrypt("Hello, World!", 3))
print(decrypt(encrypt("Hello, World!", 3),3))