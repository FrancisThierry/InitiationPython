## créer un programme qui permet d'insérer des voitures / prix, marque bonus ECO. et les sauvegarder dans un fichier

from functions.carsFunctions import promptCarInfos, prixTTC, saveCarsToFile
import os



## demander à l'utilisateur de saisir le nombre de voitures à ajouter



## demander à l'utilisateur de saisir le prix de la voiture, le bonus écologique et la marque






def mainProgramme():
    prixFlotte = {}
    # inITIALISATION DES VARIABLES
    ## liste de voitures
    carFloat = []
    ## chemon vers le fichier de données à sauvegarder
    carsFilePath = "C:\\data\\cars.txt"
    nbCars = input("Combien de voitures voulez-vous ajouter ?")

    if nbCars.isdigit():
        nbCars = int(nbCars)
    else:   
        print("Erreur : Veuillez entrer un nombre valide pour le nombre de voitures.")
        nbCars = 0
    for i in range(nbCars):
        print(f"Voiture {i+1} :")
        promptCarInfos(prixFlotte)
        print(prixFlotte)
        carFloat.append(prixFlotte)
    print(carFloat)

    # Sauvegarder les voitures dans un fichier
    saveCarsToFile(carFloat, carsFilePath)
mainProgramme()