# Day 5: Python Loops
An overview of my progress, key learnings, and the project built on Day 5 of the 100 Days of Code Python Bootcamp.

<br><br>
### 🛠️ Features
---
* **For Loops with Lists:** Iterating over sequential collections to isolate and execute logic on individual elements one by one.
* **Replicating Built-In Functions:** Building manual tracking algorithms to mimic the behavior of Python's native `sum()`, `len()`, and `max()` functions without actually using them.
* **The Range Function:** Utilizing `range(start, end, step)` to iterate a specific number of times and generate custom number sequences dynamically.
* **Code Block Logic:** Managing nested control flow structures by placing complex conditional `if/elif/else` statements cleanly inside active loop blocks.
* **Hard Work and Perseverance:** Reaffirming that deliberate practice, consistency, and pushing through complex logic puzzles beats raw talent every single time.

<br><br>
### 🚀 Day 5 Project: Create a Password Generator
---
**Description:** A command-line utility that prompts the user for a preferred number of letters, symbols, and numbers, then dynamically processes those configurations to generate a highly secure, completely randomized password.

```python
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
for letter in range(0, nr_letters):
    password_list += (random.choice(letters))

for symbol in range(0, nr_symbols):
    password_list += random.choice(symbols)

for number in range(0, nr_numbers):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = str()
for char in password_list:
    password += char

print(f"You\'re randomly genereated password: {password}")
```
