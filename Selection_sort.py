def selectionSort(data):
    n = len(data)
    for i in range(0,n):
         for j in range(i,n):
            if(data[i] > data[j]):
               data[i],data[j] = data[j],data[i]
    return data

        
R_sel = selectionSort([64,25,32,20,40,15])
print(R_sel)