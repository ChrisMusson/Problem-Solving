'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''


def sum_divisors(x):
    total = 1  # Every integer will always have a proper divisor of 1
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            total += i + x // i
    return total


def main():
    total = 0
    for i in range(1, 10**4):
        sd = sum_divisors(i)
        if i == sum_divisors(sd) and sd != i:
            total += i
    return total


if __name__ == "__main__":
    print(main())

# Output: 31626
