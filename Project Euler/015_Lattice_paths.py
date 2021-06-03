'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

# There must be a total of 40 moves to end up at the bottom right, and you have to choose
# which 20 of those will be moves where you go right, with only one other option.
# This is the same as 40 choose 20, the binomial coefficient.


from math import factorial


def main():
    return factorial(40) // factorial(20)**2


if __name__ == "__main__":
    print(main())

# Output: 137846528820
