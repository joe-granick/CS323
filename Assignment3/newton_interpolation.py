def newton_polynomial
    pass
def div_diff(x=[], y=[],f=lambda x: e**x, order = 1):
        """ 
        
        calculates coefficient for next order of polynomial
        
        """
    
    coef=[] #table of coefficients for degree polynomial
    for i in range(len(x)-1):
       coef[i] = (y[i+1] - y[i])/(x[i+1]-x[i])
        return coef


def generate_uniform_samples(n=501):
    pass
