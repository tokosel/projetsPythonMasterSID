# Arithmanceur
# Auteur : Abdoulaye SALL

import re  # Importation du module pour les expressions régulières

# Fonction pour obtenir le nombre associé à chaque lettre dans le nom
def get_number(name):
    # Dictionnaire assignant un nombre à chaque lettre de l'alphabet
    code = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, 
            "I": 9, "J": 1, "K": 2, "L": 3, "M": 4, "N": 5, "O": 6, "P": 7,  
            "Q": 8, "R": 9, "S": 1, "T": 2, "U": 3, "V": 4, "W": 5, "X": 6,
            "Y": 7, "Z": 8}
    
    # Définition des voyelles et consonnes
    voyelles = "AEIOU"
    consonnes = "BCDFGHJKLMNPQRSTVWXZ"
    
    # Initialisation des variables pour l'expression, l'intime et la réalisation
    expression = 0
    intime = 0
    realisation = 0
    
    # Parcours de chaque lettre du nom en majuscules
    for letter in name.upper():
        if letter in code:  # Vérification si la lettre est dans le dictionnaire
            num = code[letter]  # Récupération du nombre associé à la lettre
            expression += num  # Ajout du nombre à l'expression totale
            if letter in voyelles:  # Vérification si la lettre est une voyelle
                intime += num  # Ajout du nombre à l'intime
            elif letter in consonnes:  # Vérification si la lettre est une consonne
                realisation += num  # Ajout du nombre à la réalisation
    
    # Réduction des nombres à un chiffre en ajoutant les chiffres ensemble
    while expression >= 10:
        expression = sum(int(d) for d in str(expression))

    while intime >= 10:
        intime = sum(int(d) for d in str(intime))
            
    while realisation >= 10:
        realisation = sum(int(d) for d in str(realisation))
            
    return expression, intime, realisation  # Retourne les valeurs d'expression, d'intime et de réalisation

# Dictionnaire associant un nombre à une signification
definition = {
    0: "ouroboros",
    1: "individualite",
    2: "interaction",
    3: "completude",
    4: "stabilite",
    5: "instabilite",
    6: "harmonie",  
    7: "empathie",
    8: "succes",
    9: "completude2"    
}

# Fonction principale
def main():
    print("Bienvenue dans l'arithmanceur!")
    
    again = "oui"  # Initialisation de la variable pour continuer ou non
    while again.lower() == "oui":  # Boucle pour continuer le processus
        name = input("Entrez un nom (1-1000 caracteres) : ")  # Saisie du nom
        
        # Vérification si le nom contient uniquement des lettres et des espaces
        if not re.match(r"^[a-zA-Z ]+$", name):
            print("Erreur: caracteres non autorises. Seuls les lettres et espaces sont autorises.")
            continue
        
        # Vérification si le nom ne dépasse pas 1000 caractères
        if len(name) > 1000:
            print("Erreur: nom trop long (maximum 1000 caracteres)") 
            continue
            
        name = name.replace(" ", "")  # Suppression des espaces du nom  
        expr, inti, real = get_number(name)  # Appel de la fonction pour obtenir les nombres associés
        
        # Affichage des significations associées au nom
        print(name.lower(), definition[expr], definition[inti], definition[real])
        
        again = input("Voulez-vous continuer ? (oui/non) ")  # Demande pour continuer ou non

    print("Au revoir !")  # Message de sortie
        
if __name__ == "__main__":
    main()  # Appel de la fonction principale si le script est exécuté directement
