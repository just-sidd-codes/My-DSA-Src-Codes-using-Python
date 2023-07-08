#Selection Sort

array_size = int(input("Enter the size of Array : "))
print("") 

input_array = []

for i in range(0,array_size):
    value = int(input("Enter Element in array : "))
    input_array.append(value)

print("")

print("Unsorted Input array : ",input_array)

for i in range(0,array_size):
    min = i
    for j in range((i+1),array_size):
        if(input_array[min]>input_array[j]):
            min = j
    temp = input_array[i]
    input_array[i] = input_array[min]
    input_array[min] = temp

print("Sorted array         : ",input_array)    