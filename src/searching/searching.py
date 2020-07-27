def linear_search(arr, target):
    # Your code here
    for i, data in enumerate(arr):
        if data == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr)-1
    while high >= low:
        middle = (low + high) // 2
        if arr[middle] == target:
            return middle
        else:
            if target < arr[middle]:
                high = middle - 1
            else:
                low = middle + 1
    return -1  # not found
