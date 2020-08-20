import random

# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        current_index = i  # set current to i
        smallest_index = current_index  # set smallest_index to current
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(current_index + 1, len(arr)):  # loop through range between current +1 and length of array
            if arr[j] < arr[smallest_index]:  # check if element at array index j < element at array index smallest index
                smallest_index = j  # set smallest index to new location of smallest element

        # TO-DO: swap
        # Your code here
        arr[smallest_index], arr[current_index] = arr[current_index], arr[smallest_index]  # swap smallest index and current index

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    sort_on = True  # boolean to turn sorting on and off
    while sort_on:
        sort_on = False  # start by turning sort off
        for i in range(0, len(arr)-1):  # iterate through range for index locations
            if arr[i] > arr[i+1]:  # check position i against i + 1
                arr[i], arr[i+1] = arr[i+1], arr[i]  # swap
                sort_on = True  # a swap was performed, so turn sort_on back to on

    return arr