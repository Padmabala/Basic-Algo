def partition(a, low,high):
    pivot=a[high]
    i=low-1
    for j in range(low,high):
        if(a[j]<pivot):
            i=i+1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[high]=a[high],a[i+1]
    return i+1

def quickSort(a , low , high):
   if(low<high):
       pivot = partition(a, low, high)
       quickSort(a, low, pivot-1)
       quickSort(a, pivot+1, high)

# n=int(input("Enter total number of elemets"))
# arr=[int(x) for x in input("Enter the elements").split()]
arr=['a','b','a']
quickSort(arr,0,len(arr)-1)
print("After Quick Sort:",arr)