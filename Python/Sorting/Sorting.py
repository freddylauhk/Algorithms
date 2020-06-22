# Import random library
from random import seed
from random import randint

from SortUtil import *
from BubbleSort import *
from InsertionSort import *
from SelectionSort import *
from MergeSort import *
from QuickSort import *

# Generate Integer Array
def Generate_Int_Array(n):
    arr = []
    for i in range(n):
        arr.append(randint(1, 999))
    return arr

# Display Array
def Print_Array(arr):
    print('[ ', end = '')
    for i in arr:
        print(i, end = ', ')
    print(']')

# Code Testing
def main():
    #array = [6, 5, 9, 7, 5, 3, 4, 6]
    print("Unsorted Array")
    array = Generate_Int_Array(10)
    Print_Array(array)
    print()

    print("Sorted By Bubble Sort")
    array = Generate_Int_Array(10)
    Print_Array(array)
    sorted_array = Bubble_Sort(array)
    Print_Array(sorted_array)
    print()

    print("Sorted By Insertion Sort")
    array = Generate_Int_Array(10)
    Print_Array(array)
    sorted_array = Insertion_Sort(array)
    Print_Array(sorted_array)
    print()
    
    print("Sorted By Selection Sort")
    array = Generate_Int_Array(10)
    Print_Array(array)
    sorted_array = Selection_Sort(array)
    Print_Array(sorted_array)
    print()

    print("Sorted By Merge Sort")
    array = Generate_Int_Array(10)
    Print_Array(array)
    sorted_array = Merge_Sort(array)
    Print_Array(sorted_array)
    print()

    print("Sorted By Quick Sort")
    array = Generate_Int_Array(10)
    Print_Array(array)
    sorted_array = QuickSort(array, 0, len(array) - 1)
    Print_Array(sorted_array)
    print()

main()
