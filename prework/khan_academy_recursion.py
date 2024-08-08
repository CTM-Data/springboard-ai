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


def recursive_factorial(n):
    # base case: 
    if n == 0 or n == 1: 
        print(1)
    # recursive case: 
    else:
        print(n * factorial(n-1))

print(recursive_factorial(5))


def is_palindrome(string):
    # base case: 
    if len(string) == 0 or len(string) == 1:
        return True
    if string[0] != string[-1]:
        return False
    elif string[0] == string[-1]:
        substring = string[1:-1]
        return is_palindrome(substring)
    else:
        return False

word = 'taat'
print(f'is {word} a palidrome?', is_palindrome(word))



