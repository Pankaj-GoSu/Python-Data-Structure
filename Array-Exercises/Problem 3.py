#=================== Problem statement 3 ===================
'''
Create a list of all odd numbers between 1 and a max number. Max number is
something you need to take from a user using input() function

'''

#================= Solution =======================

n = int(input("Enter a number upto you want odd numbers\n"))
odd_no_list = []
for i in range(n+1):
    if (i % 2!= 0):
        odd_no_list.append(i)

print(f"Your list of odd number is {odd_no_list}\n")
