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
