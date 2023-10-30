#Creating a list.
my_list = ["apple", "banana", "cherry"]
print(my_list)

#Accesing items on list.
my_list = ["apple", "banana", "cherry"]
print(my_list[1])

#Changing item on list.
my_list = ["apple", "banana", "cherry"]
my_list[0] = "blackcurrant"
print(my_list)

#Removing elements from lists.
my_list = ["apple", "banana", "cherry"]
my_list.remove("banana")
print(my_list)

my_list = ["apple", "banana", "cherry", "apple"]
my_list.remove("apple")
print(my_list)
#Only the first "apple" will be removed.

#Poppring items from list.
my_list = ["apple", "banana", "orange"]
item = my_list.pop(2)
print(my_list)
print(item)

my_list = ["apple", "banana", "orange"]
item = my_list.pop()
print(my_list)
print(item)
#Pop will default to last element in last if index isn't supplied.

#Adding items to list.
my_list = ["apple", "banana", "orange"]
my_list.append("strawberry")
print(my_list)

#Extending list.
my_list = ["apple", "banana", "cherry"]
my_new_list = ['pineapple', 'mango']
my_list.extend(my_new_list)
print(my_list)

#Inserting item into list.
my_list = ["apple", "banana", "cherry"]
my_list.insert(1, 'orange')
print(my_list)

#Iterating with lists.
my_list = ["apple", "banana", "cherry"]
for fruit in my_list:
    print(fruit)
    
#Removing list items.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
this.remove("cherry")
print(thislist)

#Loop through list.
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
    
#Creating tuple.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Allowing tuples to include duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Changing tuple values.
x = ("apple", "banana", "cherry")
y = list(x)
y[0] = "kiwi"
x = tuple(y)

print(x)