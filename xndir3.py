def factorial(x):
    r = 1
    for i in range(1,x+1):
        r*=i
    return r
print(factorial(5))