import string
alphabet=[chr(i) for i in range(32,127)] 
lat_alpabhet=[i for i in string.ascii_uppercase] #латинский алфавит

def encrypt(plaintext: str, keyword: str) -> str:
    result=""
    line_with_kod=""
    new_keyword=""
    keyword=keyword.upper()
    for word in keyword: #проверка на нахождение букв ключа в лат. а.(если нету то игнор символа)
        if word in lat_alpabhet:
            new_keyword+=word
        else:
            pass
    
    while len(line_with_kod)<len(plaintext): #создание строчки длинной с plaintext из букв keyworda
        for word in new_keyword:
            if len(line_with_kod)<len(plaintext):
                line_with_kod+=word
        if len(line_with_kod)==len(plaintext):
            break
    
    for indx in range(len(plaintext)): #выполнение кодирования: индекс буквы из плэйнтекста(по алфавиту аске табле) + индекс буквы из строчки с буквами кейворда(по латинскому алфавиту)
        id1=alphabet.index(plaintext[indx])
        id2=lat_alpabhet.index(line_with_kod[indx])
        # print(id1,plaintext[indx])
        # print(id2,line_with_kod[indx])
        result+=alphabet[(id1+id2)%len(alphabet)] #добавление символа по индексу в алфавите(%длинны алфавита, чтобы не было list out of range)
    return result

def decrypt(ciphertext: str, keyword: str) -> str:
    result=""
    new_keyword=""
    line=""
    keyword=keyword.upper()
    for word in keyword: #проверка на нахождение букв ключа в лат. а.(если нету то игнор символа)
        if word in lat_alpabhet:
            new_keyword+=word
        else:
            pass
    while len(line)<len(ciphertext): #создание строчки длинной с ciphertext из букв keyworda
        for word in new_keyword:
            if len(line)<len(ciphertext):
                line+=word
        if len(line)==len(ciphertext):
            break
    for indx in range(len(ciphertext)): #выполнение декодирования: индекс буквы из ciphertextа(по алфавиту аске табле) + индекс буквы из строчки с буквами кейворда(по латинскому алфавиту)
        id1=alphabet.index(ciphertext[indx])
        id2=lat_alpabhet.index(line[indx])
        # print(id1,plaintext[indx])
        # print(id2,line_with_kod[indx])
        result+=alphabet[(id1-id2)%len(alphabet)]
    return result
encr=encrypt("attack at dawn", "LEMON")
print(encr)
print(decrypt(encr,"LEMON"))