def insertionSort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while(j>=0 and key<a[j]):
            a[j+1]=a[j]
            j-=1
        a[j+1]=key

n=int(input("Enter the Number of Elements"))
a=[int(x) for x in input("Enter Elements separated by a space").split()]
print("Before Merge Sort: ",a)
insertionSort(a)
print("After Merge Sort: ",a)
print(a)