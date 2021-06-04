'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''


def is_palindrome(input: str):
	return input == input[::-1]

def main():
	total = 0
	for x in range(1, 10**6):
		if is_palindrome(str(x)) and is_palindrome(str(bin(x))[2:]):
			total += x
	return total

if __name__ == "__main__":
	print(main())

 # Output: 872187
