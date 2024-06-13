import os
from tkinter import messagebox, filedialog

def save_to_file(code, default_filename="generated_code.py"):
    """Saves the provided code to a file with user-chosen name and location."""
    try:
        # Ask the user to choose a directory and filename
        filename = filedialog.asksaveasfilename(
            defaultextension=".py",
            filetypes=[("Python Files", "*.py"), ("All Files", "*.*")]
        )

        if filename:  # If the user selects a file
            with open(filename, 'w') as file:
                file.write(code)
            messagebox.showinfo("Success", f"Code saved to:\n{filename}")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving code to file:\n{e}")