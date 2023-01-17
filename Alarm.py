import time
import multiprocessing
import threading
import tkinter as tk
from tkinter import *
from playsound import playsound

def abf(): #Button to handle timer thread to prevent GUI from freezing.
	seconds = int(name_var.get())
	t = threading.Thread(target=timer , args=[seconds])
	#timer(int(seconds))
	t.start()
	return 0

def clock():
	cur_time = time.strftime("%H:%M:%S")
	t.config(text = cur_time)
	t.after(1000, clock)


def timer(seconds):
	while seconds:
		time.sleep(1)
		seconds -= 1

	playsound('C:/Windows/Media/Alarm01.wav')


def alarm():
	sleep(0)


root = tk.Tk()
root.geometry("300x400")
root.resizable(width = False, height = False)
root.title("Alarm Clock")
t = Label(root, font = ("Helvetica", 14), fg='#000')

t.grid(row = 0, column = 1, pady = 2)

name_var = tk.StringVar()
cd = Spinbox(root, from_= 0, to = 60, increment = 1, state='readonly', wrap=True, textvariable = name_var)
cd.grid(row = 2, column = 1, padx = 5)

ab = Button(root, text = "Timer", command = lambda: abf())
#ab.pack(side = BOTTOM)
ab.grid(row = 2, column = 0, padx = 0)



clock()
mainloop()
	
