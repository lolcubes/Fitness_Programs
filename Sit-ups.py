from playsound import playsound
from tkinter import *
import time
tk = Tk()
def beeps(amount):
	amount = int(w.get())
	for x in range(0, amount):
		playsound('/Users/Mukeshkhare/Downloads/beep-02.wav')
		time.sleep(60/amount)



label = Label(tk, text="Enter number of sit-ups:")
label.pack(padx=5, side=LEFT)
w = Entry(tk)
w.bind("<Return>", beeps)
w.pack(padx=5, side=RIGHT)

