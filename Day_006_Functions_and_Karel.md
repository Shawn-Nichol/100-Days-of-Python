# Day 6: Python Functions & Karel
An overview of my progress, key learnings, and the project built on Day 6 of the 100 Days of Code Python Bootcamp.

<br><br>
### 🛠️ Features
---
* **Defining and Calling Functions:** Learning how to bundle instructions together using the `def` keyword to create reusable, custom blocks of code.
* **Indentation Rules:** Understanding how spaces and blocks define code execution scope in Python, preventing indentation syntax errors.
* **While Loops:** Executing logic repeatedly *while* an overarching condition remains true, shifting away from fixed sequence ranges.
* **Infinite Loops Defensively:** Recognizing the logic traps that trigger endless runtime loops and designing fallback checks to navigate them safely.
* **Edge-Case Pathfinding:** Programming a conditional instruction set to help an autonomous agent navigate varying obstacle layout structures dynamically.

<br><br>
### 🚀 Day 6 Project: Escaping the Maze
---
**Description:** A pathfinding script designed to solve a dynamic grid maze of unknown proportions using conditional logic blocks to follow an unbroken boundary path to the destination.

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Outer game loop running until the goal condition is reached
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
