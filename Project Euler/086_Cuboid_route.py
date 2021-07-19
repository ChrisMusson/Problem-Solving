'''
A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F,
sits in the opposite corner. By travelling on the surfaces of the room the shortest
"straight line" distance from S to F is 10 and the path is shown on the diagram.

------------------------------------------------
----- https://projecteuler.net/problem=86 ------
------------------------------------------------

However, there are up to three "shortest" path candidates for any given cuboid and the
shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer
dimensions, up to a maximum size of M by M by M, for which the shortest route has integer length
when M = 100. This is the least value of M for which the number of solutions first exceeds two
thousand; the number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one million.
'''


# IDEA:
# The shortest path between the fly and the spider will be the hypotenuse of a 
# right-angled triangle on the unfolded net of the cuboid.  
# For a cuboid with side lengths x <= y <= z, the (base, height) of the triangle that
# that gives the shortest path will be (x + y, z).
#
# If this hypotenuse is integral, then we need to count how many x, y pairs could
# form this (x + y, z, hypotenuse) pythagorean triple while following x <= y <= z.
#
# If x + y <=z, then this is just (x + y) // 2
# If x + y > z, then this is z - (x + y - 1) // 2
# (can be best seen with an example such as x + y = 12, z = 9, hypotenuse = 15)


def main():
    target = 10**6
    z = 1
    count = 0
    while count < target:
        z += 1
        # x <= y <= z so x + y must be at least 1 + 1, and can be at most 2 * z
        for x_plus_y in range(2, 2 * z + 1):
            hypotenuse = (x_plus_y**2 + z**2)**0.5
            if hypotenuse == int(hypotenuse):
                if x_plus_y <= z:
                    count += x_plus_y // 2
                else:
                    count += z - (x_plus_y - 1) // 2
    return z


if __name__ == "__main__":
    print(main())

# Output: 1818
