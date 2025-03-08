def reverse_string(s):
    """
    Reverses the input string in-place.

    :param s: List[str] - The input string as a list of characters
    :return: None (Modifies s in-place)

    # Example Test Cases:
    # s = ["h", "e", "l", "l", "o"]
    # reverse_string(s)
    # Expected output: ["o", "l", "l", "e", "h"]

    # s = ["H", "a", "n", "n", "a", "h"]
    # reverse_string(s)
    # Expected output: ["h", "a", "n", "n", "a", "H"]
    """
    # Implement your solution here
    start = 0
    end = len(s) - 1
    while start < end:
        s[start],s[end] = s[end],s[start]
        start += 1
        end -= 1
    

if __name__ == "__main__":
    test_cases = [
        ["h", "e", "l", "l", "o"],  # Expected: ["o", "l", "l", "e", "h"]
        ["H", "a", "n", "n", "a", "h"],  # Expected: ["h", "a", "n", "n", "a", "H"]
        ["A", "B", "C", "D"],  # Expected: ["D", "C", "B", "A"]
        ["x"],  # Single character, Expected: ["x"]
        []  # Empty list, Expected: []
    ]

    for s in test_cases:
        print("Original:", s)
        reverse_string(s)
        print("Reversed:", s)
        print("-" * 30)
