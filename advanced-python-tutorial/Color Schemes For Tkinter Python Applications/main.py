import json
import tkinter as tk


def load_theme(theme_name):
    with open(f"{theme_name}.json", "r") as f:
        theme = json.load(f)
    return theme


def apply_theme(theme):
    app.config(bg=theme["background"])
    textbox.config(
        fg=theme["foreground"],
        bg=theme["background"],
        font=(theme["font"], theme["fontsize"]),
    )
    button.config(
        fg=theme["foreground"],
        bg=theme["background"],
        font=(theme["font"], theme["fontsize"]),
    )
    option_menu.config(
        fg=theme["foreground"],
        bg=theme["background"],
        font=(theme["font"], theme["fontsize"]),
    )
    current_theme.update(theme)


def show_custom_message():
    popup = tk.Toplevel(app)
    popup.title("message")
    popup.config(bg=current_theme["messagebox_bg"])
    msg = tk.Label(
        popup,
        text=textbox.get(),
        fg=current_theme["messagebox_fg"],
        bg=current_theme["messagebox_bg"],
    )
    msg.pack(padx=20, pady=20)
    button_close = tk.Button(popup, text="close", command=popup.destroy)
    button_close.pack(pady=20)


def on_theme_change(*args):
    theme = load_theme(theme_var.get())
    apply_theme(theme)


# app, textbox, button, option_menu, -> ui elements
# current_theme -> {...}
app = tk.Tk()
app.title("theme changing app")
current_theme = {}

textbox = tk.Entry(app)
button = tk.Button(app, text="show message", command=show_custom_message)
theme_var = tk.StringVar(app)
theme_var.set("classic elegance")
option_menu = tk.OptionMenu(
    app,
    theme_var,
    "Classic Elegance",
    "Midnight Oasis",
    "Ocean Breeze",
    "Soft Serenity",
    "Sunset Glow",
)
theme_var.trace("w", on_theme_change)

textbox.pack(padx=10, pady=10)
button.pack(padx=10, pady=10)
option_menu.pack(padx=10, pady=10)

default_theme = load_theme("Classic Elegance")
apply_theme(default_theme)

app.mainloop()
