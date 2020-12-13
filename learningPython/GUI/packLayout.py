import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)

tk.Label(frame, text="text1").pack()
buton1 = tk.Button(frame, text="one").pack(side=tk.LEFT, fill=tk.Y)
buton2 = tk.Button(frame, text="two").pack(side=tk.TOP, fill=tk.X)
buton3 = tk.Button(frame, text="three").pack(side=tk.RIGHT, fill=tk.X)
buton4 = tk.Button(frame, text="4").pack(side=tk.LEFT, fill=tk.X)


frame.pack()
root.mainloop()