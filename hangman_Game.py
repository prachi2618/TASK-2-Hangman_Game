import tkinter as tk
from tkinter import messagebox
import random
import string
import sqlite3
import pandas as pd
import logging

# Set up logging
logging.basicConfig(filename="game_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

# Initialize the database
from database import setup_database
setup_database()

# Function to choose a random word
def choose_word():
    words = ["Python", "Coding", "Portfolio", "Data", "Programming", "Code", "Jupyter", "Anaconda"]
    return random.choice(words).upper()

# Function to update word display
def update_display():
    global guessed_letters, secret_word
    display_text = "".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    word_label.config(text="Word: " + display_text)
    return display_text

# Function to handle a guessed letter
def guess_letter(letter):
    global guessed_letters, attempts, secret_word

    if letter in guessed_letters:
        messagebox.showwarning("Duplicate", f"You already guessed '{letter}'!")
        return

    guessed_letters.add(letter)
    logging.info(f"User guessed: {letter}")

    if letter in secret_word:
        word_display = update_display()
        if "_" not in word_display:
            messagebox.showinfo("Game Over", "Congratulations! You guessed the word!")
            save_game_result(secret_word, "Won", 7 - attempts)
            root.quit()
    else:
        attempts -= 1
        attempts_label.config(text=f"Attempts left: {attempts}")
        if attempts == 0:
            messagebox.showerror("Game Over", f"You lost! The word was {secret_word}")
            save_game_result(secret_word, "Lost", 7 - attempts)
            root.quit()

# Function to show game history from SQLite
def show_history():
    conn = sqlite3.connect("game_history.db")
    df = pd.read_sql_query("SELECT * FROM game_results", conn)
    conn.close()

    history_window = tk.Toplevel(root)
    history_window.title("Game History")
    text_widget = tk.Text(history_window, wrap="none")
    text_widget.insert(tk.END, df.to_string(index=False))
    text_widget.pack()

# Setup the game window
root = tk.Tk()
root.title("Word Guessing Game")
root.geometry("500x500")

# Initialize game variables
secret_word = choose_word()
guessed_letters = set()
attempts = 7

# UI Components
word_label = tk.Label(root, text="Word: " + "_" * len(secret_word), font=("Arial", 20))
word_label.pack(pady=10)

attempts_label = tk.Label(root, text=f"Attempts left: {attempts}", font=("Arial", 14))
attempts_label.pack(pady=5)

# Letter Buttons
frame = tk.Frame(root)
frame.pack()
for letter in string.ascii_uppercase:
    tk.Button(frame, text=letter, width=4, height=2, command=lambda l=letter: guess_letter(l)).pack(side=tk.LEFT)

# Show history button
history_button = tk.Button(root, text="Show Game History", command=show_history)
history_button.pack(pady=10)

root.mainloop()
