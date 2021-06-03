'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


def pythagorean_triplet_sum(n):
    '''Returns the product of the numbers of the first pythagorean triplet whose 3 elements sum to n'''
    for a in range(1, n):
        for b in range(a, n - a):
            c = n - a - b
            if a**2 + b**2 == c**2:  # if a, b, c form a pythagorean triplet
                return a * b * c


def main():
    return pythagorean_triplet_sum(1000)


if __name__ == "__main__":
    print(main())

# Output: 31875000
