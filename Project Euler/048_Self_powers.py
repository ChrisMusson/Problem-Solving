'''
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.
Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
'''


def main():
	total = 0
	for a in range(1, 1001):
		total += int(str(a**a))

	return int(str(total)[-10:])


if __name__ == "__main__":
	print(main())

# Output: 9110846700
