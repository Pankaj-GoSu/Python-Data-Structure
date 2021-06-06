# ============== Problem 1 Statement =========================
'''
heros=['spider man','thor','hulk','iron man','captain america']

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

'''

# ====================== Solution =============================

# Answer 1
heros=['spider man','thor','hulk','iron man','captain america']

# using inbuild function 
print(f"length of list is {len(heros)}\n")

#we can also make a loop for this
i = 0
for item in heros:
    i += 1
print(f"length of list is {i}\n")

# Answer 2 
heros1 = heros[:] # when we want to give copy of list then we use this code
heros1.append('black panther')
print(f"updated list is {heros1}\n")

# Answer 3 

# This is using inbuild function 
heros2 = heros[:]
heros2.insert(3,'black panther')
print(heros2)

# We can do this with other method let suppose we do not know index of hulk and that how we give index for black panther.

heros3 = heros[:]
for i in range(len(heros3)):
    if heros3[i] == "hulk":
        heros3.insert(i+1,'black panther')

print(f"Updated list is {heros3}")
        

# Answer 4 

heros4 = heros[:]
heros4[1:3] = ["doctor strange"] # Important 

print(heros4)
# Answer 5 

# here i am using inbuild function for sort 
# this function sort alphabetical order 
heros.sort()
print(heros)

heros_reverse = heros[::-1]
print(heros_reverse)