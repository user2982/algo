ALGORITHM:
1. Build a max heap from the given array. 
2. Swap the root (maximum element) with the last element of the heap and reduce the size of the heap 
by 1. 
3. Heapify the root of the heap. 
4. Repeat steps 2 and 3 until the heap is empty. 
------------------------------------------------------------------------------------------------------------
PROGRAM:
def heapify(arr, n, i):
    largest = i         
    left = 2 * i + 1     
    right = 2 * i + 2    

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  

        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)

arr = list(map(int, input().split()))
heap_sort(arr)
print(arr)
