def longest_substring(string):
    left = 0
    tracking = set()
    max_length = 0

    for right in range(len(string)):
        print(f"Window: {string[left:right+1]}, Set: {tracking}, MaxLen: {max_length}")

        while string[right] in tracking:
            print(f"Duplicate '{string[right]}' found. Removing '{string[left]}' from set.")
            tracking.remove(string[left])
            left += 1
        tracking.add(string[right])
        max_length = max(max_length, right - left + 1)

    
    return max_length

# Test
print(longest_substring("abcadab"))  # Output: 4 ("bcad")
