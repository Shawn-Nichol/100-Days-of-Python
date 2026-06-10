# Day 4: Randomization and Python Lists
An overview of my progress, key learnings, and the project built on Day 4 of the 100 Days of Code Python Bootcamp.

<br><br>
### 🛠️ Features
---
* **The Random Module:** Implementing pseudo-random number generation via the Mersenne Twister engine to generate random integers using `random.randint()` and floats using `random.random()`.
* **Understanding the Offset:** Mastering zero-based indexing to cleanly retrieve, read, and interpret data points isolated inside linear data structures.
* **Data Manipulation with Lists:** Storing grouped data collections dynamically using Python Lists, altering their contents using `.append()`, and merging structures using `.extend()`.
* **IndexErrors & Defensively Coding:** Identifying out-of-bounds index exceptions and implementing proper list boundary restrictions to keep software stable.
* **Nested Lists:** Architecting multidimensional structures (2D arrays) by storing lists inside other lists to represent grids, coordinates, or grouped categories.

<br><br>
### 🚀 Day 4 Project: Rock Paper Scissors
---
**Description:** An interactive command-line game where the player competes against a pseudo-randomized computer opponent in a match of Rock, Paper, Scissors, complete with rendered ASCII art graphics and strict input validation.

```python
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps =[rock, paper, scissors]


user_choice = (int(input('''What do you choose? 
0 for "Rock"
1 for "Paper"
2 for "Scissors"\n
''')))

print(rps[user_choice])

if 0 <= user_choice < 3:
    print("Computer chose:")
    cpu_choice = random.randint(0, 2)

    print(rps[cpu_choice])
    if user_choice == 0 and cpu_choice == 2:
        print("You win! 🎉")
    elif cpu_choice == 0 and user_choice == 2:
        print("You lose. 😢")
    elif user_choice > cpu_choice:
        print("You win! 🎉")
    elif cpu_choice > user_choice:
        print("You lose. 😢")
    else:
        print("It's a draw! 🤝")

else:
    print("Invalid choice")
