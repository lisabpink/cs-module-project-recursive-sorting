# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # init pointers that start at each list
    A_idx = 0
    B_idx = 0
    # idx = 0

    # traverse lists if starting index is less than length of array
    while A_idx < len(arrA) and B_idx < len(arrB):

        #! if A_idx  is <  B_idx
        if arrA[A_idx] < arrB[B_idx]:
            # take index in merged array and set it to element of A_idx index
            merged_arr = arrA[A_idx]
            # increase A_idx by 1
            A_idx += 1

        #! if A_idx is > B_idx
        else:
            # take index in the merged array and set it to element of the B_idxindex
            merged_arr = arrB[B_idx]
            # increase B_idxby 1
            B_idx += 1

    #! traversing complete for one list
    # Add all of  elements from the other list to the combined one

    # loop if starting index <  length of A_idx
    while A_idx < len(arrA):
        # take index in merged array and set it to element of A_idx index
        merged_arr = arrA[A_idx]
        # increase A_idx by 1
    while B_idx < len(arrB):
        # take index in the merged array and set it to element of the B_idxindex
        merged_arr = arrB[B_idx]
        # increase B_idxby 1
        B_idx += 1

    # print(f"merged array: {merged_arr}")
    return merged_arr


# A_idx = [1, 2, 3, 7]
# B_idx = [0, 2, 5, 6, 8]
# print(merge(A_idx, B_idx))

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here

    if len(arr) > 1:

        # find the mid index so we can slice into left and right sublists
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # recur on the left
        left = merge_sort(left)
        # recur on the right
        right = merge_sort(right)

        arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
