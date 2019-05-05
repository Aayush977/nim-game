import random
players = []
count = []
count_number = []
name = ['A','B','C']
asterisk = "*"

# defining a player
def player():
    player1=input("Enter the name of the first player")
    players.append(player1)
    player2 = input("Enter the name of the next player")
    players.append(player2)
    
# creating heap name and stick count
def createHeap(heap_name, heap_number):

    return dict(zip(heap_name, heap_number))

#updating the stick count and pile 
def update_dictionary(pile_choice,stick_number):
    count_number = []
    for key, values in this_dict.items():
        
        if key == pile_choice:
            this_dict[key] = asterisk *(len(values) - stick_number)
        count_number.append(len(this_dict[key]))
    print(count_number)
       
 

for __ in range(3):
    count.append(asterisk * random.randint(5,15))
    
this_dict = createHeap(name, count)
for key, values in this_dict.items():
    count_number.append(len(values))

    
    
#Creating players
player()


print("========================Welcome to Nim Game============================")
print("Here are the three piles")

#assign players lists
current_player = 0
print(count_number)
keep_playing = True
while(keep_playing != False):
    print(this_dict)
    #print(count_number)
    
    
    pile_is_valid = False    
  
    while(pile_is_valid != True):
        pile_choice = input("{} Choose your pile (A, B, C)". format(players[current_player])).upper()
        if(pile_choice in this_dict and len(this_dict["{}".format(pile_choice)])>0):
            
            print("Pile Exists")
            pile_is_valid = True
       # elif(pile_choice in (A.name, B.name, C.name) and this_dict["{}".format(pile_choice)<=0]):
        #    del(this_dict["{}".format(pile_choice)])
        else:
            print("\n Invalid choice. You must select the right pile")
            
        
    count_is_valid = False
    while(count_is_valid != True):
        print("How many sticks do you want to remove from pile {}".format(pile_choice))
        stick_count = int(input())
        if (stick_count <1):
            print("you must choose at least 1 stick. \n\n\n")
        elif(stick_count > len(this_dict['{}'.format(pile_choice)])):
            print("\n Pile doesn't have many sticks")

        #elif (stick_count == sum(this_dict.values())):
            print("you cannot take all the values from the pile")        
        else:
            print("You choose the right stick number")
            count_is_valid = True
        
            update_dictionary(pile_choice,stick_count) 
           
                 
    count = 0
    for key, values in this_dict.items():
        count  +=len(values)
    keep_playing = count > 0
       
    #Checking whether play should continue
    if (keep_playing):
    #using XOR functions to toggle between two players
        current_player ^= 1
        
    else:
        print("The winner is {}".format(players[current_player^1]))
