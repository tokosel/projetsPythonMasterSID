# Chiffrement RSA
# Auteur : Abdoulaye SALL

p = 17  # Premier nombre premier
q = 23  # Deuxième nombre premier
n = p * q  # Produit des deux nombres premiers
phi = (p-1) * (q-1)  # Valeur de la fonction d'Euler pour n
e = 5  # Exposant de la clé publique

# Fonction pour calculer le PGCD de deux nombres
def pgcd(a, b):
    while b != 0:  # Boucle pour calculer le PGCD
        a, b = b, a % b
    return a  # Retourne le PGCD

# Fonction pour générer la clé privée
def generer_cle_privee(e, phi):
    d = -1  # Initialisation de la clé privée
    for i in range(1, phi):  # Boucle pour trouver la clé privée
        if (e * i) % phi == 1:  # Vérification de la condition pour la clé privée
            d = i  # Affectation de la clé privée
            break
    return d, n  # Retourne la clé privée et le produit des nombres premiers

# Fonction pour chiffrer un texte
def chiffrer(texte, cle_publique):
    e, n = cle_publique  # Récupération de la clé publique
    texte_chiffre = []  # Initialisation de la liste pour le texte chiffré
    for char in texte:  # Boucle pour chiffrer chaque caractère du texte
        texte_chiffre.append(pow(ord(char), e, n))  # Chiffrement du caractère et ajout à la liste
    return texte_chiffre  # Retourne le texte chiffré

# Fonction pour déchiffrer un texte chiffré
def dechiffrer(texte_chiffre, cle_privee):
    d, n = cle_privee  # Récupération de la clé privée
    texte_clair = ""  # Initialisation du texte clair
    for char in texte_chiffre:  # Boucle pour déchiffrer chaque caractère du texte chiffré
        texte_clair += chr(pow(char, d, n))  # Déchiffrement du caractère et ajout au texte clair
    return texte_clair  # Retourne le texte déchiffré

cle_publique = (e, n)  # Clé publique (exposant, produit des nombres premiers)
cle_privee = generer_cle_privee(e, phi)  # Génération de la clé privée

continuer = "oui"  # Initialisation de la variable pour continuer ou non
while continuer == "oui":  # Boucle pour continuer le processus de chiffrement/déchiffrement
    message = input("Entrez le message à chiffrer : ")  # Saisie du message à chiffrer
    
    texte_chiffre = chiffrer(message, cle_publique)  # Chiffrement du message
    
    texte_clair = dechiffrer(texte_chiffre, cle_privee)  # Déchiffrement du texte chiffré
    
    print("Message clair :", message)  # Affichage du message clair
    print("Message chiffré :", texte_chiffre)  # Affichage du message chiffré
    print("Message déchiffré :", texte_clair)  # Affichage du message déchiffré
    
    continuer = input("Voulez-vous chiffrer/déchiffrer un autre message (oui/non) ? ")  # Demande pour continuer ou non

print("Au revoir !")  # Message de sortie
