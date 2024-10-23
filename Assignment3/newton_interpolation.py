def newton_polynomial():
    pass
def div_diff(x=[], y=[],order=1):
    """     
        calculates coefficient for next order of polynomial    
    """
    n=len(x)
    coef=[None]*n #table of coefficients for degree polynomial
    for i in range(len(x)-1):
        print(i)
        coef[i] = (y[i+1]-y[i])/(x[i+1]-x[i])
    return coef


def generate_uniform_samples(n=501):
    pass

order2_coef = div_diff(x=[0,1,2],y=[0,2,4],order=2)
for coef in order2_coef:
    print(coef)
