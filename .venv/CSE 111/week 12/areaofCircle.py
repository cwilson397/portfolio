#################################################
# Colby Wilson
# 3/24/2025
# Calculate the Area of a circle with a GUI
#################################################


import tkinter as tk
from tkinter import messagebox
import math

class CircleAreaCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Circle Area Calculator")
        
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self.root, text="Enter Radius:").grid(row=0, column=0, padx=10, pady=5)
        
        self.radius_var = tk.StringVar()
        self.radius_entry = tk.Entry(self.root, textvariable=self.radius_var)
        self.radius_entry.grid(row=0, column=1, padx=10, pady=5)
        self.radius_entry.bind("<KeyRelease>", self.calculate_area)
        
        tk.Label(self.root, text="Area:").grid(row=1, column=0, padx=10, pady=5)
        
        self.area_var = tk.StringVar()
        self.area_label = tk.Label(self.root, textvariable=self.area_var, width=20)
        self.area_label.grid(row=1, column=1, padx=10, pady=5)
        
        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_inputs)
        self.clear_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.status_var = tk.StringVar()
        self.status_label = tk.Label(self.root, textvariable=self.status_var, fg="red")
        self.status_label.grid(row=3, column=0, columnspan=2, pady=5)
        
    def calculate_area(self, event=None):
        radius = self.radius_var.get()
        try:
            r = float(radius)
            if r < 0:
                raise ValueError("Radius cannot be negative.")
            area = math.pi * r ** 2
            self.area_var.set(f"{area:.2f}")
            self.status_var.set("")  # Clear status bar on valid input
        except ValueError:
            self.area_var.set("")
            self.status_var.set("Please enter a valid positive number.")
        
    def clear_inputs(self):
        self.radius_var.set("")
        self.area_var.set("")
        self.status_var.set("")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = CircleAreaCalculator(root)
    root.mainloop()
