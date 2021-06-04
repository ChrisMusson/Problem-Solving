'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier,
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.'
'''

# there must be 9 digits in total, so that must mean either a 1-digit * 4-digit = 4-digit qualifies,
# or a 2-digit * 3-digit qualifies. Can ignore 4x1 and 3x2 as symmetrical solutions are ignored


def is_pandigital(n1, n2, n3):
    n = str(n1) + str(n2) + str(n3)
    return set(n) == set("123456789")


def main():
    pan_products = set()  # set so I can add to it without worrying about duplicates

    # 1-digit * 4-digit = 4-digit
    for i in range(1, 10):
        for j in range(1000, 10000):
            prod = i * j
            if prod >= 10000:  # no longer interested if the product becomes 5 digits long
                break
            if is_pandigital(i, j, prod):
                pan_products.add(prod)

    # 2-digit * 3-digit = 4-digit
    for i in range(10, 100):
        for j in range(100, 1000):
            prod = i * j
            if prod >= 10000:
                break
            if is_pandigital(i, j, prod):
                pan_products.add(prod)

    return sum(pan_products)


if __name__ == "__main__":
    print(main())

# Output: 45228
