import math
def newton_polynomial(px=0,x=[],y=[], deg=0):
    coef = [0]*deg

    pass

def calculate_polynomial(x=0,div_table=[]):
    pass

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


def generate_uniform_samples(n=501):
    pass


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

#order3_coef = div_diff(x=[1,2,3,4,5,6,7,8,9,10],y=order2_coef,order=2)
#for coef in order2_coef:
#    print(coef)

