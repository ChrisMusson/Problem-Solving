'''
You have a test string S
Your task is to match the pattern xxxXxxxxxxxxxxXxxx
Here x denotes any word character and X denotes any non-word character.
'''

regex_pattern = r"\w{3}\W\w{10}\W\w{3}"
