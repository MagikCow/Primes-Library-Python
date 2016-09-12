# Returns true or False
# Depending on weather the number is prime or not
#
# Usage:
# is_prime(n) where n is the number to determine primeness

import is_whole
import math


def is_prime(n):
    sqrt_n = int(math.sqrt(n) + 2)

    if n <= 1 or is_whole.is_whole(n) == False:  # If n is less than 1 or not whole
        return False

    if n == 2 or n == 3:
        return True

    else:
        if n % 6 == 1 or n % 6 == 5: # Al primes are of form (6k +- 1)

            for i in range(2, sqrt_n):  # generate list of all numbers up to sqrt(n)

                if n % i == 0:  # if n goes into i n is not prime
                    return False

                if i == (sqrt_n - 1):  # if this is reached no number between n is prime
                    return True
        else:
            return False
