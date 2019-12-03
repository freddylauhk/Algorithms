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
