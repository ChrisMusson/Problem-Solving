'''
You have a test string S
Your task is to write a regex that will match S with the following conditions:

S must be of length: 20
character01: lowercase letter.
character02: word character.
character03: whitespace character.
character04: non word character.
character05: digit.
character06: non digit.
character07: uppercase letter.
character08: letter (either lowercase or uppercase).
character09: vowel (a, e, i , o , u, A, E, I, O or U).
character10: non whitespace character.
character11: should be same as 1st character.
character12: should be same as 2nd character.
character13: should be same as 3rd character.
character14: should be same as 4th character.
character15: should be same as 5th character.
character16: should be same as 6th character.
character17: should be same as 7th character.
character18: should be same as 8th character.
character19: should be same as 9th character.
character20: should be same as 10th character.
'''

regex_pattern = r"^([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([a-zA-Z])([aeiouAEIOU])(\S)\1\2\3\4\5\6\7\8\9\10$"
