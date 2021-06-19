# ===== Reverse the array ====

'''
Example -
Input - [1,2,3,4,5]
output - [5,4,3,2,1]

'''
# First method # Time complexity --> O(n)

list = [1,2,3,4,5]
reverse_list1 = []

for item in list: 
    reverse_list1.insert(0,item)

print("Method 1 result")
print(reverse_list1)

# secoond method recursion
reverse_list2 =[]
def reverse_list(list):
    if len(list) == 1:
        reverse_list2.append(list[0])
    else:
        temp = list[-1]
        list.pop()
        reverse_list(list)
        reverse_list2.insert(0,temp)

print("Method 2 result")
reverse_list(list)
print(reverse_list2)

#third method - swaping # Time complexity --> O(n)
list1 = [1,2,3,4,5]
i = 0
j = -1
for x in range(len(list1)//2):
    list1[i],list1[j] = list1[j],list1[i]
    i = i + 1
    j = j - 1 

print("Method 3 result")
print(list1)

#four method - # Using python list slicing

list2 = [1,2,3,4,5]

def reverselist(list):
    print(list[::-1])

print("Method 4 result")
reverselist(list2)