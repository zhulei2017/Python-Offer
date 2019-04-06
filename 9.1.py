def fibonacci(n):
    result = [0, 1]
    if n < 2:
        return result[n]

    fibNMinusOne = 0
    fibNMinusTwo = 1
    fibN = 1
    while n:
        fibN = fibNMinusOne + fibNMinusTwo
        fibNMinusOne = fibNMinusTwo
        fibNMinusTwo = fibN
        n = n-1
    return fibN


if __name__ == "__main__":
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(4))
    print(fibonacci(5))
    print(fibonacci(6))




