a1 = [4, 1]
a2 = [5, 5, 7, 2]


if __name__ == "__main__":
    k =a1[1]
    while k > 0:
        a2order = sorted(a2)
        if a2order[0] == 0:
            print(0)
            k = k-1
        else:
            print(a2order[0])
            k = k-1