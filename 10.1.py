def num_of_1(n):
    print("the binary of {} is {}".format(n, bin(n)))
    bits = 0
    while n:
        bits += 1
        n = (n-1)&n
    return bits


def num_of_1_2(n):
    print("the binary of {} is {}".format(n, bin(n)))
    ruler = 1
    count = 0
    for _ in range(32):
        if n & ruler:
            count += 1
        ruler = ruler << 1
    return count


if __name__ == "__main__":
    print(num_of_1(7))
    print(num_of_1_2(0x80000000))