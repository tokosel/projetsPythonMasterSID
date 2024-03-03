# Projet Horoscope
# Auteurs : Abdoulaye SALL

import datetime

# Liste des signes astrologiques avec leurs dates de début et de fin
signes = [
    ("Bélier", (3, 21), (4, 20)),
    ("Taureau", (4, 21), (5, 21)),
    ("Gémeaux", (5, 22), (6, 21)),
    ("Cancer", (6, 22), (7, 23)),
    ("Lion", (7, 24), (8, 23)),
    ("Vierge", (8, 24), (9, 23)),
    ("Balance", (9, 24), (10, 23)),
    ("Scorpion", (10, 24), (11, 22)),
    ("Sagittaire", (11, 23), (12, 22)),
    ("Capricorne", (12, 23), (1, 20)),
    ("Verseau", (1, 21), (2, 19)),
    ("Poisson", (2, 20), (3, 20))
]

# Fonction pour vérifier si une année est bissextile
def est_bissextile(annee):
    if annee % 4 != 0:
        return False
    elif annee % 100 == 0 and annee % 400 != 0:
        return False
    else:
        return True

# Fonction pour obtenir le signe astrologique en fonction de la date
def get_signe(jour, mois, annee):
    date = datetime.date(annee, mois, jour)
    
    # Parcours de la liste des signes
    for signe in signes:
        nom_signe = signe[0]
        debut, fin = signe[1:]  # Début et fin de la période du signe
        debut = datetime.date(date.year, debut[0], debut[1])  # Date de début du signe dans l'année en cours
        fin = datetime.date(date.year, fin[0], fin[1])  # Date de fin du signe dans l'année en cours
        
        # Vérification si la date de naissance se situe entre le début et la fin du signe
        if date >= debut and date <= fin:
            return nom_signe  # Retourne le nom du signe

# Boucle principale pour demander la date de naissance et afficher le signe astrologique
while True:
    while True:  # Boucle pour vérifier la validité du jour, du mois et de l'année
        try:
            j = int(input("Jour : "))  # Saisie du jour de naissance
            if j < 1 or j > 31:  # Vérification si le jour est dans l'intervalle valide
                raise ValueError   
        except ValueError:
            print("Erreur, les jours sont entre 1 et au plus 31.")  # Message d'erreur si la saisie est invalide
            continue
        
        try:
            m = int(input("Mois : "))  # Saisie du mois de naissance
            if m < 1 or m > 12:  # Vérification si le mois est dans l'intervalle valide
                raise ValueError
        except ValueError:
            print("Erreur, les mois sont entre 1 et 12.")  # Message d'erreur si la saisie est invalide
            continue
            
        try:
            a = int(input("Année : "))  # Saisie de l'année de naissance
            if a <= 1800:  # Vérification si l'année est valide
                raise ValueError
        except ValueError:
            print("Erreur, l’année doit être supérieure strictement à 1800.")  # Message d'erreur si la saisie est invalide
            continue
            
        try:
            max_jours = 28 if m==2 and not est_bissextile(a) else 29 if m==2 else [31,None,31,30,31,30,31,31,30,31,30,31][m-1]
            # Calcul du nombre maximum de jours pour le mois saisi
            if j > max_jours:  # Vérification si le jour de naissance est valide pour le mois saisi
                raise ValueError
            break
        except TypeError:
            print(f"Erreur, le mois {m} ne correspond pas à un mois valide")  # Message d'erreur si le mois saisi est invalide
            continue 
        except ValueError:
            if m == 2:
                print("Erreur, le mois correspondant ne dépasse pas 28 jours car l’année n’est pas bissextile.")  # Message d'erreur spécifique pour février
            else:    
                print("Erreur, le mois correspondant ne dépasse pas 30 jours.")  # Message d'erreur générique pour les autres mois
            continue
            
    signe = get_signe(j, m, a)  # Appel de la fonction pour obtenir le signe astrologique
    print(f"Votre signe astrologique est : {signe}")  # Affichage du signe astrologique
    
    rep = input("Voulez vous continuer ? (oui/non) : ")  # Demande à l'utilisateur s'il souhaite continuer
    if rep.lower() != "oui":  # Condition pour quitter la boucle principale si la réponse n'est pas "oui"
        print("Au revoir !")  # Message de sortie
        break  # Sortie de la boucle principale
