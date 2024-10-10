import math
class FindRoot:
    def newton_method(f,f_prime,x0,tol=10**-6):
        """
        approximates root of a function
        takes the function and divides by the derivative
        subtract result from initial guess and result should be  closer
        to true root
        assign result to new point, and perform same operation
        using the new estimate as the guess input
        after each input check the difference between the power of the
        estimated root and the number we are trying to find the root for 
        if the difference is within the set tolerance return the estkmate
        if not continue until within set tolerance level
        """
        p0=x0
        while True:
            p1=p0-((f(p0))/f_prime(p0))
            # print(p1)
            if abs(p1-p0)<tol:
                return p1
            p0=p1


    def secant_method(f, x0,x1,tol=10**-6):
        p0,p1 = x0,x1

        while True:
            p2=p1-(f(p1)*(p1-p0))/(f(p1)-f(p0))
            #print(p2)
            if abs(p2-p1)<tol:
                return p2
            p0=p1
            p1=p2


        

    def bisection_method(a,b,f,tol=10**-6):
        while ((b-a)/2)>tol: 
            p=((a+b)/2)
            # print(p)
            if abs(f(p))<tol: return p 
            if f(a)*f(p)<0:b=p
            else:a=p
        return p


#problem 1
print("Problem a")
f = lambda x:1-(2*x)*math.e**(-x/2)
f_prime = lambda x:(x/(math.e**(x/2)) - 2/(math.e**(x/2)))
x = 0
print("Newton's Method: ",FindRoot.newton_method(f,f_prime,x))
print()

x0,x1=x,1 
print("Secant Method: ",FindRoot.secant_method(f,x1,x0))
print()

a,b=x0,x1
print("Bisection Method: ",FindRoot.bisection_method(a,b,f))
print()

#problem 2 
print("Problem b")
f = lambda x:5-1/x
f_prime = lambda x:1/(x**2)
x = (1/4)
print("Newton's Method: ",FindRoot.newton_method(f,f_prime,x))
print()

x0,x1=x,(1/2) 
print("Secant Method: ",FindRoot.secant_method(f,x1,x0))
print()

a,b=0.1,x0
print("Bisection Method: ",FindRoot.bisection_method(a,b,f))
print()

#problem 3 
print("Problem c")
f = lambda x: (x**3)-(2*x)-5
f_prime = lambda x:3*(x**2)-2
x = 2
print("Newton's Method: ",FindRoot.newton_method(f,f_prime,x))
print()

x0,x1=x,5
print("Secant Method: ",FindRoot.secant_method(f,x1,x0))
print()

a,b=0.1,3
print("Bisection Method: ",FindRoot.bisection_method(a,b,f))
print()

#problem 4 
print("Problem d")
f = lambda x: (math.e**x-2)
f_prime = lambda x: (math.e**x)
x = 1
print("Newton's Method: ",FindRoot.newton_method(f,f_prime,x))
print()

x0,x1=x,5
print("Secant Method: ",FindRoot.secant_method(f,x1,x0))
print()

a,b=.1,1
print("Bisection Method: ",FindRoot.bisection_method(a,b,f))
print()

#problem 5 
print("Problem e")
f = lambda x: (x- 1/math.e**x)
f_prime = lambda x: (1/math.e**x+1)
x = 1
print("Newton's Method: ",FindRoot.newton_method(f,f_prime,x))
print()

x0,x1=x,5
print("Secant Method: ",FindRoot.secant_method(f,x1,x0))
print()

a,b=.1,1
print("Bisection Method: ",FindRoot.bisection_method(a,b,f))
print()

#problem 6 
print("Problem f")
f = lambda x: x**6-x-1
f_prime = lambda x: 6*x**5-1
x = 1
print("Newton's Method: ",FindRoot.newton_method(f,f_prime,x))
print()

x0,x1=x,5
print("Secant Method: ",FindRoot.secant_method(f,x1,x0))
print()

a,b=1,2
print("Bisection Method: ",FindRoot.bisection_method(a,b,f))
print()

#problem 7 
print("Problem g")
f = lambda x: x**2-math.sin(x)
f_prime = lambda x: 2*x-math.cos(x)
x = 1/2
print("Newton's Method: ",FindRoot.newton_method(f,f_prime,x))
print()

x0,x1=x,5
print("Secant Method: ",FindRoot.secant_method(f,x1,x0))
print()

a,b=x0,2
print("Bisection Method: ",FindRoot.bisection_method(a,b,f))
print()

#problem 8 
print("Problem h")
f = lambda x: x**3-2
f_prime = lambda x: 3*x**2
x = 1
print("Newton's Method: ",FindRoot.newton_method(f,f_prime,x))
print()

x0,x1=x,5
print("Secant Method: ",FindRoot.secant_method(f,x1,x0))
print()

a,b=1,2
print("Bisection Method: ",FindRoot.bisection_method(a,b,f))
print()

#problem 9 
print("Problem i")
f = lambda x: x+math.tan(x)
f_prime = lambda x: 1/(math.cos(x)**2)+1
x = 3
print("Newton's Method: ",FindRoot.newton_method(f,f_prime,x))
print()

x0,x1=3,5
print("Secant Method: ",FindRoot.secant_method(f,x1,x0))
print()

a,b=1,3
print("Bisection Method: ",FindRoot.bisection_method(a,b,f))
print()

#problem 10 
print("Problem j")
f = lambda x: 2-(math.log(x)/x)
f_prime = lambda x: math.log(x)/(x**2)-1/(x**2)
x = 1
#print("Newton's Method: ",FindRoot.newton_method(f,f_prime,x))
print()

x0,x1=(1/3),3
#print("Secant Method: ",FindRoot.secant_method(f,x1,x0))
print()

a,b=(1/3),3
print("Bisection Method: ",FindRoot.bisection_method(a,b,f))
print()


