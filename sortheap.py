def heapify(A, n, i):
    """
    Performs heapify operation on a subtree rooted at index i.

    Args:
        A: The list representing the heap.
        n: The size of the heap.
        i: The index of the root of the subtree.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and A[left] > A[largest]:
        largest = left
    if right < n and A[right] > A[largest]:
        largest = right

    if largest != i:
        A[i], A[largest] = A[largest], A[i]  # Swap
        heapify(A, n, largest)  # Recursively heapify affected subtree

def heap_sort(A):
    """
    Sorts a list in ascending order using heapsort.

    Args:
        A: The list to be sorted.

    Returns:
        None. Modifies the input list directly.
    """
    n = len(A)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)

    # Extract elements from the heap
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]  # Swap root with last element
        heapify(A, i, 0)  # Heapify the remaining sub-heap

# Example usage
arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heap_sort(arr)
print("Sorted array:", arr)
  # Output: [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
