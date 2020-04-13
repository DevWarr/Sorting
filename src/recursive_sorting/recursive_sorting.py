# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    # m = merged_arr index
    # b = arrA index
    # b = arrB index
    m, a, b, = 0, 0, 0
    while a < len(arrA) and b < len(arrB):
        # Move through both halves, placing the smallest
        # number inside the merged array
        if arrA[a] < arrB[b]:
            merged_arr[m] = arrA[a]
            a += 1
        else:
            merged_arr[m] = arrB[b]
            b += 1
        m += 1

    # Leftover values in either array? add them in '' '
    if a < len(arrA):
        for f in range(a, len(arrA)):
            merged_arr[m] = arrA[f]
            m += 1

    if b < len(arrB):
        for f in range(b, len(arrB)):
            merged_arr[m] = arrB[f]
            m += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    # Slice the array into two arrays
    half = int(len(arr)/2)

    arrA = [0] * half # proper length of array
    for i in range(0, half):
        arrA[i] = arr[i]

    arrB = [0] * (len(arr)-half) # proper length of array
    b = 0
    for i in range(half, len(arr)):
        arrB[b] = arr[i]
        b += 1

    # If either array has a length greater than 1, recurse!
    if len(arrA) > 1:
        arrA = merge_sort(arrA)
    if len(arrB) > 1:
        arrB = merge_sort(arrB)

    return merge(arrA, arrB)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
