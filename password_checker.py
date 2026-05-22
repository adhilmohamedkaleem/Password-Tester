import tkinter as tk
import re

# -----------------------------
# Crack Time Function
# -----------------------------
def crack_time(password):

    chars = 0

    if re.search(r"[a-z]", password):
        chars += 26

    if re.search(r"[A-Z]", password):
        chars += 26

    if re.search(r"\d", password):
        chars += 10

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        chars += 32

    if chars == 0:
        return "0 sec"

    combinations = chars ** len(password)

    seconds = combinations / 1_000_000_000

    if seconds < 60:
        return f"{int(seconds)} sec"

    elif seconds < 3600:
        return f"{int(seconds / 60)} min"

    elif seconds < 86400:
        return f"{int(seconds / 3600)} hrs"

    elif seconds < 31536000:
        return f"{int(seconds / 86400)} days"

    else:
        return f"{int(seconds / 31536000)} years"


# -----------------------------
# Password Checker
# -----------------------------
def check(event=None):

    password = entry.get()

    score = 0
    length = len(password)

    has_upper = re.search(r"[A-Z]", password)
    has_lower = re.search(r"[a-z]", password)
    has_number = re.search(r"\d", password)
    has_symbol = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    # Length
    if length >= 6:
        score += 1
        length_check.config(text="☑ Minimum 6 Characters", fg="green")
    else:
        length_check.config(text="☐ Minimum 6 Characters", fg="red")

    # Uppercase
    if has_upper:
        score += 1
        upper_check.config(text="☑ Uppercase Letter", fg="green")
    else:
        upper_check.config(text="☐ Uppercase Letter", fg="red")

    # Lowercase
    if has_lower:
        score += 1
        lower_check.config(text="☑ Lowercase Letter", fg="green")
    else:
        lower_check.config(text="☐ Lowercase Letter", fg="red")

    # Number
    if has_number:
        score += 1
        number_check.config(text="☑ Number", fg="green")
    else:
        number_check.config(text="☐ Number", fg="red")

    # Symbol
    if has_symbol:
        score += 1
        symbol_check.config(text="☑ Special Symbol", fg="green")
    else:
        symbol_check.config(text="☐ Special Symbol", fg="red")

    # Strength
    if score <= 2:
        text = "Weak"
        color = "red"
        width = 80

    elif score <= 4:
        text = "Medium"
        color = "orange"
        width = 180

    else:
        text = "Strong"
        color = "green"
        width = 300

    strength.config(
        text=f"Strength: {text}",
        fg=color
    )

    # Progress Bar
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

    # Crack Time
    crack.config(
        text=f"Crack Time: {crack_time(password)}"
    )


# -----------------------------
# Show / Hide Password
# -----------------------------
def toggle():

    if entry.cget("show") == "*":
        entry.config(show="")
        btn.config(text="Hide")

    else:
        entry.config(show="*")
        btn.config(text="Show")


# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()

root.title("Password Strength Tester")

root.geometry("500x500")

root.config(bg="#121212")


# -----------------------------
# Title
# -----------------------------
title = tk.Label(
    root,
    text="Password Strength Tester",
    font=("Arial", 18, "bold"),
    bg="#121212",
    fg="white"
)

title.pack(pady=20)


# -----------------------------
# Entry Frame
# -----------------------------
frame = tk.Frame(root, bg="#121212")

frame.pack()


# -----------------------------
# Password Entry
# -----------------------------
entry = tk.Entry(
    frame,
    width=25,
    font=("Arial", 14),
    bg="#1e1e1e",
    fg="white",
    insertbackground="white",
    show="*"
)

entry.pack(side="left", padx=10, ipady=6)

entry.bind("<KeyRelease>", check)


# -----------------------------
# Toggle Button
# -----------------------------
btn = tk.Button(
    frame,
    text="Show",
    command=toggle,
    bg="#333333",
    fg="white",
    relief="flat"
)

btn.pack(side="left")


# -----------------------------
# Strength Label
# -----------------------------
strength = tk.Label(
    root,
    text="Type Password...",
    font=("Arial", 12, "bold"),
    bg="#121212",
    fg="white"
)

strength.pack(pady=20)


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

canvas.pack(pady=10)


# -----------------------------
# Crack Time
# -----------------------------
crack = tk.Label(
    root,
    text="Crack Time:",
    font=("Arial", 11),
    bg="#121212",
    fg="white"
)

crack.pack(pady=15)


# -----------------------------
# Checkboxes
# -----------------------------
length_check = tk.Label(
    root,
    text="☐ Minimum 6 Characters",
    bg="#121212",
    fg="red",
    font=("Arial", 11)
)

length_check.pack(anchor="w", padx=100)

upper_check = tk.Label(
    root,
    text="☐ Uppercase Letter",
    bg="#121212",
    fg="red",
    font=("Arial", 11)
)

upper_check.pack(anchor="w", padx=100)

lower_check = tk.Label(
    root,
    text="☐ Lowercase Letter",
    bg="#121212",
    fg="red",
    font=("Arial", 11)
)

lower_check.pack(anchor="w", padx=100)

number_check = tk.Label(
    root,
    text="☐ Number",
    bg="#121212",
    fg="red",
    font=("Arial", 11)
)

number_check.pack(anchor="w", padx=100)

symbol_check = tk.Label(
    root,
    text="☐ Special Symbol",
    bg="#121212",
    fg="red",
    font=("Arial", 11)
)

symbol_check.pack(anchor="w", padx=100)


# -----------------------------
# Run App
# -----------------------------
root.mainloop()
