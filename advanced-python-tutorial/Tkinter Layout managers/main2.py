import tkinter as tk

root = tk.Tk()

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

label1 = tk.Label(frame1, text='Label 1:')
entry1 = tk.Entry(frame1)
label2 = tk.Label(frame1, text='Label 2:')
entry2 = tk.Entry(frame1)
button1 = tk.Button(frame2, text='Button 1')
button2 = tk.Button(frame2, text='Button 2')

label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
button1.pack()
button2.pack()

frame1.pack(side=tk.LEFT)
frame2.pack(side=tk.LEFT)

root.mainloop()
