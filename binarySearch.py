def binarySearch(arr, x):
   left = 0
   right = len(arr) - 1

   while left <= right:
       mid = (left + right) // 2

       if arr[mid] == x:
           return mid

       if arr[mid] < x:
           left = mid + 1
       else:
            right = mid - 1

   return -1

mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 11

result = binarySearch(mylist, x)
print(result)