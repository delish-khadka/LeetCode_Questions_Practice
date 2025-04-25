def next_greater_element(item):
    result = []
    stack = []

    for i in range(len(item) - 1, -1, -1):  # 👈 Loop from right to left
        current = item[i]

        # Remove all elements smaller or equal to current
        while stack and stack[-1] <= current:
            stack.pop()

        # If stack is empty, no greater element to the right
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])  # Top of stack is the next greater element

        # Add current element to stack
        stack.append(current)

    # Since we built result from the end, reverse it before returning
    return result[::-1]

# Example usage
print(next_greater_element([4, 5, 2, 25]))
