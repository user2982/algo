ALGORITHM: 
• Base Case: 
• If the list has only one element, return that element as both the maximum and minimum. 
• Divide: 
• Split the list into two halves. 
• Conquer: 
• Recursively find the maximum and minimum in each half. 
• Combine: 
• Compare the maximum and minimum of the two halves to find the overall maximum and minimum.
------------------------------------------------------------------------------------------------------
PROGRAM:
def find_max_min(arr, start, end):
    if start == end:
        return arr[start], arr[start]

    if end - start == 1:
        return max(arr[start], arr[end]), min(arr[start], arr[end])

    mid = (start + end) // 2
    max1, min1 = find_max_min(arr, start, mid)
    max2, min2 = find_max_min(arr, mid+1, end)

    overall_max = max(max1, max2)
    overall_min = min(min1, min2)

    return overall_max, overall_min

arr = list(map(int, input().split()))
max, min = find_max_min(arr, 0, len(arr)-1)
print(max, min)
