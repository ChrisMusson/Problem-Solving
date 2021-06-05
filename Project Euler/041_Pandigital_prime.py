'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''


# Can't be an 8- or 9-digit pandigital prime because the sum of 1-9 is 45 so is divisible by 3,
# and the sum of 1-8 is 36 so also divisible by 3

from sympy import isprime
from itertools import permutations


def generate_permutations(min_digits, max_digits):
    '''returns all integer permutations of 1-n digits without repetition and in descending order'''
    all_perms = []
    for i in range(min_digits, max_digits + 1):
        digits = "".join([str(x) for x in range(1, i + 1)])
        [all_perms.append(int("".join(x))) for x in permutations(digits, i)]
    return sorted(all_perms, reverse=True)


def main():
    # Since the permutations are in descending order, the loop
    # can terminate as soon as the first prime is found
    perms = generate_permutations(1, 7)
    for perm in perms:
        if isprime(perm):
            return perm


if __name__ == "__main__":
    print(main())

# Output: 7652413
