def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]
x = 4

result = linearSearch(mylist, x)
print(result)