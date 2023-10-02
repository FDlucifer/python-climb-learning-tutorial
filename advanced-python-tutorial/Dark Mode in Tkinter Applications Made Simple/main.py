import tkinter as tk

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.is_dark_mode = False

        self.light_mode = {
            "bg": "white",
            "fg": "black",
            "entry_bg": "#eee",
            "entry_fg": "black",
            "btn_bg": "#ddd",
            "btn_fg": "black",
        }

        self.dark_mode = {
            "bg": "#333",
            "fg": "white",
            "entry_bg": "#555",
            "entry_fg": "white",
            "btn_bg": "#444",
            "btn_fg": "white",
        }

        self.label_username = tk.Label(root, text="Username")
        self.label_username.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.entry_username = tk.Entry(root)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.label_password = tk.Label(root, text="Password")
        self.label_password.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.toggle_button = tk.Button(
            root, text="Toggle Dark Mode", command=self.toggle_theme
        )
        self.toggle_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.apply_theme(self.light_mode)

    def apply_theme(self, theme):
        self.root.config(bg=theme["bg"])
        for widget in self.root.winfo_children():
            widget_type = widget.winfo_class()

            if widget_type == "Label":
                widget.config(bg=theme["bg"], fg=theme["fg"])
            elif widget_type == "Entry":
                widget.config(
                    bg=theme["entry_bg"],
                    fg=theme["entry_fg"],
                    insertbackground=theme["fg"],
                )
            elif widget_type == "Button":
                widget.config(bg=theme["btn_bg"], fg=theme["btn_fg"])

    def toggle_theme(self):
        if self.is_dark_mode:
            self.apply_theme(self.light_mode)
        else:
            self.apply_theme(self.dark_mode)

        self.is_dark_mode = not self.is_dark_mode

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "user" and password == "pass":
            CustomMessagebox(self.root, 'Login', 'successfully logged in!', self.dark_mode if self.is_dark_mode else self.light_mode)
        else:
            CustomMessagebox(self.root, 'Login', 'Login Failed!', self.dark_mode if self.is_dark_mode else self.light_mode)


class CustomMessagebox(tk.Toplevel):
    def __init__(self, parent, title, message, theme):
        super().__init__(parent)
        self.theme = theme

        self.title(title)
        self.geometry("300x100")
        self.config(bg=self.theme["bg"])

        self.label = tk.Label(
            self, text=message, bg=self.theme["bg"], fg=self.theme["fg"]
        )
        self.label.pack(pady=20, padx=20)

        self.ok_button = tk.Button(
            self,
            text="OK",
            bg=self.theme["btn_bg"],
            fg=self.theme["btn_fg"],
            command=self.destroy,
        )
        self.ok_button.pack(pady=10)

root = tk.Tk()
root.title('Login App')
app = LoginApp(root)
root.mainloop()
