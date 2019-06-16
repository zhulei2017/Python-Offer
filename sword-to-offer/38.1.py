def get_first_k(nums, k):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left+right) // 2
        if nums[mid] == k:
            if (mid-1 > 0 and nums[mid-1] != k) or mid-1 == 0:
                return mid
            else:
                right = mid - 1
        elif nums[mid] > k:
            right = mid -1
        else:
            left = mid + 1
    return -1


def get_last_k(nums, k):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left+right) // 2
        if nums[mid] == k:
            if (mid < len(nums)-1 and nums[mid+1] != k) or mid == len(nums)-1:
                return mid
            else:
                left = mid + 1
        elif nums[mid] > k:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def get_num_of_k(nums, k):
    first = get_first_k(nums, k)
    last = get_last_k(nums, k)
    if first < 0 and last < 0:
        return 0
    if first < 0 or last < 0:
        return 1
    return last - first + 1


if __name__ == '__main__':
    test = [1, 2, 3, 3, 3, 3, 4, 5]
    print(get_num_of_k(test, 3))
