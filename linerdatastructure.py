# # QUESTION 5

def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for value in arr:
        if value in seen:
            duplicates.add(value)
        else:
            seen.add(value)
    return duplicates

# Example usage
arr = [1, 2, 3, 4, 2, 3, 5, 6]
print(find_duplicates(arr)) 

# QUESTION 6

def kth_largest_smallest(arr, k):
    arr.sort()
    return arr[k-1], arr[-k]

# Example usage
arr = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input("Enter element: "))
    arr.append(ele)
k = int(input("Enter the value of k: "))
kth_largest, kth_smallest = kth_largest_smallest(arr, k)
print(f"The {k}th largest number is {kth_largest}")
print(f"The {k}th smallest number is {kth_smallest}")