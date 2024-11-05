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
        
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            
            if left < n and arr[left] > arr[largest]:
                largest = left

            
            if right < n and arr[right] > arr[largest]:
                largest = right

            
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                i = largest
            else:
                break  


arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heapify(arr)
print(arr) 
