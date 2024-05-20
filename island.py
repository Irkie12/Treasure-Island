print("This code and storyline is written by Isaac Earl")
print("Welcome to Treasure Island.")
print("There is a treasure chest on the island in the lake, can you find it?") 

#First choice of where to go
choice_1=input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. Or type 'raft' to make a raft to get across.")

"""
in python you don't need these brackets on the if statement - you can just do 

if choice_1 == "swim"

to make it a bit more robust - what I would do is 

if choice_1.strip().lower() == "swim"
this means that if somebody puts in "swim " or "Swim" or "SWIM" it will still recognise it

you can also use return instead of exit - return completely ends the program

you can do these for all of these
"""
if(choice_1 == "swim"):

    print("You got attacked by an angry trout and drown. Game Over")
    print("Better luck next time.")
    exit(1)

elif(choice_1 == "wait"):

    print("You waited for a boat but it never came.")

extra=input("Should you swim or make a raft to get across? Type 'swim' to swim and type 'raft' to build a raft.")




if (extra == 'swim'):
     print("You got attacked by an angry trout and drown. Game Over")
     print("Better luck next time.")
          
     exit(1)

elif (extra == 'raft'):
     print("You start making a raft.")

elif(choice_1 == "raft"):

    print("You start making a raft.")



else:
    print("Using an imaginary transport are we? Game Over for trying to cheat")
    print("Better luck next time.")
    exit(1)



choice_2=input("For putting your raft together what should you use? Type 'palm leaves' or 'rope'.")

if (choice_2 == "rope"):
    print("You use rope and set off on your raft.")


elif (choice_2 == "palm leaves"):
    print("You use palm leaves and set off on your raft")
    print("20 seconds after you set off the raft falls apart and you get attacked by an angry trout and drown. Game Over")
    print("Better luck next time.")
    exit(1)


else:
    print("Using imaginary methods of transport are we? Game Over for trying to cheat")
    print("Better luck next time.")
    exit(1)


choice_3=input("You arrive at the island and there is a path left and right, which one do you follow? Type 'left' or 'right'")

if (choice_3 == "left"):
    print("You walked left, a bear came out and ate you. Game Over")
    print("Better luck next time.")
    exit(1)


if (choice_3 == "right"):

    print("You walk right")

else:
    print("Um.... there isn't a path that way... Game Over for trying to cheat")
    print("Better luck next time.")
    exit(1)



choice_4=input("It is getting dark, you have two options, type 'camp' to stay and camp for the night or 'walk' to carry on walking.")

if (choice_4 == "walk"):

    print("You carry on walking, but suddenly a pack of wolves spring out before you and tear you to pieces. Game Over")
    print("Better luck next time.")
    exit(1)

if (choice_4 == "camp"):
    print("You light a campfire and sleep under a tree for shelter.")

else:
    print("Made up an imaginary option did you? Game Over for trying to cheat.")
    print("Better luck next time.")
    exit(1)

choice_5=input("You wake up and it is morning, you carry on walking. But then you see a little hut. Type 'enter' to enter the hut or 'walk' to walk away")

if (choice_5 == 'enter'):

    print("You walk in the hut, there is nothing there. But suddenly the floor opens like a trapdoor and drops you in a pond. An angry trout eats you. Game Over")
    print("Better luck next time.")
    exit(1)

if (choice_1 == 'wait'):
    print("You walk along and find yourself at a cliff, you see a chest in a brick shelter and open it. Oh No! Because you waited for a boat, someone else got here first and took all the treasure!")
    print("Game Over")
    print("Better luck next time!")
    exit(1)



if (choice_5 == 'walk'):
    print("You walk along and find yourself at a cliff, you see a chest in a brick shelter and open it. It has the treasure!")
    
    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
    
    print("You beat the game!")
    print("Thank you for playing!")



    print("Code and story written by Isaac Earl")
    exit(1)

else:
    print("Trying to use another option are you? Game Over for trying to cheat.")
    exit(1)










    
