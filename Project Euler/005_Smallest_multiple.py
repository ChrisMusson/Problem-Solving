def is_leap_year(year):
    if year % 4 == 0:
        if year % 400 > 0 and year % 100 == 0:
            return False
        else:
            return True
    else:
        return False

all_day = 0
sunday_cnt = 0
for year in range(1900, 2001):
    for month in range(1, 13):
        for day in range(1, 32):
            if month in [4, 6, 9, 11] and day > 30:
                break
            elif month == 2 and not is_leap_year(year) and day > 28:
                break
            elif month == 2 and is_leap_year(year) and day > 29:
                break
            else:
                all_day += 1
                if year >= 1901 and day == 1 and all_day % 7 == 0:
                    sunday_cnt += 1

print(all_day)
print(sunday_cnt)
