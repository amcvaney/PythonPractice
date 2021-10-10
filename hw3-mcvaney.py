
#user input value float
fp=float(input("Enter a floating point number grater than or equal to 1: "))

#user input value int
n=int(input("Enter a positive integer n: "))

#zero term of sequence
x=1

#calculating nth term 
for ith in range(1,n+1):
    #formula given in hw problem
    x=(x+(fp/x))/2

print("The nth term of sequence is {:0.8f}".format(x))
