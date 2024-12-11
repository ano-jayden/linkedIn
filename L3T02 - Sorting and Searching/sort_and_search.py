def binary_search(arr, target):
    arr.sort() 
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  

# Array 
arr = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
target = 9

index = binary_search(arr, target)

if index != -1:
    print(f"Number {target} found at index {index} in the sorted array.")
else:
    print(f"Number {target} not found in the array.")
'''i used binary search because its able to eliminate parts of the list we are not using resulting in
quicker searches for the target item 

'''
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Array 
arr = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]


insertion_sort(arr)

# Print the sorted array
print("Sorted array:", arr)

# Linear search 
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index found
    return -1  

# Array 
arr = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]


insertion_sort(arr)

# Perform linear search to find the target
target = 9
index = linear_search(arr, target)

# Output the sorted array and search result
print("Sorted array:", arr)
if index != -1:
    print(f"Number {target} found at index {index} in the sorted array.")
else:
    print(f"Number {target} not found in the array.")
    '''I would say we would use linear search on data we know we are looking for such as someones id number,
    a specific order number or a specific user'''