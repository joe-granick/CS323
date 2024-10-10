import math
class FindRoot:
    def bisection_method(a,b,f,tol=10**-10):
        print(tol)
        k=0
        c=(a+b)/2
        fc = f(c)
        while abs(fc)>tol:
            c=((a+b)/2)
            fa=f(a)
            fb=f(b)
            fc=f(c)
            print("k: ",k)
            print("a: ", a, "b: ", b, "c: ", c)
            print("f(a): ", fa)
            print("f(b): ", fb)
            print("f(c): ", fc)
            print("f(a)xf(c): ", fa*fc)
            print("f(b)xf(c): ", fb*fc)
            print()
    

            if abs(fc)<tol: return c 
            if fa*fc<0:b=c
            else:a=c
            k+=1
        return c


#problem 1
a,b=.01,.05
monthly_payment=600
term=30
principle = 150_000
f=lambda rate: ((12*monthly_payment)/rate)*(1-(1+rate/12)**(-12*term))-principle
print("Bisection Method")
print()
FindRoot.bisection_method(a,b,f)

