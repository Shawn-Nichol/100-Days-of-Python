# Day 15: Local Development Environment Setup & the Coffee Machine
An overview of my progress, key learnings, and the project built on Day 15 of the 100 Days of Code Python Bootcamp.

<br><br>
### 🛠️ Features
---
* **Local IDE Transition:** Transitioning from web-based sandboxes to a professional local development workflow using PyCharm, configuring virtual environments (`venv`), and managing project structures.
* **Global State & Resource Management:** Maintaining a persistent system state utilizing deeply nested dictionaries to track volatile real-time quantities (water, milk, coffee, and money).
* **Functional Modularity:** Refactoring monolithic logic into dedicated, single-responsibility helper functions to check resources, process transactions, and deduct ingredients.
* **User Input & System Triggers:** Implementing loop-driven control flows to monitor customer selection while maintaining "hidden" administrative commands (`off`, `report`) for machine maintenance.
* **Transaction Math & Coin Processing:** Standardizing monetary input by converting physical coin counts (quarters, dimes, nickels, pennies) into float calculations, processing refunds, and calculating exact change.

<br><br>
### 🚀 Day 15 Project: The Digital Coffee Machine
---
**Description:** A command-line simulation of a commercial coffee vending machine. The program manages dynamic resource tracking, processes physical coin values, updates a central ledger, handles change logic, and serves three distinct beverage recipes with strict validation at every stage.
