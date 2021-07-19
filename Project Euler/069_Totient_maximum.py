'''
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine
the number of numbers less than n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9) = 6.

n   Relatively Prime   φ(n)   n/φ(n)
2   1                  1      2
3   1,2                2      1.5
4   1,3                2      2
5   1,2,3,4            4      1.25
6   1,5                2      3
7   1,2,3,4,5,6        6      1.1666...
8   1,3,5,7            4      2
9   1,2,4,5,7,8        6      1.5
10  1,3,7,9            4      2.5

It can be seen that n = 6 produces a maximum n / φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
'''


# IDEA
# # https://en.wikipedia.org/wiki/Euler%27s_totient_function#Euler.27s_product_formula
# phi(n) = n * (product( 1 - (1 / p) ) for all distinct p such that p divides n)
# so maximising n / phi(n) === minimising product( 1 - (1 / p) ) for all p such that p divides n
#
# Similar idea to the sieve of Eratosthenes
# Have two 10**6 + 1 length arrays, one containing all False (A), the other all 1 (B)
# Starting at 2, go to every 2nd element of array A and mark it as true to denote having visited that index
# Starting at 2, go to every 2nd element of array B and multiply by (1 - 1/2) to update product
# Starting at 3, go to every 3rd element of array A and mark it as true to denote having visited that index
# Starting at 3, go to every 3rd element of array B and multiply by (1 - 1/3) to update product
# Skip 4 because already visited by 2
# Starting at 5, ...
# etc.


def main():
    N = 10**6

    # keeps track of which indices have been visited by previous primes
    visited = [False] * (N + 1)

    # keeps track of product of (1 - 1 / p)s
    product = [1] * (N + 1)

    p = 2
    while p <= N:
        if not visited[p]:  # new prime p found
            # visit each position in array that is at index of a multiple of p
            for i in range(p, N + 1, p):  
                visited[i] = True
                product[i] *= (1 - 1 / p)
        p += 1

    return product.index(min(product))


if __name__ == "__main__":
    print(main())

# Output: 510510
