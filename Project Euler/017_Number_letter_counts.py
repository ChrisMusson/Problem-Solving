'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''


# Number of letters in numbers whose word form doesn't seem to follow any pattern
mydict = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8,
          15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}


def num_letters(x):
    def one_to_99(x):
        if 0 < x and x <= 20 or x % 10 == 0:
            return mydict[x]
        else:
            # e.g. 'fifty' + 'eight'
            return mydict[x - x % 10] + mydict[x % 10]

    def hundred_to_999(x):
        if x % 100 == 0:
            return mydict[x / 100] + 7  # e.g. 'nine' + 'hundred'
        else:
            # e.g. 'four' + 'hundred' + 'and' + 'twenty' + 'two'
            return mydict[(x - x % 100) / 100] + 7 + 3 + one_to_99(x % 100)

    if 0 < x and x < 100:
        return one_to_99(x)
    elif 100 <= x and x < 1000:
        return hundred_to_999(x)
    elif x == 1000:
        return 11
    else:
        return "Number not in range 1-1000"


def main():
    return sum([num_letters(x) for x in range(1, 1001)])


if __name__ == "__main__":
    print(main())

# Output: 21124
