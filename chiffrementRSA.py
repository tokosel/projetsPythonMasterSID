
p = 17  
q = 23 
n = p * q
phi = (p-1) * (q-1)
e = 5  

def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def generer_cle_privee(e, phi):
    d = -1
    for i in range(1, phi):
        if (e * i) % phi == 1:
            d = i
            break
    return d, n

def chiffrer(texte, cle_publique):
    e, n = cle_publique
    texte_chiffre = []
    for char in texte:
        texte_chiffre.append(pow(ord(char), e, n))
    return texte_chiffre

def dechiffrer(texte_chiffre, cle_privee):
   d, n = cle_privee
   texte_clair = ""
   for char in texte_chiffre:
       texte_clair += chr(pow(char, d, n))
   return texte_clair

cle_publique = (e, n) 
cle_privee = generer_cle_privee(e, phi)

continuer = "oui"
while continuer == "oui":

    message = input("Entrez le message à chiffrer : ")
    
    texte_chiffre = chiffrer(message, cle_publique)

    texte_clair = dechiffrer(texte_chiffre, cle_privee)

    print("Message clair :", message)
    print("Message chiffré :", texte_chiffre) 
    print("Message déchiffré :", texte_clair)
    
    continuer = input("Voulez-vous chiffrer/déchiffrer un autre message (oui/non) ? ")
    
print("Au revoir !")
