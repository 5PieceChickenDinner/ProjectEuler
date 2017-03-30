#Each new term in the Fibonacci sequence is generated by adding the previous
#two terms. By starting with 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values do not exceed
#four million, find the sum of the even-valued terms.

Sum = 0 #Initialize sum to zero

x=1     #Set initial values of Fibonacci sequence
y=1
z=2

while z < 4000000:  #Sum even terms of Fibonacci sequence under 4,000,000
    if z % 2 == 0:
        Sum += z
    x = y
    y = z
    z = x + y

print('The sum of all even terms of the Fibonacci sequence not exceeding 4,000,000 is ' + str(Sum) + '.')
