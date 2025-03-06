def selection_sort(arr):
    """
    Sorts an array in ascending order using the Selection Sort algorithm.

    :param arr: List[int] - The array to be sorted
    :return: None (Sorting is done in-place)

    # Example Test Cases:
    # arr = [64, 25, 12, 22, 11]
    # selection_sort(arr)  
    # Expected output: [11, 12, 22, 25, 64]
    """
    # Implement your solution here
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
        

# Function calling with test cases
if __name__ == "__main__":
    # Test cases with expected outputs
    test_cases = [
        ([64, 25, 12, 22, 11], [11, 12, 22, 25, 64]),  # Unsorted list
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Already sorted list
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Reverse sorted list
        ([3, 3, 3, 3, 3], [3, 3, 3, 3, 3]),  # All elements are the same
        ([10], [10]),  # Single element
        ([], []),  # Empty list
        ([7, -2, 4, 0, -5, 8, 3], [-5, -2, 0, 3, 4, 7, 8]),  # List with negative numbers
    ]

    for arr, expected in test_cases:
        print("Original:", arr)
        selection_sort(arr)
        print("Sorted:  ", arr)
        print("Expected:", expected)
        print("Pass" if arr == expected else "Fail")
        print("-" * 30)
