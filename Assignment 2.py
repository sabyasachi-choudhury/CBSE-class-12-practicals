"""Assignment 2"""

def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

num = int(input("Enter number whose factorial you wish to find: "))
result = factorial(num)
print(result)
