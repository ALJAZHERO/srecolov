import csv
import tkinter as tk
from tkinter import messagebox

def load_data_from_csv(filename):
    data_dict = {}
    with open(filename, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            try:
                number, name = row
                data_dict[int(number)] = name
            except ValueError:
                messagebox.showerror("Error", "Error parsing CSV data. Please check the CSV format.")
                return {}
    return data_dict

def lookup_name(event=None):
    try:
        user_input = int(entry.get())
        if 1 <= user_input <= 1000:
            if user_input in data_dict:
                result_label.config(text=f"{data_dict[user_input]}")
            else:
                result_label.config(text="Number not found in the CSV.")
        else:
            result_label.config(text="Please enter a number between 1 and 1000.")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")

def on_exit():
    if messagebox.askokcancel("Exit", "Do you want to exit the program?"):
        root.destroy()

if __name__ == "__main__":
    filename = "dobitki.csv"  # Replace with the actual filename of your CSV
    data_dict = load_data_from_csv(filename)

    if not data_dict:
        exit()

    root = tk.Tk()
    root.title("SREČELOV")
    root.geometry("1000x800")  # Velikost okna

    label = tk.Label(root, text="Vpiši številko (1-1000):", font=("Arial", 16)) 
    label.pack(pady=80)

    entry = tk.Entry(root, width=10, font=("Arial", 16))  # Increase font size
    entry.pack(pady=40)

    lookup_button = tk.Button(root, text="Poišči", font=("Arial", 14), command=lookup_name)
    lookup_button.pack(pady=80)

    result_label = tk.Label(root, text="", font=("Arial", 24))
    result_label.pack(pady=80)

    # Bind the <Return> event to the root window, so it triggers the lookup_name function
    root.bind("<Return>", lookup_name)

    root.protocol("WM_DELETE_WINDOW", on_exit)
    root.mainloop()
