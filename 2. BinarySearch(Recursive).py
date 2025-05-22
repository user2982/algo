ALGORITHM: 
1. Compare the target element with the middle element of the array. 
2. If the target element is equal to the middle element, return the index. 
3. If the target element is less than the middle element, recursively search the left half of the array. 
4. If the target element is greater than the middle element, recursively search the right half of the array. 
5. If the array is empty or the target element is not present, return -1. 
6. Repeat the experiments for different values of n and draw graph 

------------------------------------------------------------------------------------------------------------
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1 


arr = list(map(int, input().split()))
target = int(input())

result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")


# Time Complexity
# Best Case - O(1)
# Average Case - O(n)
# Worst case - O(n)

# Space Complexity
# Iterative approach - O(1)
# Recursive approach - O(n)
