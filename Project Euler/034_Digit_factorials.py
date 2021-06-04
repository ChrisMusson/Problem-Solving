'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
'''

from math import factorial
from itertools import combinations_with_replacement
from collections import Counter

# similar to the logic in problem 030, a number can't have 8 digits because 8 * 9! = 2,903,040 < 10**7
# 7 * 9! = 2,540,160, so it is sufficient to check up to there

'''
# # brute force method 1 - about 3.5 seconds on my pc
# def main():
#     total = 0
#     for i in range(3, 2540161):
#         fact_sum = 0
#         for let in str(i):
#             fact_sum += factorial(int(let))
#         if fact_sum == i:
#             total += i
#     return total
'''

# method 2 - about 70ms on my pc
# idea is to generate all unique unordered combinations of digits and calculate their digit factorial sum,
# and then check if that sum's digits are some permutation of the original digits
# This reduces the number of times you need to calculate the factorial sum from
# 2,500,000 to < 20,000

# precalculate the factorials for a very minor speed improvement
factorials = {str(x): factorial(x) for x in range(10)}


def generate_combinations(min_digits, max_digits):
    all_combinations = []
    for i in range(min_digits, max_digits + 1):
        [all_combinations.append(x) for x in combinations_with_replacement("0123456789", i)]
    return all_combinations


def main():
    total = 0
    for comb in generate_combinations(2, 7):
        fact_sum = sum([factorials[x] for x in comb])
        if Counter(comb) == Counter(str(fact_sum)):
            total += fact_sum
    return total


if __name__ == "__main__":
    print(main())

# Output: 40730
