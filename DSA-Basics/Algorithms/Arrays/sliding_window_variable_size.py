def max_sum_sliding_window(arr, k):
    # Use Initial window to get initial max_sum
    max_sum = 0
    for i in range(0, k):
        max_sum += arr[i]
    
    # Set window_sum to max_sum
    window_sum = max_sum
    for r in range(k, len(arr)):
        # Update window sum
        # Add value of new r and subtract value of old l (r - k)
        window_sum += arr[r] - arr[r - k]
        max_sum = max(window_sum, max_sum)

    return max_sum
    

# Driver code
if __name__ == '__main__':

    # TEST 1:
    arr = [5, 2, -1, 0, 3]
    k = 3
    expected = 6
    actual = max_sum_sliding_window(arr, k)
    if actual == expected:
        print("TEST 1 PASSED!")
    else:
        print("TEST 1 FAILED!")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")


    # TEST 2:
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    expected = 39
    actual = max_sum_sliding_window(arr, k)
    if actual == expected:
        print("TEST 2 PASSED!")
    else:
        print("TEST 2 FAILED!")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")