'''
Using names.txt -*- I changed it to 022_names.txt -*- (right click and 'Save Link/Target As...'), a 46K text file containing
over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each
name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''


def main():
    with open("022_names.txt", "r") as f:
        names = sorted([x.replace('"', "") for x in f.read().split(",")])

    total_score = 0
    for i, name in enumerate(names, start=1):
        name_score = 0
        for letter in name:
            # All letters are capitals so can use the ASCII code minus 64
            name_score += ord(letter) - 64
        name_score *= i
        total_score += name_score
    return total_score


if __name__ == "__main__":
    print(main())

# Output: 871198282
