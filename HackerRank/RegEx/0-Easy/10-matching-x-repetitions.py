'''
You have a test string S
Your task is to write a regex that will match S using the following conditions:

S must be of length equal to 45.
The first 40 characters should consist of letters(both lowercase and uppercase), or of even digits.
The last 50 characters should consist of odd digits or whitespace characters.
'''

regex_pattern = r"^[a-zA-z02468]{40}[13579\s]{5}$"
