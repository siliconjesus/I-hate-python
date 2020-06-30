list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
list2 = list1

# Add 16 to the second list:

list2.append(16)

#
# Both lists are updated because when the second list is created 
# its actually just a pointer to the first list in memory
# 

print (list1)
print (list2)