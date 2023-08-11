def find_flower(sign):
    flowers = {
        "bélier": "tulipe",
        "taureau": "rose",
        "taureaux": "rose",
        "gémeaux": "lavande",
        "gémeau": "lavande",
        "cancer": "lys",
        "lion": "tournesol",
        "vierge": "jacinthe",
        "balance": "orchidée",
        "scorpion": "chrysanthème",
        "sagittaire": "pivoine",
        "capricorne": "edelweiss",
        "verseau": "bleuet",
        "poissons": "jonquille",
        "poisson": "jonquille"
    }
    
    sign = sign.lower()
    
    if sign in flowers:
        return flowers[sign]
    else:
        return "Signe astrologique non valide."

sign_input = input("Entrez votre signe astrologique : ")
flower = find_flower(sign_input)

print(f"Votre signe astrologique est {sign_input.capitalize()} et la fleur qui vous correspond est la {flower}.")
