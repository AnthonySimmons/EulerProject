
#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^1000?
from math import pow
from Problem20 import SumOfDigits

def Solve():
    base = 2
    exp = 1000
    res = int(pow(base, exp))
    sum = SumOfDigits(res)
    print("\n{}^{}=\n{}\n".format(base, exp, res))
    print("Sum Of Digits = {}".format(sum))
    return sum