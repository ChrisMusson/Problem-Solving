'''
You have a test string S
Your task is to match the pattern Xxxxxx
Here, x denotes a word character, and X denotes a digit.
S must start with a digit X and end with . symbol.
S should be 6 characters long only.
'''

regex_pattern = r"^\d\w{4}\.$"
