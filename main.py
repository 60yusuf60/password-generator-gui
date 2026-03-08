import tkinter as tk
from tkinter import messagebox
import random
import string

# GUI window
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x200")

# Function to generate password
def generate_password():
    length = entry_length.get()
    if not length.isdigit():
        messagebox.showerror("Error", "Please enter a valid number")
        return
    length = int(length)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    result_var.set(password)

# Labels and input
tk.Label(root, text="Password length:").pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Result display
result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, width=40).pack(pady=5)

# Run GUI
root.mainloop()