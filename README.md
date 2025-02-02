# Word Guessing Game (Hangman)

## Overview
This is a **GUI-based Word Guessing Game** (similar to Hangman) built using **Python and Tkinter**. The game allows users to guess letters to complete a secret word. It tracks the number of attempts, prevents duplicate guesses, and provides real-time updates. Additionally, the game integrates **SQLite for persistent storage**, **Pandas for displaying past game history**, and **Logging for tracking user activity**.

## Features
- 🎮 **GUI-Based Gameplay** using Tkinter
- 🔠 **Letter Buttons for Input** instead of manual text entry
- 🏆 **Tracks Win/Loss Status and Attempts**
- 📊 **Game History Storage** using SQLite
- 📜 **View Game History** with Pandas in a readable format
- 📝 **Logs User Activity** for tracking guesses

## Technologies Used
- **Python** (Core Logic)
- **Tkinter** (GUI Development)
- **SQLite** (Persistent Storage)
- **Pandas** (Data Display)
- **Logging** (Tracking User Activity)

## Installation
### 1️⃣ Prerequisites
Ensure you have Python installed. You may need to install the following dependencies:
```bash
pip install tk pandas sqlite3
```

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/word-guessing-game.git
cd word-guessing-game
```

### 3️⃣ Run the Game
```bash
python hangman_gui.py
```

## How to Play
1. **Click on a letter button** to guess a letter.
2. The **game updates the displayed word** if the letter is correct.
3. If the guess is wrong, **attempts decrease**.
4. **Win Condition:** You guess all letters correctly.
5. **Lose Condition:** You run out of attempts.
6. Click **"Show Game History"** to view past results stored in SQLite.

## Database Integration (SQLite)
- **Setup Database** (Automatically created on first run)
- Stores **word, result (Win/Loss), attempts, timestamp**
- View game history in a new window using **Pandas**

## Logging System
- Tracks **all guessed letters** in `game_log.txt`
- Logs **successful and failed attempts**

## Future Enhancements
✅ Add **Hangman Graphics** for incorrect guesses
✅ Implement **Leaderboard** to track top players
✅ Provide **Restart & Difficulty Level Options**


