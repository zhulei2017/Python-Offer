import sys
if __name__ == "__main__":
    for line in sys.stdin:
        n = int(sys.stdin.readline().strip())
        ans = 0
        for i in range(n):
            line = sys.stdin.readline().strip()
            values = list(map(int, line.split()))
            for v in values:
                ans += v
        print(ans)


