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
list1 = [0,2,1,0,1]
print(x.kth_min_element(list1,5))
