def calcul_clients_salaire(salaire_souhaite):
    smic_mensuel = 1830.03  # Montant du SMIC mensuel en euros
    montant_client = 500  # Montant reçu par chaque client de type 1
    montant_client2 = 200 # Montant reçu de client de type 2
    montant_client3 = 20 # Montanr reçu de client de type 3

    clients_necessaires = salaire_souhaite / montant_client
    clients_necessaires2 = salaire_souhaite / montant_client
    clients_necessaires3 = salaire_souhaite / montant_client
    return clients_necessaires
    return clients_necessaires2
    return clients_necessaires3
    
    # il faudra differencier et faire une formule par client !

salaire_souhaite = float(input("Entrez le salaire souhaité en euros : "))
clients_necessaires = calcul_clients_salaire(salaire_souhaite)

print("Pour atteindre un smic, il vous faut", clients_necessaires,"clients de type 1")
print(f"Il vous faudra {clients_necessaires:.2f} clients à 500 euros chacun pour atteindre le salaire souhaité.")
