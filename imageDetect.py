#Import des différentes libraries.
import cv2 #On importe OpenCV pour le traitement de l'image et l'affichage final.

#Import des différents outils nécessaire au traitement.
cascadeClassifierPath = 'ressources/haarcascade_frontalface_alt.xml' #Chemin du classifier ou de la base de données.
cascadeClassifier = cv2.CascadeClassifier(cascadeClassifierPath) #Traitement du classifier.
imageFile = "image.jpg" #Nom de l'image utilisée.
imagePath = "images/"+imageFile #Emplacement de l'image utilisée.

#Traiement de l'image.
image = cv2.imread(imagePath) #On lit l'image.
grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #On passe l'image en noir et blanc.
detectedFaces = cascadeClassifier.detectMultiScale(image) #On detect les visages par rapport au jeu de données.

#Affichage des résultats.
for(x,y, width, height) in detectedFaces:
    cv2.rectangle(image,(x,y),(x+width, y+height),(0,255,0),5) #On affiche les rectangle en fonction des résultats.

cv2.imshow("resultat",image) #Ouverture de la fenêtre.
cv2.waitKey(0) #En attente qu'on appuie sur la touche "0" pour la fermeture.
cv2.destroyAllWindows() #Quand "0" est pressé, on détruit toute les fenêtres.