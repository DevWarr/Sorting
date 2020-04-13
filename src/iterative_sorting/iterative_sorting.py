def insertion_sort(arr):
    # ===========================================================
    # [5, 4, 7, 23, 8, 5, 3, 6, 4, 6] is our array
    #
    #  ↓ Is considered 'sorted'
    # [5,                       4, 7, 23, 8, 5, 3, 6, 4, 6]
    #
    # current_val = 4
    #  ↓ Is 4 less than 5?
    # [5,                       4, 7, 23, 8, 5, 3, 6, 4, 6]
    #
    # current_val = 4
    #  ↓ Is 4 less than 5? Yes  ↓ becomes 5, continue
    # [5,                       5, 7, 23, 8, 5, 3, 6, 4, 6]
    #
    # current_val = 4
    #  ↓ becomes 4     
    # [4,                       5, 7, 23, 8, 5, 3, 6, 4, 6]
    #
    #
    #
    #  ↓ Is now sorted           ↓ new current_val
    # [4, 5,                     7, 23, 8, 5, 3, 6, 4, 6]
    #
    # current_val = 7
    # Is  ↓ 7 less than 5?
    # [4, 5,                     7, 23, 8, 5, 3, 6, 4, 6]
    #
    # current_val = 7
    # Is  ↓ 7 less than 5? No    ↓ becomes 7, and we're done
    # [4, 5,                     7, 23, 8, 5, 3, 6, 4, 6]
    #
    #
    #
    #  ↓ Is now sorted           ↓ new current_val
    # [4, 5, 7,                  23, 8, 5, 3, 6, 4, 6]
    #
    # current_val = 23
    # Is 23  ↓ less than 7?
    # [4, 5, 7,                  23, 8, 5, 3, 6, 4, 6]
    #
    # current_val = 23
    # Is 23  ↓ less than 7? No    ↓ becomes 23, and we're done
    # [4, 5, 7,                  23, 8, 5, 3, 6, 4, 6]
    #
    #
    #
    #  ↓ Is now sorted           ↓ new current_val
    # [4, 5, 7, 23,              8, 5, 3, 6, 4, 6]
    #
    # current_val = 8
    # Is 8 less  ↓ than 23?
    # [4, 5, 7, 23,              8, 5, 3, 6, 4, 6]
    #
    # current_val = 8
    # Is 8 less  ↓ than 23? Yes  ↓ becomes 23, continue
    # [4, 5, 7, 23,              23, 5, 3, 6, 4, 6]
    #
    # current_val = 8
    # Is 8   ↓ less than 7?
    # [4, 5, 7, 23,              8, 5, 3, 6, 4, 6]
    #
    # current_val = 8
    # Is 8   ↓ less than 23? No
    # [4, 5, 7, 8,              23, 5, 3, 6, 4, 6]
    #           ↑ becomes 8, and we're done
    #
    #
    #
    #  ↓ Is now sorted             ↓ new current_val
    # [4, 5, 7, 8, 23,             5, 3, 6, 4, 6]
    #
    # current_val = 5
    # Is 5 less    ↓↓ than 23?
    # [4, 5, 7, 8, 23,             5, 3, 6, 4, 6]
    #
    # current_val = 5
    # Is 5 less    ↓↓ than 23? Yes
    # [4, 5, 7, 8, 23,            23, 3, 6, 4, 6]
    #                             ↑↑ becomes 23, continue
    #
    # current_val = 5
    # Is 5 less ↓ than 8?
    # [4, 5, 7, 8, 23,             23, 3, 6, 4, 6]
    #
    # current_val = 5
    # Is 5 less ↓ than 8? Yes
    # [4, 5, 7, 8, 8,              23, 3, 6, 4, 6]
    #              ↑ becomes 8, continue
    #
    # current_val = 5
    # Is 5   ↓ less than 7?
    # [4, 5, 7, 8, 8,              23, 3, 6, 4, 6]
    #
    # current_val = 5
    # Is 5   ↓ less than 7? Yes
    # [4, 5, 7, 7, 8,              23, 3, 6, 4, 6]
    #           ↑ becomes 7, continue
    #
    # current_val = 5
    # Is  ↓ 5 less than 5?
    # [4, 5, 7, 8, 8,              23, 3, 6, 4, 6]
    #
    # current_val = 5
    # Is  ↓ 5 less than 5? No
    # [4, 5, 5, 7, 8,              23, 3, 6, 4, 6]
    #        ↑ becomes 5, and we're done
    #
    # And this keeps going on and on
    # until the whole list is sorted.
    # ===========================================================
    if len(arr) < 2:
        return arr

    for i in range(1, len(arr)):
        # Start at ↑ the second value in the array
        # (The first value is considered 'sorted' already)
        current_val = arr[i]
        j = i
        while j > 0 and current_val < arr[j-1]:
        # Loop through from our current value back to the beginning
        # as long as our current value is less than our checking value,
        # swapping ↓↓↓ our values as we go
            arr[j] = arr[j-1]
            j -= 1
        # Otherwise, set our current value at [j]
        arr[j] = current_val
    
    return arr


# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index, smallest_index = i, i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # TO-DO: swap
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(arr)):
            # Start at index 1 and look behind us.
            # This way we don't need to worry about looking
            # Outside the array at the end
            if arr[i-1] > arr[i]:
                # If we find two values to swap,
                # Set swapped to True (so we keep looping)
                # and swap the values
                swapped = True
                temp = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = temp

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
