import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)

plotno = tk.Canvas(frame, width=300, height=300)
plotno.create_oval(10,20, 40, 40, fill='blue')
plotno.create_line(0, 40, 300, 340, width=2, fill='black')

tk.Button(frame, text='czysc', command=lambda: plotno.delete('all')).pack()


plotno.pack()
frame.pack()
root.mainloop()