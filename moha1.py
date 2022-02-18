from tkinter import *
from tkinter import filedialog
import pygame
import numpy as np
import wave
import sys
import matplotlib.pyplot as plt

plt.style.use("seaborn")
print("Veuillez sélectionner le fichier audio .wav que vous voulez analyser")
fichierAudio = filedialog.askopenfilename(initialdir="/Desktop/", title="Select a .wav file", filetypes=[("Sound file", "*.wav")])

#f = float(input("Veuillez entrer la fréquence de votre son: "))

wav = wave.open(fichierAudio, "r")
print(wav.getframerate())

raw = wav.readframes(-1)
raw = np.frombuffer(raw, np.int16)
sampleRate= wav.getframerate()

time = np.linspace(0, len(raw)/sampleRate, num= len(raw))
plt.title("Graphique du son")
plt.plot(time, raw, color= "red")
plt.ylabel("Amplitude")
plt.show()
