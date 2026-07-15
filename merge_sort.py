def Divide(data,l,r):

    if(l< r):
        m =(l+r)//2
        Divide(data,l,m)
        Divide(data, m+1, r)
        mergeSort(data, l,m,r)
    return data

def mergeSort(data, l,m,r):
    s1 = m-l+1
    s2 = r-m
    L =[0]*s1
    R =[0]*s2

    for i in range(s1):
        L[i] = data[l+i]

    for j in range(s2):
        R[j] = data[m+1+j]

    i = j=0
    k=l
    while(i< s1 and j < s2):
        if(L[i]< R[j]):
            data[k] = L[i]
            i =i+1
            k = k+1
        else:
            data[k] =R[j]
            j = j+1
            k= k+1

    while(i<s1):
        data[k] = L[i]
        i = i+1
        k =k+1

    while(j< s2):
        data[k] =R[j]
        j =j+1
        k= k+1

    return 

data =[21,34,11,5,45,9,50]
A = Divide(data,0 ,6)
print(A)
