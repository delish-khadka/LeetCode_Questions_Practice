def move_zeroes(nums):
    """
    Given an integer array nums, move all 0's to the end of it while maintaining
    the relative order of the non-zero elements. This must be done in-place without
    making a copy of the array.

    :param nums: List[int] - The input array
    :return: None - The function modifies nums in-place

    # Test cases
    # test_cases = [
    #     [0, 1, 0, 3, 12],  # Expected output: [1, 3, 12, 0, 0]
    #     [0, 0, 1],  # Expected output: [1, 0, 0]
    #     [2, 0, 4, 0, 5],  # Expected output: [2, 4, 5, 0, 0]
    #     [1, 2, 3, 4],  # Expected output: [1, 2, 3, 4] (No changes needed)
    #     [0, 0, 0],  # Expected output: [0, 0, 0] (Already all zeroes)
    # ]
    """

    # Implement your solution here
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[count] = nums[i]
            count = count + 1
    
    while count < len(nums):
        nums[count] = 0
        count += 1



# Example usage
nums = [0, 1, 0, 3, 12]
move_zeroes(nums)
print(nums)  # Expected output: [1, 3, 12, 0, 0]
