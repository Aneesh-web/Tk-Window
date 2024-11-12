import tkinter as tk
from time import strftime
import random

# Initialize the main window
root = tk.Tk()
root.title("Digital Clock")

# Configure the label to display the time
clock_label = tk.Label(root, font=("Helvetica", 48), background="black", foreground="cyan")
clock_label.pack(anchor="center")

def update_time():
    # Get current time in HH:MM:SS format
    current_time = strftime("%H:%M:%S")
    # Update the label with current time
    clock_label.config(text=current_time)
    
    # Generate random colors for text and background
    random_text_color = random.choice(["cyan", "yellow", "green", "red", "purple", "orange", "white"])
    random_bg_color = random.choice(["black", "navy", "darkgreen", "brown", "darkgray", "purple", "teal"])
    
    # Apply random colors to the label
    clock_label.config(foreground=random_text_color, background=random_bg_color)
    
    # Call update_time again after 1000ms (1 second)
    clock_label.after(1000, update_time)

# Start the clock update function
update_time()

# Run the application
root.mainloop()
