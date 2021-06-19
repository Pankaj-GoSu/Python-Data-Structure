#====== Find the kth max and min elelment of an array =========

'''
Input -->
N = 6 
arr[] = 7 10 4 3 20 15
k = 3
output : 7

Explanation:
3rd smallest element in the given array is 7

'''
# kth smallest element
list = [7,10,4,3,20,15]
k = 3

acceding_list =[]
def kth_min_element(list):
    i = list[0]
    if len(list) == 1:
        acceding_list.append(list[0])
    else:
        for item in list:
            if item < i:
                i = item
        acceding_list.append(i)
        list.remove(i)
        kth_min_element(list)

kth_min_element(list)
print("kth minimum")
print(acceding_list[k-1])

# kth max element
desceding_list = acceding_list[::-1]
print("kth maximum")
print(desceding_list[k-1])


