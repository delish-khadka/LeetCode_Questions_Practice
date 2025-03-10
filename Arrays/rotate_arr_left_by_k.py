def rotate_left(arr, k):
    """
    Rotates the array left by k positions in-place.
    """
    n = len(arr)
    if n == 0 or k == 0:
        return  # No rotation needed
    
    k = k % n  # Handle cases where k > n

    # Reverse the first k elements
    reverse(arr, 0, k - 1)
    # Reverse the remaining elements
    reverse(arr, k, n - 1)
    # Reverse the whole array
    reverse(arr, 0, n - 1)

def reverse(arr, start, end):
    """Helper function to reverse elements in the array"""
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Function calling with test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 2),  # Expected: [3, 4, 5, 1, 2]
        ([10, 20, 30, 40, 50], 3),  # Expected: [40, 50, 10, 20, 30]
        ([1, 2, 3, 4, 5], 5),  # Expected: [1, 2, 3, 4, 5] (No change)
        ([7, 8, 9], 1),  # Expected: [8, 9, 7]
        ([], 2),  # Expected: [] (Empty array)
        ([1], 3)  # Expected: [1] (Single element)
    ]

    for arr, k in test_cases:
        original_arr = arr[:]  # Copy for printing
        print("Original:", original_arr)
        rotate_left(arr, k)
        print("Rotated: ", arr)
        print("-" * 30)
