'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously
remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''


from sympy import isprime
		

def is_truncatable(p: int):
	word = str(p)
	leng = len(word)
	ends = [2, 3, 5, 7]
	mids = [1, 3, 5, 7, 9]

	# must start and end in 3 or 7 generally, or also possibly 2 or 5 if a 2 digit number
	if p // 10**(leng - 1) not in ends or p % 10 not in ends:
		return False
	
	# central digits must be odd
	for i in range(1, leng - 1):
		if int(word[i]) not in mids:
			return False

	# must itself be prime
	if not isprime(p):
		return False

	# must be left truncatable
	for i in range(1, leng + 1):
		if not isprime(p % 10**i):
			return False

	# must be right truncatable
	for i in range(1, leng):
		if not isprime(p // 10**i):
			return False

	return True

def main():
	num_primes = 0
	total = 0
	i = 11
	while num_primes < 11:  # told in problem statement that only 11 exist
		if is_truncatable(i):
			total += i
			num_primes += 1
		i += 2
	return total

if __name__ == "__main__":
	print(main())

# Output: 748317
