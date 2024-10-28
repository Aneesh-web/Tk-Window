import tkinter as tk
import random

# Initialize scores
player_score = 0
computer_score = 0

# Function to determine the winner
def play(player_choice):
    global player_score, computer_score
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    result = ""

    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Scissors" and computer_choice == "Paper") or \
         (player_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
        player_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    # Update the result label and scores
    result_label.config(text=f"Your Choice: {player_choice}\nComputer Choice: {computer_choice}\n{result}")
    player_score_label.config(text=f"Your Score: {player_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

# Setting up the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Displaying the game title and instructions
tk.Label(root, text="Choose Rock, Paper, or Scissors").pack(pady=10)

# Player's choice buttons
button_rock = tk.Button(root, text="Rock", width=10, command=lambda: play("Rock"))
button_rock.pack(pady=5)

button_paper = tk.Button(root, text="Paper", width=10, command=lambda: play("Paper"))
button_paper.pack(pady=5)

button_scissors = tk.Button(root, text="Scissors", width=10, command=lambda: play("Scissors"))
button_scissors.pack(pady=5)

# Labels to display result and scores
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

player_score_label = tk.Label(root, text="Your Score: 0", font=("Helvetica", 12))
player_score_label.pack(pady=5)

computer_score_label = tk.Label(root, text="Computer Score: 0", font=("Helvetica", 12))
computer_score_label.pack(pady=5)

# Run the application
root.mainloop()
