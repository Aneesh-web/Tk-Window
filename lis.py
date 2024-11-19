import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task.strip():
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty.")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Main Tkinter window
root = tk.Tk()
root.title("To-Do List")

# Input frame
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack()

tk.Label(input_frame, text="Task:").grid(row=0, column=0, padx=5)
task_entry = tk.Entry(input_frame, width=30)
task_entry.grid(row=0, column=1, padx=5)

add_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=2, padx=5)

# Task listbox
task_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
task_listbox.pack(padx=10, pady=10)

# Delete button
delete_button = tk.Button(root, text="Delete Selected Task", command=delete_task)
delete_button.pack(pady=5)

# Run the application
root.mainloop()
