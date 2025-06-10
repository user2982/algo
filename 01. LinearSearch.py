ALGORITHM: 
1. Start from the beginning of the list. 
2. Compare the target element with each element in the list. 
3. If the target element is found, return the index. 
4. If the end of the list is reached without finding the target element, return -1. 
5. Repeat the experiments for different values of n and draw graph 

-----------------------------------------------------------------------------------
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
