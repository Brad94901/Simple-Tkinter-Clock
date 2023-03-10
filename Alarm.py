import time
import multiprocessing
import threading
import tkinter as tk
from tkinter import *
from playsound import playsound

def abh():
	t = threading.Thread(target=alarm, args=(min_var.get(), hour_var.get()))
	t.start()
	return 0

def tbh(): #Button to handle timer thread to prevent GUI from freezing.
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


def alarm(hours, minutes):
	while True:
		if time.strftime("%H") == hours and time.strftime("%M") == minutes:
			playsound('C:/Windows/Media/Alarm02.wav')
			return 0
		time.sleep(1)


root = tk.Tk()
root.geometry("350x100")
root.resizable(width = False, height = False)
root.title("Alarm Clock")
t = Label(root, font = ("Helvetica", 14), fg='#000')

t.grid(row = 0, column = 1, pady = 2)

#GUI elements for spinbox and button for countdown timer
name_var = tk.StringVar()
cd = Spinbox(root, from_= 0, to = 60, increment = 1, state='readonly', wrap=True, textvariable = name_var)
cd.grid(row = 2, column = 1, padx = 5)
tb = Button(root, text = "Timer", command = lambda: tbh())
tb.grid(row = 2, column = 0, padx = 0)

#GUI elements for spinboxes and alarm
min_var = tk.StringVar()
hour_var = tk.StringVar()
msb = Spinbox(root, from_ = 0, to = 24, increment = 1, state='readonly', wrap = True, textvariable = min_var)
msb.grid(row = 4, column =1, padx = 5)
hsb = Spinbox(root, from_ = 0, to = 60, increment = 1, state='readonly', wrap = True, textvariable = hour_var)
hsb.grid(row = 4, column =2, padx = 5)
ab = Button(root, text = "Alarm", command = lambda: abh())
ab.grid(row = 4, column = 0, padx = 5)

clock()
mainloop()
	
