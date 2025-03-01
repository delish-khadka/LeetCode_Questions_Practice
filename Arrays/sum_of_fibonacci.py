def fibonacci_sum(n):
    """
    Given an integer n, return the sum of Fibonacci numbers up to the nth Fibonacci number.

    :param n: int - The upper limit of Fibonacci numbers to sum
    :return: int - The sum of Fibonacci numbers up to n

    # Example Test Cases:
    # fibonacci_sum(5)  # Expected output: 12 (1 + 1 + 2 + 3 + 5)
    # fibonacci_sum(7)  # Expected output: 33 (1 + 1 + 2 + 3 + 5 + 8 + 13)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    a = 0
    b = 1
    total_sum = a+b
    for i in range(2,n+1):
        added = a+b
        a = b
        b = added
        total_sum = total_sum + b
    return total_sum

# Example usage
print(fibonacci_sum(5))  # Expected output: 12
print(fibonacci_sum(7))  # Expected output: 33