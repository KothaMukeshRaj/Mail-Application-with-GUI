import tkinter as tk
from tkinter import messagebox

def send_mail():
    # Add your logic to send the mail here
    messagebox.showinfo("Success", "Mail sent successfully!")

# Create the main application window
window = tk.Tk()
window.title("Mail Application")
window.configure(bg="#333333")  # Set background color

# Define colors
text_color = "#FFFFFF"  # White text color
bg_color = "#222222"    # Dark gray background color
button_color = "#4CAF50"  # Green button color

# Create the GUI elements with custom colors
label_to = tk.Label(window, text="To:", bg=bg_color, fg=text_color)
label_to.pack()
entry_to = tk.Entry(window, bg=bg_color, fg=text_color)
entry_to.pack()

label_subject = tk.Label(window, text="Subject:", bg=bg_color, fg=text_color)
label_subject.pack()
entry_subject = tk.Entry(window, bg=bg_color, fg=text_color)
entry_subject.pack()

label_body = tk.Label(window, text="Body:", bg=bg_color, fg=text_color)
label_body.pack()
entry_body = tk.Text(window, bg=bg_color, fg=text_color)
entry_body.pack()

send_button = tk.Button(window, text="Send", command=send_mail, bg=button_color, fg=text_color)
send_button.pack()

# Start the GUI event loop
window.mainloop()
