def remove_duplicates(arr):
    if not arr:
        return None

    slow = 1

    for fast in range(1,len(arr)):

        if arr[fast] != arr[slow-1]:
            arr[slow] = arr[fast]
            slow += 1
    
    return slow

test = [1,1,2,2,3,3,3,4,4,5,5,5]
unique = remove_duplicates(test)
print("unique values: ", unique)
print("new array: ",test[:unique])