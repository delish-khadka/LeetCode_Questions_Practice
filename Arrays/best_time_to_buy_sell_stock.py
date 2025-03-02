def max_profit(prices):
    """
    Given an array of prices where prices[i] represents the stock price on the ith day, 
    return the maximum profit that can be achieved by buying and selling once.

    :param prices: List[int] - An array of stock prices
    :return: int - The maximum profit possible, or 0 if no profit can be achieved

    # Example Test Cases:
    # max_profit([7,1,5,3,6,4])  # Expected output: 5 (Buy at 1, sell at 6)
    # max_profit([7,6,4,3,1])  # Expected output: 0 (No profit possible)
    # max_profit([1,2,3,4,5])  # Expected output: 4 (Buy at 1, sell at 5)
    """
    # Implement your solution here
    smallest_index = 0
    for i in range(0,len(prices)):
        if prices[smallest_index] > prices[i]:
            smallest_index = i 
    highest_index_after_smallest = smallest_index
    for i in range(smallest_index,len(prices)):
        if prices[i] > prices[highest_index_after_smallest]:
            highest_index_after_smallest = i
    if smallest_index == highest_index_after_smallest:
        return 0
    else:
        return prices[highest_index_after_smallest] - prices[smallest_index]
# Example test cases
if __name__ == "__main__":
    print(max_profit([7,1,5,3,6,4]))  # Expected output: 5
    print(max_profit([7,6,4,3,1]))  # Expected output: 0
    print(max_profit([1,2,3,4,5]))  # Expected output: 4
