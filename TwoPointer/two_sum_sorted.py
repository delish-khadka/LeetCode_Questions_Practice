def two_sum_sorted(arr,target):
    left = 0
    right = len(arr) - 1

    while left < right:
        curr_sum = arr[left] + arr[right]
        if(curr_sum == target):
            return (arr[left],arr[right])
        elif curr_sum < target:
            left +=1
        else:
            right -= 1
    return None

# Test case
print(two_sum_sorted([1, 2, 3, 4, 6], 6))   # Output: (2, 4)
print(two_sum_sorted([1, 3, 5, 7, 9], 12))  # Output: (3, 9)
print(two_sum_sorted([1, 2, 3, 9], 8))      # Output: None

        