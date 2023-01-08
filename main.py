#Import des différentes libraries.
from tkinter import * #On importe la library Tkinter pour pouvoir générer l'UI de l'application.
import os as os #On importe la library os pour pouvoir manipuler les fichiers du pc.


#Définition des caractéristiques de la fenêtre.
window = Tk() #On déclare la fenêtre.
window.title("FaceDetect") #On donne un titre à la fenêtre.
window.geometry('300x200') #Taille de la fenêtre en pixel.
icon = PhotoImage(file = "ressources/visuals/icon.png") #On donne l'emplacement de l'icone.
window.iconphoto(False, icon) #On applique l'icone choisi à la fenêtre.



#Définition des différentes fonctions.
#Ici on utilise la library OS pour pouvoir executer les différents programmes annexes.
def ImageDetect():
    os.system("python imageDetect.py") #On execute imageDetect.
  
def VideoDetect():
    os.system("python videoDetect.py") #On execute videoDetect.

def WebcamDetect():
    os.system("python webcamDetect.py") #On execute webcamDetect.


#Contenue de la fenêtre

btnImage = Button(window, text="Image", command=ImageDetect) #Un bouton lié à la détection sur les images.
btnImage.grid(column=0, row=0) #La position du bouton.

btnVideo = Button(window, text="Video", command=VideoDetect) #Un bouton lié à la détection sur les vidéos.
btnVideo.grid(column=1, row=0) #La position du bouton.

btnWebcam = Button(window, text="Webcam", command=WebcamDetect) #Un bouton lié à la détection sur la webcam.
btnWebcam.grid(column=2, row=0) #La position du bouton.

#Fin
window.mainloop() #On fini en "exécutant" la fenêtre.