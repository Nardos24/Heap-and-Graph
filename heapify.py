def heapify(arr, n, i):
  """
  Heapifies a sub-tree rooted at index i in an array.

  Args:
    arr: The array to heapify.
    n: The size of the array.
    i: The index of the root of the sub-tree to heapify.
  """

  largest = i  # Initialize largest as root
  l = 2 * i + 1  # Left child
  r = 2 * i + 2  # Right child

  # See if left child is larger than root
  if l < n and arr[l] > arr[largest]:
    largest = l

  # See if right child is larger than largest so far
  if r < n and arr[r] > arr[largest]:
    largest = r

  # If largest is not root
  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]  # Swap

    # Recursively heapify the affected sub-tree
    heapify(arr, n, largest)


def build_heap(arr):
  """
  Builds a max heap from an array.

  Args:
    arr: The array to build the heap from.
  """

  n = len(arr)

  # Start from the last non-leaf node and heapify all sub-trees
  for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)


# Example usage
arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]

# Build the heap
build_heap(arr)

print("Heapified array:", arr)

