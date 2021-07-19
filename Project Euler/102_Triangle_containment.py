'''
Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000,
such that a triangle is formed. Consider the following two triangles:
A(-340,495), B(-153,-910), C(835,-947)
X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt, a 27K text file containing the co-ordinates of one thousand "random" triangles,
find the number of triangles for which the interior contains the origin.
'''


# IDEA:
# Use the shoelace formula - https://en.wikipedia.org/wiki/Shoelace_formula - to calculate the area
# of the triangle described by the given points in two separate ways:
#   1: Use the shoelace formula on the 3 points given in the text file
#   2: Split the large triangle up into 3 smaller triangles, each time replacing one vertex with
#      the origin, and use the shoelace formula on these newly formed triangles. Then, take the sum
#      of these areas.

# If the sum of the areas of the smaller triangles is equal to the area of the larger triangle,
# then the origin lies on the interior of the triangle, otherwise, it is on the exterior.


def area_tri(tri):
    '''Implementation of the shoelace formula to return the area of a triangle'''
    term1 = (tri[0] * (tri[3] - tri[5]))
    term2 = (tri[2] * (tri[1] - tri[5]))
    term3 = (tri[4] * (tri[1] - tri[3]))

    determinant = term1 - term2 + term3

    return abs(determinant) / 2


def contains_origin(tri):
    '''Calculates whther the given triangle contains the origin, as explained in the IDEA section'''
    small_a = area_tri([0, 0] + tri[2:])
    small_b = area_tri(tri[:2] + [0, 0] + tri[4:])
    small_c = area_tri(tri[:4] + [0, 0])
    return (small_a + small_b + small_c) == area_tri(tri)


def main():
    count = 0
    with open("102_triangles.txt") as file:
        for line in file:
            tri = [int(x) for x in line.split(",")]
            if contains_origin(tri):
                count += 1
    return count


if __name__ == "__main__":
    print(main())

# Output: 228
