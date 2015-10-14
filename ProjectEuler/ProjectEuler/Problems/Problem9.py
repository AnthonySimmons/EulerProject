

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2

#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

# sqrt(a^2 + b^2) = 1000 - a - b
# sqrt(a^2 + b^2) + a + b = 1000

from math import sqrt

def SolvesEquation(sum, a, b):
    result = sqrt(a * a + b * b) + a + b
    #print("a: {}, b: {}".format(a, b))
    return result == sum


def FindAandB(sum):
    for a in range(1, sum):
        for b in range(a + 1, sum):
            if SolvesEquation(sum, a, b):
                return a, b
    return 0, 0


def FindPythTriplets(sum):
    # c = sqrt(a^2 + b^2)
    a, b = FindAandB(sum)
    c = sqrt(a * a + b * b)
    return a, b, c

    
def Solve():
    sum = 1000
    a, b, c = FindPythTriplets(sum)
    print("{}^2 + {}^2 = {}^2".format(a, b, c))
    product = a * b * c
    print("Product: {}".format(product))
    return product