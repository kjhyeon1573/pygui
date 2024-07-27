import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First Window")

# Set window size
root.geometry("400x300")

# Add a label
label = tk.Label(root, text="Hello, World!")
label.pack(pady=20)

# Add a button to close the window
button = tk.Button(root, text="Close", command=root.quit)
button.pack(pady=20)

# Run the application
root.mainloop()