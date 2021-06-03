'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''


def max_prime_factor(n):
    '''Returns the largest prime factor of n'''
    max_ = 1
    while n % 2 == 0:
        max_ = 2
        n //= 2

    for i in range(3, int(n**0.5), 2):
        while n % i == 0:
            max_ = i
            n //= i

    return n if n > 2 else max_


def main():
    return max_prime_factor(600851475143)


if __name__ == "__main__":
    print(main())

# Output: 6857
