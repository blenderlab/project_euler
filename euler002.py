def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

def euler002(maxi=40):
    
    somme=0
    n=1
    f=fib(n)
    while f<maxi:
        if f%2==1 :
            somme=somme+f
        n=n+1
        f=fib(n)
    return somme

print (euler002(maxi=4000000))