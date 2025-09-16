import sys,string
lat_alp=[i for i in string.ascii_uppercase]
asci_alp=[chr(i) for i in range(32,126+1)]
def is_prime(n):
    if len(delit(n))==2:
        return True
    else:
        return False

def multiplicative_inverse(e: int, phi:int) -> int:
    for d in range(1,phi):
        if (e*d)%phi==1:
            return d


def delit(n):
    deli=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            deli.append(i)
            if n//i!=i:
                deli.append(n//i)
    deli.sort()
    return(deli)

def gcd(x,y):
    obsh_deliteli=[]
    delit_x=delit(x)
    delit_y=delit(y)
    for i in delit_x:
        if i in delit_y:
            obsh_deliteli.append(i)
    return(obsh_deliteli[-1])

# def f_eyler(n):
#     res=[]
#     for i in range(1,n+1):
#         if gcd(n,i)==1:
#             res.append(i)
#     return(len(res))

def generate_keypair(p: int, q: int):
    if q==p:
        return 0
    # if sys.getsizeof(p)>=2048 and sys.getsizeof(q)>=2048:
    n=p*q
    phi=(p-1)*(q-1)
    elements=[]
    for element in range(1,phi):
        if gcd(element,phi)==1 and element<phi and element>1:
            elements.append(element)
    e=elements[0]
    d=multiplicative_inverse(e,phi)
    return ((e,n),(n,d))

def encrypt(public_key: tuple, text: str):
    result=[]
    public_key=public_key[0]
    n=public_key[1]
    e=public_key[0]
    for i in text:
        M=asci_alp.index(i)
        C=(M**e)%n
        result.append(C)
    return result

def decrypt(private_key: tuple, cipher_list: list):
    result=""
    private_key=private_key[-1]
    n=private_key[0]
    d=private_key[1]
    for C in cipher_list:
        M=(C**d)%n
        word=asci_alp[M]
        result+=word
    return result
key=generate_keypair(61,53)
encr=encrypt(key,"Special chars: @#$%^&*()")
print(encr)
print(decrypt(key,encr))
 