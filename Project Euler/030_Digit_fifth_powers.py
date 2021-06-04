'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

# any number that meets the criteria must be at most 6 digits, because if a number has 7 digits,
# the largest sum of 5th powers of its digits would be 7 * 9**5 = 413,343 < 10**. Therefore, checking
# numbers up to 6 * 9**5 = 354,294 is sufficient


def main():
    total = 0
    for i in range(2, 354295):  # 1 is not included as in the problem statement
        number = sum(int(x)**5 for x in str(i))
        if number == i:
            total += i
    return total


if __name__ == "__main__":
    print(main())

# Output: 443839
