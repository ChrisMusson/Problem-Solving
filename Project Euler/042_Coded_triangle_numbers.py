'''
The nth term of the sequence of triangle numbers is given by, tn = n(n+1)/2;
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical
position and adding these values we form a word value. For example, the word value
for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we
shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing
nearly two-thousand common English words, how many are triangle words?
'''


def score(word):
    return sum([ord(char) - 64 for char in word])


def main():
    with open("042_words.txt", "r") as f:
        words = f.read().replace('"', "").split(",")

    triangle_nums = [x * (x + 1) / 2 for x in range(1, 20)]

    count = 0
    for word in words:
        if score(word) in triangle_nums:
            count += 1
    return count


if __name__ == "__main__":
    print(main())

# Output: 162
