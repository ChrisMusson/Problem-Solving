'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

# Collatz is recursively called so it's a good idea to use a cache to stop repeating calculations


def Collatz(n, cache):
    if n in cache:
        return cache[n]
    if n % 2 == 0:
        cache[n] = Collatz(n // 2, cache) + 1
    else:
        cache[n] = Collatz(3 * n + 1, cache) + 1
    return cache[n]


def main():
    max_num_reached = 1
    max_i = 1
    cache = {1: 0}
    for i in range(1, 10**6):
        cache[i] = Collatz(i, cache)
        if cache[i] > max_num_reached:
            max_num_reached = cache[i]
            max_i = i
    return max_i


if __name__ == "__main__":
    print(main())

# Output: 837799
