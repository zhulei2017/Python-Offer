def bit_add(n1, n2):
    carry = 1
    while carry:
        s = n1 ^ n2
        carry = (n1 & n2) << 1
        n1 = s
        n2 = carry
    return n1


def bit_add2(n1, n2):
    carry = 1
    while carry:
        s = n1 ^ n2
        carry = 0xFFFFFFFF & (n1 & n2) << 1
        carry = -(~(carry -1) & 0xFFFFFFFF) if carry > 0x7FFFFFFF else carry
        n1 = s
        n2 = carry
    return n1


if __name__ == "__main__":
    test1, test2 = 5, 17
    print(bit_add(test1, test2))
    print(bit_add2(test1, test2))
