def reorderoddeven(arr):
    if len(arr) < 1:
        return
    pbegin = 0
    pend = len(arr)-1
    while pbegin < pend:
        while not is_even(arr[pbegin]):
            pbegin += 1
        while is_even(arr[pend]):
            pend -= 1
        if pbegin < pend:
            temp = arr[pbegin]
            arr[pbegin] = arr[pend]
            arr[pend] = temp


def is_even(num):
    if num & 1:
        return False
    return True


if __name__ == "__main__":
    test = [1, 2, 3, 4, 5]
    reorderoddeven(test)
    print(test)
