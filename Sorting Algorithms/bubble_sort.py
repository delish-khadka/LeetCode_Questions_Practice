def bubble_sort(arr):
    """
    Sorts an array in ascending order using the Bubble Sort algorithm.

    :param arr: List[int] - The array to be sorted
    :return: None (Sorting is done in-place)

    # Example Test Cases:
    # arr = [5, 3, 8, 4, 2]
    # bubble_sort(arr)  
    # Expected output: [2, 3, 4, 5, 8]
    """
    # Implement your solution here
    for i in range(len(arr)):
        swapped = False
        for j in range(0,len(arr) - i - 1 ):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if(swapped == False):
            break

# Function calling with test cases
if __name__ == "__main__":
    # Test cases
    test_cases = [
        [5, 3, 8, 4, 2],  # Unsorted list
        [1, 2, 3, 4, 5],  # Already sorted list
        [5, 4, 3, 2, 1],  # Reverse sorted list
        [3, 3, 3, 3, 3],  # All elements are the same
        [10],  # Single element
        [],  # Empty list
        [7, -2, 4, 0, -5, 8, 3],  # List with negative and positive numbers
    ]

    for arr in test_cases:
        print("Original:", arr)
        bubble_sort(arr)
        print("Sorted:  ", arr)
        print("-" * 30)
