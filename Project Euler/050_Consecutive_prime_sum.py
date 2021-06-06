'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''


# IDEA:
# go through the primes from 2 until their sum is >= 10**6 to get an upper bound U of the length
# of the longest possible chain. Then, sum each chain of length U - 1 and check if any of these
# are primes below 10**6. If any one is, that's the answer. Otherwise, do the same for U - 2, etc.
# until a solution is foun

from sympy import sieve


def get_upper_bound(primes):
    counter = 0
    cumulative_sum = 0
    while cumulative_sum < 10**6:
        cumulative_sum += primes[counter]
        counter += 1

    return counter


def main():
    primes = list(sieve.primerange(2, 10**6))
    primes_set = set(primes)  # created for faster lookup in main loop
    U = get_upper_bound(primes) - 1

    while True:
        # OK to ascend in this loop because the question implies that there is a single
        # prime that is the sum of consec. primes with the maximum length
        # Also likely that the terms in the final sum will be low, so ascending should be slightly faster
        for i in range(len(primes) - U):
            p = sum(primes[i:i + U])
            if p >= 10**6:
                break
            if p in primes_set:
                return p
        U -= 1


print(main())

# Output: 997651
