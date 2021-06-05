'''
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	T_n = n(n+1)/2    1, 3,  6, 10, 15, ...
Pentagonal	 	P_n = n(3n−1)/2	  1, 5, 12, 22, 35, ...
Hexagonal	 	H_n = n(2n−1)	  1, 6, 15, 28, 45, ...
It can be verified that T_285 = P_165 = H_143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''


def main():
    # All hexagonal numbers are also triangle numbers, so triangle numbers can be ignored
    h_n, p_n = 144, 166
    h = h_n * (2 * h_n - 1)
    p = p_n * (3 * p_n - 1) // 2
    # p increases at the rate 3n+1, h increases at the rate 4n+1
    # whichever one is smaller, increase it, and repeat until they are equal
    while True:
        if p == h:
            return p
        elif p < h:
            p += 3*p_n + 1
            p_n += 1
        else:
            h += 4*h_n + 1
            h_n += 1


if __name__ == "__main__":
    print(main())

# Output: 1533776805
