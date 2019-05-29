def numofones(n):
    ones, m = 0, 1
    while m < n:
        ones += ((n // m + 8) // 10 * m) + (n % m + 1 if n//m % 10 == 1 else 0)
        m *= 10
    return ones


if __name__ == '__main__':
    print(numofones(12))