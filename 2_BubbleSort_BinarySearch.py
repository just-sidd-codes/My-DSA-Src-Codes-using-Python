#Linear Sort and Binary Search
#Binary Search only works for the sorted array

array_size = int(input("Enter the size of Array : "))
print("") 

input_array = []

#Bubble Sort----------------------------------------------
for i in range(0,array_size):
    value = int(input("Enter Element in array : "))
    input_array.append(value)

print("")
print("Unsorted Input Array : ",input_array)   
for i in range(0,array_size):
    for j in range(0,array_size-1):
        if(input_array[j]>input_array[j+1]):
            temp = input_array[j]
            input_array[j] = input_array[j+1]
            input_array[j+1] = temp

print("Sorted Array         : ",input_array)
print("") 

#Binary Search---------------------------------------------
key = int(input("Enter the Element you want to search : "))
print("") 

low = 0
high = array_size-1
mid = int((low+high)/2)

while(low<=high):
    if(input_array[mid]==key):
        print("Element is present at index ",mid," in Sorted Array")
        break
    elif(key<input_array[mid]):
        high = mid-1
        mid = int((low+high)/2)
    else:
        low = mid+1
        mid = int((low+high)/2)

if(low>high):
    print("Element ",key," is not present in Array")