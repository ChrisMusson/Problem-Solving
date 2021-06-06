'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit
numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this
property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''


from sympy import isprime as ip, sieve
from sympy.utilities.iterables import multiset_permutations as mp


def main():
	# lowest term can be no more than 3332 since the arithmetic sequence's 3rd term would then have 5 digits
	primes = sieve.primerange(1000, 3333)

	for prime in primes:
		# get the digit permutations of this prime that are larger than itself
		perms = [int("".join(x)) for x in mp(str(prime), 4) if int("".join(x)) > prime]
		
		# loop through these permutations and see if any 3 of them form an arithmetic progression,
		# as well as them all being primes
		# know that perms[i] < perms[j] < perms[k] because multiset_permutations returns an
		# increasing list with no repetitions, and i < j < k
		l = len(perms)
		for i in range(0, l - 2):
			for j in range(i + 1, l - 1):
				for k in range(j + 1, l):
					bool_1 = perms[k] - perms[j] == perms[j] - perms[i]
					bool_2 = ip(perms[i]) and ip(perms[j]) and ip(perms[k])
					if bool_1 and bool_2:
						return f"{perms[i]}{perms[j]}{perms[k]}"


if __name__ == "__main__":
	print(main())

# Output: 296962999629
