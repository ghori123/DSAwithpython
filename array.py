from array import array
 
arr = array('i', [1, 2, 3, 4, 5])                     #'b' / 'B': Signed / Unsigned 1-byte integer
                                                      # 'h' / 'H': Signed / Unsigned 2-byte integer
print (arr)                                           # 'i' / 'I': Signed / Unsigned 2 or 4-byte integer
                                                      #  'l' / 'L': Signed / Unsigned 4-byte integer
for i in range (0,len(arr)):                          # 'q' / 'Q': Signed / Unsigned 8-byte integer
      print(arr[i], end=" ")                          # 'f': 4-byte floating-point (float)
print()                                               #'d': 8-byte floating-point (double)
                                                      #'u': Unicode character (deprecated since Python 3.13)
for val in arr:
    print(val, end=" " )                                                     

print(arr.typecode)   

reverse_arr = array(arr.typecode, reversed(arr))
print("\nReversed array:", reverse_arr)

arr.insert(2, 10)  # Insert 10 at index 2
print (arr)

arr.append(6)
print (arr)

arr[2] = 20  # Update the value at index 2
print (arr)

copy_arr = array(arr.typecode, [i for i in arr])
print(copy_arr)

arr.remove(20)  # Remove the first occurrence of 20
arr.pop(3)  # Remove the element at index 3
print (arr)

# slicing of array
sliced_arr = arr[1:4] # 4 is not included in the slice
sliced_arr2 = arr[1:4:2]  # Slicing with a step of 2
sliced_arr3 = arr[::-1]  # Reverse the array
print("Sliced array:", sliced_arr)
print("Sliced array with step:", sliced_arr2)
print("Reversed array:", sliced_arr3)

# input from user
arr_user = array('i', [])
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr_user.append(element)

print("User-defined array:", arr_user)

# for searching an element in the array
index = arr.index(5)  # Find the index of the first occurrence of 4
print(f"Index of 5 in the array: {index}")