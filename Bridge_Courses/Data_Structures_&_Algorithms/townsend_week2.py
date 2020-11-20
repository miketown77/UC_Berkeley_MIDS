## Ask user to enter a number to compute which player has the winning strategy (1st or 2nd player)
n = float(input("Enter a float: "))

def winning_strategy(n):
    ## All numbers below n == 2 do not have the winning strategy
    if n < 2.0:
        return 0
    else:
        ## A number is "hot" if one of the two options produces a "cold" result for their opponent
        if ((winning_strategy(n-1) == 0) | (winning_strategy(n/2) == 0)):
            return 1
        ## If both options for advancing the game give your opponent a "hot" result, your opponent has the winning strategy
        else:
            return 0

## Returning 1 means you have the winning strategy & zero means your opponent does.
if (winning_strategy(n) == 1):
    print('1st Player has the winning strategy')
else:
    print('2nd Player has the winning strategy')
