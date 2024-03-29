'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''


# I could use python's datetime module but I feel like that would defeat the purpose of this exercise

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def days_in_month(month, year):
    '''returns the number of days in the specified month, where Jan=1, Feb=2, etc.'''
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        return 28
    return 31


def main():
    days_passed = 0
    sunday_count = 0
    for year in range(1900, 2001):
        for month in range(1, 13):
            days_passed += days_in_month(month, year)
            # monday is 0 mod 7 from 1 Jan 1900 based on the first line in problem statement, so sunday must be -1 === 6 mod 7
            if year >= 1901 and days_passed % 7 == 6:
                sunday_count += 1
    return sunday_count


if __name__ == "__main__":
    print(main())

# Output: 171
