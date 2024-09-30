class FindRoot:
    def newton_method(f,f_prime,x0,tol=10e-6):
        po=x0
        while True:
            p1 =p0-f(p0)/f(po)
            if abs(f(p1)-x0)<=tol:
                return p1


    def secant_method():
        pass
        

    def bisection_method():
        pass


f = lambda x:x**2
f_prime = lambda x:2*x
x = 2
print(newton_method(f,f_prime,x))

