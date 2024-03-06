import tkinter as tk
import webbrowser

def check_website():
    url = entry.get()
    scamadviser_url = f"https://www.scamadviser.com/check-website/{url}"
    webbrowser.open(scamadviser_url)

# Create the main window
root = tk.Tk()
root.title("Website Legitimacy Checker")

# Create input field
label = tk.Label(root, text="Enter a website URL:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Create button to check website
check_button = tk.Button(root, text="Check Website", command=check_website)
check_button.pack()

# Run the GUI
root.mainloop()
