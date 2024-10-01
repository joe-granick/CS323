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
            print(p1)
            if abs(p1-p0)<tol:
                return p1
            p0=p1


    def secant_method(f, x0,x1,tol=10**-6):
        p0,p1 = x0,x1

        while True:
            p2=p1-(f(p1)*(p1-p0))/(f(p1)-f(p0))
            print(p2)
            if abs(p2-p1)<tol:
                return p2
            p0=p1
            p1=p2


        

    def bisection_method(a,b,f,tol=10**-6):
        p1 = a+(b-a)/2 
        print(p1)
        if math.abs(f(p1)) <tol:return p1 
        if f(p1)>0:return bisection_method(a,p1,f,tol)
        else: return bisection_method(p1,b,f,tol)


#test newton_method
f = lambda x:x**2-2
f_prime = lambda x:2*x
x = 2
print(FindRoot.newton_method(f,f_prime,x))
print()
print(FindRoot.secant_method(f,2,1))
a,b=1,2
print(FindRoot.bisection_method(,2,1))
#problem 1
print("Problem 1")
f = lambda x:-(2*x)/math.e**(x/2)+1
f_prime = lambda x:(x/(math.e**(x/2)) - 2/(math.e**(x/2)))
x = 0
print("Newton's Method: ", FindRoot.newton_method(f,f_prime,x))
print()

#problem 2 
print("Problem 2")
f = lambda x:5-x**-1
f_prime = lambda x:1/(x**2)
x = (1/4)
print("Newton's Method: ",FindRoot.newton_method(f,f_prime,x))
print()
#problem 2
#f = lambda x:1-2*x*math.e**(-x/2)
#f_prime = lambda x:(x-2)*math.e**(-x/2)
#x = 0
#print(FindRoot.newton_method(f,f_prime,0))

#problem 3 
#f = lambda x:1-2*x*math.e**(-x/2)
#f_prime = lambda x:(x-2)*math.e**(-x/2)
#x = 0
#print(FindRoot.newton_method(f,f_prime,0))

#problem 4
#f = lambda x:1-2*x*math.e**(-x/2)
#f_prime = lambda x:(x-2)*math.e**(-x/2)
#x = 0
#print(FindRoot.newton_method(f,f_prime,0))

#problem 5
#f = lambda x:1-2*x*math.e**(-x/2)
#f_prime = lambda x:(x-2)*math.e**(-x/2)
#x = 0
#print(FindRoot.newton_method(f,f_prime,0))

#problem 6
#f = lambda x:1-2*x*math.e**(-x/2)
#f_prime = lambda x:(x-2)*math.e**(-x/2)
#x = 0
#print(FindRoot.newton_method(f,f_prime,0))

#problem 7
#f = lambda x:1-2*x*math.e**(-x/2)
#f_prime = lambda x:(x-2)*math.e**(-x/2)
#x = 0
#print(FindRoot.newton_method(f,f_prime,0))

#problem 8
#f = lambda x:1-2*x*math.e**(-x/2)
#f_prime = lambda x:(x-2)*math.e**(-x/2)
#x = 0
#print(FindRoot.newton_method(f,f_prime,0))

#problem 9
#f = lambda x:1-2*x*math.e**(-x/2)
#f_prime = lambda x:(x-2)*math.e**(-x/2)
#x = 0
#print(FindRoot.newton_method(f,f_prime,0))

#problem 10
#f = lambda x:1-2*x*math.e**(-x/2)
#f_prime = lambda x:(x-2)*math.e**(-x/2)
#x = 0
#print(FindRoot.newton_method(f,f_prime,0))


