# TO-DO: Complete the selection_sort() function below
# this is in-place-selection-sort
def selection_sort(arr):
    # loop through n-1 elements
    for current_index in range(0, len(arr) - 1):
        smallest_index = current_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for index in range(current_index + 1, len(arr)):
            # if the array[index] is less array[smallest_index]
            # set smallest index to index
            if arr[index] < arr[smallest_index]:
                smallest_index = index
        # TO-DO: swap
        # Your code here
        arr[current_index], arr[smallest_index] = arr[smallest_index], arr[current_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr: list):
    # Your code here

    search_space = len(arr) - 1 
    index = 0
    while search_space > 0:
        current_item = arr[index]
        next_item = arr[index + 1]
        
        if current_item > next_item:
            arr[index], arr[index+1] =  arr[index+1],  arr[index] # swaps
        
        index += 1
        # reset index
        if index == search_space:
            index = 0
            search_space -= 1

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
