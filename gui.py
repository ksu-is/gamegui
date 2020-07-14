import tkinter as tk 
from tkinter import *
import webbrowser

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()


def pac():
    import pacc.py
def tiktak():
    import tiktak.py  
def snake():
    import snake.py  
def search():
    webbrowser.open("https://www.miniclip.com/games/search/en/?query=" + e.get(), "#t-sd")



button = tk.Button(frame, text="QUIT", fg="red", bg= "purple", command=quit)
button.pack(side=tk.RIGHT)
button = tk.Button(frame, text= "Snake", fg="yellow", bg= "green", command= snake) 
button.pack(side=tk.LEFT)
button = tk.Button(frame, text="Tik Tak Toe", fg="blue",bg= "pink", command= tiktak)
button.pack(side=tk.LEFT)
button = tk.Button(frame, text="Pac Man", fg="green", bg= "blue", command= pac)
button.pack(side=tk.LEFT)
e = Entry(root)
e.pack()
button = Button(root, text= "Search for game", command= search)
button.pack(side=tk.BOTTOM)
root.mainloop()