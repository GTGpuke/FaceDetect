#Import des différentes libraries.
import cv2 #On importe OpenCV pour le traitement de la vidéo et l'affichage final.

#Import des différents outils nécessaire au traitement.
cascadeClassifierPath = 'ressources/haarcascade_frontalface_alt.xml' #Chemin du classifier ou de la base de données.
cascadeClassifier = cv2.CascadeClassifier(cascadeClassifierPath) #Traitement du classifier.
videoPath="title-artist.mp4" #Nom de la vidéo utilisée.
cap = cv2.VideoCapture("videos/"+videoPath) #Emplacement de la vidéo utilisée.

#Traiement de la vidéo.
while(cap.isOpened()):
	_, frame = cap.read() #On lit chaque frame de la vidéo tant que celle ci est ouverte.
	grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # On convertit chaque frame en noir et blanc.
	detectedFaces = cascadeClassifier.detectMultiScale(grayImage,  scaleFactor=1.1, minNeighbors=10, minSize=(20, 20)) #On detect les visages par rapport au jeu de données. 

#Affichage des résultats.
	for(x,y, width, height) in detectedFaces:
		cv2.rectangle(frame, (x, y), (x+width, y+height), (0,255,0), 3) #On affiche les rectangle en fonction des résultats.
		
	cv2.imshow("resultat", frame) #Ouverture de la fenêtre.
	if cv2.waitKey(1) == ord('q'):
		break #On attend que quelqu'un appuie sur la touche "q" et on passe à la suite du programme.

cap.release()
cv2.destroyAllWindows() #Quand "q" est pressé, on détruit toutes les fenêtres.