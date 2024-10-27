import math
def coefficients(x=[],y=[], deg=0):
    """
    calculates coeffiecients for each degree polynomial
    """
    fx = [None]*(deg+1)
    fx[0]=y
    for i in range(1,deg+1):
        fx[i]=diff_col(x,fx[i-1],i)
    return fx

def polynomial_degree(px=0,x=[],coef=[]):
    """
    calculates 
    """
    deg = len(x)
    values = [0]*deg
    points = point_value(px,x,deg)
    for degree in range(deg):
        sum=0
        for i in range(degree):
            print(coef[i][0], " * ", points[i])
            sum += (coef[i][0]*points[i])
            print(sum)
        values[degree]=sum
    return values

def point_value(px=0,x=[],deg=0):
    """
    calculates point value of polynomial for each 
    additional degree polynomial imterpolated

    """
    points=[0]*(deg+1)
    points[0] = 1.0 
    #print(points[0])
    if deg == 0: return points
    # print(px, " - ", x[0])
    points[1]=(px-x[0])
    print(px-x[0])
    if deg == 1: return points
    for i in range(2,deg+1):
        points[i]=points[i-1]*(px-x[i-1])
        # print(points[i-1])
        # print(px, " - ", x[i-1])
        # print(points[i])
    return points

def div_diff(f_x1,f_x0, x1,x0):
    diff = (f_x1-f_x0)/(x1-x0)
    print("(", f_x1," - ", f_x0, ")", "/","(",x1, " - ", x0,")"," = ", diff) 
    return diff

def diff_col(x=[], y=[],deg=0):
    """     
        calculates coefficient for next order of polynomial
        f[x_(i),x_(i+1)] = (f[x_(i+1)]-f[x_(i+1)])/(x_(i+1)-x(i))   
    """
    fx = [0]*(len(y))
    for i in range(0,len(y)-deg):
        fx[i]=div_diff(y[i+1],y[i],x[i+deg],x[i])
        #print(fx[i])
    return fx

def generate_samples(n,f,x0,xn):
    """
    generates uniform sample distirbuton
    of x and f(x) between a given range
    for desired number of sample points n
    """
    x_sample=[0]*n
    y_actual=[0]*n
    for i in range(0,n):
        xi=x0+((xn-x0)*i/(n-1))
        x_sample[i]=xi
        y_actual[i]= f(xi)
    return x_sample,y_actual

def generate_dimensions(dim,x0,xn):
    n = len(dim)
    pd =[None]*n
    for _ in range(n):
        d=dim[_]
        i = (xn-x0)/d
        x=[0]*(d+1)
        xi=x0
        j=0
        while xi <= xn:
            x[j]=xi
            xi+=i
            j+=1
        pd[_]=x

x=[1,2,3,4,5,6,7,8,9,10]
y= [None]*len(x)
f = lambda x: x**2
for i in range(len(x)):
    y[i]=f(x[i])
    print("x: ", x[i], ", ", "y: ", y[i])

x =[1.0,1.3,1.6,1.9,2.2]
y=[0.7651977,0.6200860,0.4554022,0.2818186,0.1103623]
f_d1 = diff_col(x,y,1)
f_d2 = diff_col(x,f_d1,2)
f_d3 = diff_col(x,f_d2,3)
f_d4 = diff_col(x,f_d3,4)
fx = [y,f_d1,f_d2,f_d3,f_d4]
print()

for xi in x:print(xi, ",", end="")
print()
for yi in y:print(yi, ",", end="")
print()
for fi in f_d1: print(fi, ",", end="")
print()
for fi in f_d2:print(fi, ",", end="")
print()
for fi in f_d3:print(fi, ",", end="")
print()
for fi in f_d4:print(fi, ",", end="")
print()

points = point_value(1.5,x,4)
for px in points:print(px)

sum=0
for i in range(len(points)):
    print(fx[i][0], " * ", points[i])
    sum += (fx[i][0]*points[i])
    print(sum)

coef=coefficients(x,y,4)
for co in coef:
    print()
    for fx in co:
        print(fx, ",",end="")
px=1.5
poly=deg_val = polynomial_degree(px,x, coef)

for d in range(len(poly)):
    print(poly[d])

x0 =-1
xn=1
dim=[2,4,8,16,32]
generate_dimensions(dim,x0,xn)
n=501
f = lambda x: math.e**x
x0,xn=-1.0,1.0
x_sample,y_actual = generate_samples(n,f,x0,xn) 
for i in range(n):print("(",x_sample[i],",",y_actual[i],")")
