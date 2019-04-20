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

print(inv(3,26))