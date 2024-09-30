class FindRoot
    def newton_method(f,f_prime,x0,tol=10e-6):
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
            p1 =p0-f(p0)/f(p0)
            if abs(f(p1)-x0)<=tol:
                return p1


    def secant_method():
        pass
        

    def bisection_method():
        pass


f = lambda x:x**2
f_prime = lambda x:2*x
x = 2
print(FindRoot.newton_method(f,f_prime,x))

