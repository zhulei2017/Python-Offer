import sys

# rot


def print_line(matrix, start, rows, ret):
    row = rows - start - 1
    col = row
    # left->right
    for c in range(start, col + 1):
        ret.append(matrix[start][c])
    # top to bottom
    for r in range(start + 1, row + 1):
        ret.append(matrix[r][col])
    # right to left
    for c in range(start, col)[::-1]:
        ret.append(matrix[row][c])
    # bottom to top
    for r in range(start + 1, row)[::-1]:
        ret.append(matrix[r][start])
        ret_single = ret
    return ret_single

def print_circle(matrix, start, rows, ret):


def move_right(lis, k):
    return lis[k:] + lis[:k]


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    ans = 0
    j = 0
    res = []
    for i in range(n):
        temp = []
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        for v in values:
            temp.append(v)
        res.append(temp)
    m = int(sys.stdin.readline().strip())
    m_result = m % ((n-1)*4)

    ret = []
    ret_after = []
    start = 0
    while start * 2 < n:
        print_line(res, start, n, ret)
        ret_after = move_right(ret, (m % ((start*2-1)*4)))
        tmp =

