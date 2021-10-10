# hw2.py
# This program has many problems, and will NOT run as-is. 
# For part of this assignment, you need to correct it.

#Calculate the solution of a quadratic equation using user inputs for values a, b, and c.

print("If you put zero, this error will show: ZeroDivisionError: float division by zero.\nThis error is saying you cannot divide by zero.\n")

a = float(input("Please enter a value for a: "))
b = float(input("Please enter a value for b: "))
c = float(input("Please enter a value for c: "))

x1 = (-b + (  ((b**2) - (4*a*c))**(1/2)  )) /(2*a)
x2 = (-b - (  ((b**2) - (4*a*c))**(1/2)  )) /(2*a)

print ("value of x1: ", x1,"value of x2: ",x2)
