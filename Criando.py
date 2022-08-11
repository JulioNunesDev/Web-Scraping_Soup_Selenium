import os
import sys


def teste(n):
    if n == 0: return 1
    return n * teste(n - 1)



ultimo = 1
penultimo = 1

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(9))

# "5" - F(4,3) -
# "4" - F(3,2) - 
# "3" - F(2,1) -
# "2" - F(2,1) -
# "1" - F(1,0)