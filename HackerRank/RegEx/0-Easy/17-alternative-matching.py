'''
Given a test string, S, write a RegEx that matches S under the following conditions:
S must start with Mr., Mrs., Ms., Dr. or Er..
The rest of the string must contain only one or more English alphabetic letters (upper and lowercase).
'''

regex_pattern = r"^(Mr|Mrs|Ms|Dr|Er)\.[a-zA-Z]+$"
