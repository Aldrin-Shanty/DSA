def binary_search(arr: list[int], target: int) -> int:
    """
    Perform binary search on a sorted array.

    Args:
        arr (list[int]): The sorted array to search.
        target (int): The value to search for.

    Returns:
        int: The index of the target value if found; otherwise, -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def left_binary_search(arr: list[int], target: int) -> int:
    """
    Perform binary search to find the leftmost occurrence of a target value in a sorted array.

    Args:
        arr (list[int]): The sorted array to search.
        target (int): The value to search for.

    Returns:
        int: The index of the leftmost occurrence of the target value if found; otherwise, -1.
    """
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue to search in the left half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result
