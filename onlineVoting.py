import tkinter as tk
from tkinter import messagebox
import smtplib
from email.message import EmailMessage


def send_confirmation(receiver_email):
    sender_email = "onlineVoter@gmail.com"
    sender_password = "YOUR_APP_PASSWORD"  # use Gmail App Password

    msg = EmailMessage()
    msg.set_content(
        "Thank you for registering as a voter.\n"
        "You have successfully registered."
    )
    msg["Subject"] = "Voter Registration Confirmation"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
    except Exception as e:
        messagebox.showerror("Email Error", str(e))
        return

    messagebox.showinfo("Success", "Confirmation email sent!")


def register():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    district = district_entry.get()
    nrc = nrc_entry.get()

    # VALIDATION
    if not name or not age or not email or not district or not nrc:
        messagebox.showerror("Error", "All fields are required.")
        return

    if not age.isdigit() or int(age) < 18:
        messagebox.showerror("Error", "You must be at least 18 years old.")
        return

    if "@" not in email or "." not in email:
        messagebox.showerror("Error", "Invalid email address.")
        return

    if len(nrc) != 8:
        messagebox.showerror("Error", "NRC must be exactly 8 characters.")
        return

    messagebox.showinfo(
        "Registered",
        f"{name}, you have successfully registered as a voter!"
    )

    send_confirmation(email)

    # CLEAR FIELDS
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    district_entry.delete(0, tk.END)
    nrc_entry.delete(0, tk.END)


# WINDOW
root = tk.Tk()
root.title("Voter Registration System")
root.geometry("400x350")
root.resizable(False, False)

# LABELS & ENTRIES
tk.Label(root, text="Voter Registration", font=("Arial", 16, "bold")).pack(pady=10)

form = tk.Frame(root)
form.pack(pady=10)

tk.Label(form, text="Name").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(form, width=30)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(form, text="Age").grid(row=1, column=0, sticky="w")
age_entry = tk.Entry(form, width=30)
age_entry.grid(row=1, column=1, pady=5)

tk.Label(form, text="Email").grid(row=2, column=0, sticky="w")
email_entry = tk.Entry(form, width=30)
email_entry.grid(row=2, column=1, pady=5)

tk.Label(form, text="District").grid(row=3, column=0, sticky="w")
district_entry = tk.Entry(form, width=30)
district_entry.grid(row=3, column=1, pady=5)

tk.Label(form, text="NRC Number").grid(row=4, column=0, sticky="w")
nrc_entry = tk.Entry(form, width=30)
nrc_entry.grid(row=4, column=1, pady=5)

# BUTTON
tk.Button(
    root,
    text="Register",
    command=register,
    bg="green",
    fg="white",
    width=20
).pack(pady=20)

root.mainloop()
