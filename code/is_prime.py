# Returns true or False
# Depending on weather the number is prime or not
#
# Usage:
# is_prime(n) where n is the number to determine primeness

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
            break
        if i == n - 1:
            return True
            break
