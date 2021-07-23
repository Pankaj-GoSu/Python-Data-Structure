arr = [1,2]
print(arr)

for item in arr:
    print(item)
    if item == 0:
        arr.insert(0,0)
    elif item == 1:
        arr.insert(0,1)
    else:
        arr.insert(0,2)
print(arr)