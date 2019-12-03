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
