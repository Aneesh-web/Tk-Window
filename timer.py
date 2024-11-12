import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Countdown Timer")

# Variables to keep track of time and counter state
counter = 0
running = False

# Label to display the time
counter_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48), background="black", foreground="cyan")
counter_label.pack(anchor="center")

# Entry fields to set initial time
hours_entry = tk.Entry(root, width=3, font=("Helvetica", 18))
hours_entry.insert(0, "00")
hours_entry.pack(side="left")
tk.Label(root, text=":", font=("Helvetica", 18)).pack(side="left")

minutes_entry = tk.Entry(root, width=3, font=("Helvetica", 18))
minutes_entry.insert(0, "00")
minutes_entry.pack(side="left")
tk.Label(root, text=":", font=("Helvetica", 18)).pack(side="left")

seconds_entry = tk.Entry(root, width=3, font=("Helvetica", 18))
seconds_entry.insert(0, "00")
seconds_entry.pack(side="left")

def update_counter():
    global counter, running
    if running and counter > 0:
        # Calculate hours, minutes, and seconds from counter
        hours, remainder = divmod(counter, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
        
        # Update the label with the current counter value
        counter_label.config(text=time_str)
        
        # Decrement the counter
        counter -= 1
        
        # Schedule the function to run again after 1 second
        root.after(1000, update_counter)
    elif counter == 0:
        # Stop the timer when it reaches zero
        running = False
        counter_label.config(text="Time's up!")

def start():
    global running, counter
    if not running:  # Start only if not already running
        # Get the initial time from entry fields
        hours = int(hours_entry.get())
        minutes = int(minutes_entry.get())
        seconds = int(seconds_entry.get())
        
        # Convert the initial time to total seconds
        counter = hours * 3600 + minutes * 60 + seconds
        
        if counter > 0:  # Only start if there's time to count down
            running = True
            update_counter()

def stop():
    global running
    running = False  # Stop the counter

def reset():
    global counter, running
    running = False  # Stop the counter
    counter = 0  # Reset the counter to zero
    counter_label.config(text="00:00:00")  # Reset label display

# Buttons to control the counter
start_button = tk.Button(root, text="Start", command=start, font=("Helvetica", 12), width=10)
start_button.pack(side="left")

stop_button = tk.Button(root, text="Stop", command=stop, font=("Helvetica", 12), width=10)
stop_button.pack(side="left")

reset_button = tk.Button(root, text="Reset", command=reset, font=("Helvetica", 12), width=10)
reset_button.pack(side="left")

# Run the application
root.mainloop()
