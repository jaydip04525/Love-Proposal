import tkinter as tk
import random
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("💖 Love Proposal 💖")
root.geometry("500x300")
root.resizable(False, False)

# Background and label
root.configure(bg="#ffe6f0")
label = tk.Label(root, text="Will you be mine? 💘", font=("Arial", 24, "bold"), bg="#ffe6f0")
label.pack(pady=50)

# Yes button behavior
def yes_clicked():
    messagebox.showinfo("Yay! 💖", "My heart is officially smiling! 😍")
    root.destroy()

# No button behavior (dodges the mouse)
def move_no_button(event):
    # Random new position within the window
    new_x = random.randint(0, 400)
    new_y = random.randint(100, 200)
    no_button.place(x=new_x, y=new_y)

# Buttons
yes_button = tk.Button(root, text="YES", font=("Arial", 16, "bold"), bg="#ff4d6d", fg="white", command=yes_clicked)
yes_button.place(x=100, y=200)

no_button = tk.Button(root, text="NO", font=("Arial", 16, "bold"), bg="#4d79ff", fg="white")
no_button.place(x=300, y=200)

# Bind mouse movement over "No" button to dodge
no_button.bind("<Enter>", move_no_button)

# Run the application
root.mainloop()
