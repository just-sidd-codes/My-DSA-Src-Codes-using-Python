#QuickSort-----CheatCode

def QuickSort(input_array,pivot):
    if(len(input_array)<=1):
        return input_array
    else: 
        left   = [i for i in input_array[0:] if i<pivot]
        middle = [i for i in input_array[0:] if i==pivot]
        right  = [i for i in input_array[0:] if i>pivot]
        return QuickSort(left,input_array[int(len(left)/2)]) + middle + QuickSort(right,input_array[int(len(right)/2)])

array_size = int(input("Enter the size of Array : "))
print("") 

input_array = []

for i in range(0,array_size):
    value = int(input("Enter Element in array : "))
    input_array.append(value)

print("") 
condition=0
pivot = 0
while(condition==0):
    pivot = int(input("Enter the pivot Element : "))
    print("")
    for i in range(0,array_size):
        if(input_array[i]==pivot):
            condition=1
            break
    if(condition==0):
        print("Input Pivot Element is not present in the list")
        print("Enter Valid Pivot Element")

print("Unsorted Input array : ",input_array)

print("Sorted Array         : ",QuickSort(input_array,pivot))