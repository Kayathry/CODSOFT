# import required libraries
import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
import random
import string


# Define the password generator function
def password_generator(length, use_uppercase, use_digits, use_special_letter):
    Characters: str = string.ascii_lowercase

    if use_uppercase:
        Characters += string.ascii_uppercase
    if use_digits:
        Characters += string.digits
    if use_special_letter:
        Characters += string.punctuation
    password = ''.join(random.choice(Characters) for i in range(length))
    return password


# create gui application
class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator App")
        self.root.config(bg='sky blue')


        label_font = tkfont.Font(family="Helvetica", size=12)
        entry_font = tkfont.Font(family="Helvetica", size=12)

        # password Length
        self.length_label = tk.Label(root, text="Password Length:", font=label_font, bg='skyblue')
        self.length_label.pack(padx=10, pady=5, )
        self.length_entry = tk.Entry(root, font=entry_font, width=10)
        self.length_entry.pack(padx=10, pady=5)

        # uppercase letter option
        self.uppercase_letter = tk.BooleanVar()
        self.uppercase_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.uppercase_letter, font=label_font, bg='skyblue')
        self.uppercase_check.pack(padx=10, pady=10)

        # digits option
        self.digits = tk.BooleanVar()
        self.digits_check = tk.Checkbutton(root, text="Include Digits", variable=self.digits, font=label_font, bg='skyblue')
        self.digits_check.pack(padx=10, pady=10)

        # Special characters option
        self.special_character = tk.BooleanVar()
        self.special_check = tk.Checkbutton(root, text="Include Special Characters", variable=self.special_character, font=label_font, bg='skyblue')
        self.special_check.pack(padx=10, pady=10)

        # Generate button with green color
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, bg='green', fg='white', font=label_font)
        self.generate_button.pack(padx=10, pady=10)

        # Display generated password
        self.password_label = tk.Label(root, text="Generated Password:", font=label_font, bg='skyblue')
        self.password_label.pack()
        self.password_entry = tk.Entry(root, state='readonly', font=entry_font)
        self.password_entry.pack(padx=10, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be a positive integer")
        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))
            return

        use_uppercase = self.uppercase_letter.get()
        use_digits = self.digits.get()
        use_special = self.special_character.get()

        password = password_generator(length, use_uppercase, use_digits, use_special)
        self.password_entry.config(state='normal')
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        self.password_entry.config(state='readonly')


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('487x450')
    app = PasswordGeneratorApp(root)
    root.mainloop()
