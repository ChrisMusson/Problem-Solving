'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''


# from now on I will be using sympy for prime-related things because it is easier and fast
import sympy


def filter_primes(x):
    # used to filter out primes that contain any even digits or 5, other than 2 and 5 themselves,
    # since none of these can be circular primes
    return x == 2 or x == 5 or set(map(int, str(x))).issubset(set([1, 3, 7, 9]))


def is_circular_prime(n):
    num = str(n)
    for i in range(0, len(num)):
        rotated_num = num[i:] + num[:i]
        if not sympy.isprime(int(rotated_num)):
            return False
    return True


def main():
    primes = filter(filter_primes, sympy.sieve.primerange(2, 10**6))
    total = 0
    for p in primes:
        if is_circular_prime(p):
            total += 1

    return total


if __name__ == "__main__":
    print(main())

# Output: 55
