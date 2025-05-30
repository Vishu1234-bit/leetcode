def mergeSort(arr):
    if(len(arr) == 1):
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[0:mid])
    right=mergeSort(arr[mid:len(arr)])
    return merge(left,right)
def merge(l,r):
    i=0
    j=0
    result=[]
    while(i<len(l) and j<len(r)):
        if(l[i]<=r[j]):
            result.append(l[i])
            i+=1
        else:
            result.append(r[j])
            j+=1
    while(i<len(l)):
        result.append(l[i])
        i+=1
    while(j<len(r)):
        result.append(r[j])
        j+=1
    return result
    
arr=[10,56,3,2,65,4]
print(mergeSort(arr))
