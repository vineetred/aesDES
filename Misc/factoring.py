import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def exponent(num,e,n):
    if(int((int(e)&1))==1):
        remainder = num%n
    else:
        remainder = 1
    e //=2

    while(e>0):
        num = (num*num) % n
        if((int(e)&1)==1):
            remainder = (remainder*num)%n
        e//=2
    return remainder

def check_Member(n):
    num = random.randrange(0,(n-1))
    flag = 0
    while(flag!=0):
        flag = gcd(num,n)
    return num

def findFactor(n,e,d):

    s=0
    t = (e*d) - 1

    while (t%2==0):
        s = s + 1
        t = t/2

    b = 0
    check = True
    while (check == True):
        a = check_Member(n)
        b = exponent(a,t,n)
        while (exponent(b,2,n)) != 1:
            b = b*b%n
        if ((b%n!=1) and ((b+1)%n!=0)):
            check = False

    p = gcd(b-1,n)
    q = n/p
    return(int(p),int(q))

def modCheck(phi):
    temp = e*d
    if((temp%phi)==1):
        return True
    else:
        return False


e = 323
d = 539
n = 1501
p,q = findFactor(n,e,d)
print(p,q)
phi_n = (p-1)*(q-1)
print(modCheck(phi_n))