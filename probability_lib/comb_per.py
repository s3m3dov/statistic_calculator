from math import factorial
def combination(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))
def permutation(n, r):
    return factorial(n)/factorial(n-r)