import random
import tkinter as tk
from tkinter import messagebox

# Initialize scores
user_score = 0
computer_score = 0

# Function to generate computer's choice
def computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner and update scores
def play_game(user_choice):
    global user_score, computer_score
    computer_choice_val = computer_choice()
    
    # Determine winner
    if user_choice == computer_choice_val:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice_val == 'scissors') or \
         (user_choice == 'paper' and computer_choice_val == 'rock') or \
         (user_choice == 'scissors' and computer_choice_val == 'paper'):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    # Display result and scores
    messagebox.showinfo("Result", f"User's Choice: {user_choice}\nComputer's Choice: {computer_choice_val}\n{result}\n\nUser Score: {user_score}\nComputer Score: {computer_score}")

# Create the main GUI window
root = tk.tk()
root.title("Rock-Paper-Scissors Game")

# Create a frame for the game
frame = tk.Frame(root)
frame.pack(pady=10)

# Create buttons for rock, paper, and scissors
rock_button = tk.Button(frame, text="Rock", command=lambda: play_game('rock'))
rock_button.pack(side=tk.LEFT, padx=10)

paper_button = tk.Button(frame, text="Paper", command=lambda: play_game('paper'))
paper_button.pack(side=tk.LEFT, padx=10)

scissors_button = tk.Button(frame, text="Scissors", command=lambda: play_game('scissors'))
scissors_button.pack(side=tk.LEFT, padx=10)

# Start the GUI main loop
root.mainloop()
