import uuid


def promptCarInfos(prixFlotte):
    try:

        carName = input("Veuillez saisir le nom de la voiture : ")
        prixFlotte["carName"] = carName
        prixVoiture = input("Veuillez saisir le Prix de la voiture : ")

        prixFlotte["uiid"] = str(uuid.uuid4())

        if prixVoiture.isdigit():
            prixFlotte["price"] = int(prixVoiture)
     
        else:
            print("Erreur : Veuillez entrer un nombre valide pour le prix.")



        bonusEco = input("Veuillez saisir le bonus écologique en pourcentage : ")
        if bonusEco.isdigit():
            bonusEco = int(bonusEco)

            if(bonusEco < 0 or   bonusEco > 100):
                print("Erreur : Le bonus écologique ne peut pas dépasser 100% ou être négatif.")
                return

            prixFlotte["bonusEco"] = float(bonusEco) / 100
        else:
            print("Erreur : Veuillez entrer un nombre valide pour le bonus écologique.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

def prixTTC(prixHT, tva):
    return prixHT * (1 + tva)

def remiseEco(prixHT, primeEco):
    return prixHT * (1 - primeEco) 

def saveCarsToFile(cars, filePath):
    try:
        with open(filePath, 'w') as file:
            for car in cars:
                file.write(f"{car['uiid']},{car['carName']},{car['price']},{car['bonusEco']}\n")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde des voitures : {e}")
    finally:
        file.close()