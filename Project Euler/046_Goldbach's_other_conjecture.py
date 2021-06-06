'''
It was proposed by Christian Goldbach that every odd composite number can be written
as the sum of a prime and twice a square.

 9 =  7 + 2×12
15 =  7 + 2×22
21 =  3 + 2×32
25 =  7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''


from sympy import isprime


def is_Goldbach(n):
    ''' returns whether n is of the from p + 2 * q**2 for some prime p and integer q'''
    if isprime(n):
        return True  # q = 0 / not a composite number
    i = 1
    while True:
        p = 2 * i**2
        if p > n:
            return False
        if isprime(n - p):
            return True
        i += 1


def main():
    n = 3
    while is_Goldbach(n):
        n += 2
    return n


if __name__ == "__main__":
    print(main())

# Output: 5777
