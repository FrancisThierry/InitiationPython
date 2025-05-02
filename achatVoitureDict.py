# Créer une variable pour le prix d'une voiture 
# et dans le programme indiquer sa valeur TTC,
#  HT et son prix si on accorde un bonus écologique de 5% (définir une variable)

# sur le prix HT

# Créer une variable pour le prix autre voiture 
# et dans le programme indiquer sa valeur TTC,
#  HT et son prix si on accorde un bonus écologique de 5% (définir une variable)
# sur le prix HT

# prixVoiture1 = 452566
# prixVoiture2 = 566688
# tuple de données = (452566, 566688)
# prixFlotte = (452566,566688)
prixFlotte = {"price":452566, "bonusEco":0.05, "name":"Ford B Max"}


tva = 0.2
primeEco = 0.05
beneficiePrimeEco = True
# calcul de la remise eco
# calcul du prix ttc



def prixTTC(prixHT, tva):
    return prixHT * (1 + tva)   

def remiseEco(prixHT, primeEco):
    return prixHT * (1 - primeEco)  

# for prixVoiture in prixFlotte:
#     prixTTCVoiture = prixTTC(prixVoiture["price"], prixVoiture["bonusEco"])
#     print("Prix TTC : {0}".format(prixTTCVoiture))
#     prixRemiseEco = remiseEco(prixVoiture, primeEco) 
#     print("Prix avec prime éco : {0}".format(prixRemiseEco))


# for i in range(len(prixFlotte)):
#     print("i :",i)
#     prixTTCVoiture = prixTTC(prixFlotte[i]["price"], tva)
#     print("Prix TTC : {0}".format(prixTTCVoiture
#     prixRemiseEco = remiseEco(prixFlotte[i], primeEco) 
#     print("Prix avec prime éco : {0}".format(prixRemiseEco))

# def affichePrix():
#     print("Prix TTC : {0}".format(prixTTC(prixVoiture1, tva)))
#     print("Prix HT : {0}".format(prixVoiture1))
#     print("Prix avec prime éco : {0}".format(remiseEco(prixVoiture1, primeEco)))

# affichePrix()

# Créer une programme qui permet d'insérer des voitures / prix, marque bonus ECO.
try:
    prixVoiture = input("Veuillez saisir le Prix de la voiture : ")

    if prixVoiture.isdigit():
        prixFlotte["price"] = int(prixVoiture)
    else:
        print("Erreur : Veuillez entrer un nombre valide pour le prix.")
except Exception as e:
    print(f"Une erreur est survenue : {e}")



