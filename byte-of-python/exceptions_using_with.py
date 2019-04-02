import time

with open("poem.txt") as f:
    for line in f:
        print(line, end=' ')
        time.sleep(2)
