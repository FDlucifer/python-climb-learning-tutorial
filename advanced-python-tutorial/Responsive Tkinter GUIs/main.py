import tkinter as tk

root = tk.Tk()

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

label1 = tk.Label(frame1, text='Label1')
entry1 = tk.Entry(frame1)
label2 = tk.Label(frame1, text='Label2')
entry2 = tk.Entry(frame1)
label3 = tk.Label(frame1, text='Label3')
text1 = tk.Text(frame1, width=20, height=5)
button1 = tk.Button(frame1, text='Button1')

label1.pack(fill='x')
entry1.pack(fill='x')
label2.pack(fill='x')
entry2.pack(fill='x')
label3.pack(fill='x')
text1.pack(fill='both', expand=True)
button1.pack(fill='x')

label4 = tk.Label(frame2, text='Label4')
text2 = tk.Text(frame2, width=20, height=10)
button2 = tk.Button(frame2, text='Button2')

label4.pack(fill='x')
text2.pack(fill='both', expand=True)
button2.pack(fill='x')

frame1.pack(side=tk.LEFT, fill='both', expand=True)
frame2.pack(side=tk.LEFT, fill='both', expand=True)

root.mainloop()
