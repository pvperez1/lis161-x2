def chop(lst):
    lst.pop()
    lst.pop(0)

def middle(lst):
    return lst[1:-1]


my_list = [0,1,2,3,4,5]
print("My current list is:", my_list)
chop(my_list)
print("My list after chop:", my_list)
print("Output of middle:", middle(my_list))
print("My list after middle:", my_list)
