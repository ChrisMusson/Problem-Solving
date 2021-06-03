'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

# Could use a more efficient method of generating primes (such as the Sieve of Eratosthenes), but this simple method
# works in roughly two seconds so is good enough


def is_prime(n):
    ''' Returns True if n is a prime number, and False otherwise'''
    if n % 2 == 0:
        return False
    for x in range(3, int(n**0.5 + 1), 2):
        if n % x == 0:
            return False
    return True


def main():
    sum_ = 2  # account for 2 being prime
    for n in range(3, 2*10**6, 2):
        if is_prime(n):
            sum_ += n
    return sum_


if __name__ == "__main__":
    print(main())

# Output: 142913828922
