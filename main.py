from tkinter import *
from tkinter import filedialog
import numpy as np
import wave
from tqdm import tqdm
from time import sleep
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(i):
    line.set_ydata(raw[saut-len(raw)+i])  # update the data.
    return line,
def sommeRie(x,n,p): #fonction somme qui permet de calculer l'air avec la méthode du trapèze (Somme de Riemann)
    air=0
    M=len(x)
    #print(len(x))
    if p==1:
        for k in tqdm(range(1,int(R))) :
            #sleep(0.0001) #sert au chargement, aspect esthetique ;)
            air += (raw[k])*np.sin(2*np.pi*n*f*dt*k)*dt
    if p==2:
        for k in tqdm(range(1,int(R))) :
            #sleep(0.0001) #sert au chargement, aspect esthetique ;)
            air += (raw[k])*np.cos(2*np.pi*n*f*dt*k)*dt
    return air
plt.style.use("bmh") #style de graphique
print("Veuillez sélectionner le fichier audio .wav que vous voulez analyser")#Importation de fichier wav à analyser
fichierAudio = filedialog.askopenfilename(initialdir="/Desktop/", title="Select a .wav file",filetypes=[("Sound file", "*.wav")])
f = float(input("Veuillez entrer la fréquence de votre son: ")) #l'utilisateur entre la fréquence
N = int(input("Veuillez entrer le nombre d'harmonique désiré pour votre son: ")) #l'utilisateur entre la fréquence

#Lecture du fichier audio
wav = wave.open(fichierAudio, "r")
raw = wav.readframes(-1) #trame en bytes
raw = np.frombuffer(raw, np.int16) #en 16 bits
E = wav.getframerate() #Fréquence d'échantillonage :nombre de points par seconde qui sont interprétés dans un fichier audio: double de l'audition humaine (généralement=44100)
#print(raw, len(raw))

#Partie Intervalle
time = np.linspace(0, len(raw) / (2*E), num=len(raw))
y=[0]*len(time)
saut=np.arange(0, len(raw),1)
print("time=",time)

#Liste de constante
T=1/f #Période en (s)
dt=time[1] #Varriation du temps entre les points du graphique du signal sonore
R=T/dt #Nombre de rectangle à aditionner pour la somme de riemann (nombre de points sur le signal dans une période)
#print("T=",T,"dt=",dt,"R=",R) #Permet de voir les valeurs

#Calcul des coéficients a[n] et b[n] de la n"iem" harmonique. n est le numéro de l'harmonique
a=[0]*(N)
b=[0]*(N)
for n in range(1,(N+1)):
    a[n-1]=(2*f*sommeRie(raw,n,1)) #sommeRie(raw,n,1)
    b[n-1]=(2*f*sommeRie(raw,n,2))
# for n in range(0,N):
#     print(a[n], "---", b[n])

#Permet de voir les n"iem" harmonnique
q = int(input("Veuillez entrer le nombre d'harmoniques désiré à voir dans un graph: ")) #l'utilisateur entre la fréquence
harm=[0]*q

#Partie spectre
A=[0]*N # Liste d'amplitude
liste_f = [0]*N # Liste de fréquence
for n in range(0,N):
    A[n]=np.sqrt((a[n]**2+b[n]**2))
    liste_f[n]= n*f
    #print(A[n]) #Impression des amplitude
Amp_max, freq_max = None, None
for k in range(1, len(A)):
    if (Amp_max is None or A[k] > Amp_max):
        Amp_max = A[k]
        freq_max= liste_f[k]
print('Maximum value:', Amp_max,"et la fréquence corréspondante: ",freq_max , "Hz")

#Partie Graphique
fig = plt.figure(figsize=(15,6)) #position des graphs
graphPrincipale = plt.subplot(221)
garphHarmonique = plt.subplot(223)
spectre = plt.subplot(122)
#fig, (graphPrincipale, garphHarmonique, spectre)= plt.subplots(3,1, figsize=(6.5,10)) #Laisse en cas ou
fig.subplots_adjust(left=0.16, bottom=0.12, right=0.95, top=0.950, wspace=0.2, hspace=0.414) #parametre des dimensions de la fenêtre

#graphPrincipale
graphPrincipale.set(title="Graphique du son pour une période",ylabel="Amplitude (Bytes) ", xlabel="Temps (s)") #titre et axe
line, = graphPrincipale.plot(time, raw, color="c")  #graduation d'axe est couleur
graphPrincipale.plot(time,y,linewidth=0.25, color="black",) #axe des y=0
graphPrincipale.set_xlim(0,1/f) #limte des x (jusqu'à sa période)

#garphHarmonique
garphHarmonique.set(title="Graphique des harmoniques du son pour une période",ylabel="Amplitude (Bytes) ", xlabel="Temps (s)") #titre et axe
for j in range (0,q):
    harm[j] = a[j] * np.sin(2 * np.pi * f * (j+1) * time) + b[j] * np.cos(2 * np.pi * f * (j+1) * time)
    garphHarmonique.plot(time, harm[j])
garphHarmonique.set_xlim(0,1/f) #limte des x (jusqu'à sa période)

#Spectre
spectre.set(title="Spectre du son",ylabel="Amplitude (Bytes) ", xlabel=" Fréquence des harmoniques (Hz)") #titre et axe
spectre.bar(liste_f, A, width=10, edgecolor="b", linewidth=0.7)

#Texte pour afficher max
spectre.text(freq_max, Amp_max, 'Amplitude max.', style='italic',
        bbox={'facecolor': 'c', 'alpha': 0.1, 'pad': 2})

#Animation
ani = animation.FuncAnimation(fig, animate, interval=10, blit=True, save_count=50)

plt.tight_layout()
plt.show()

