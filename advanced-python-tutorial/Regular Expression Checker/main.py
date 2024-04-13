import re
import tkinter as tk


def check_matche():
    regex = regex_entry.get()
    text = text_entry.get("1.0", "end-1c")

    if regex and text:
        if re.match(regex, text):
            result_label.config(text="regex matches the whole text!", fg="green")
        else:
            result_label.config(text="regex dose not matche the whole text!", fg="red")


def find_matchs():
    regex = regex_entry.get()
    text = text_entry.get("1.0", "end-1c")

    if regex and text:
        matches = re.finditer(regex, text)
        for match in matches:
            start_index = f"1.0 + {match.start()} chars"
            end_index = f"1.0 + {match.end()} chars"
            text_entry.tag_add("match", start_index, end_index)
        text_entry.tag_config(
            "match", foreground="black", background="red", font=("Arial", 10, "bold")
        )


root = tk.Tk()
root.title("RegEx Checker")

regex_label = tk.Label(root, text="enter regex:")
regex_label.grid(row=0, column=0, padx=5, pady=5)

regex_entry = tk.Entry(root, width=50)
regex_entry.grid(row=0, column=1, padx=5, pady=5)

text_label = tk.Label(root, text="enter text:")
text_label.grid(row=1, column=0, padx=5, pady=5)

text_entry = tk.Text(root, width=50, height=10)
text_entry.grid(row=1, column=1, padx=5, pady=5)

find_button = tk.Button(root, text="find matches", command=find_matchs)
find_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")

check_button = tk.Button(root, text="check matches", command=check_matche)
check_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

result_label = tk.Label(root, text="", fg="green")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
