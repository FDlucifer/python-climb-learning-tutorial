import tkinter as tk

root = tk.Tk()
root.geometry('250x170')

label1 = tk.Label(root, text='Label 1:')
entry1 = tk.Entry(root)
label2 = tk.Label(root, text='Label 2:')
entry2 = tk.Entry(root)
button1 = tk.Button(root, text='Button 1')
button2 = tk.Button(root, text='Button 2')

label1.place(x=10, y=10)
entry1.place(x=70, y=10)
label2.place(x=10, y=50)
entry2.place(x=70, y=50)

root.mainloop()
