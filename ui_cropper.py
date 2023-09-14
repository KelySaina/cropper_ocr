import tkinter as tk
from tkinter import filedialog
from cropper import Cropper
import os


def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.png")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)


def submit():
    selected_file = file_entry.get()
    if selected_file and os.path.isfile(selected_file):
        c = Cropper()
        c.start(selected_file)
        error_label.config(text="Cropped successfully", fg="green")
    else:
        error_label.config(text="Please select a valid file.", fg="red")


# Create the main window
root = tk.Tk()
root.title("File Input Example")

# Set the width and height of the window
window_width = 450
window_height = 100
root.geometry(f"{window_width}x{window_height}")
root.resizable(False, False)

# Create a label for displaying errors
error_label = tk.Label(root, text="", fg="red")
error_label.pack()

# Create a frame to hold the file input components
file_frame = tk.Frame(root)
file_frame.pack()

# Create a label and entry for file input
file_label = tk.Label(file_frame, text="Select a file:")
file_label.grid(row=0, column=0)

file_entry = tk.Entry(file_frame, width=30)
file_entry.grid(row=0, column=1)

# Create a button to open file dialog
browse_button = tk.Button(file_frame, text="Browse", command=open_file)
browse_button.grid(row=0, column=2)

# Create a button to submit
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.place(relx=0.5, rely=0.65, anchor=tk.CENTER)


# Start the main event loop
root.mainloop()
