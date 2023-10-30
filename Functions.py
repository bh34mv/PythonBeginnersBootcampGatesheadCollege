#Print welcome message.
def print_welcome_message():
    print('Hello and welcome to Python')
    
print_welcome_message()

#Return welcome message
def get_welcome_message():
    return 'Hello and welcome to Python'

print(get_welcome_message())

#Passing arguments into functions.
def multiply_by_2(num):
    doubled_num = num * 2
    return doubled_num

input_number = input('Enter an integer: ')
input_number = int(input_number)
doubled_input = multiply_by_2(input_number)
message = 'Your number doubled is ' + str(doubled_input)
print(message)

#Default arguments.
def repeat_message(message, number_of_times=2):
    for repetition in range(number_of_times):
        print(message)
        
repeat_message("Hello")
repeat_message("Hello again", 3)
#Hello" will be printed twice, "Hello again" will be printed three times.

#Add two numbers.
def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    num3 = num1 + num2
    
    return num3

#Driver code.
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")

#Some more functions.
def is_prime(n):
    if n in [2, 3]:
        return True
    if (n == 1) or (n % 2 == 0):
        return False:
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False:
        r += 2
    return True
print(is_prime(78), is_prime(79))

#Python program to demonstrate keyword arguments.
def student(firstname, lastname):
    print(firstname, lastname)
    
#Keywords arguments.
student(firstname='TestFirstname', lastname='TestSurname')
student(lastname='Test2Surname', firstname='TestFirstname')

#Return value (AKA statement).
def square_value(num):
    #Function returns square value of entered number.
    return num**2

print(square_value(2))
print(square_value(-4))