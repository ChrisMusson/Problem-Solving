'''
An irrational decimal fraction is created by concatenating the positive integers:

0.12345678910*1*112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''


def main():
    multiplier = 1
    total_digits = 0
    n = 1
    for i in range(7):
        while total_digits < 10**i:
            total_digits += len(str(n))
            n += 1
            # index into the previous number by the correct amount and multiply
        multiplier *= int(str(n-1)[10**i - total_digits - 1])
    return multiplier


if __name__ == "__main__":
    print(main())

# Output: 210
