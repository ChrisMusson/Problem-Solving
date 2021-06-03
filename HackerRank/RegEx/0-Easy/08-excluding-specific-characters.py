'''
You have a test string S
Your task is to write a regex that will match S with the following conditions:
S must be of length 6.
First character should not be a digit
Second character should not be a lowercase vowel
Third character should not be b, c, D or F.
Fourth character should not be a whitespace character ( \r, \n, \t, \f or <space> ).
Fifth character should not be a uppercase vowel
Sixth character should not be a . or , symbol.
'''

regex_pattern = r"^\D[^aeiou][^bcDF]\S[^AEIOU][^\.\,]$"
