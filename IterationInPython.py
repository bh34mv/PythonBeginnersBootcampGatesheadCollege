#FOR ... ENDFOR
total = 0
for counter in range (1, 8):
    max_temp = input('Enter maximum temperature for day ' + str(counter) + ': ')
    max_temp = int(max_temp)
    total = total + max_temp
    
average_temp = total / 7
print('The average temperature for the week was:', average_temp)

#More for loops in Python.
for x in range(6):
    print(x)
    
for x in 'banana':
    print(x)
    
#WHILE ... ENDWHILE
email_address = input('Enter email address: ')
while '@' not in email_address:
    email_address = input('Invalid email address - please re-enter: ')
print('Thank you')

#REPEAT ... UNTIL
counter = 0
while True:
    counter += 1
    print(counter)
    if counter >= 6:
        break
        
#Print first 10 natural numbers while using loop.
i = 1
while i <10:
    print(i)
    i += 1
    
#Print number pattern using loop.
print("Number Pattern ")
row = 5
#Start: 1
#Stop: r+1 (range never includes stop number in result).
#Step: 1
#Run loop 5 times.
for i in range(1, row + 1, 1):
    #Run inner loop i+1 times.
    for j in range(1, i, + 1):
        print(j, end=' ')
        #Empty line after each row.
        print("")
        
#Print multiplication table of given number.
n = 2
#Stop: 11 (range never includes stop number in results).
#Run loop 10 times.
for i  in range(1, 11, 1):
    #2 *  i (current number)
    product = n * i
    print(product)
    
#Display numbers from -10 to -1 using for loop.
for num in range(-10, 0, 1):
    print(num)
    
#99 bottles of beer on the wall song.
for i in range(99, 0, -1):
    if(i == 2):
        print(*{} "bottles of beer on the wall, take one down, pass it around, {} bottle of beer on the wall".format(i, i, i-1))
    elif(i == 1):
        print(*{} "bottle of beer on the wall, take one down, pass it around, no bottles of beer on the wall".format(i, i))
    else:
        print(*{} "bottles of beer on the wall, {} bottles of beer, take one down, pass it around, {} bottles of beer on the wall".format(i, i, i-1))