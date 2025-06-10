Algorithm for Merge Sort
Function MergeSort(arr)

1. Divide:
  - If the input array arr has 0 or 1 element, it is already sorted. Return arr. (This is the base case for recursion).
  - Otherwise, find the middle index mid of the array: mid = floor(length(arr) / 2).
  - Divide the array arr into two halves:
    left_half = arr[0 ... mid-1]
    right_half = arr[mid ... length(arr)-1]
2. Conquer (Recursively Sort Sub-arrays):
  - Recursively call MergeSort on the left_half: sorted_left = MergeSort(left_half)
  - Recursively call MergeSort on the right_half: sorted_right = MergeSort(right_half)
3. Combine (Merge Sorted Sub-arrays):
  - Call the Merge function (described below) to combine sorted_left and sorted_right into a single sorted array.
  - merged_array = Merge(sorted_left, sorted_right)
  - Return merged_array.
----------------------------------------------------------------------------------------------------------------------------------------
Program: 

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


arr = list(map(int, input().split()))
merge_sort(arr)
print(arr)
