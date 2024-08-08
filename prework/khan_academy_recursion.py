def factorial(n):
    result = 1
    for num in range(1, n+1):
        result *= num
    return result

fac5 = 5*4*3*2*1
fac5func = factorial(5)
print(f'5! the same? {fac5 == fac5func}')

fac0 = 1
fac0func = factorial(0)
print(f'0! the same: {fac0 == fac0func}')

