''' Write a program to Implement Binary Search using python '''

def binary_search(list, key):
    low = 0
    high = len(list) - 1
    mid = 0

    # Repeat until the pointers low and high meet each other
    while low <= high:
        mid = (high + low) // 2
    # Check If key is present at mid
        if list[mid] < key:
          low = mid + 1
    # If key is greater, compare to right of mid
        elif list[mid] > key:
           high = mid + 1
    # If key is smaller, compare to left of mid
        else:
           return mid
    return -1


# initial List
list = [7.8, 8.9, 6.8, 8.5, 9.2, 9.7, 6.5, 5.7, 4.9, 7.5, 8.8]
key = 9.7
# Function Call
result = binary_search(list, key)
if result != -1:
    print("This semester top scorer is in room no:", str(result))
else:
    print("This semester top scorer is not in this list")
