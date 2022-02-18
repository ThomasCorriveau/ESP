from tkinter import *
from tkinter import filedialog
import pygame
import numpy as np
import wave
import sys
import matplotlib.pyplot as plt

wav= wave.open("test.wave","r")

raw=wav.readframes(-1)
raw= np.frombuffer(raw,"Int16")

if wav.getnchannels()==2:
    prinnt("Stereo files are not supported.Use Mono Files")
    sys.exit(0)

plt.title("Notre son")
plt.plot(raw, color= "pink")
plt.ylabel("Amplitude")
plt.show()
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

# yoyoyoyyo


root.mainloop()

