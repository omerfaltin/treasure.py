from sys import addaudithook

print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("You find yourself on a mysterious island after a long journey at sea. "
      "Your goal? Find the hidden treasure! But be careful—one wrong move could mean disaster.")
print("As you step onto the island, you face a crossroad.")
choice1 = input('If you go "left", you hear the sounds of waves crashing nearby.'
                'If you go "right", you notice strange markings on the ground.')
if choice1 == "left" :
    choice2= input( 'You reach a lake with an old wooden dock.You can "wait" for a boat or "swim" across.')
    if choice2 == "wait":
        choice3 =input('A small boat arrives, and a mysterious figure gestures for you to step in.'
              'The boat takes you safely across to an ancient house with three doors:'
              '"Red door" "Blue door" "Yellow door"')
        if choice3 == "Yellow door":
            print("The yellow door creaks open… inside, you find a shining chest filled with gold and jewels!")
        if choice3 == "Red door":
            print("The red door leads to a room full of fire—you don’t stand a chance!")
        elif choice3 == "Blue door":
            print("The blue door reveals a wild beast that leaps at you!")

    else:
        print("Before you can react, a giant sea creature pulls you under! Game Over.")


else :
    print("You fall into a deep spike pit and your adventure ends. Game Over.")

git remote add origin https://github.com/omerfaltin/3.git
git branch -M main
git push -u origin main


