def creer_adresse_email(nom, prenom):
    adresse_email = f"{nom.lower()}.{prenom.lower()}@mail.com"
    return adresse_email

def main():
    nom = input("Entrez votre nom : ")
    prenom = input("Entrez votre prénom : ")
    pays = input("Entrez votre pays : ")
    age = int(input("Entrez votre âge : "))

    adresse_email = creer_adresse_email(nom, prenom)

    print(f"Adresse e-mail : {adresse_email}")
    print(f"Pays : {pays}")

    if age < 18:
        print("Nous sommes désolés, vous ne pouvez pas prétendre à un compte mail de notre hébergeur.")

if __name__ == "__main__":
    main()
