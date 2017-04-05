#Find the difference between the sum of the squares of the first one hundred
#natural numbers and the square of the sum.

def sumSquares(low,high): #Sums the squares of natural numbers 1-100
    z = 0
    for x in range(low,high,+1):
        z = z + x*x
    return z

def squareSum(low,high): #Squares the sum of natural numbers 1-100
    z = 0
    for x in range(low,high,+1):
        z = z + x
    return z*z

print('The difference between the sum of the squares and the square of the sum of the first 100 natural numbers is ' + str(squareSum(1,101) - sumSquares(1,101)) + '.')
