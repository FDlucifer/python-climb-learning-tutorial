import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text='Label 1:')
entry1 = tk.Entry(root)
label2 = tk.Label(root, text='Label 2:')
entry2 = tk.Entry(root)
button1 = tk.Button(root, text='Button 1')
button2 = tk.Button(root, text='Button 2')

# label1.pack(padx=5, pady=5, side=tk.LEFT)
# entry1.pack(padx=5, pady=5, side=tk.LEFT)
# label2.pack(padx=5, pady=5, side=tk.LEFT)
# entry2.pack(padx=5, pady=5, side=tk.LEFT)
# button1.pack(padx=5, pady=5)
# button2.pack(padx=5, pady=5)

label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
button1.pack(expand=True, fill=tk.BOTH)
button2.pack(expand=True, fill=tk.BOTH)

root.mainloop()
