def f(x):
    return (x*x - x + 41)


def build_list(M):
    List = []
    i = 1
    while i <= M:
        List.append(f(i))
        i += 1
    return List


def isprime(N):
    i = 2
    while i*i <= N:
        if N%i == 0:
            return False
        i += 1
    return True

mylist = build_list(45)
for val in mylist:
    if isprime(val):
        print("{0} is prime.".format(val))
    else:
        print("{0} is NOT prime.".format(val))