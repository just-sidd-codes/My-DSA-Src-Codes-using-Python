# Linear Search in Python

array_size = int(input("Enter the size of Array : "))
print("") 

input_array = []
indexes = []

for i in range(0,array_size):
    value = int(input("Enter Element in array : "))
    input_array.append(value)

print("") 
key = int(input("Enter the element you want to search : "))
print("") 

for i in range(0,array_size):
    if(input_array[i]==key):
        indexes.append(i)

length = len(indexes)

if(length==0):
    print("Element ",key," is not present in the Array")
elif(length==1):
    print("Element ",key," is present at index ",indexes[0])
else:
    print("Element ",key," is present at indexes : ",indexes)


print("") 
print("Thanks")
    