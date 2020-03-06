def Fibonacci_series(n):

    if n == 0 :
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else :
        return Fibonacci_series(n-1) + Fibonacci_series(n-2)


for n in range(0,30):
     print(Fibonacci_series(n))