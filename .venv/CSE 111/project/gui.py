############################
# Colby Wilson
# 3/24/2025
# Password program (GUI)
###########################

import tkinter as tk
from tkinter import messagebox
from password_generation import generate_strong_password  # Import from your generation file
from password_validation import check_password_strength  # Import from your validation file
from breach_check import is_breached  # Import from your breach check file

# startup process
def on_start():
    """ Application is starting message"""
    print("Starting the Password application...")

# Function to handle password
#  generation and validation from the GUI
def generate_password():
    """
    Generates a password based on the selected length from the GUI, displays it, 
    checks its strength, and checks if it has been breached.
    """
    try:
        # Get the selected length from the slider
        length = password_length_slider.get()       
        # Generate the password using the external function
        password = generate_strong_password(length)

        # Display the password in the entry box
        password_display.delete(0, tk.END)
        password_display.insert(0, password)

        # Check the password strength using the external function
        strength_message = check_password_strength(password)
        strength_label.config(text=f"Password Strength: {strength_message}")        
        # Check if the password has been breached using the external function
        if is_breached(password):
            breach_label.config(text="Warning: This password has been breached!")
        else:
            breach_label.config(text="Password is safe.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def test_entered_password():
    """
    Tests the manually entered password for strength and breach status.
    """
    try:
        # Get the password entered by the user
        password = entered_password.get()

        # Check the password strength
        strength_message = check_password_strength(password)
        strength_label.config(text=f"Password Strength: {strength_message}")

        # Check if the password has been breached
        if is_breached(password):
            breach_label.config(text="Warning: This password has been breached!")
        else:
            breach_label.config(text="Password is safe.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def on_closing():
    """
    Handles the closing of the GUI, printing a message to the console.
    """
    print("Closing the Password application...")
    root.destroy()  # Closes the Tkinter window

on_start()

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Add the handler for the close event
root.protocol("WM_DELETE_WINDOW", on_closing)

# Label for the password length
length_label = tk.Label(root, text="Select Password Length (8-20):")
length_label.pack(pady=10)

# Slider for password length (8 to 20 characters)
password_length_slider = tk.Scale(root, from_=8, to_=20, orient=tk.HORIZONTAL)
password_length_slider.set(16)  # Set default length to 16
password_length_slider.pack(pady=10)

# Button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Entry field to display the generated password
password_display = tk.Entry(root, width=30)
password_display.pack(pady=10)

# Label for password strength
strength_label = tk.Label(root, text="Password Strength: ")
strength_label.pack(pady=10)

# Label for breach warning
breach_label = tk.Label(root, text="Password is safe.")
breach_label.pack(pady=10)

# Entry field for manually entered password to test
entered_password_label = tk.Label(root, text="Enter Password to Test:")
entered_password_label.pack(pady=10)

entered_password = tk.Entry(root, width=30)
entered_password.pack(pady=10)

# Button to test the entered password
test_password_button = tk.Button(root, text="Test Password", command=test_entered_password)
test_password_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
