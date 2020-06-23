from SortUtil import *

# Quick Sort
def QuickSort(arr, low, high):
    if(low < high):
        pivot = Partition(arr, low, high)
        QuickSort(arr, low, pivot - 1)
        QuickSort(arr, pivot + 1, high)
    return(arr)

def Partition(arr, low, high):
    pivot = high        # Set the last element in the array as pivot 
    i = low - 1
    for j in range(low, high):
        if(arr[j] <= arr[pivot]):
            i += 1
            Swap(arr, i, j)
    Swap(arr, i + 1, pivot)
    return i + 1
    
