import tkinter as tk
from time import strftime

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
    # Call update_time again after 1000ms (1 second)
    clock_label.after(1000, update_time)

# Start the clock update function
update_time()

# Run the application
root.mainloop()
