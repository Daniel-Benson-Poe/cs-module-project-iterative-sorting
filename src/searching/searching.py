def linear_search(arr, target):
    # Your code here
    # Create variable to track index
    i = 0
    # Loop through each element in array
    for value in arr:
        # Check if target and element are the same
        if target == value:
            # return index target value can be found
            return i
        # Increment index variable by 1
        i += 1

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    # Set low count
    low = 0
    # Set high count
    high = len(arr) - 1
    # Loop through until low > high
    while low <= high:

        # set midpoint
        midpoint = (low + high) // 2

        # set guess
        guess = arr[midpoint]
        # Check if guess and target are the same
        if guess == target:
            # return midpoint
            return midpoint
        # check if guess is greater than target
        if guess > target:
            # set high to midpoint -1
            high = midpoint - 1
        # otherwise; if guess < target
        else:
            # set low to midpoint = 1
            low = midpoint + 1

    return -1  # not found

if __name__ == "__main__":
    my_items = [2,4,7,8,9,10,12,34,45]
    print(linear_search(my_items, 7))
    print(linear_search(my_items, 34))
    print(binary_search(my_items, 7))
    print(binary_search(my_items, 34))