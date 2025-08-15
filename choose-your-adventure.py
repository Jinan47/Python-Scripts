import time 
name = input('Type your name: ')
print('Welcome', name, 'to this adventure. Where you choose what you want to do!')

time.sleep(2)
while True:
    print("Ok so now let's go on our adventure")
    time.sleep(1)

    first = input('There is a sea infront of you, and you have 2 paths to cross it. The 1st path is a dity road that may make your clothes dirty,and the 2nd one is a road that have the possbility of crocodiles may eat you.so which one would you rather go? Type 1 for the first road and 2 for the 2nd road: ')

    if first == '1':
        print('Amazing! you are really smart, this is the best choice.Because the crocodiles will eat you if you pass from there.And we dont want to lose you!')

    elif first == '2':
        print('We are realy feel sorry for you....because you died from the crocodiles, youve shouldnt pass from this road.Bye bye...')
        
    else:
        print('This option is invalid,You lost!')
