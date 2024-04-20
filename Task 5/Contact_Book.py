import tkinter as tk
from tkinter import ttk, messagebox

# Initialize contact list
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
        messagebox.showinfo("Success", "Contact added successfully.")
        clear_fields()
        update_contact_list()
    else:
        messagebox.showwarning("Warning", "Name and Phone number are required.")

# Function to clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Function to update the contact list display
def update_contact_list():
    contact_tree.delete(*contact_tree.get_children())
    for contact in contacts:
        contact_tree.insert("", "end", values=(contact["Name"], contact["Phone"]))

# Function to search for a contact
def search_contact():
    search_term = search_entry.get().lower()
    found_contacts = [contact for contact in contacts if search_term in contact['Name'].lower() or search_term in contact['Phone']]
    
    contact_tree.delete(*contact_tree.get_children())
    for contact in found_contacts:
        contact_tree.insert("", "end", values=(contact["Name"], contact["Phone"]))

# Function to display full contact details
def display_contact(event):
    selected_item = contact_tree.selection()
    if selected_item:
        selected_contact = contacts[int(selected_item[0][1])]
        messagebox.showinfo("Contact Details", f"Name: {selected_contact['Name']}\nPhone: {selected_contact['Phone']}\nEmail: {selected_contact['Email']}\nAddress: {selected_contact['Address']}")

# Function to delete a contact
def delete_contact():
    selected_item = contact_tree.selection()
    if selected_item:
        del contacts[int(selected_item[0][1])]
        update_contact_list()
        messagebox.showinfo("Success", "Contact deleted successfully.")
    else:
        messagebox.showwarning("Warning", "Please select a contact to delete.")

# Create the main GUI window
root = tk.Tk()
root.title("Contact Book")
root.geometry("800x500")

# Create input fields for contact details
input_frame = tk.Frame(root)
input_frame.pack(pady=20)

name_label = tk.Label(input_frame, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(input_frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)

phone_label = tk.Label(input_frame, text="Phone:")
phone_label.grid(row=1, column=0, padx=10, pady=5)
phone_entry = tk.Entry(input_frame)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

email_label = tk.Label(input_frame, text="Email:")
email_label.grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(input_frame)
email_entry.grid(row=2, column=1, padx=10, pady=5)

address_label = tk.Label(input_frame, text="Address:")
address_label.grid(row=3, column=0, padx=10, pady=5)
address_entry = tk.Entry(input_frame)
address_entry.grid(row=3, column=1, padx=10, pady=5)

# Create buttons for adding, searching, deleting contacts
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Contact", command=add_contact)
add_button.pack(side=tk.LEFT, padx=10)

search_label = tk.Label(button_frame, text="Search:")
search_label.pack(side=tk.LEFT, padx=10)
search_entry = tk.Entry(button_frame)
search_entry.pack(side=tk.LEFT, padx=5)

search_button = tk.Button(button_frame, text="Search", command=search_contact)
search_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Delete Contact", command=delete_contact)
delete_button.pack(side=tk.LEFT, padx=5)

# Create a treeview to display contacts
contact_tree = ttk.Treeview(root, columns=("Name", "Phone"), show="headings")
contact_tree.heading("Name", text="Name")
contact_tree.heading("Phone", text="Phone")
contact_tree.pack(padx=20, pady=10)

contact_tree.bind("<Double-1>", display_contact)

# Start the GUI main loop
root.mainloop()
