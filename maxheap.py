#implementation of max-heapify in an iterative fashion
def heapify(arr):
    """
    Converts a list into a max heap in-place using an iterative approach.

    Args:
        arr: The list to be heapified.

    Returns:
        None. Modifies the input list directly.
    """
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        # Start from the last non-leaf node and work upwards
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            # Compare with left child
            if left < n and arr[left] > arr[largest]:
                largest = left

            # Compare with right child
            if right < n and arr[right] > arr[largest]:
                largest = right

            # Swap if necessary and move to the next level
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                i = largest
            else:
                break  # No more swaps needed at this level

# Example usage
arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heapify(arr)
print(arr)  # Output: [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
