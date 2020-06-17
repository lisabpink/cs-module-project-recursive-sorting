# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # init pointers that start at each list
    arrA_idx = 0
    arrB_idx = 0
    idx = 0

    # traverse lists if starting index is less than length of array
    while arrA_idx < len(arrA) and arrB_idx < len(arrB):
        # if arrA_idx  is <  arrB_idx
        if arrA[arrA_idx] < arrB[arrB_idx]:
            # take index in merged array and set it to element of arrA_idx index
            merged_arr[idx] = arrA[arrA_idx]
            # increase merged_array by 1
            idx += 1
            # increase arrA_idx by 1
            arrA_idx += 1

        # if arrA_idx is > arrB_idx
        else:
            # take index in the merged array and set it to element of the arrB_idx index
            merged_arr[idx] = arrB[arrB_idx]
            # increase merged_array by 1
            idx += 1
            # increase arrB_idx by 1
            arrB_idx += 1

    #! traversing complete for one list
    # Add all of  elements from the other list to the combined one

    # loop if starting index <  length of arrA_idx
    while arrA_idx < len(arrA):
        # take index in merged array and set it to element of arrA_idx index
        merged_arr[idx] = arrA[arrA_idx]
        # increase merged_array by 1
        idx += 1
        # increase arrA_idx by 1
        arrA_idx += 1

     # loop if starting index <  length of arrB_idx
    while arrB_idx < len(arrB):
        # take index in the merged array and set it to element of the arrB_idx index
        merged_arr[idx] = arrB[arrB_idx]
        # increase merged_array by 1
        idx += 1
        # increase arrB_idx by 1
        arrB_idx += 1
    print(f"merged array: {merged_arr}")
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here

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
