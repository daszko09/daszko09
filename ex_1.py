# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# 1. Add on to the previous program by asking the user for another number and printing out that many 
# copies of the previous message.
# 2. Print out that many copies of the previous message on separate lines.

import datetime
teraz=datetime.datetime.now()

name=input("What's your name?: ")
age=int(input('Hi ' + name + ', how old are you?: '))
year=str((teraz.year+(100-age)))

message=(name+' you will turn 100 in '+year+' ! :)')
print(message)
number=int(input('\n'+name+', type a random number: '))

n=0

while n < number:
    print('\n'+message+'\n')
    n+=1
