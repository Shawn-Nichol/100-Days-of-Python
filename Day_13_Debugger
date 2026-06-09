# Day 13: Debugging: How to Find and Fix Errors in Your Code
An overview of my progress, key learnings, and the debugging exercises completed on Day 13 of the 100 Days of Code Python Bootcamp.

<br><br>
### 🛠️ Features
---
* **Describing the Problem:** Untangling broken code by untangling expectations from reality, forcing a precise breakdown of what the code is *supposed* to do versus what it is *actually* doing.
* **Reproducing the Bug:** Intentionally triggering exceptions and edge cases under controlled conditions to isolate the exact environment and inputs causing the failure.
* **Playing Computer:** Step-by-step evaluation of code execution from the interpreter's perspective to track variable changes and conditional logic shifts.
* **Squashing Bugs with Print():** Utilizing tactical `print()` statements to peer inside active loops and data states without shifting application flow.
* **Using a Debugger:** Harnessing professional IDE debugging tools to set breakpoints, inspect stack traces, step into functions, and watch variables live.

<br><br>
### 🚀 Day 13 Project: Debugging FizzBuzz
---
**Description:** Reviewing, isolating, and refactoring a broken implementation of the classic FizzBuzz game. The assignment focused on diagnosing logical errors stemming from Python's operator precedence rules (bitwise `&` vs. logical `and`) and flattening independent `if` statements into structured conditional branches.

```python
def fizz_buzz(target):
    for number in range(1, target + 1):
        # 1. Fixed operator precedence by swapping bitwise '&' with logical 'and'
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        
        # 2. Transformed independent 'if' blocks into 'elif' structures to prevent multiple triggers
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            # 3. Ensured clean numerical output for non-matching integers
            print(number)

fizz_buzz(15)
