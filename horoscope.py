import datetime

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

def est_bissextile(annee):
    if annee % 4 != 0:
        return False
    elif annee % 100 == 0 and annee % 400 != 0:
        return False
    else:
        return True

def get_signe(jour, mois, annee):
    date = datetime.date(annee, mois, jour)
    
    for signe in signes:
        nom_signe = signe[0]
        debut, fin = signe[1:]
        debut = datetime.date(date.year, debut[0], debut[1])
        fin = datetime.date(date.year, fin[0], fin[1])
        
        if date >= debut and date <= fin:
            return nom_signe

while True:
    while True:        
        try:
            j = int(input("Jour : "))
            if j < 1 or j > 31:
                raise ValueError   
        except ValueError:
            print("Erreur, les jours sont entre 1 et au plus 31.")
            continue
        
        try:
            m = int(input("Mois : "))
            if m < 1 or m > 12:
                raise ValueError
        except ValueError:
            print("Erreur, les mois sont entre 1 et 12.")
            continue
            
        try:
            a = int(input("Année : "))
            if a <= 1800:
                raise ValueError
        except ValueError:
            print("Erreur, l’année doit être supérieure strictement à 1800.")
            continue
            
        try:
            max_jours = 28 if m==2 and not est_bissextile(a) else 29 if m==2 else [31,None,31,30,31,30,31,31,30,31,30,31][m-1]
            if j > max_jours:
                raise ValueError
            break
        except TypeError:
            print(f"Erreur, le mois {m} ne correspond pas à un mois valide")
            continue 
        except ValueError:
            if m == 2:
                print("Erreur, le mois correspondant ne dépasse pas 28 jours car l’année n’est pas bissextile.")
            else:    
                print("Erreur, le mois correspondant ne dépasse pas 30 jours.")
            continue
            
    signe = get_signe(j, m, a)
    print(f"Votre signe astrologique est : {signe}")
    
    rep = input("Voulez vous continuer ? (oui/non) : ")
    if rep.lower() != "oui": 
        print("Au revoir !")
        break
