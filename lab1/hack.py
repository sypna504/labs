alphabet=[chr(i) for i in range(32,126+1)]
glasnie="EYUIOA"
sogl="QWRTPSDFGHJKLZXCVBNM"
rare_symbols="()%`@#$+=*/" 
never_symbols="~`^|\{[}]<>_'" + '"'
nums="0123456789"

def hack(ciphertext: str) -> tuple:
    result=[]
    for shift in range(1,25+1):
        line=""
        count_glassnoy=0
        count_rare_symbols=0
        coumt_never_symbols=0
        count_nums=0

        for word in ciphertext:
            new_idndx_word=(alphabet.index(word)-shift)%len(alphabet)
            new_word=alphabet[new_idndx_word]
            line+=new_word

            if new_word in nums:
                count_nums+=1
            if new_word in never_symbols:
                coumt_never_symbols+=1
            if new_word.upper() in glasnie:
                count_glassnoy+=1
            if new_word in rare_symbols:
                count_rare_symbols+=1

        if 0.25<=(count_glassnoy/len(line))<=0.5: #примерный эталонный процент нахождения гласныъ в слове(от 25% до 50%)
            sogl_global_count=0
            local_count=0

            for i in range(len(line)):
                if line[i].upper() in sogl:
                    local_count+=1
                    sogl_global_count=max(local_count,sogl_global_count)
                else:
                    local_count=0

            if len(line)>0:
                if 1<=sogl_global_count<=4:
                    if count_rare_symbols/len(line)<0.01: #процент встречи этих символов примерно меньше 1 процента
                        if coumt_never_symbols/len(line)<0.002: #шанс встречи не 0 но есть(<0.2%)
                            if count_nums/len(line)<0.01: #процент всетрчи чисел в английсом языке(<1%)
                                result.append((line,shift))
    return result 
    
print(hack(""""uv!-v!-n-"r!"-zr!!ntr-%v"u-p|zz|{-r{tyv!u-%| q!"""))