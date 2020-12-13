import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)  # jak panel w javie
labelText = tk.StringVar() # do zmieniania labelki dynamicznie
labelka = tk.Label(frame, textvariable=labelText)

buton = tk.Button(frame, text="kliknij!",
                  command=lambda: print("ASD"))

labelText.set("labelkalalal")

labelka.pack()
buton.pack()
frame.pack()
root.mainloop()