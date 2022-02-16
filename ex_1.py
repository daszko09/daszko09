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
