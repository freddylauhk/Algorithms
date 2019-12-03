# Bubble Sort
def Bubble_Sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr)-1):
            if(arr[j] > arr[j+1]):
                # Swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
