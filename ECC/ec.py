import numpy as np
import math

file = open("variables.txt", 'r')
contents = file.read().split(" ")
file.close()
p = int(contents[0])
a = int(contents[1])
b = int(contents[2])

infinity = [-1,-1]

def bits(n):
    while n:
        yield n & 1
        n >>= 1

def ext_GCD(arg1, arg2):
    prevRemain, remainder = abs(arg1), abs(arg2)
    x, oldX, y, oldY = 0, 1, 1, 0
    while remainder:
        prevRemain, (quotient, remainder) = remainder, divmod(prevRemain, remainder)
        x, oldX = oldX - quotient*x, x
        y, oldY = oldY - quotient*y, y
    return prevRemain, oldX * (-1 if arg1 < 0 else 1), oldY * (-1 if arg2 < 0 else 1)

def inv(e, phi):
    g, x, y = ext_GCD(e, phi)
    if (g != 1):
	    raise Exception("No modular inverse exists")
    posans = (x%phi)
    return posans

def addition(arg1,arg2):
    if(arg1==[-1,-1] and arg2==[-1,-1]): #This is the infinity added to infinity
        return arg1
    '''
    This next construct is for when a point is added to the point
    at infinity
    '''
    if(arg1==[-1,-1]):
        return arg2
    if(arg2==[-1,-1]):
        return arg1
    '''
    Same X coordinate
    '''
    if(arg1[0]==arg2[0]):
        return infinity

    if(arg1[0]!=arg2[0]):
        inverse = inv((arg2[0]-arg1[0]),p)
        slope = ((arg2[1]-arg1[1])*inverse)%p   
        x_r = (pow(slope,2) - arg1[0] - arg2[0])%p
        y_r = (slope*(arg1[0]-x_r) - arg1[1])%p
        return [x_r,y_r]

def pointDoubling(arg1):
    inverse = inv(2*arg1[1],p)
    slope = (3*pow(arg1[0],2)+a)*inverse
    x_r = (pow(slope,2)-(2*arg1[0]))%p
    y_r = (slope*(arg1[0]-x_r)-arg1[1])%p
    return [x_r,y_r]

def multiplePoint(N,times):
    Q = [-1,-1]
    d = []
    for bit in bits(times):
        d.append(bit)
    for i in range(0,len(d)):
        if(d[i]==1):
            Q = addition(Q,N)
        N = pointDoubling(N)
    return Q

def negationPoint(point):
    return [point[0],(-point[1])%p]

def subtractionPoint(point1,point2):
    return addition(point1,negationPoint(point2))

def EC_Check(point): #function to check if given co-ordinates are part of EC or not
    x,y = point
    if(x>p or x<0 or y>p or y<0):
        return False
    flag = ((y**2 - (x**3 + a*x + b)))%p==0
    return flag

def functionCheck(xcord):
    y2 = (xcord**3 + a*xcord + b)%p
    y = math.sqrt(y2)
    return int(y)

def write_to_File(variable):
    file = open("output.txt", 'w')
    file.write(str(variable))
    file.close()

#Check addition
print(addition([15,53],[4,14]))

#Check negation
print(negationPoint([8,2]))

#Check point doubling

print(pointDoubling([4,14]))

#Check multiple point scalar multiplication
print("Point Double")
print(multiplePoint([8,2],26))

#Check Subtraction
write_to_File(subtractionPoint([15,53],[4,14]))

#Check if a point is on the curve
print(EC_Check([8,57]))