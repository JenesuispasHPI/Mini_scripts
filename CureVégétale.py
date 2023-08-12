
# Création du dictionnaire associant les plantes à leurs utilisations médicinales
plantes_et_usages = {
    "Camomille": "Apaisante et relaxante",
    "Menthe": "Digestive et rafraîchissante",
    "Valériane": "Sédative et calmante",
    "Mélisse": "Anti-stress et relaxante",
    "Thym": "Antiseptique et expectorante",
    "Échinacée": "Renforce le système immunitaire",
    "Gingembre": "Anti-nausée et anti-inflammatoire",
    "Passiflore": "Soulage l'anxiété et l'insomnie",
    "Calendula": "Cicatrisante et anti-inflammatoire",
    "Aloe Vera": "Hydratante et apaisante pour la peau",
    "Ginseng": "Stimulant et énergisant",
    "Cannelle": "Antioxydante et régulatrice de sucre",
    "Réglisse": "Anti-inflammatoire et expectorante",
    "Sauge": "Antibactérienne et antiseptique",
    "Ortie": "Dépurative et reminéralisante"
}

# Demande à l'utilisateur d'entrer le nom d'une plante
plante = input("Entrez le nom d'une plante : ")

# Vérifie si la plante est dans le dictionnaire et affiche son usage médicinal
if plante in plantes_et_usages:
    usage = plantes_et_usages[plante]
    print(f"L'usage médicinal de la plante {plante} est : {usage}")
else:
    print("Plante non trouvée dans la liste.")
    
# Dictionnaire associant les plantes à leurs parties/organes recommandés
plantes_et_parties = {
    "Camomille": "Fleurs",
    "Menthe": "Feuilles",
    "Valériane": "Racines",
    "Mélisse": "Feuilles",
    "Thym": "Feuilles",
    "Échinacée": "Racines et parties aériennes",
    "Gingembre": "Rhizome",
    "Passiflore": "Feuilles et fleurs",
    "Calendula": "Fleurs",
    "Aloe Vera": "Gel de la feuille",
    "Ginseng": "Racines",
    "Cannelle": "Écorce",
    "Réglisse": "Racines",
    "Sauge": "Feuilles",
    "Ortie": "Feuilles"
}

# Demande à l'utilisateur d'entrer le nom d'une plante
plante = input("Entrez de nouveau le nom d'une plante : ")

# Vérifie si la plante est dans le dictionnaire et affiche la partie/organe recommandé
if plante in plantes_et_usages:
    usage = plantes_et_usages[plante]
    partie = plantes_et_parties[plante]
    print(f"L'usage médicinal de la plante {plante} est : {usage}")
    print(f"La partie/organe recommandé(e) à consommer est : {partie}")

    # Demande au client la durée de la cure
    duree = input("Choisissez la durée de la cure (3 jours, 7 jours, ou 15 jours) : ")
    
    if duree in ["3 jours", "7 jours", "15 jours"]:
        print(f"Vous avez choisi une cure de {duree}.")
        if duree == "15 jours":
            print("N'oubliez pas de consulter un médecin avant une cure prolongée.")
    else:
        print("Durée de cure non valide.")
else:
    print("Plante non trouvée dans la liste.")
    