import tkinter as tk

root = tk.Tk()
root.title("Hello!")
buton = tk.Button(root, text="kliknij!", command=lambda: print("ASD"))
buton.pack()
root.mainloop()
