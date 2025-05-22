ALGORITHM: 
1. Compare the target element with the middle element of the array. 
2. If the target element is equal to the middle element, return the index. 
3. If the target element is less than the middle element, recursively search the left half of the array. 
4. If the target element is greater than the middle element, recursively search the right half of the array. 
5. If the array is empty or the target element is not present, return -1. 
6. Repeat the experiments for different values of n and draw graph 

------------------------------------------------------------------------------------------------------------
def binary_search_recursive(arr, target, low, high):
    
    # Base case: element not found
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    # Base case: element found
    if arr[mid] == target:
        return mid
    
    # Recursive cases
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)

# Example usage
if __name__ == "__main__":
    sorted_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23
    
    result = binary_search_recursive(sorted_array, target, 0, len(sorted_array) - 1)
    
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the array")

# Time Complexity
# Best Case - O(1)
# Average Case - O(n)
# Worst case - O(n)

# Space Complexity
# Iterative approach - O(1)
# Recursive approach - O(n)
