def max_sum_of_subarray(arr,k):
    max_sum = 0
    curr_sum = 0
    for i in range(0,k):
        curr_sum = curr_sum + arr[i]
        max_sum = curr_sum
    for i in range(k,len(arr)):
        curr_sum = arr[i] + curr_sum - arr[i-k]
        if max_sum < curr_sum:
            max_sum = curr_sum
    return max_sum

# Example:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print(max_sum_of_subarray(arr, k))   # Output: 24
    