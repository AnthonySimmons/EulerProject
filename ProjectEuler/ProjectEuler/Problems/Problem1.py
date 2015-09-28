import sys




#If we list all the natural numbers below 10 that are multiples of 3 or 5,
#we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.


def SumOfMultiples(vals, maxVal):
    sumVal = 0
    i = 0
    for i in range(1000):
        for val in vals:
            if (i % val == 0):
                sumVal += i
                break
    return sumVal

def Solve():
    maxVal = 1000
    vals = [3, 5]

    sumOf3sAnd5s = SumOfMultiples(vals, maxVal)
    print("Sum Of the multiples of 3's and 5's less than 1000: \n" + str(sumOf3sAnd5s))
    return sumOf3sAnd5s