import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Function to calculate age
def calculate_age():
    try:
        year = int(entry_year.get())
        month = int(entry_month.get())
        day = int(entry_day.get())
        today = datetime.today()
        birth_date = datetime(year, month, day)
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        messagebox.showinfo("Age Calculator", f"Hello, {entry_name.get()}!\nYou are {age} years old.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for year, month, and day.")

# Setting up the GUI
root = tk.Tk()
root.title("Age Calculator")

# Labels
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=10)

label_year = tk.Label(root, text="Year of Birth:")
label_year.grid(row=1, column=0, padx=10, pady=10)

label_month = tk.Label(root, text="Month of Birth:")
label_month.grid(row=2, column=0, padx=10, pady=10)

label_day = tk.Label(root, text="Day of Birth:")
label_day.grid(row=3, column=0, padx=10, pady=10)

# Entry widgets
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

entry_year = tk.Entry(root)
entry_year.grid(row=1, column=1, padx=10, pady=10)

entry_month = tk.Entry(root)
entry_month.grid(row=2, column=1, padx=10, pady=10)

entry_day = tk.Entry(root)
entry_day.grid(row=3, column=1, padx=10, pady=10)

# Button to calculate age
button_calculate = tk.Button(root, text="Calculate Age", command=calculate_age)
button_calculate.grid(row=4, column=0, columnspan=2, pady=20)

# Run the GUI
root.mainloop()
