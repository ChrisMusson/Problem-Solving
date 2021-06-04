'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120.

{20, 48, 52}, {24, 45, 51}, {30, 40, 50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''


def main():
    count = {}
    for a in range(1, 1000):
        for b in range(a, 1000):  # assume b >= a
            c = ((a**2) + (b**2))**0.5
            perim = int(a + b + c)
            if perim > 1000:  # no need to continue with this a if perim > 1000
                break
            if c == int(c):
                if str(perim) in count.keys():
                    count[str(perim)] += 1
                else:
                    count[str(perim)] = 1
    return max(count.keys(), key=(lambda k: count[k]))


if __name__ == "__main__":
    print(main())

# Output: 840
