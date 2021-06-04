'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

# top left - bottom right diagonal = 1 + 3 + 7 + 13 + ..., nth term = n^2 - n + 1, want n in range 1-1001 inclusive
# centre - top right diagonal = 1 + 9 + 25 + 49 + ..., nth term = (2n-1)^2 (= 4n^2 - 4n + 1), want n in range 1 - 501 inclusive
# centre - bottom left diagonal = 1 + 5 + 17 + 37 + ..., nth term = (2n-2)^2 + 1 (=4n^2 - 8n + 5), want n in range 1-501 inclusive
# take off 2 as the 1 was counted 3 times


def main():
	total = 0
	for n in range(1,1002):
		total += n**2 - n + 1

	for n in range(1,502):
		total += 4 * n**2 - 4 * n + 1
		total += 4 * n**2 - 8 * n + 5

	return total - 2


if __name__ == "__main__":
	print(main())


# Output: 669171001
