import tkinter as tk
import re

# -----------------------------
# Estimate Crack Time
# -----------------------------
def estimate_crack_time(password):

    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26

    if re.search(r"[A-Z]", password):
        charset += 26

    if re.search(r"\d", password):
        charset += 10

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 32

    length = len(password)

    if charset == 0 or length == 0:
        return "Instantly"

    combinations = charset ** length

    guesses_per_second = 1_000_000_000

    seconds = combinations / guesses_per_second

    return convert_time(seconds)


# -----------------------------
# Convert Time
# -----------------------------
def convert_time(seconds):

    minute = 60
    hour = 3600
    day = 86400
    year = 31536000

    if seconds < 1:
        return "Less than 1 second"

    elif seconds < minute:
        return f"{int(seconds)} seconds"

    elif seconds < hour:
        return f"{int(seconds / minute)} minutes"

    elif seconds < day:
        return f"{int(seconds / hour)} hours"

    elif seconds < year:
        return f"{int(seconds / day)} days"

    elif seconds < year * 1000:
        return f"{int(seconds / year)} years"

    else:
        return "Thousands of years"


# -----------------------------
# Password Checker
# -----------------------------
def check_strength(event=None):

    password = entry.get()

    score = 0
    feedback = []

    # Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letter")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letter")

    # Number
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add a number")

    # Special Character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special character")

    # Strength Levels
    if score <= 2:
        strength = "Weak"
        color = "#ff4d4d"
        width = 80

    elif score <= 4:
        strength = "Medium"
        color = "#ffaa00"
        width = 180

    else:
        strength = "Strong"
        color = "#00cc66"
        width = 300

    # Update Strength Label
    strength_label.config(
        text=f"Password Strength: {strength}",
        fg=color
    )

    # Update Bar
    canvas.delete("bar")

    canvas.create_rectangle(
        0,
        0,
        width,
        20,
        fill=color,
        outline="",
        tags="bar"
    )

    # Suggestions
    if feedback:
        tips_label.config(
            text="Suggestions:\n" + "\n".join(feedback)
        )

    else:
        tips_label.config(
            text="Excellent Password ✅"
        )

    # Crack Time
    crack_time = estimate_crack_time(password)

    crack_label.config(
        text=f"Estimated Crack Time: {crack_time}"
    )


# -----------------------------
# Toggle Password Visibility
# -----------------------------
def toggle_password():

    if entry.cget("show") == "*":
        entry.config(show="")
        toggle_btn.config(text="Hide")

    else:
        entry.config(show="*")
        toggle_btn.config(text="Show")


# -----------------------------
# GUI Window
# -----------------------------
root = tk.Tk()

root.title("Password Tester")

root.geometry("500x420")

root.config(bg="#121212")

# -----------------------------
# Title
# -----------------------------
title = tk.Label(
    root,
    text="Password Strength Tester",
    font=("Arial", 20, "bold"),
    bg="#121212",
    fg="white"
)

title.pack(pady=20)

# -----------------------------
# Password Entry Frame
# -----------------------------
frame = tk.Frame(root, bg="#121212")
frame.pack(pady=10)

# Entry
entry = tk.Entry(
    frame,
    width=28,
    font=("Arial", 14),
    bg="#1e1e1e",
    fg="white",
    insertbackground="white",
    relief="flat",
    show="*"
)

entry.pack(side="left", padx=10, ipady=8)

# Real-time Detection
entry.bind("<KeyRelease>", check_strength)

# Show/Hide Button
toggle_btn = tk.Button(
    frame,
    text="Show",
    command=toggle_password,
    bg="#333333",
    fg="white",
    activebackground="#444444",
    activeforeground="white",
    relief="flat"
)

toggle_btn.pack(side="left")

# -----------------------------
# Strength Label
# -----------------------------
strength_label = tk.Label(
    root,
    text="Type a password...",
    font=("Arial", 12, "bold"),
    bg="#121212",
    fg="white"
)

strength_label.pack(pady=15)

# -----------------------------
# Progress Bar
# -----------------------------
canvas = tk.Canvas(
    root,
    width=300,
    height=20,
    bg="#2a2a2a",
    highlightthickness=0
)

canvas.pack(pady=5)

# -----------------------------
# Crack Time Label
# -----------------------------
crack_label = tk.Label(
    root,
    text="Estimated Crack Time:",
    font=("Arial", 11, "bold"),
    bg="#121212",
    fg="#cccccc"
)

crack_label.pack(pady=20)

# -----------------------------
# Suggestions Label
# -----------------------------
tips_label = tk.Label(
    root,
    text="",
    font=("Arial", 10),
    bg="#121212",
    fg="#bbbbbb",
    justify="left"
)

tips_label.pack(pady=10)

# -----------------------------
# Run App
# -----------------------------
root.mainloop()