def is_palindrome(string):
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True

# Test cases
print(is_palindrome("racecar"))  # True
print(is_palindrome("madam"))    # True
print(is_palindrome("hello"))    # False
