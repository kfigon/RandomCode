import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)

tk.Label(frame, text="text1").grid(row=0, column=0)
buton1 = tk.Button(frame, text="one").grid(row=0, column=1)
buton2 = tk.Button(frame, text="two").grid(row=1, column=0)
buton3 = tk.Button(frame, text="three").grid(row=1, column=1)
buton4 = tk.Button(frame, text="4").grid(row=2, column=0)


frame.pack()
root.mainloop()