'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to
simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value,
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''
from fractions import Fraction


def is_digit_cancelling(a, b):
    '''returns whether or not the fraction a/b is a non-trivial digit-cancelling fraction'''
    w = int(str(a)[0])
    x = int(str(a)[1])
    y = int(str(b)[0])
    z = int(str(b)[1])

    if z == 0:
        return False
    if w == y:
        if x / z == a / b:
            return True
    if w == z:
        if x / y == a / b:
            return True
    if x == y:
        if w / z == a / b:
            return True
    if x == z:
        if w / y == a / b:
            return True
    return False


def main():
    num = 1
    denom = 1
    for a in range(10, 100):
        for b in range(a + 1, 100):
            if is_digit_cancelling(a, b):
                num *= a
                denom *= b
    return Fraction(num, denom).denominator


if __name__ == "__main__":
    print(main())

# Output: 100
