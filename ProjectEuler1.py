#If we list all the natural numbers below 10 that are multiples of 3 or 5,
#we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

sum = 0

for i in range(0,1000,3): #Adds all multiples of 3 below 1000
    sum += i

for i in range(0,1000,5): #Adds all multiples of 5 below 1000 that aren't a multiple of 3
    if i % 3 != 0:
        sum += i

print('The sum of all multiples of 3 or 5 below 1000 is ' + str(sum) + '.')
