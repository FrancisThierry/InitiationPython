import uuid


def promptCarInfos(prixFlotte):
    try:
        prixVoiture = input("Veuillez saisir le Prix de la voiture : ")

        prixFlotte["uiid"] = str(uuid.uuid4())

        if prixVoiture.isdigit():
            prixFlotte["price"] = int(prixVoiture)
     
        else:
            print("Erreur : Veuillez entrer un nombre valide pour le prix.")



        bonusEco = input("Veuillez saisir le bonus écologique : ")
        if bonusEco.isdigit():
            prixFlotte["bonusEco"] = float(bonusEco) / 100
        else:
            print("Erreur : Veuillez entrer un nombre valide pour le bonus écologique.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")