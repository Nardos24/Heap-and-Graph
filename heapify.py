def heapify(arr, n, i):
  """
  Heapifies a sub-tree rooted at index i in an array.

  Args:
    arr: The array to heapify.
    n: The size of the array.
    i: The index of the root of the sub-tree to heapify.
  """

  largest = i  
  l = 2 * i + 1  
  r = 2 * i + 2  

  
  if l < n and arr[l] > arr[largest]:
    largest = l

  
  if r < n and arr[r] > arr[largest]:
    largest = r

  
  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]  

    
    heapify(arr, n, largest)


def build_heap(arr):
  """
  Builds a max heap from an array.

  Args:
    arr: The array to build the heap from.
  """

  n = len(arr)

  
  for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)



arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]


build_heap(arr)

print("Heapified array:", arr)

