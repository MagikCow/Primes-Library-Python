'''
Returns the greatest common divisor
of any amount of numbers
'''

def gcd(*args):

    numbers = list(args) # puts the inout arguments into a list
    n = max(numbers)

    
    for i in range(n, 0, -1): # generates a descending list from the biggest input number down to 1
        if all(num % i == 0 for num in numbers): # if all the (input numbers mod i) divide equally
            return i
