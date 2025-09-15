def is_prime(n):
    if len(delit(n))==2:
        return True
    else:
        return False

def multiplicative_inverse(e: int, phi:int) -> int:
    if gcd(e,phi)==1:
        return True
    False

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
    n=p*q
    phi=(p-1)*(q-1)
    e=65537
    d=multiplicative_inverse(e,phi)
    return ((e,n),(n,d))
        