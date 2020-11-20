###
## Q 1
## Question 1 - Part 2
## Write a script that prompts the user for their phone number, x. Then carry out the following steps:
### 1. Compute x minus the sum of the digits of x. Call this result y. (hint: to find the sum of the digits of x, check to see what x//10 and x%10 give you)
### 2. Compute the sum of the digits of y, and store the result back in y.
### 3. Repeat step 2 until y has just one digit, then display it.
### What answer do you get?

def x_minus_sum(x):
    y = x
    while (x != 0):
        y = y - x % 10
        x = x // 10
    return y

def sumOfDigits(x):
    sum = 0
    while (x != 0):
        sum = sum + x % 10
        x = x // 10
    return sum

x = int(input("Enter your phone number: "))
y = x_minus_sum(x)
print(y)
while int(y) > 9:
    y = sumOfDigits(y)
    print(y)










