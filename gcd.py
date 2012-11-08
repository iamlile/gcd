####
# GCD calculator using euclidean algorithm
# author: charles taylor
####


####
#  Euclid_gcd - finds the GCD of two integers
#  @param x - is the first integer
#  @param y - is the second integer
####

def euclid_gcd(x,y) :
    new_gcd = y
    remainder = x % y
    #print x,y, new_gcd, remainder
    if(remainder != 0) :
        new_gcd = euclid_gcd(y,remainder)
    return new_gcd
    

###
# Extended euclidean algorithm psuedocode
# wikipedia has a great example:
# function extended_gcd(a, b)
#    if b = 0
#        return (1, 0)
#    else
#        (q, r) := divide (a, b)
#        (s, t) := extended_gcd(b, r)
#        return (t, s - q * t)
###

def extended_gcd(x, y):
    if x == 0:
        return (0, 1)
    else:
        z, w = extended_gcd((y % x), x)
        print x, y, x, y
        return (w - int(y / x) * z, z)
    
    
