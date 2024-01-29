# pip install matplotlib pandas

import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class CSVPlotter:
    def __init__(self, root):
        self.root = root
        root.title("CSV Plotter")

        self.plot_types = ["Line Plot", "Bar Plot", "Scatter Plot"]
        self.plot_type_var = tk.StringVar(value=self.plot_types[0])
        plot_menu = tk.OptionMenu(
            self.root, self.plot_type_var, *self.plot_types, command=self.update_plot
        )
        plot_menu.pack(padx=10, pady=10)

        load_button = tk.Button(self.root, text="Load CSV", command=self.load_csv)
        load_button.pack(padx=10, pady=10)

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.widget = self.canvas.get_tk_widget()
        self.widget.pack(padx=10, pady=10)

        self.df = None

    def load_csv(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.df = pd.read_csv(file_path)
            self.update_plot()

    def update_plot(self, event=None):
        if self.df is not None:
            plot_type = self.plot_type_var.get()
            x = self.df.columns[0]
            y = self.df.columns[1]

            self.ax.clear()
            if plot_type == "Line Plot":
                self.ax.plot(self.df[x], self.df[y], label=f"{y} vs {x}")
            elif plot_type == "Bar Plot":
                self.ax.bar(self.df[x], self.df[y], label=f"{y} vs {x}")
            elif plot_type == "Scatter Plot":
                self.ax.scatter(self.df[x], self.df[y], label=f"{y} vs {x}")

            self.ax.set_xlabel(x)
            self.ax.set_ylabel(y)
            self.ax.legend()
            self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = CSVPlotter(root)
    root.mainloop()
