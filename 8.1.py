def find_min(nums):
    if len(nums) <= 0:
        raise print("the nums is none")

    index1 = 0
    index2 = len(nums)-1
    indexmid = index1
    if nums[index1] < nums[index2]:
        return nums[index1]
    while nums[index1] >= nums[index2]:
        if index2 - index1 == 1:
            return nums[index2]
        if nums[index1] == nums[indexmid] & nums[index2] == nums[indexmid]:
            return mininorder(nums[index1:index2+1])
        indexmid = int((index1+index2)/2)
        if nums[index1] < nums[indexmid]:
            index1 = indexmid
        elif nums[indexmid] < nums[index2]:
            index2 = indexmid


def mininorder(nummin):
    result = nummin[0]
    for i in nummin:
        if result >= i:
            result = i
    return result


if __name__ == "__main__":
    num1 = [3, 4, 5, 1, 2]
    num2 = [1, 0, 1, 0, 1]
    print(find_min(num1))