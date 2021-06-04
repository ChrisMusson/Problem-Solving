'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	 = 	0.5
1/3	 = 	0.(3)
1/4	 = 	0.25
1/5	 = 	0.2
1/6	 = 	0.1(6)
1/7	 = 	0.(142857)
1/8	 = 	0.125
1/9	 = 	0.(1)
1/10 = 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

# My idea is to do long division on 1 / x until a remainder repeats.
# Then it must be true that the decimal expansion repeats from that point,
# so the number of other remainders found between these 2 occurences of the remainder
# must be the cycle length


def cycle_length(x):
    '''returns the cycle length of 1 / x if it contains one'''
    remainders = set()
    rem = 1  # start off with 1.0000... in long division
    while rem > 0:
        while rem < x:
            rem *= 10  # multiply by 10 until x goes into rem at least once, as in long division
        rem %= x
        # if this remainder has already been seen, the decimal expansion must now start repeating
        if rem in remainders:
            return len(remainders)
        else:
            remainders.add(rem)
    # if rem ever becomes 0 then the decimal expansion has terminated, so the cycle length must be 0
    return 0


def main():
    max_cycle_length = 0
    max_x = 0
    for x in range(1, 1000):
        leng = cycle_length(x)
        if leng > max_cycle_length:
            max_cycle_length = leng
            max_x = x
    return max_x


if __name__ == "__main__":
    print(main())

# Output: 983
