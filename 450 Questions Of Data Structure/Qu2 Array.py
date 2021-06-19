# === Find the maximum and minimum element in an array ====

'''
input = [2,3,4,55,735,8,9]
output => max element is 735 and min element is 2.

'''

#first method

from functools import reduce

list = [2,3,4,55,735,8,9]

def max_(a,b):
    if a >= b:
        return a
    else:
        return b

def min_(a,b):
    if a <= b:
        return a
    else:
        return b
max_val = reduce(max_,list) # reduce function reduces the array size by doing operation in it.
                            # here we can also use inbuild function {max and min} but here i create those function.
min_val = reduce(min_,list)

print("Method 1 output")
print(f"max element is {max_val} and min element is {min_val}.")


#second method

list1 = [2,3,4,55,735,8,9]

i = list[0]
j = list[0]

# for max value in array:
for item in list1: # here we doing comparison 
    if item > i:
        i = item
#for min value in array:
for item in list1:
    if item < j:
        j = item

print("Method 2 output")
print(f"max element is {i} and min element is {j}.")


# third method : using class:

list2 = [2,3,4,55,735,8,9]

class Max_and_min:

    def __init__(self):
        self.max = None
        self.min =None


def find_min_max(arr):

    maxmin = Max_and_min()
    if len(arr) == 1:
        maxmin.max = arr[0]
        maxmin.min = arr[0]
        return maxmin
    else:
        if arr[0] > arr[1] :
            maxmin.max = arr[0]
            maxmin.min = arr[1]
        else:
            maxmin.max = arr[1]
            maxmin.min = arr[0]

        for i in range(2,len(arr)):
            if arr[i] > maxmin.max:
                maxmin.max = arr[i]
            elif arr[i] < maxmin.min :
                maxmin.min = arr[i]
    
    print(f"max element is {maxmin.max} and min element is {maxmin.min}.")
    return maxmin
print("Method 3 output")
a = find_min_max(list2)
print(a.max)
print(a.min)

# === 4th method ==== : Tournament method:

'''
Divide tha array into two parts and compare the maximums and minimus of the two parts to 
get maximum and minimum of whole array

'''
class Max_Min:

    def __init__(self):
        self.max = None
        self.min = None
        

def max_min(list):
    
    object_maxmin = Max_Min()

    if len(list) == 1:
        object_maxmin.max = list[0]
        object_maxmin.min = list[0]
        return (object_maxmin.max , object_maxmin.min)
    
    elif len(list) == 2:
        if list[0] >= list[1]:
            object_maxmin.max = list[0]
            object_maxmin.min = list[1]
        else:
            object_maxmin.max = list[1]
            object_maxmin.min = list[0]
        return (object_maxmin.max , object_maxmin.min)
    else:
        list_1 = list[:len(list)//2]
        list_2 = list[len(list)//2:]
        
        max_val1,min_val1 = max_min(list_1)
        max_val2,min_val2 = max_min(list_2)

        if max_val1 > max_val2 :
            object_maxmin.max = max_val1
        else:
            object_maxmin.max = max_val2

        if min_val1 < min_val2:
            object_maxmin.min = min_val1
        else:
            object_maxmin.min = min_val2

    return object_maxmin

   
list3 = [90,3,4,55]
print("method 4 output")
x = max_min(list3)
print(x.max)
print(x.min)
    