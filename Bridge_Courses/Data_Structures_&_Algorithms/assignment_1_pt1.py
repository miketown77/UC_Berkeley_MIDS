###
## Q 1
## Question 1 - Part 1
## Write a script to compute how many unique prime factors an integer has.
## For example, 12 = 2 x 2 x 3, so has two unique prime factors, 2 and 3.
## Use your script to compute the number of unique prime factors of 1234567890.
import math

x = int(input("Enter an integer: "))
count = 0

while ((x % 2 > 0) == False):
    x = x/2
    count += 1

if (count > 0):
    print('Start')
    print(2, count)


for i in range (3,int(math.sqrt(x)) + 1):
    count = 0
    while (x % i == 0):
        count += 1
        x = int(x/i)
    if (count > 0):
        print('Inside For')
        print(i, count)
    i += 2


