'''
The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''


def main():
    upper, sum_of_squares, square_of_sum = 100, 0, 0

    for x in range(1, upper + 1):
        sum_of_squares += x**2

    square_of_sum = (upper * (upper + 1) // 2)**2
    return abs(square_of_sum - sum_of_squares)


if __name__ == "__main__":
    print(main())

# Output: 25164150
