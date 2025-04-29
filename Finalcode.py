import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import json
import os
from datetime import datetime

# File to save medication data
DATA_FILE = "medications.json"

# List to store medications
medications = []

# Function to load medication data from file
def load_medications():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Function to save medication data to file
def save_medications():
    with open(DATA_FILE, "w") as file:
        json.dump(medications, file)

# Function to show medication reminder
def remind_medication():
    if medications:
        med_list = "\n".join(
            [f"{med['name']} - {med['dosage']} at {med['time']}" for med in medications]
        )
        messagebox.showinfo("Medication Reminder", f"Time to take your meds:\n\n{med_list}")
    else:
        messagebox.showinfo("Medication Reminder", "No medications added yet!")

# Function to show hydration reminder
def remind_hydration():
    messagebox.showinfo("Hydration Reminder", "Don't forget to drink a glass of water!")

# Function to show a simple exercise
def suggest_exercise():
    exercises = [
        "Stand up and stretch your arms overhead.",
        "Rotate your ankles while seated.",
        "March in place for 1 minute.",
        "Gently roll your shoulders back and forth.",
        "Take 10 deep breaths."
    ]
    exercise = random.choice(exercises)
    messagebox.showinfo("Exercise Time!", exercise)

# Function to add a medication
def add_medication():
    name = simpledialog.askstring("Medication Name", "Enter medication name:")
    if name:
        dosage = simpledialog.askstring("Dosage", f"Enter dosage for {name}:")
        time = simpledialog.askstring("Reminder Time", f"When should you take {name}? (24hr e.g. 14:30)")
        if dosage and time:
            medications.append({"name": name, "dosage": dosage, "time": time})
            update_med_list()
        else:
            messagebox.showwarning("Incomplete Info", "Please provide both dosage and time.")
    else:
        messagebox.showwarning("No Name", "Medication name is required.")

# Function to edit a medication
def edit_medication():
    selected = med_display.curselection()
    if selected:
        index = selected[0]
        med = medications[index]
        new_name = simpledialog.askstring("Edit Medication", "Edit name:", initialvalue=med['name'])
        new_dosage = simpledialog.askstring("Edit Dosage", "Edit dosage:", initialvalue=med['dosage'])
        new_time = simpledialog.askstring("Edit Time", "Edit time (24hr e.g. 14:30):", initialvalue=med['time'])
        if new_name and new_dosage and new_time:
            medications[index] = {"name": new_name, "dosage": new_dosage, "time": new_time}
            update_med_list()
        else:
            messagebox.showwarning("Incomplete Info", "All fields are required.")
    else:
        messagebox.showwarning("No Selection", "Select a medication to edit.")

# Function to delete a medication
def delete_medication():
    selected = med_display.curselection()
    if selected:
        index = selected[0]
        del medications[index]
        update_med_list()
    else:
        messagebox.showwarning("No Selection", "Select a medication to delete.")

# Function to update the medication list display
def update_med_list():
    med_display.delete(0, tk.END)
    for med in medications:
        med_display.insert(tk.END, f"{med['name']} - {med['dosage']} at {med['time']}")

# Function to check if it's time for a medication
def check_medication_times():
    now = datetime.now().strftime("%H:%M")
    for med in medications:
        if med['time'] == now:
            messagebox.showinfo("Medication Time!", f"It's time to take {med['name']} ({med['dosage']})")
    root.after(60000, check_medication_times)  # Check every 60 seconds

# Main window setup
root = tk.Tk()
root.title("Senior Signal - Health Reminder")
root.geometry("380x550")
root.config(bg="#e6f2ff")

# Title label
title_label = tk.Label(root, text="Senior Signal", font=("Helvetica", 20, "bold"), bg="#e6f2ff")
title_label.pack(pady=10)

# Buttons
tk.Button(root, text="Medication Reminder", font=("Helvetica", 14), bg="#cce5ff", command=remind_medication).pack(pady=5, ipadx=10, ipady=5)
tk.Button(root, text="Hydration Reminder", font=("Helvetica", 14), bg="#cce5ff", command=remind_hydration).pack(pady=5, ipadx=10, ipady=5)
tk.Button(root, text="Exercise Suggestion", font=("Helvetica", 14), bg="#cce5ff", command=suggest_exercise).pack(pady=5, ipadx=10, ipady=5)
tk.Button(root, text="Add Medication", font=("Helvetica", 14), bg="#b3e6cc", command=add_medication).pack(pady=5, ipadx=10, ipady=5)

# Listbox label
tk.Label(root, text="Your Medications:", font=("Helvetica", 14, "bold"), bg="#e6f2ff").pack(pady=5)

# Listbox to display medications
med_display = tk.Listbox(root, font=("Helvetica", 12), width=40)
med_display.pack(pady=5)

# Edit and Delete buttons
tk.Button(root, text="Edit Selected", font=("Helvetica", 12), bg="#ffe680", command=edit_medication).pack(pady=3, ipadx=10, ipady=3)
tk.Button(root, text="Delete Selected", font=("Helvetica", 12), bg="#ff9999", command=delete_medication).pack(pady=3, ipadx=10, ipady=3)

# Exit button
tk.Button(root, text="Exit App", font=("Helvetica", 14), bg="#ffcccc", command=lambda: (save_medications(), root.quit())).pack(pady=20, ipadx=10, ipady=5)

# Load medications from file
medications = load_medications()
update_med_list()

# Start the medication time check loop
check_medication_times()

# Run the GUI loop
root.mainloop()
