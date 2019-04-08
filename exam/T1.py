

def is_even(num):
    if num & 1:
        return False
    return True


if __name__ == "__main__":
    a = [5, 2]
    n = int(a[0])
    k = int(a[1])
    times = 0
    while k > 1:
        if is_even(n):
            n = int(n/2)
            k = k-1
            times = times + 1
        else:
            n = n-1
            times = times + 1
    while n > 0:
        n = n-1
        times = times + 1
    print(times)
