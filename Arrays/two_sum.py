def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target.

    :param nums: List[int] - An array of integers
    :param target: int - The target sum
    :return: List[int] - A list containing the indices of the two numbers

    # Example Test Cases:
    # two_sum([2, 7, 11, 15], 9)  # Expected output: [0, 1] (2 + 7 = 9)
    # two_sum([3, 2, 4], 6)  # Expected output: [1, 2] (2 + 4 = 6)
    # two_sum([3, 3], 6)  # Expected output: [0, 1] (3 + 3 = 6)
    """
    # Implement your solution here
    # index = 0
    # for i in range(0,len(nums)):
    #     val = target - nums[i]
    #     index = i
    #     for j in range(i+1,len(nums)):
    #         if nums[j] == val:
    #             return i,j
    # return None
    num_mapping = {}
    for i,val in enumerate(nums):
        complement = target - val
        if complement in num_mapping:
            return[num_mapping[complement],i]
        num_mapping[val] = i
    return []


if __name__== "__main__":
    print(two_sum([2, 7, 11, 15],9))
    print(two_sum([3, 2, 4], 6))
    print(two_sum([3, 3], 6))
    print(two_sum([1,4,3,3,5], 9))
