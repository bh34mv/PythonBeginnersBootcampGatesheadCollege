#String methods.
fruit = 'orange'
print(fruit)
print(fruit.capitalizer())

#Title method - capitalises first letter of each word.
book_name = 'python for the enthusiastic'
print(book_name.title())

#Count method - counts number of instances of specified letter.
book_name = 'python for the enthusiastic'
print(book_name.count('t'))

#Find method - gives index of first instance of letter.
book_name = 'python for the enthusiastic'
print(book_name.find('t'))

#Dictionary methods.
book_dict = {'title': 'python for the enthusiastic',
             'year': 2022,
             'weight_in_kg': 0.5,
             'no_of_pages': 198}

#Use keys method.
book_dict = {'title': 'python for the enthusiastic',
             'year': 2022,
             'weight_in_kg': 0.5,
             'no_of_pages': 198}

print(book_dict.keys())

#Access value for particular key.
book_dict = {'title': 'python for the enthusiastic',
             'year': 2022,
             'weight_in_kg': 0.5,
             'no_of_pages': 198}

print(book_dict['no_of_pages'])

#Empty dictionary using clear method.
book_dict = {'title': 'python for the enthusiastic',
             'year': 2022,
             'weight_in_kg': 0.5,
             'no_of_pages': 198}

book_dict.clear()
print(book_dict)

#List methods
#Create list.
List = []
print("Blank List: ")
print(List)

#Creating list of numbers.
List = [10, 24, 14]
print("\nList of numbers: ")
print(List)

#Creating list of strings and accessing using index.
List = ["Session", "For", "Python"]
print("\nList Items: ")
print(List[0])
print(List[1])

#Creating list with use of numbers (havind duplicate values).
List = [1, 2, 4, 4, 3, 3, 3, 6 , 5]
print("\nList with the user of Numbers: ")
print(List)

#Creating list with mixed type of values (having numbers and strings).
List = ["Session", "For", "Python"]
print("\nList with the user of Mixed Values: ")
print(List)

#Creating list.
List1 = []
print(len(List1))

#Creating list of numbers.
List2 = [10, 20, 14]
print(len(List2))

#Using map.
#Input size of list.
n = int(input("Enter the size of the list: "))
#Store integer in list using map, split and strip functions.
lst = list(map(int, input("Enter the integer\elements:").strip().split()))[:n]

#Printing the list.
print('The list is:', lst)

#Addition of elements in list.
#Creating list
List = []
print("Initial blank List: ")
print(List)

#Addition of elements.
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)

#Adding elements to list using iterator.
for i in range(1, 4):
	List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)

#Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)

#Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)