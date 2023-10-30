#Nested selection.
member = input('Are you an adult or child? ')
day = input('Enter a day: ')

if member == 'child':
    if day == 'Saturday':
        admission_price = 2.00
    else:
        admission_prince = 2.50
else:
    admission_price: 4.00
        
print(admission_price)