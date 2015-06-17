__author__ = 'Oliver'

# accepts number and returns True or False if the number is prime or not

def is_it_prime(num):
    if num % 2 == 0 and num != 2:
        return False
    elif num < 8:
        return True
    else:
        counter = range(9, num, 2)
        for next_num in counter:
            if num % next_num == 0:
                return False
        return True

print is_it_prime(209)
