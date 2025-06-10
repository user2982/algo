ALGORITHM: 
INSERTION SORT: 
 
1. Start with the second element (index 1) and consider it as the key. 
2. Compare the key with the element before it. 
3. If the key is smaller, move the larger element to the right. 
4. Repeat step 3 until a smaller element is found or the beginning of the array is reached. 
5. Insert the key at the correct position. 
6. Repeat steps 1-5 for the remaining elements in the array. 

----------------------------------------------------------
def insertionSort(arr, size):

    for i in range(1, size):
        key = arr[i]
        j = i-1

        while (j >= 0 and arr[j] > key):
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key

arr = [20,10,40,30,50]
size = len(arr)

insertionSort(arr, size)
print(arr)

----------------------------------------------------------
# Time Complexity
# Average - O(n^2)
# Worst - O(n^2)
# Best - O(1)

# Space Complexity
# O(1)
