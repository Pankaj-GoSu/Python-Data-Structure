# === Given an array which consist of 0s,1s,2s .sort the array without using any sorting also ====

'''
Given an array of size N containing only 0s,1s, and 2s; sort the array in asceding order.

Example -
input-
N = 5
arr[] = 0 2 1 2 0
output-
0 0 1 2 2

'''
# method 1

class Sorting:
    asceding_list = []
    def kth_min_element(self,list,N):
        i = list[0]
        if len(list) == 1:
            self.asceding_list.append(list[0])
        else:
            for item in list:
                if item < i:
                    i = item
            self.asceding_list.append(i)
            list.remove(i)
            self.kth_min_element(list,N)
        return self.asceding_list
x = Sorting()
print("method 1st")
list1 = [0,2,1,0,1]
print(x.kth_min_element(list1,5))


# method 2 

def sort012(arr,n):
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for item in arr:
        if item == 0:
            count_0 += 1
        elif item == 1:
            count_1 += 1
        else:
            count_2 += 1
    i = 0
    while count_0 or count_1 or count_2:
        if count_0:
            arr[i] = 0
            i += 1
            count_0 -= 1
            continue 
        elif count_1:
            arr[i] = 1
            i += 1
            count_1 -= 1
            continue 
        else:
            arr[i] = 2
            i += 1
            count_2 -= 1
            continue 

list1 = [0,2,1,0,2]
sort012(list1,5) # jo argument hum pass kringe usme ye operation perform krega and then hume wo 
                 # aur us argument m function k operation k hisab se change milinge jaise list1 
                 # m change ho jayega wo sorted hoga. 
print("method 2nd")
print(list1)

def sort012(arr,n):

    if n == 1:
        return arr
    arr1 = arr[:]
    arr2 = arr[:]
    arr3 = arr[:]
    for item in arr1:
        if item == 0:
            arr.insert(0,0)
    
    for item in arr2:
        if item == 1:
            arr.insert(0,1)
   
    for item in arr3:
        if item == 2:
            arr.insert(0,2)

    
    for i in range(n):
        arr.pop()
    
    arr.reverse()
    
list1 = [0,2,1,0,2]
sort012(list1,5)
print("method 3rd")
print(list1)

