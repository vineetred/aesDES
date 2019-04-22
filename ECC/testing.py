
def exponent(num,e,n):
    if((e&1)==1):
        remainder = num%n
    else:
        remainder = 1
    e //=2

    while(e>0):
        num = (num*num) % n
        if((e&1)==1):
            remainder = (remainder*num)%n
        e//=2
    return remainder

def find_Y(point):
    p,a,b = 11,3,3

    condition = exponent(a, ((p-1)//2), p)
    print(condition)
    if (condition == 1 ): #Eulers criterion to check if point is a quadratic residue of p
        a,u = (pow(point,3) + a*point + b),0
        flag = True
        
        while (flag == True):
            u = u + 1
            if (exponent(u, int((p-1)/2), p) != 1):
                flag = False 
        s,variable = 0,p-1
        while ((variable % 2) == 0):
            s = s + 1
            variable = (variable/2)

        t,k = variable,s
        z = exponent(u, int(t), p)
        point = exponent(a, int((t+1)/2), p)
        b = exponent(a, int(t), p)
        while (b != 1 % p):
            m = 1
            variable = pow(b,pow(2,m))
            while ((variable - 1) % p != 0):
                m +=1

            y = exponent(2, (k-m-1), p)
            z = exponent(y,2,p)
            b = b*z % p
            point = point*y % p
            k = m
        return point
    else :
        return ("Y does not exist for given x =",point)
# p,a,b = 59,17,5
print(find_Y(9))

def return_EC_pt(x): #implement Shanks Algorithm
    # p,a,b = read_EC_param()
    p,a,b = 11,3,3
    u = 0
    a = (x**3 + a*x + b)
    #check if it is a QR
    if (pow(a, (p-1)/2, p) == 1): #Eulers criterion
        pass
    else :
        return ("y cord does not exist")

    QR_flag = True
    
    while (QR_flag == True):
        u +=1
        if (pow(u, (p-1)/2, p) != 1): #Eulers criterion
            QR_flag = False 
    s = 0
    term = p-1    
    while (term % 2 == 0):
        s +=1 
        term = term/2

    t = term
    k = s
    z = pow(u, t, p)
    x = pow(a, (t+1)/2, p)
    b = pow(a, t, p)
    while (b != 1 % p):
        m = 1
        term = b**(2**m)
        while ((term - 1) % p != 0):
            m +=1

        y = pow(2, (k-m-1), p)
        z = pow(y,2,p)
        b = b*z % p
        x = x*y % p
        k = m
    return x
# print(find_Y(9))

def legendre(a, p):
    return pow(a, (p - 1) // 2, p)
print(legendre(9,11))