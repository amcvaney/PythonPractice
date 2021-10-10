# HW 4
# Abigayle McVaney  

M = int(input("Enter positive integer: "))
a = 0
b = 1 

while(1):
  a = a+1
  b = 1
  if(a**2 + b**2 > M):
    break

  while(a**2 + b**2 <= M):
    result = a**2 + b**2

    if(result == M):
      print("Pair found-> a = ", a, "b = ", b)
      
    if(result > M):
      break

    b = b+1

