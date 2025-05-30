def quickSort(arr):
    if(len(arr)<=1):
        return arr
    pivot = arr[len(arr)-1]
    left=[]
    right=[]
    for i in range(0,len(arr)-1):
        if(arr[i]<pivot):
            left.append(arr[i])
        else:
            right.append(arr[i])
    result=[]
    result.extend(quickSort(left))
    result.append(pivot)
    result.extend(quickSort(right))
    return result
arr=[10,56,3,2,65,4]
print(quickSort(arr))
