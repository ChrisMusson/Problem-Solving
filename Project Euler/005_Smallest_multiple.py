'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# lcm(a, b) = |a * b| / gcd(a, b)
# in python 3.9+, lcm is also in the math module, however I am using python 3.8
from math import gcd


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def main():
    final = 1
    for i in range(1, 21):
        final = lcm(final, i)
    return final


if __name__ == "__main__":
    print(main())

# Output: 232792560
