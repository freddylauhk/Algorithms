from SortUtil import *

# Bubble Sort
def Bubble_Sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr)-1):
            if(arr[j] > arr[j+1]):
                Swap(arr, j, j + 1)
    return arr
