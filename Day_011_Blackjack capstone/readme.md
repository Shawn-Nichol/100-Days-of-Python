# Day 11: The Blackjack Capstone Project

## 📌 Project Overview
For Day 11, I built a command-line **Blackjack (21) game** program from scratch. This project serves as a beginner capstone, combining multiple foundational Python concepts including control flow, functions with outputs, loops, and mutability.

## 🛠️ Concepts Covered
* **Functions with Outputs:** Designing modular code blocks that return values.
* **While Loops & Game State:** Managing the main game loop and conditional breaks.
* **Lists & Mutability:** Adding (`.append()`), tracking, and clearing card hands.
* **Mathematical Logic:** Handling special Blackjack rules (e.g., Ace tracking dynamically as 11 or 1 depending on the total score).

---

## 🚀 How It Works
1.  The user is asked if they want to play a game of Blackjack.
2.  Both the player and the computer are dealt two random cards from a standard deck layout.
3.  The player can see their total score and the computer's first card.
4.  The player is prompted to either "hit" (draw another card) or "stand" (keep their current hand).
5.  Once the player stands, the computer automatically draws cards until its total score is 17 or higher.
6.  The winner is determined by checking for a Blackjack, busting (going over 21), or comparing the final scores.

---

## 💻 Code Structure & Hints Applied
The project was refactored using a modular mindset based on the course walkthrough guidelines:
* `deal_card()`: Returns a random card value from a pre-defined deck list.
* `calculate_score()`: Takes a list of cards and returns the sum, while also handling automated adjustments for Aces if the score exceeds 21.
* `compare()`: Determines the final win, loss, or draw outcomes between the user and computer scores.

---

## 🧠 Reflection & Challenges
* **The Ace Rule Dilemma:** Implementing the logic to change an Ace from an 11 to a 1 when the user's score was over 21 required a careful conditional check inside the scoring function.
* **Game Loop Execution:** Managing the exact moment a game should end (either immediately due to an initial Blackjack or after a user chooses to stand) required careful tracking of boolean game-state variables.

## 📁 How to Run
1. Ensure you have Python installed.
2. Clone this repository and navigate to the project directory.
3. Run the application:
   ```bash
   python main.py
