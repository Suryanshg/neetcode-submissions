from typing import List

def binary_search(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (r + l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


# Driver code
if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert binary_search(my_list, 7) == 6


    print("All tests passing!")