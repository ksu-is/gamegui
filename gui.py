import tkinter as tk
    
def pac():
    import pacc.py

def tiktak():
    import tiktak.py

def snake():
    import snake.py

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="QUIT", fg="red", command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame, text= "Snake", fg="yellow", width= 6, height= 3, command= snake) 
slogan = tk.Button(frame, text="Tik Tak", fg="blue", command= tiktak)
slogan = tk.Button(frame, text="Pac Man ", fg="green", command= pac)
slogan.pack(side=tk.LEFT)
slogan.pack(side=tk.RIGHT)
root.mainloop()