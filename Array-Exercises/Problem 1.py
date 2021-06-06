# ============== Problem 1 Statement =========================
'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this

'''

# =================== Solution ==============================

list_expense = [["january" , 2200] , ["February" , 2350],["March",2600],["April",2130],["May",2190]]

# Answer 1 -

dollar_=list_expense[1][1]- list_expense[0][1] # using List slicing
print(f"You spend {dollar_} dollars Extra in {list_expense[1][0]}\n")

# Answer 2-

total_expense = 0
for expense in range(3): # simple loop for addition
    total_expense = list_expense[expense][1] + total_expense

print(f"Your Total Expense of 3 month is {total_expense}\n")

# Answer 3 -

for i in range(len(list_expense)): # it give index values 
    for item in list_expense[i]: # it give what inside the list which we iterate
        if item == 2000:
            print(f"You spend 2000 in {list_expense[i][0]}\n")
        else:
            pass
print(f"Sorry You did not spend exactly 2000 dollars\n")          


# Answer 4 -

june = ["june",1980] 
list_expense.append(june)
print(f"Your updated list is {list_expense}\n")

# Answer 5 -

# we can do it with simple method of slicing but i make a looped program so that if we change only 
#month then we can update our list

refund = 200 # a/c to question got this in april month
for i in range(len(list_expense)):
    for item in list_expense[i]:
        if item == "April":
            list_expense[i][1] = list_expense[i][1] - refund
        else:
            pass

print(f"Your updated list is {list_expense}")