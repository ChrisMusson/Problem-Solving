'''
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''


# This took a while to get my head around but in plain words
# create an array of length N+1 and set N[0]=1, all other indexes 0 (1 way to make 0; use 0 coins)
# take a coin value. Then, go to every later index in the array and ask "how many
# ways can I get to this current position after having just used this coin?"
# it will be as many times as the value currently in array[index - coin_value]
# so the total ways of reaching this index can be increased by that amount


def main():
    target_value = 200
    coin_values = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (target_value + 1)
    ways[0] = 1

    for coin_value in coin_values:
        for i in range(coin_value, target_value + 1):
            ways[i] += ways[i - coin_value]
    return ways[target_value]


if __name__ == "__main__":
    print(main())

# Output: 73682
