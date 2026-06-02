# Day 7: Hangman Game
An overview of my progress, key learnings, and the project built on Day 7 of the 100 Days of Code Python Bootcamp.

<br><br>
### 🛠️ Features
---
* **Problem-Solving & Flowcharts:** Breaking a multi-step game loop down into discrete, manageable programming steps and visual logic before writing a single line of code.
* **String Masking & Tracking:** Generating an evolving list of placeholders (`_`) and using index matching to dynamically reveal letters as correct guesses are made.
* **Game State Management:** Implementing a robust `while` loop controlled by boolean flags (`game_over = False`) to keep the gameplay active until a definitive win or loss condition is reached.
* **UX/UI with External Modules:** Separating presentation and data from core logic by importing modular ASCII graphics (`hangman_art.py`) and a comprehensive secret word repository (`hangman_words.py`).
* **Hard Work and Perseverance:** Reaffirming that deliberate practice, consistency, and pushing through complex logic puzzles beats raw talent every single time.

<br><br>
### 🚀 Day 7 Project: Create a Hangman Game
---
**Description:** A classic command-line implementation of Hangman that chooses a random word, processes player guesses, tracks remaining lives, and draws a progressive visual hangman stage using ASCII art until the player wins or runs out of turns.
