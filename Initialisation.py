from tkinter import filedialog
import wave

print("Veuillez sélectionner le fichier audio .wav que vous voulez analyser")
fichierAudio = filedialog.askopenfilename(initialdir="/Desktop/", title="Select a .wav file", filetypes=[("Sound file", "*.wav")])
Wave_read = wave.open(fichierAudio, "rb")

N = int(input("Veuillez entrer le nombre d'harmoniques que vous voulez analyser: "))
f = float(input("Veuillez entrer la fréquence de votre son: ")) # fréquence
T = 1/f # période
E = Wave_read.getframerate() # fréquence d'échantillonnage : nombre de points par seconde qui sont interprétés dans un fichier audio : double de l'audition humaine
deltaT = 1/E # variation de temps entre les points du graphique du signal sonore.
R = T/deltaT # nombre de rectangles à additionner pour la somme de Riemann : correspond au nombre de points sur le signal dans une période.
