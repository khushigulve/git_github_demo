import tkinter as tk
from tkinter import ttk

# Window
root = tk.Tk()
root.title("Beautiful Python UI")
root.geometry("450x350")
root.configure(bg="#2C3E50")
root.resizable(False, False)

# Style
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TButton",
    font=("Arial", 11, "bold"),
    padding=8
)

style.configure(
    "TLabel",
    background="#2C3E50",
    foreground="white",
    font=("Arial", 12)
)

# Title
title = tk.Label(
    root,
    text="Welcome",
    bg="#2C3E50",
    fg="white",
    font=("Arial", 22, "bold")
)
title.pack(pady=20)

# Frame
frame = tk.Frame(root, bg="#34495E", padx=20, pady=20)
frame.pack(pady=10)

# Username
ttk.Label(frame, text="Username").grid(row=0, column=0, sticky="w", pady=5)
username = ttk.Entry(frame, width=30)
username.grid(row=1, column=0, pady=5)

# Password
ttk.Label(frame, text="Password").grid(row=2, column=0, sticky="w", pady=5)
password = ttk.Entry(frame, width=30, show="*")
password.grid(row=3, column=0, pady=5)

# Output
result = tk.Label(root, text="", bg="#2C3E50", fg="lightgreen", font=("Arial", 11))
result.pack(pady=10)

# Button Function
def login():
    name = username.get()
    result.config(text=f"Welcome, {name}!")

ttk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()