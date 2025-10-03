my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newlist = []

for num in my_list:
    if num not in newlist:
        newlist.append(num)
my_list = newlist[:]
print("The list with unique elements only:")
print(my_list)
