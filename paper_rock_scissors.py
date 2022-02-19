import random
name=input("\nHi there! What's your name?\n")
game=input('\n'+name+' do you want to play rock/paper/scissors? (y/n)\n')
a=['rock','paper','scissors']
while True:
    if game=='y':
        player=input("\nChoose between rock/paper/scissors or type 'stop':\n")
        cpu=random.choice(a)
        if cpu==player:
            print('You: '+player+'\nCPU: '+cpu)
            print("it's a draw! :D\n")
        elif (cpu==a[0] and player==a[1]) or (cpu==a[1] and player==a[2]) or (cpu==a[2] and player==a[0]):
            print('You: '+player+'\nCPU: '+cpu)
            print("You win!\n")
        elif(cpu==a[0] and player==a[2]) or (cpu==a[1] and player==a[0]) or (cpu==a[2] and player==a[1]):
            print('You: '+player+'\nCPU: '+cpu)
            print("CPU wins!\n")
        elif player=='stop':
            print('\nNice game! See you later! :D')
            break
    else:
        print('\nSure! Maybe next time ! :)')
