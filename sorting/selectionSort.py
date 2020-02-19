n=input("Enter the Number of Elements")
a=[x for x in input("Enter "+n+" Elements separated by a space").split()]
print("Before Selection Sort: ",a)
for i in range(0,len(a)):
    minElement = i
    for j in range(i+1,len(a)):
        if( a[j] < a[minElement] ):
            minElement = j
    a[i] , a[minElement] = a[minElement] , a[i]
print(a);