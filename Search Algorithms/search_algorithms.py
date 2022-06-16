"""
Implementation of search algorithms:
Linear Search, Binary Search - Recursion, Binary Search - Iteration, Jump Search, Fibonacci Search,
Exponential Search, Interpolation Search
"""


def linear_search(lst, val):
    """Returns index of first occurrence of val in lst."""
    for i in range(0, len(lst)):
        if lst[i] == val:
            return i
    return -1


def binary_search_recursion(lst, low, high, val):
    """Returns index of val in lst, or returns -1, if val not present in lst.
    Binary search using recursion. The lst has to be sorted.
    """
    if low <= high:
        mid = (high + low) // 2
        if lst[mid] == val:
            return mid
        elif lst[mid] > val:
            return binary_search_recursion(lst, low, mid - 1, val)
        else:
            return binary_search_recursion(lst, mid + 1, high, val)
    else:
        return -1


def binary_search_iteration(lst, val):
    """Returns index of val in lst, or returns -1, if val not present in lst.
    Binary search using iteration. The lst has to be sorted.
    """
    low = 0
    high = len(lst) - 1
    index = -1
    while low <= high and index == -1:
        mid = (low + high) // 2
        if lst[mid] == val:
            index = mid
        elif lst[mid] > val:
            high = mid - 1
        elif lst[mid] < val:
            low = mid + 1
    return index


def jump_search(lst, val):
    """Returns index of val in lst, or returns -1, if val not present in lst.
    The lst has to be sorted
    """
    length = len(lst)
    if length == 0:
        return -1
    # Finding the block size to be jumped
    step = int(length**0.5)
    # Finding the block where element is present
    previous = 0
    while lst[int(min(step, length) - 1)] < val:
        previous = step
        step += int(length**0.5)
        if previous >= length:
            return -1
    # Linear search for value in block beginning with previous
    while lst[int(previous)] < val:
        previous += 1
        if previous == min(step, length):
            return -1
    if lst[int(previous)] == val:
        return previous
    return -1


def fibonacci_search(lst, val):
    """Returns index of val in lst, or returns -1, if val not present in lst.
    The lst has to be sorted
    """
    length = len(lst)
    if length == 0:
        return -1
    # initialize fibonacci numbers
    fib_m2 = 0
    fib_m1 = 1
    fib = 1
    # fib is going to store the smallest Fibonacci number greater then or equal to length
    while fib < length:
        fib_m2 = fib_m1
        fib_m1 = fib
        fib = fib_m1 + fib_m2
    # Marks the eliminated range from front
    offset = -1

    # While there are elements to be inspected.
    while fib > 1:
        # Check if fib_m2 is a valid location
        i = min(fib_m2 + offset, length - 1)
        # If val is greater than the value at index fib_m2,
        # cut the subarray from offset to i
        if lst[i] < val:
            fib = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib - fib_m1
            offset = i
        # If val is less then the value at index fib_m2,
        # cut the subarray after i+1
        elif lst[i] > val:
            fib = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib - fib_m1
        # element found
        else:
            return i
    # comparing the last element with val
    if fib_m1 and lst[length - 1] == val:
        return length - 1
    # element not found
    return -1


def exponential_search(lst, val):
    """Returns index of val in lst, or returns -1, if val not present in lst.
    The lst has to be sorted
    """
    length = len(lst)
    if length == 0:
        return -1
    # is val present at index 0?
    if lst[0] == val:
        return 0
    # find range for binary search
    i = 1
    while i < length and lst[i] <= val:
        i *= 2
    # use binary search for the found range
    return binary_search_recursion(lst, i // 2, min(i, length - 1), val)


def interpolation_search(lst, low, high, val):
    """Returns index of val in lst, or returns -1, if val not present in lst.
    The lst has to be sorted
    """
    if low <= high and val >= lst[low] and val <= lst[high]:
        # Probing the position with keeping uniform distribution in mind
        position = low + \
            (high - low) // (lst[high] - lst[low]) * (val - lst[low])
        # Is it the position of val? Or is val larger or smaller?
        if lst[position] == val:
            return position
        # If val is larger, val is in right subarray
        if lst[position] < val:
            return interpolation_search(lst, position + 1, high, val)
        # If val is smaller, val is in left subarray
        if lst[position] > val:
            return interpolation_search(lst, low, position - 1, val)
    return -1
