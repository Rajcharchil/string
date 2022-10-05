num_1 = int(input('Enter your first number: '))
num_2 = int(input('Enter your second number: '))
 
# Addition
print('{} + {} = '.format(num_1, num_2))
print(num_1 + num_2)
 
# Subtraction
print('{} - {} = '.format(num_1, num_2))
print(num_1 - num_2)
 
# Multiplication
print('{} * {} = '.format(num_1, num_2))
print(num_1 * num_2)
 
# Division
print('{} / {} = '.format(num_1, num_2))
print(num_1 / num_2)
# The format() will help out output look descent and formatted.










#make a letter
letter = ''' dear, <|name|>,
\ti am happy for your selection in pornstar
 your are selected 
 thank you
 
 date,<|date|>
'''
name = input ("enter your name :\n")
date = input ("enter date :\n ")
letter = letter.replace("<|name|>",name)
letter = letter.replace("<|date|>",date)

print(letter)