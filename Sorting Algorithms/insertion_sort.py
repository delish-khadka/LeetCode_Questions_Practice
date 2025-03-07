def insertion_sort(arr):
    """
    Sorts an array in ascending order using the Insertion Sort algorithm.

    :param arr: List[int] - The array to be sorted
    :return: None (Sorting is done in-place)
    """
    # Implement your solution here
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements that are greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

# Function calling with test cases
if __name__ == "__main__":
    # Sample test cases
    test_cases = [
        [5, 3, 8, 4, 2],  
        [1, 2, 3, 4, 5],  
        [5, 4, 3, 2, 1],  
        [3, 3, 3, 3, 3],  
        [10],  
        [],  
        [7, -2, 4, 0, -5, 8, 3],  
    ]

    for arr in test_cases:
        print("Original:", arr)
        insertion_sort(arr)
        print("Sorted:  ", arr)
        print("-" * 30)
