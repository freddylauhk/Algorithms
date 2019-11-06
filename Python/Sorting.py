# Import random library
from random import seed
from random import randint

# Sorting Algorithm
# Bubble Sort
def Bubble_Sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr)-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr          

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
    array = Generate_Int_Array(50)
    Print_Array(array)

    print("Sorted Array")

    sorted_array = Bubble_Sort(array)
    Print_Array(sorted_array)
