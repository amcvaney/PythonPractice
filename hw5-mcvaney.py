def F3n1(N):
  if(N % 2 == 0):
    return N//2
  else:   
    return 3*N+1
  
def sequence(ret):
  seq = []
  while(ret != 1):
    ret = F3n1(ret) 
    seq.append(ret)
  return seq



N = int(input("Enter a positive integer N:"))
seq = sequence(N)
print("The resulting sequence is: {0}".format(seq)) 
print("It has length {0}".format(len(seq)))

