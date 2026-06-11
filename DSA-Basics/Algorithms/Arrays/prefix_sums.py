def prefix_sum(arr):
    result = [arr[0]]
    sum_so_far = arr[0]
    for i in range(1, len(arr)):
        sum_so_far += arr[i]
        result.append(sum_so_far)
    return result


# Driver code
if __name__ == '__main__':

    # TEST 1:
    arr = [10, 20, 10, 5, 15]
    expected = [10, 30, 40, 45, 60]
    actual = prefix_sum(arr)
    if actual == expected:
        print("TEST 1 PASSED!")
    else:
        print("TEST 1 FAILED!")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")


    # TEST 2:
    arr = [30, 10, 10, 5, 50]
    expected = [30, 40, 50, 55, 105]
    actual = prefix_sum(arr)
    if actual == expected:
        print("TEST 2 PASSED!")
    else:
        print("TEST 2 FAILED!")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")