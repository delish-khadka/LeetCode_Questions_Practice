def sort_three_numbers(a, b, c):
    """
    Given three numbers a, b, and c, return them in sorted order.

    :param a: int - First number
    :param b: int - Second number
    :param c: int - Third number
    :return: Tuple[int, int, int] - The three numbers sorted in ascending order

    # Example Test Cases:
    # sort_three_numbers(3, 1, 2)  # Expected output: (1, 2, 3)
    # sort_three_numbers(5, 7, 2)  # Expected output: (2, 5, 7)
    # sort_three_numbers(-1, -5, 0)  # Expected output: (-5, -1, 0)
    """
    # Implement your solution here
    if a>b:
        a,b = b,a
    if a>c:
        a,c = c,a
    if b>c:
        b,c = c,b
    return (a,b,c)

# Example test cases
if __name__ == "__main__":
    print(sort_three_numbers(3, 1, 2))  # Expected output: (1, 2, 3)
    print(sort_three_numbers(5, 7, 2))  # Expected output: (2, 5, 7)
    print(sort_three_numbers(-1, -5, 0))  # Expected output: (-5, -1, 0)
