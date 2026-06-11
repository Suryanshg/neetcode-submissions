
def two_sum_using_two_ptrs(arr, target):
    """
    Given an array `arr` and an integer `target`, return indices i and j
    such that i != j and arr[i] + arr[j] == target. The array `arr` is 
    sorted.
    """
    l = 0
    r = len(arr) - 1
    while l < r:
        if arr[l] + arr[r] == target:
            return l, r
        elif arr[l] + arr[r] < target:
            l += 1
        else:
            r -= 1
    return -1, -1



# Driver code
if __name__ == '__main__':

    # TEST 1:
    arr = [-3, -1, 0, 1, 2]
    target = -2
    expected = (0, 3)
    actual = two_sum_using_two_ptrs(arr, target)
    if actual == expected:
        print("TEST 1 PASSED!")
    else:
        print("TEST 1 FAILED!")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")