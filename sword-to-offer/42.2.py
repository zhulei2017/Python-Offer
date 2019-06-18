def left_rotate_string(sentence, n):
    if not sentence:
        return ''
    n %= len(sentence)
    return sentence[n:] + sentence[:n]


if __name__ == "__main__":
    test = 'abcdefg'
    num = 2
    print(left_rotate_string(test, num))
