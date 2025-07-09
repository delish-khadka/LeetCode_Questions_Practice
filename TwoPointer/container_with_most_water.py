def max_area(height):
    """
    Given an array of integers `height` representing the height of vertical lines,
    return the maximum amount of water a container can store.
    """

    # two pointers go here
    left = 0
    right = len(height) - 1

    max_area = 0

    while left < right:
        # 1. Calculate current area
        area = min(height[left],height[right]) * (right-left)
        # 2. Update max_area if needed
        if area > max_area:
            max_area = area
        # 3. Move the pointer pointing to the shorter line  
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


# Test example
print(max_area([1,8,6,2,5,4,8,3,7]))  # Expected: 49
