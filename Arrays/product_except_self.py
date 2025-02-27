def product_except_self(nums):
    """
    Given an integer array nums, return an array answer such that answer[i] 
    is equal to the product of all the elements of nums except nums[i].

    :param nums: List[int] - An array of integers
    :return: List[int] - An array where each element is the product of all other elements except itself

    # # Test cases
    # test_cases = [
    #     [1, 2, 3, 4],  # Expected output: [24, 12, 8, 6]
    #     [-1, 1, 0, -3, 3],  # Expected output: [0, 0, 9, 0, 0]
    #     [2, 3, 4, 5],  # Expected output: [60, 40, 30, 24]
    #     [10, 3, 5, 6, 2],  # Expected output: [180, 600, 360, 300, 900]
    #     [1, 1, 1, 1, 1]  # Expected output: [1, 1, 1, 1, 1]
    # ]

    """
    # Implement your solution here
    """
    #brute force solution
    modified_nums = nums.copy()
    for i in range(0,len(modified_nums)):
        changed_index_value = 1
        for j in range(0,len(modified_nums)):
            if i == j:
                continue
            changed_index_value *= nums[j]
        modified_nums[i] = changed_index_value
    return modified_nums"""

    n = len(nums)

    suffix = [1] * n
    prefix = [1] * n
    result = [1] * n

    for i in range(1,n):
        prefix[i] = prefix[i-1] * nums[i-1]
    
    for i in range(n-2,-1,-1):
        suffix[i] = suffix[i+1] * nums[i+1]
    
    for i in range(0,n):
        result[i] = prefix[i] * suffix[i]
    return result

print(product_except_self([1,2,3,4]))

