# Dictionnaire des fleurs et de leurs couleurs
fleurs_et_couleurs = {
    "Rose": "rouge",
    "Tulipe": "jaune",
    "Pivoine": "rose",
    "Marguerite": "blanche",
    "Lavande" : "violet",
    "Lys" : "blanc",
    "Orchidée": "violet",
    "Coquelicot": "rouge",
	  "Jonquille": "jaune",
	  "Bleuet": "Bleu",
	  "Camélia": "Rouge",
	  "Muguet" : "Blanc",
    "Iris" : "Violet",
	  "Nénuphar": "Blanc",
	  "Glaïeul": "Multicolore",
	  "Lilas": "Violet",
	  "Hortensia": "Rose",
	  "Jasmin" : "Blanc",
	  "Renoncule": "Multicolore",
	  "Œillet": "Rouge",
	  "Anémone": "Rouge",
	  "Chrysanthème": "Jaune",
	  "Primevère": "Jaune",
    "Souci": "Orange",
	  "Amaryllis": "Rouge",
	  "Edelweiss": "Blanc",
	  "Fuchsia": "Rose",
	  "Gentiane": "Bleu",
    "Bégonia": "Multicolore",
	  "Églantine": "Rose",

}

def trouver_couleur_fleur(fleur):
    if fleur in fleurs_et_couleurs:
        return fleurs_et_couleurs[fleur]
    else:
        return "Fleur non trouvée"

def trouver_fleurs_par_couleur(couleur):
    fleurs = [fleur for fleur, col in fleurs_et_couleurs.items() if col == couleur]
    if fleurs:
        return fleurs
    else:
        return "Couleur non trouvée"

# Demander au client le nom de la fleur ou la couleur
entree = input("Entrez le nom d'une fleur ou une couleur : ")

# Vérifier si l'entrée correspond à une fleur ou une couleur
if entree in fleurs_et_couleurs:
    couleur_correspondante = trouver_couleur_fleur(entree)
    print(f"La fleur {entree} est de couleur {couleur_correspondante}")
else:
    fleurs_correspondantes = trouver_fleurs_par_couleur(entree)
    if isinstance(fleurs_correspondantes, list):
        print(f"Les fleurs de couleur {entree} sont : {', '.join(fleurs_correspondantes)}")
    else:
        print(fleurs_correspondantes)
