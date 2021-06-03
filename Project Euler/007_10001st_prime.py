'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''


def is_prime(n):
    ''' Returns True if n is a prime number, and False otherwise'''
    if n % 2 == 0:
        return False
    for x in range(3, int(n**0.5 + 1), 2):
        if n % x == 0:
            return False
    return True


def nth_prime(n):
    '''Returns the nth prime by checking all odd numbers 3 and above for primality'''
    count = 1  # Accounts for 2 being prime
    check = 1  # Ensures that the first number to be checked in the while loop will be 3
    while count < n:
        check += 2
        if is_prime(check):
            count += 1
    return check


def main():
    return nth_prime(10001)


if __name__ == "__main__":
    print(main())

# Output: 104743
