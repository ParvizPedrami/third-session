
my_list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("original list : " + str(my_list))


li = []
for i in my_list:
  if i not in li:
    li.append(i)


print ("list without duplicates : " + str(li))




original_list : [1, 3, 5, 6, 3, 5, 6, 1]
list_without_duplicates : [1, 3, 5, 6]
