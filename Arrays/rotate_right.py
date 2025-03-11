def rotate_right(arr, k):
    """
    Rotates the array right by k positions in-place.

    :param arr: List[int] - The input array
    :param k: int - Number of positions to rotate right
    :return: None (Modifies arr in-place)
    """
    n = len(arr)
    if n == 0 or k == 0:
        return  # No rotation needed
    k = k%n
    
    #rotate the entire list first
    reverse(arr,0,n-1)
    #rotate elements except k
    reverse(arr,0,k-1)
    #rotate remaining elements
    reverse(arr,k,n-1)

def reverse(arr, start, end):
    """Helper function to reverse elements in the array"""
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Example usage
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 2),  # Expected: [4, 5, 1, 2, 3]
        ([10, 20, 30, 40, 50], 3),  # Expected: [30, 40, 50, 10, 20]
        ([1, 2, 3, 4, 5], 5),  # Expected: [1, 2, 3, 4, 5] (No change)
        ([7, 8, 9], 1),  # Expected: [9, 7, 8]
        ([], 2),  # Expected: [] (Empty array)
        ([1], 3)  # Expected: [1] (Single element)
    ]

    for arr, k in test_cases:
        original_arr = arr[:]  # Copy for printing
        print("Original:", original_arr)
        rotate_right(arr, k)
        print("Rotated: ", arr)
        print("-" * 30)
