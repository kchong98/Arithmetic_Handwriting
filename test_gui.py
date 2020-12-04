import tkinter as tk
import os
from importlib import import_module as im

def write_slogan():
    print("Tkinter is easy to use!")

def run():
    os.system('webcam.py')

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.title("Equation Solver")
root.geometry('1280x720')

button = tk.Button(frame, text="Webcam", fg="blue", command = run)
button.pack(side=tk.LEFT)

leave = tk.Button(frame, text = "Exit", command=quit)
leave.pack(side=tk.LEFT)

root.mainloop()