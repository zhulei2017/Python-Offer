def find_number_with_sum(nums, s):
    if not nums:
        return None
    i, j = 0, len(nums)-1
    total = nums[i] + nums[j]
    while i < j:
        total = nums[i] + nums[j]
        if total > s:
            j -= 1
        elif total < s:
            i += 1
        else:
            return [nums[i], nums[j]]
    return None


if __name__ == "__main__":
    test = [1, 2, 4, 7, 11, 15]
    print(find_number_with_sum(test, 15))
