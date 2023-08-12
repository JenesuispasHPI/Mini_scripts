
# Création du dictionnaire associant les plantes à leurs utilisations médicinales
plantes_et_usages = {
   # Dictionnaire associant les plantes à leurs usages médicinaux
plantes_et_usages = {
    "Camomille": "Apaisante, anti-inflammatoire, digestive",
    "Menthe": "Digestive, rafraîchissante, anti-nausée",
    "Valériane": "Sédative, relaxante, favorise le sommeil",
    "Mélisse": "Calme le système nerveux, digestive",
    "Thym": "Antibactérien, antiviral, stimule l'immunité",
    "Échinacée": "Renforce le système immunitaire",
    "Gingembre": "Anti-inflammatoire, stimule la digestion",
    "Passiflore": "Relaxante, favorise le sommeil",
    "Calendula": "Anti-inflammatoire, cicatrisante",
    "Aloe Vera": "Cicatrisante, apaisante pour la peau",
    "Ginseng": "Tonique, adaptogène, stimule l'énergie",
    "Cannelle": "Anti-infectieuse, stimule la circulation",
    "Réglisse": "Anti-inflammatoire, expectorante",
    "Sauge": "Antibactérienne, aide à la digestion",
    "Ortie": "Tonique, reminéralisante, antiallergique",
    "Romarin": "Stimulant, tonique, améliore la circulation",
    "Lavande": "Apaisante, anti-stress, favorise le sommeil",
    "Fenouil": "Digestive, antispasmodique, favorise la lactation",
    "Aubépine": "Soutient le cœur, régule la tension",
    "Passionaria": "Anxiolytique, aide au sommeil",
    "Achillée millefeuille": "Cicatrisante, antispasmodique",
    "Guimauve": "Adoucissante, anti-inflammatoire",
    "Houblon": "Sédatif, favorise le sommeil",
    "Sureau": "Décongestionnant, stimule l'immunité",
    "Eucalyptus": "Décongestionnant, antiseptique",
    "Chardon Marie": "Protège le foie, détoxifiant",
    "Passiflora": "Apaisante, favorise le sommeil",
    "Curcuma": "Anti-inflammatoire, antioxydant",
    "Pissenlit": "Dépuratif, diurétique, stimule la digestion",
    "Artichaut": "Protège le foie, stimule la digestion",
    "Boldo": "Digestive, protège le foie",
    "Griffonia": "Régule l'humeur, favorise le sommeil",
    "Astragale": "Stimule l'immunité, adaptogène",
    "Ail": "Antibactérien, antiviral, stimule l'immunité",
    "Ginkgo Biloba": "Améliore la circulation, stimule la mémoire",
    "Passiflora incarnata": "Soulage l'anxiété, favorise le sommeil",
    "Valeriana officinalis": "Sédative, favorise le sommeil",
    "Hypericum perforatum": "Antidépresseur léger, apaise les nerfs",
    "Matricaria chamomilla": "Anti-inflammatoire, digestive",
    "Salvia officinalis": "Antibactérienne, digestive",
    "Urtica dioica": "Tonique, reminéralisante, antiallergique",
    "Melissa officinalis": "Calme le système nerveux, digestive",
    "Echinacea purpurea": "Renforce le système immunitaire",
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
    