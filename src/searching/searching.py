# STRETCH: implement Linear Search
def linear_search(arr, target):

    # TO-DO: add missing code
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1
    break_loop = False

    # TO-DO: add missing code
    while low < high:

        half = (low + high)//2

        if arr[half] == target:
            # Values equal each other? Return!
            return half
        elif arr[half] > target:
            # Halfway point is too big? Take the lower half
            high = half
        else:
            # Halfway point is too small? Take the upper half
            low = half + 1

        if break_loop:
            break

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
    if not low < high:
        # Still making sure to return -1 if we can't find the target
        return -1

    if arr[middle] == target:
        return middle
    elif arr[middle] > target:
        # Halfway point is too big? Take the lower half
        return binary_search_recursive(arr, target, low, middle)
    else:
        # Halfway point is too small? Take the upper half
        return binary_search_recursive(arr, target, middle+1, high)
