# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # base case, loop if end point is > or = to start
    if end >= start:
        # declare mid point
        mid = (end + start) // 2
        # If > mid, in left subarray
        if arr[mid] > target:
            # recurse back to base case
            return binary_search(arr, target, start, mid - 1)
        # If < mid,  in right subarray
        elif arr[mid] < target:
            # recurse back to base case
            return binary_search(arr, target, mid + 1, end)
        # If target
        elif arr[mid] == target:
            # dont recurse- return element
            return mid
    #target not in arr
    return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    pass
    # Your code here
