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
    if tofind == "d":
        q = int(input("enter the q value"))
        p = int(input("enter the p value"))
        t = (q-1)*(p-1)
        e = int(input("enter the e value"))
        n= p*q

        #d = ed%w = 1
        x = 1
        while((e * x)%t != 1):
            x = x+1


        print(x)

print (main(solvefor))
