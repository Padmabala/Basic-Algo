def bubbleSort(array):
    n=len(array)
    for i in range(1,n):
        for j in range(n-i):
            if(array[j]>array[j+1]):
                array[j],array[j+1]=array[j+1],array[j]


arr=[64,34,25,12,22,11,1]
bubbleSort(arr)
for i in range(len(arr)):
    print("%d" %arr[i])