import tkinter as tk
from tkinter import messagebox

# Function to add a new task to the to-do list with priority
def add_task():
    task = task_entry.get()
    priority = priority_var.get()
    
    if task:
        todo_list.insert(tk.END, f"{task} - Priority: {priority}")
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete a selected task from the to-do list
def delete_task():
    try:
        selected_task = todo_list.curselection()[0]
        todo_list.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to clear all tasks from the to-do list
def clear_tasks():
    todo_list.delete(0, tk.END)

# Create the main GUI window
root = tk.Tk()
root.title("To-Do List with Priorities")

# Create a frame for the to-do list
frame = tk.Frame(root)
frame.pack(pady=10)

# Create a scrollbar for the to-do list
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create the to-do list
todo_list = tk.Listbox(frame, width=50, height=15, font=("Arial", 12, "bold"), yscrollcommand=scrollbar.set)
todo_list.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=todo_list.yview)

# Create a frame for task input and buttons
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Create an entry for new tasks
task_entry = tk.Entry(input_frame, width=30, font=("Arial", 12))
task_entry.pack(side=tk.LEFT, padx=5)

# Create a dropdown menu for priorities
priority_var = tk.StringVar(root)
priority_var.set("Urgent")
priority_dropdown = tk.OptionMenu(input_frame, priority_var, "Urgent", "Moderate Priority", "Minimum Priority")
priority_dropdown.pack(side=tk.LEFT, padx=5)

# Create buttons for adding, deleting, and clearing tasks
add_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(input_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(input_frame, text="Clear All", command=clear_tasks)
clear_button.pack(side=tk.LEFT, padx=5)

# Start the GUI main loop
root.mainloop()
