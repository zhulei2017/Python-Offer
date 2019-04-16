def find_integer(matrix, num):
    """
    :param matrix: [[]]
    :param num: int
    :return: bool
    """
    if not matrix:
        return False
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols-1
    while col >= 0 and row <= cols-1:
        if matrix[row][col] == num:
            return True
        elif matrix[row][col] > num:
            col = col-1
        else:
            row = row+1
    return False


mat = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print(find_integer(mat, 123))
