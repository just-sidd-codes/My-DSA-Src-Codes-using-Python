#Insertion Sort

array_size = int(input("Enter the size of Array : "))
print("") 

input_array = []

for i in range(0,array_size):
    value = int(input("Enter Element in array : "))
    input_array.append(value)

print("") 

print("Unsorted Input array : ",input_array)

for i in range(0,array_size-1):
    for j in range((i+1),0,-1):
        if(input_array[j]<input_array[j-1]):
            input_array[j],input_array[j-1] = input_array[j-1],input_array[j]

print("Sorted array         : ",input_array)