# Name : Abigayle McVaney
# Homework 8

import math

# Q1)
def Newton(F, dF, x0, epsilon):

    error_flag = 0
    x_prev = x0
    x_cur = 0

    # Only 20 iterations 
    for i in range(1,21):
        
        Fx = F(x_prev)
        
        if(abs(Fx) < epsilon):
            return x_prev

        dFx = dF(x_prev)
        
        if(abs(dFx) < epsilon):
            print("\n Error occured - denominator less than tolerance")
            error_flag = 1
            break

        x_cur = x_prev - (Fx/dFx)
        x_prev = x_cur

    if (x_cur > 0):
        print("It is Divergent, because it took more than  20 iterations")
        
    return x_cur


# Q2)
def h(x):
    return (x**5 - x**4 + x**2 - 2*x + 1)
def dh(x):
    return ((5*(x**4)) - (4*(x**3)) + (2*x))

x = 5
xn = Newton(h , dh , x,  (1e-10))
if type(xn) is float:
    print("h(%1.8f) = %1.8f" % (xn , h(xn)))



# Q3)
def h1(x):
    return (x**2 - math.cos(2*x))

def dh1(x):
    return (3*(x**2) + 2*math.sin(2*x))

x = 1
xn = Newton(h1 , dh1 , x,  (1e-10))
if type(xn) is float:
    print("h(%1.8f) = %1.8f" % (xn , h1(xn)))

       
'''
Testing Code:
'''

def g1(t):
    return t**2 - 3
def dg1(t):
    return 2*t
x=2
xn = Newton(g1, dg1, x, 1e-10)
if type(xn) is float:
    print("g1(%1.8f) = %1.8f" % (xn, g1(xn)))




