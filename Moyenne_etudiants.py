def calculer_moyenne(notes):
    total = sum(notes)
    moyenne = total / len(notes)
    return moyenne

# Liste des notes des étudiants
notes_etudiants = [85, 92, 78, 65, 90, 87]

# Calcul de la moyenne
moyenne_classe = calculer_moyenne(notes_etudiants)

# Affichage du résultat
print("La moyenne de la classe est :", moyenne_classe)
