Algorithm:
1. Choose a pivot element from the array. This can be done in various ways, such as picking the first, last, 
  middle, or a random element. 
2. Partition the array into two sub-arrays - elements less than the pivot and elements greater than the 
  pivot. 
3. Recursively apply the QuickSort algorithm to the sub-arrays. 
4. Combine the sorted sub-arrays to get the final sorted array. 
---------------------------------------------------------------------------------------------------------------
Program:
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

arr = list(map(int, input().split()))
arr = quick_sort(arr)
print(arr)
