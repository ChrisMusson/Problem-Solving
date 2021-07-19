'''
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number
of positive numbers less than or equal to n which are relatively prime to n. For example,
as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109) = 79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10**7, for which φ(n) is a permutation of n and the ratio n / φ(n) produces a minimum.
'''


# Very similar thought process to 069
# Ends up taking roughly 20 seconds which isn't great, but I can't see a good way to improve.
# Almost all solutions I have since seen on the forum use the argument that the N that produces the minimum n / phi(n)
# should have few prime factors, so they just tested all products of 2 primes and found the answer.
# I don't consider this good enough reasoning so will stick to my solution unless I think of anything better


def main():
    N = 10**7

    # keeps track of which indices have been visited by previous primes
    visited = [False] * (N + 1)

    # keeps track of product of (1 - 1 / p)s
    product = {i: i for i in range(N + 1)}
    product[0] = 1

    for i in range(2, N + 1, 2):  
        visited[i] = True
        product[i] *= (1 - 1 / 2)

    p = 3
    while p <= N:
        if not visited[p]:  # new prime p found
            # visit each position in array that is at index of a multiple of p
            for i in range(p, N + 1, p):  
                visited[i] = True
                product[i] *= (1 - 1 / p)
        p += 2
    
    del product[0]
    del product[1]

    # create dict of ratio: n pairs so can easily find the minimum and query the dict with that
    mymap = {idx / round(prod): idx for idx, prod in product.items() if sorted(str(idx)) == sorted(str(round(prod)))}
    return mymap[min(mymap)]


if __name__ == "__main__":
    print(main())

# Output: 8319823
