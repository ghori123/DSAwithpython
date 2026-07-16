def QuickSort(data, l,r):
    if(l < r):
        p = partition(data,l,r)
        QuickSort(data,l,p-1)
        QuickSort(data,p+1,r)
    return 

def partition(data, l,r):
    pivot = data[l]
    i = l+1
    j = r
    while True:
        while(i <= r and data[i] < pivot):
            i=i+1


        while(j >= l and data[j]> pivot):
            j = j-1


        if (i <j):
            data[i],data[j] = data[j], data[i]
            i=i+1
            j=j-1
        else:
            break
    data[l], data[j]= data[j],data[l]
    return j


data = [23,45,12,65,34,10,3] 
QuickSort(data, 0,len(data)-1)
print(data)
data1 = [1,2,3,4,5]        # already sorted
QuickSort(data1, 0,len(data1)-1)
print(data1)
data2 = [5,4,3,2,1]        # reverse sorted
QuickSort(data2, 0,len(data2)-1)
print(data2)
data3 = [5,5,5,5]          # all equal
QuickSort(data3, 0,len(data3)-1)
print(data3)
data4 =[3,1,3,2,3]        # duplicates
QuickSort(data4, 0,len(data4)-1)
print(data4)
data5 = [1]                # single element
QuickSort(data5, 0,len(data5)-1)
print(data5)






