# pip install sympy

import tkinter as tk
import sympy as sp


class LimitCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("limit calculator")

        self.symbol_label = tk.Label(self.root, text="Symbol")
        self.symbol_label.grid(row=0, column=0, padx=2, pady=2)

        self.symbol_text = tk.Entry(self.root)
        self.symbol_text.grid(row=0, column=1, padx=2, pady=2)

        self.limit_label = tk.Label(self.root, text="limit")
        self.limit_label.grid(row=1, column=0, padx=2, pady=2)

        self.limit_text = tk.Entry(self.root)
        self.limit_text.grid(row=1, column=1, padx=2, pady=2)

        self.expression_label = tk.Label(self.root, text="expression")
        self.expression_label.grid(row=2, column=0, padx=2, pady=2)

        self.expression_text = tk.Entry(self.root)
        self.expression_text.grid(row=2, column=1, padx=2, pady=2)

        self.calculate_button = tk.Button(self.root, text='calculate limit', command=self.calculate_limit)
        self.calculate_button.grid(row=3, column=0, columnspan=2, padx=2, pady=2)

        self.result_label = tk.Label(self.root, text='-')
        self.result_label.grid(row=4, column=0, columnspan=2, padx=2, pady=2)

        self.sym = None
        self.lim = None

        self.root.mainloop()

    def calculate_limit(self):
        self.sym = sp.symbols(self.symbol_text.get())

        expression = self.expression_text.get()
        expression = f'{expression}.doit()' if 'sum' in expression else expression

        self.lim = sp.limit(expression, self.sym, self.limit_text.get())
        self.result_label.config(text=str(self.lim))


LimitCalculator()
