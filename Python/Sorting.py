# Import random library
from random import seed
from random import randint

# Sorting Algorithm
# Bubble Sort
def Bubble_Sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr)-1):
            if(arr[j] > arr[j+1]):
                # Swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr          

# Insertion Sort
def Insertion_Sort(arr):
    for i in range(len(arr) - 1):
        if(arr[i] > arr[i+1]): 
            j = i+1;
            while j > 0:
                if(arr[j - 1] > arr[j]):
                    # Swap
                    arr[j - 1], arr[j] = arr[j], arr[j - 1]
                    j -= 1
                else:
                    break
    return arr

# Selection Sort
def Selection_Sort(arr):
    for i in range(len(arr) - 1):
        minIndex = i
        # Find Min Value
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # Swap
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

# Merge Sort
def Merge_Sort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2   #Finding the mid of the array 
        left = arr[:mid]    # Dividing the array to left and right
        right = arr[mid:]   
  
        Merge_Sort(left) # Sort the first half 
        Merge_Sort(left) # Sort the second half 
  
        i = j = k = 0
        
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                arr[k] = left[i] 
                i+=1
            else: 
                arr[k] = right[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(left): 
            arr[k] = left[i] 
            i+=1
            k+=1
          
        while j < len(right): 
            arr[k] = right[j] 
            j+=1
            k+=1

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

    print("Sorted By Bubble Sort")
    sorted_array = Bubble_Sort(array)
    Print_Array(sorted_array)

    print("Sorted By Insertion Sort")
    sorted_array = Insertion_Sort(array)
    Print_Array(sorted_array)
    
    print("Sorted By Selection Sort")
    sorted_array = Selection_Sort(array)
    Print_Array(sorted_array)

    print("Sorted By Merge Sort")
    sorted_array = Merge_Sort(array)
    Print_Array(sorted_array) 

main()
