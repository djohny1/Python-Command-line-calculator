# Creating a simple calculaor in Python
# 1. Present user with a menu to select a type of operation
# 2. Get the user input 
# 3. Ge the numbers that the user wants to use 
# 4. Perform an operation using the input from the user 
# 5. Display the result to the user 
print " "

print "Hello there welcome to using python simple calculator!"

print " "

print "Please select a letter for the type of operations you would like to do!"
print " "

simple_dict = dict(
  Multiplication = ': A',
  Division = ': B',
  Addition = ': C',
  exponent = ': D',
  modulus = ': E',
  Subtraction = ': F',
  )
# Now we can use the for loop to interate through the dictionary to display the data nicely to the user 
# To get the data display in sorted order, use a built in function, sorted and subscript the dictionnary object using its keys method.
# With that, we can display the data in a more alphabetical order to the user.

for k in sorted(simple_dict.keys()):
  print k, simple_dict[k]

# Next, get the user operational input and store it in a variable to access it later. 
# We can call this variable operation
operation = raw_input('What type of operation you would like to do? \n ')
first_number = int(raw_input('Please enter your firts number to be computed \n '))
second_number = int(raw_input('Please enter your second number to be computed \n'))

print '\n'

# We can use the if  statement in python to compare the user input and execute the operation below.
# If the condition evaulates to be true, the program will run and if not, it will not.
# Added an else statement to accept a lower case letter input. 

if operation == 'A':
  print  first_number * second_number
else:
  if operation.lower() == 'a':
    print first_number * second_number


if operation == 'B':
  print first_number / second_number
else:
  if operation.lower() == 'b':
    print first_number / second_number

if operation == 'C':
  print first_number + second_number
else:
  if operation.lower() == 'c':
    print first_number + second_number

if operation == 'D':
  print first_number ** second_number
else:
  if operation.lower() == 'd':
    print first_number ** second_number

if operation == 'E':
  print first_number % second_number
else:
  if operation.lower() == 'e':
    print first_number % second_number

if operation == 'F':
  print first_number - second_number
else:
  if operation.lower() == 'f':
    print first_number - second_number

print '\n'

raw_input('Press enter to quit')



