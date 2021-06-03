'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
(changed these numbers to be in the file '013_nums.txt')
'''

# This wouldn't be possible with most languages and you would need to reduce each number to its first 11 digits before
# attempting to sum them. However, in python, it can just be done straight away


def main():
    with open("013_nums.txt", "r") as f:
        numbers = [int(x.strip()) for x in f.readlines()]
        # numbers = [int(x.strip()[:11]) for x in f.readlines()]  # example implementation of reducing the numbers beforehand
    return int(str(sum(numbers))[:10])


if __name__ == "__main__":
    print(main())

# Output: 5537376230
