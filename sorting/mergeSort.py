def mergeeSort(arr):
    if len(arr)>1:
        mid=int(len(arr)//2)
        l=arr[:mid]
        h=arr[mid:]
        mergeeSort(l)
        mergeeSort(h)

        i=j=k=0;
        while i<len(l) and j<len(h):
            if(l[i]<h[j]):
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=h[j]
                j+=1
            k+=1
        while i<len(l):
            arr[k]=l[i]
            i+=1
            k+=1
        while j<len(l):
            arr[k]=h[j]
            j+=1
            k+=1
n=int(input("Enter the Number of Elements"))
a=[int(x) for x in input("Enter Elements separated by a space").split()]
print("Before Merge Sort: ",a)
mergeeSort(a)
print("After Merge Sort: ",a)
print(a)


