# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# 1. Add on to the previous program by asking the user for another number and printing out that many 
# copies of the previous message.
# 2. Print out that many copies of the previous message on separate lines.

import datetime
teraz=datetime.datetime.now()

name=input("Jak masz na imie?: ")
age=int(input('Hej ' + name + ', ile masz lat?: '))
year=str((teraz.year+(100-age)))

message=(name+' skonczysz 100 lat w roku '+year+' ! :)')
print(message)
number=int(input('\n'+name+', podaj losową cyfrę: '))

n=0

while n < number:
    print('\n'+message+'\n')
    n+=1
