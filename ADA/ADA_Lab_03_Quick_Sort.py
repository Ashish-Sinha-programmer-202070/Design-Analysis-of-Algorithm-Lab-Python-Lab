'''Implement Quick Sort algorithm with all the necessary functions.'''

# Function for finding the partition of position of an array.

def partition(array, low, high):

    # Take the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater elements.
    i = low - 1

    # Traverse through all elements and 
    # compare each of element with pivot.
    for j in range(low, high):
     if array[j] <= pivot:
        # if element that is smallelement pointed by i
        i += 1

    # Swap the pivot element withr than pivot is found
    # swap it with the greater  greater element specified by i.
    (array[i+1],array[high]) = (array[high],array[i+1])

    # Return the position where partition is done.
    return i + 1

def quick_sort(array, low, high):

    # Find pivot element such that 
    # element smaller than pivot are on left
    # and element greater than poivot are on right side.
    if low < high:
      pie = partition(array, low, high)

      # Recursive call on left of pivot.
      quick_sort(array, low, pie-1)

      # Recursive call on right of pivot.
      quick_sort(array, pie+1, high)

# Driver code

array = [15, 5, 25, 30, 50, 20, 25, 35, 60, 100]
print(f"Unsorted Array is : \n {array}")

size = len(array)

quick_sort(array, 0, size - 1)

print(f"Sorted Array in Ascending Order: \n {array}")