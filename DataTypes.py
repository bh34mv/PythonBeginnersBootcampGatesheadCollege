#Integers and floats.
my_integer = -167
data_type = type(my_integer)
print(data_type)

my_floating_point_number = 10.0
data_type = type(my_floating_point_number)
print(data_type)

my_number = 10
data_type = type(my_number)
print(data_type)

my_number /= 3
data_type = type(my_number)
print(data_type)

my_number = pow(10, 2) #10 squared.
print(my_number)

data_type = type(my_number)
print(data_type)

my_number = pow(10, 2) #Square root of 100.
print(my_number)

data_type = type(my_number)
print(data_type)

my_number = 9
print(type(my_number))

my_number = pow(9, 0.5) #Square root of 9.
print(my_number)
my_number = pow(my_number, 2)
print(my_number)

print_type(my_number)

my_first_number = pow(9, 0.5)
my_second_number = 9 ** 0.5
print(my_first_number)
print(my_second_number)

data_type = type(my_first_number)
print(data_type)
data_type = type(my_second_number)
print(data_type)

my_first_number = pow(-9, 0.5)
my_second_number = -9 ** 0.5
print(my_first_number)
print(my_second_number)

data_type = type(my_first_number)
print(data_type)
data_type = type(my_second_number)
print(data_type)

my_first_float = 10.0
my_second_float = 6.8

my_first_int = int(my_first_float)
my_second_float = int(my_second_float)

print(my_first_float)
print(my_second_float)

#Strings.
my_first_string = 'George'
my_second_string = "George's dog"

data_type = type(my_first_string)
print(data_type)

data_type = type(my_second_string)
print(data_type)

my_string = '12.6'

data_type = type(my_string)
print(data_type)

my_float = float(my_string)
print(my_float)

my_first_string = '12'
my_secondstring = '4.6'

my_first_integer = int(my_first_string)
print(my_first_string)

my_second_integer = int(my_second_string)
print(my_second_string)

#Booleans.
my_boolean = True

data_type = type(my_boolean)
print(data_type)

my_boolean = (5 > 10)

data_type = type(my_boolean)
print(data_type)
print(my_boolean)

#Tuples.
my_tuple = (1, 0.5, 'banana')
print(my_tuple[2])

data_type = type(my_tuple)
print(data_type)

my_tuple_length = len(my_tuple)
print(my_tuple_length)

my_tuple = (1, 0.5, 'banana')
print(my_tuple[2])

my_tuple[2] = 'cherry'

number1 = 1
number2 = 2

number1, number2, = number2, number1

print(number1)
print(number2)

my_number = 1
my_list = ['apple', 'banana', 'orange']

my_tuple = (my_number, my_list)
print(my_tuple)

my_number = 3
my_list = [1, 2, 3]

print(my_number)
print(my_tuple)

my_number = 1
my_list = ['apple', 'banana', 'orange']

my_tuple = (my_number, my_list)
print(my_tuple)

my_number = 3
my_list.append('cherry')

print(my_number)
print(my_tuple)

#Functions as data types.
def my_function(message):
    print(message)
    
data_type = type(my_function)
print(data_type)

def my_function(message):
    print(message)
    
data_type = type(my_function)
print(data_type)

my_function('hello from my_function')
my_function2 = my_function
my_function2('hello from my_function2')

#Validate user input.
while True:
    try:
        age = int(input("Please enter your age: "))
    except: ValueError:
        print("Sorry, I didn't understand that."))
        continue
        
    if age < 0:
        print("Sorry, your response must not be negative.")
    else:
        print("Your age is", age)
        
        break