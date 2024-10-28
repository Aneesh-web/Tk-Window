import tkinter as tk
from random import randint

# Initialize the main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("300x200")

# Generate a random number between 1 and 100
random_number = randint(1, 100)

# Function to check the user's guess
def check_guess():
    try:
        guess = int(entry.get())
        if guess < random_number:
            result_label.config(text="Too low! Try again.", fg="blue")
        elif guess > random_number:
            result_label.config(text="Too high! Try again.", fg="red")
        else:
            result_label.config(text="Correct! You guessed it!", fg="green")
            guess_button.config(state="disabled")  # Disable button after correct guess
        entry.delete(0, tk.END)  # Clear entry after each attempt
    except ValueError:
        result_label.config(text="Please enter a valid number.", fg="orange")
        entry.delete(0, tk.END)  # Clear entry if invalid input is given

# Function to reset the game
def reset_game():
    global random_number
    random_number = randint(1, 100)
    entry.delete(0, tk.END)
    result_label.config(text="")
    guess_button.config(state="normal")

# Label and Entry for the user's guess
prompt_label = tk.Label(root, text="Guess a number between 1 and 100:")
prompt_label.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

# Button to submit guess
guess_button = tk.Button(root, text="Guess", command=check_guess)
guess_button.pack(pady=5)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Button to reset the game
reset_button = tk.Button(root, text="Play Again", command=reset_game)
reset_button.pack(pady=5)

# Run the application
root.mainloop()
