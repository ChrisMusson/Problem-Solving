'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that
28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called
abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written
as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers
greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest number that cannot be
expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

# I got the idea of how to do this in O(N) time and space complexity from
# https://stackoverflow.com/questions/51300360/


def sum_factors(x):
    total = 1
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            total += i
            div = x // i
            if i < div < x:
                total += div
    return total


def main():
    abundants = []  # abundant numbers as a sorted list
    abundants_set = set()  # abundant numbers as a set; the idea from stackoverflow
    total = 0
    for n in range(1, 21824):
        if sum_factors(n) > n:
            abundants.append(n)
            abundants_set.add(n)
        total += n  # add to total now and only take back away if it is an abundant sum
        for ab in abundants:
            if ab < n and (n - ab) in abundants_set:
                total -= n
                break
    return total


if __name__ == "__main__":
    print(main())

# Output: 4179871
