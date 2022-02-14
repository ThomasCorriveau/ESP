from tkinter import *
from tkinter import filedialog
import pygame
import numpy as np
# pyaudio ?

root = Tk()
root.title("Sound Player")
root.geometry("500x400")

pygame.mixer.init()


def play():
    pygame.mixer.music.load(root.filename)
    pygame.mixer.music.play(loops=0)


root.filename = filedialog.askopenfilename(initialdir="/", title="Select a .wav file", filetypes=[("Sound file", "*.wav")])
my_button = Button(root, text="Play selected sound", command=play)
my_button.pack(pady=10)



root.mainloop()

