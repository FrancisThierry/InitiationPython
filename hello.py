#print("Hello Python")

taxe = 0.2
salaire = 1000
print("salaire Brut")
print(salaire)
salaireNet = salaire * (1 - taxe)
print("salaire Net")
print(salaireNet)
print("salaire par semaine  ",1000) 
print("Salaire par semaine : {0}".format(salaireNet / 4))
print("salaire par semaine  "+str(salaireNet / 4))
print(f"salaire par semaine {salaireNet / 4}  ")


# indique si c'est un salaire moyen , bas ou élevé moyen = 1500, bas < 1500, élevé > 1500
if salaireNet < 1500:
    print("salaire bas")
    print("salaire trés bas")
elif salaireNet > 1500:
    print("salaire élevé")  
else:
    print("salaire moyen")


match salaireNet:
    case salaireNet if salaireNet < 1500:
        print("salaire bas")
    case salaireNet if salaireNet > 1500:
        print("salaire élevé")
    case _:
        print("salaire moyen")  

estEleveSalaireNet = salaireNet > 1500

if estEleveSalaireNet:
    print("salaire élevé")
if not estEleveSalaireNet:
    print("salaire bas")



# print(salaireNet / 3)