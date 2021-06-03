'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''


def is_palindrome(n):
    return str(n)[::-1] == str(n)


def main():
    max_pal = -1
    for x in range(100, 1000):
        for y in range(x, 1000):
            prod = x * y
            if is_palindrome(prod) and prod > max_pal:
                max_pal = prod
    return max_pal


if __name__ == "__main__":
    print(main())

# Output: 906609
