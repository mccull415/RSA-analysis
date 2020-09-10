"""
Program Documentation Header
## Name: Lukas McCullough
## rsa.py
##
## Purpose: rsa thingy
##
## Input: <what will the inputs to the program be>
##
## Output: <what information will the program output/return>
##
## Certification of Authenticity:
## <include one of the following>
## I certify that this lab is entirely my own work.
## I certify that this lab is my own work, but I discussed it with: <Name(s)>
##

"""
solvefor = input("enter what you are solving for (p,q,n,t,ct,d):")
def main(solvefor):
    tofind = solvefor
    if tofind == "p":
        q = int(input("enter the q value"))
        n = int(input("enter the n value"))
        return n / q
    if tofind == "q":
        p = int(input("enter the p value"))
        n = int(input("enter the n value"))
        return n / p
    if tofind == "n":
        q = int(input("enter the q value"))
        p = int(input("enter the p value"))
        return q * p
    if tofind == "t":
        q = int(input("enter the q value"))
        p = int(input("enter the p value"))
        n = q * p
        return (p-1)*(q-1)
    if tofind == "ct":
        pt = int(input("enter the pt value"))
        e = int(input("enter the e value"))
        n = int(input("enter the n value"))
        return (pt**e)%n
""" not done yet
    if tofind == "d":
        q = int(input("enter the q value"))
        p = int(input("enter the p value"))
        t = (q-1)*(p-1)
        e = int(input("enter the e value"))
        #print (t)
        #d = e**-1 (%t)
        d= (1//t)/e
        #d1 = e**-1
        #print (d1)
        #d = int(d1%t)
        #return ((e**-1)(y%t))
        print(d)
"""
print (main(solvefor))

#nc 2019shell1.picoctf.com 41419