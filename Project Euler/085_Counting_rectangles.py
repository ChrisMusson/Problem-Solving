'''
By counting carefully it can be seen that a rectangular grid
measuring 3 by 2 contains eighteen rectangles:

------------------------------------------------
--- image shown on webpage depicts this well ---
--- https://projecteuler.net/problem=85 --------
------------------------------------------------

Although there exists no rectangular grid that contains exactly two million rectangles,
find the area of the grid with the nearest solution.
'''


def num_rectangles(height, width):
    # Every rectangle in the grid can be uniquely defined by two horizontal lines
    # and two vertical lines. There are [(height + 1) choose 2] horizontal lines,
    # and [(width + 1) choose 2] vertical lines. 
    return height * (height + 1) * width * (width + 1) / 4


def main():
    dimensions = (None, None)
    nearest = 9e99

    h, w = 1, 1  # initial height, width
    
    while True:
        rectangles = num_rectangles(h, w)
        difference = abs(rectangles - 2 * 10**6)

        if difference <= nearest:
            dimensions = (h, w)
            nearest = difference
        
        if rectangles > 2 * 10**6:
            if w == 1:
                # stopping condition is when an N x 1 rectangle contains more than 2 * 10**6 rectangles
                # since an N x 2 rectangle would contain even more, as would an (N + 1) x 1 rectangle
                break
            else:
                h += 1
                w = 1
        else:
            w += 1
    
    return dimensions[0] * dimensions[1]


if __name__ == "__main__":
    print(main())

# Output: 2772
