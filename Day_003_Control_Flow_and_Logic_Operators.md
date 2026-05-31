# Day 3: Control Flow and Logical Operators
An overview of my progress, key learnings, and the project built on Day 3 of the 100 Days of Code Python Bootcamp.

### 🛠️ Features
---
* **Control Flow with if/else:** Implementing conditional logic using `if` and `else` statements to guide the program's execution path based on boolean conditions.
* **The Modulo Operator:** Utilizing the `%` operator to calculate the remainder of a division, a fundamental tool for checking number properties like even or odd.
* **Nested if and elif Statements:** Grouping multiple layers of conditional checks together to handle complex, branching decision-making scenarios seamlessly.
* **Multiple If Statements in Succession:** Executing consecutive, independent `if` statements when a single scenario requires checking and acting upon multiple valid conditions.
* **Logical Operators:** Combining multiple conditions within a single statement using `and`, `or`, and `not` to build advanced, granular validation rules.

<br><br>
### 🚀 Day 3 Project: Treasure Island
---
**Description:** A text-based, choose-your-own-adventure game built entirely in the command line. The player must make consecutive critical choices to navigate a dangerous island, utilizing complex control flows and string matching to survive and find the hidden treasure.

```python
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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

if input('You\'re at a crossroad, where do you to go "left" or "right"\n').lower() == 'left':
    if input('Do you want to "swim" or "wait?"\n').lower() == 'wait':
        door = input('Pick a door, "red", "blue", "yellow"\n').lower()
        if door == 'red':
            print('Burned by fire: Game Over.')
        elif door == 'blue':
            print('Eaten by beasts: Game Over.')
        elif door == 'yellow':
            print('You Win!')
        else:
            print('Game Over.')
    else:
        print("Game Over")
else:
    print('Game Over')

```
