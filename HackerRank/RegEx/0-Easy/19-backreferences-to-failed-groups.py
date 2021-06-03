'''
You have a test string S
Your task is to write a regex which will match S, with following condition(s):
S consists of 8 digits.
S may have "-" separator such that string S gets divided in 4 parts, with each part having exactly two digits. (Eg. 12-34-56-78)
'''

regex_pattern = r"^\d\d(-?)\d\d\1\d\d\1\d\d$"
