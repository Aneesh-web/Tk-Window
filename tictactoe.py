import tkinter as tk
from tkinter import messagebox
import random

def check_winner():
    """Check if there's a winner or if the game ends in a draw."""
    for line in winning_combinations:
        if buttons[line[0]]['text'] == buttons[line[1]]['text'] == buttons[line[2]]['text'] != "":
            for idx in line:
                buttons[idx].config(bg="lightgreen")  # Highlight the winning cells
            messagebox.showinfo("Game Over", f"Player {buttons[line[0]]['text']} wins!")
            reset_game()
            return

    if all(button['text'] != "" for button in buttons):
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_game()

def button_click(idx):
    """Handle button clicks for marking X or O."""
    global current_player
    if buttons[idx]['text'] == "":
        buttons[idx]['text'] = current_player
        check_winner()
        if mode == "computer" and current_player == "X":
            current_player = "O"
            computer_move()
        else:
            current_player = "O" if current_player == "X" else "X"
    else:
        messagebox.showwarning("Invalid Move", "This cell is already taken!")

def computer_move():
    """Let the computer make a move based on the selected difficulty."""
    global current_player
    empty_buttons = [idx for idx, button in enumerate(buttons) if button['text'] == ""]
    
    if difficulty == "Easy":
        # Random move
        idx = random.choice(empty_buttons)
    
    elif difficulty == "Medium":
        # Block the player if they are about to win
        idx = find_blocking_move("X")
        if idx is None:
            idx = random.choice(empty_buttons)

    elif difficulty == "Hard":
        # Optimal move using minimax
        idx = find_best_move("O")
    
    buttons[idx]['text'] = current_player
    check_winner()
    current_player = "X"

def find_blocking_move(player):
    """Find a move to block the given player's winning line."""
    for line in winning_combinations:
        values = [buttons[i]['text'] for i in line]
        if values.count(player) == 2 and values.count("") == 1:
            return line[values.index("")]
    return None

def find_best_move(player):
    """Find the best move using the minimax algorithm."""
    best_score = -float('inf') if player == "O" else float('inf')
    best_move = None
    for idx in range(9):
        if buttons[idx]['text'] == "":
            buttons[idx]['text'] = player
            score = minimax(0, False if player == "O" else True)
            buttons[idx]['text'] = ""
            if (player == "O" and score > best_score) or (player == "X" and score < best_score):
                best_score = score
                best_move = idx
    return best_move

def minimax(depth, is_maximizing):
    """Minimax algorithm to determine the optimal move."""
    for line in winning_combinations:
        values = [buttons[i]['text'] for i in line]
        if values == ["O", "O", "O"]:
            return 1
        elif values == ["X", "X", "X"]:
            return -1

    if all(button['text'] != "" for button in buttons):
        return 0  # Draw

    if is_maximizing:
        best_score = -float('inf')
        for idx in range(9):
            if buttons[idx]['text'] == "":
                buttons[idx]['text'] = "O"
                score = minimax(depth + 1, False)
                buttons[idx]['text'] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for idx in range(9):
            if buttons[idx]['text'] == "":
                buttons[idx]['text'] = "X"
                score = minimax(depth + 1, True)
                buttons[idx]['text'] = ""
                best_score = min(score, best_score)
        return best_score

def reset_game():
    """Reset the game to its initial state."""
    global current_player
    current_player = "X"
    for button in buttons:
        button.config(text="", bg="SystemButtonFace")

def set_mode(selected_mode):
    """Set the game mode to either 'computer' or 'person'."""
    global mode
    mode = selected_mode
    reset_game()

def set_difficulty(selected_difficulty):
    """Set the difficulty level of the computer."""
    global difficulty
    difficulty = selected_difficulty
    reset_game()

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Variables
current_player = "X"
buttons = []
mode = "person"  # Default mode is 2-player
difficulty = "Easy"  # Default difficulty
winning_combinations = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
    (0, 4, 8), (2, 4, 6)              # Diagonals
]

# Create a 3x3 grid of buttons
for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 24), width=5, height=2, 
                       command=lambda idx=i: button_click(idx))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Game mode buttons
mode_frame = tk.Frame(root)
mode_frame.grid(row=3, column=0, columnspan=3, pady=10)

person_button = tk.Button(mode_frame, text="2-Player Mode", font=("Arial", 14), 
                          command=lambda: set_mode("person"))
person_button.grid(row=0, column=0, padx=5)

computer_button = tk.Button(mode_frame, text="Play with Computer", font=("Arial", 14), 
                             command=lambda: set_mode("computer"))
computer_button.grid(row=0, column=1, padx=5)

# Difficulty selection buttons
difficulty_frame = tk.Frame(root)
difficulty_frame.grid(row=4, column=0, columnspan=3, pady=10)

easy_button = tk.Button(difficulty_frame, text="Easy", font=("Arial", 14), 
                        command=lambda: set_difficulty("Easy"))
easy_button.grid(row=0, column=0, padx=5)

medium_button = tk.Button(difficulty_frame, text="Medium", font=("Arial", 14), 
                          command=lambda: set_difficulty("Medium"))
medium_button.grid(row=0, column=1, padx=5)

hard_button = tk.Button(difficulty_frame, text="Hard", font=("Arial", 14), 
                        command=lambda: set_difficulty("Hard"))
hard_button.grid(row=0, column=2, padx=5)

# Reset button
reset_button = tk.Button(root, text="Reset Game", font=("Arial", 14), command=reset_game)
reset_button.grid(row=5, column=0, columnspan=3, pady=10)

# Run the application
root.mainloop()
