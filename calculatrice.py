# Calculatrice scientifique
# Auteurs : Abdoulaye SALL

import math  # Importation du module math pour les opérations mathématiques

# Fonction pour l'addition ou la soustraction
def addition():
    n = int(input("Entrez le nombre de termes (>=2) : "))  # Saisie du nombre de termes
    if n < 2:  # Vérification si le nombre de termes est valide
        print("Le nombre de termes doit être supérieur ou égal à 2.")
        return
    
    sum = 0  # Initialisation de la somme
    for i in range(n):  # Boucle pour saisir chaque terme
        x = float(input("Terme {} : ".format(i+1)))  # Saisie du terme
        print("Signe du terme (+, -) : ", end="")  # Saisie du signe du terme
        sign = input()
        if sign == "+":  # Addition si le signe est "+"
            sum += x
        elif sign == "-":  # Soustraction si le signe est "-"
            sum -= x
        else:  # Affichage d'un message d'erreur pour un signe invalide
            print("Signe invalide")
            return
    
    print("Somme = {}".format(sum))  # Affichage de la somme

# Fonction pour calculer le reste d'une division
def modulo():
    a = int(input("Entrez le dividende : "))  # Saisie du dividende
    b = int(input("Entrez le diviseur : "))   # Saisie du diviseur
    
    if b == 0:  # Vérification si le diviseur est différent de zéro
        print("Erreur : division par 0")
        return
    
    r = a - (a // b) * b   # Calcul du reste de la division
    print("Reste = {}".format(r))  # Affichage du reste

# Fonction pour la multiplication
def multiplication():
   n = int(input("Entrez le nombre de facteurs (>=2) : "))  # Saisie du nombre de facteurs
   if n < 2:  # Vérification si le nombre de facteurs est valide
      print("Le nombre de facteurs doit être supérieur ou égal à 2.")
      return
   
   prod = 1  # Initialisation du produit
   for i in range(n):  # Boucle pour saisir chaque facteur
      x = float(input("Facteur {} : ".format(i+1)))  # Saisie du facteur
      print("Signe du facteur (+, -) : ", end="")  # Saisie du signe du facteur
      sign = input()
      if sign == "+":  # Multiplication si le signe est "+"
         prod *= x  
      elif sign == "-":  # Multiplication par -1 si le signe est "-"
         prod *= -x
      else:  # Affichage d'un message d'erreur pour un signe invalide
         print("Signe invalide")
         return
   
   print("Produit = {}".format(prod))  # Affichage du produit

# Fonction pour la division
def division():
    a = float(input("Entrez le dividende : "))  # Saisie du dividende
    b = float(input("Entrez le diviseur : "))   # Saisie du diviseur
    if b == 0:  # Vérification si le diviseur est différent de zéro
        print("Erreur : division par 0") 
        return
    
    print("Résultat = {}".format(a / b))  # Affichage du résultat de la division

# Fonction pour calculer une puissance
def puissance():
    base = float(input("Entrez la base : "))   # Saisie de la base
    exposant = int(input("Entrez l'exposant : "))  # Saisie de l'exposant
    
    if exposant >= 0:  # Calcul de la puissance si l'exposant est positif
        resultat = 1
        for _ in range(exposant):
            resultat *= base
    else:  # Calcul de la puissance si l'exposant est négatif
        resultat = 1
        for _ in range(-exposant):
            resultat /= base
    
    print("Résultat = {}".format(resultat))  # Affichage du résultat

# Fonction pour calculer la factorielle
def factorielle():
   n = int(input("Entrez un entier positif : "))  # Saisie de l'entier
   if n < 0:  # Vérification si l'entier est positif
      print("L'entier doit être positif")
      return
   
   facto = 1  # Initialisation de la factorielle
   for i in range(1, n+1):  # Boucle pour calculer la factorielle
      facto *= i
      
   print("{}! = {}".format(n, facto))  # Affichage de la factorielle

# Fonction pour calculer le logarithme népérien
def logarithme():
    x = float(input("Entrez un nombre réel strictement positif : "))  # Saisie d'un nombre réel positif
    if x <= 0:  # Vérification si le nombre est strictement positif
        print("Le nombre doit être strictement positif.")
        return
    
    if x <= 2:  # Calcul du logarithme si le nombre est inférieur ou égal à 2
        n = 10
        s = 0
        for k in range(1, n+1):
            s += (-1)**(k+1) * (x-1)**k / k
        print("ln({}) = {}".format(x, s))
        
    else:  # Calcul du logarithme si le nombre est supérieur à 2
        n = 0
        y = x
        while y > 2:
            y /= 2
            n += 1
            
        ln2 = (2-1) - (2-1)**2/2 + (2-1)**3/3 - (2-1)**4/4    
        ln_y = (y-1) - (y-1)**2/2 + (y-1)**3/3 - (y-1)**4/4
        
        print("ln({}) = {} + {}*ln(2) = {}".format(x, ln_y, n, ln_y + n*ln2))

# Fonction pour calculer l'exponentielle
def exponentielle():
    x = float(input("Entrez un nombre réel : "))  # Saisie d'un nombre réel
    n = 10
    s = 0
    for k in range(0, n+1):  # Boucle pour calculer l'exponentielle
        s += x**k / math.factorial(k)
        
    print("exp({}) = {}".format(x, s))  # Affichage du résultat de l'exponentielle

# Fonction pour calculer la racine carrée
def racine_carree():
    K = float(input("Entrez un nombre réel positif ou nul : "))  # Saisie d'un nombre réel positif ou nul
    if K < 0:  # Vérification si le nombre est positif ou nul
        print("Le nombre doit être positif ou nul.")
        return
    
    x = K/2  # Initialisation de la valeur initiale de la racine carrée
    e = 0.00001  # Précision de la racine carrée
    while True:  # Boucle pour calculer la racine carrée
        y = (x + K/x) / 2
        if abs(y-x) < e:  # Condition d'arrêt si la différence entre deux itérations est inférieure à la précision
            break
        x = y
        
    print("sqrt({}) = {}".format(K, x))  # Affichage du résultat de la racine carrée

# Boucle principale pour choisir une opération
while True:
   print("Calculatrice scientifique")
   print("1. Pour l'addition ou la soustraction")
   print("2. Pour le reste d'une division")
   print("3. Pour la multiplication")  
   print("4. Pour la division")
   print("5. Pour la puissance")
   print("6. Pour le factorielle")
   print("7. Pour le logarithme népérien")
   print("8. Pour l'exponentielle")
   print("9. Pour la racine carrée")
   print("0. Pour quitter")
   
   choix = input("Vueillez choisir votre opération svpv : ")  # Saisie du choix de l'utilisateur
   
   if choix == "1":  # Appel de la fonction d'addition ou de soustraction
      addition()
   elif choix == "2":  # Appel de la fonction de calcul du reste d'une division
      modulo()
   elif choix == "3":  # Appel de la fonction de multiplication
      multiplication()
   elif choix == "4":  # Appel de la fonction de division
      division()
   elif choix == "5":  # Appel de la fonction de calcul de puissance
      puissance()
   elif choix == "6":  # Appel de la fonction de calcul de factorielle
      factorielle()
   elif choix == "7":  # Appel de la fonction de calcul de logarithme népérien
      logarithme()
   elif choix == "8":  # Appel de la fonction de calcul de l'exponentielle
      exponentielle()
   elif choix == "9":  # Appel de la fonction de calcul de la racine carrée
      racine_carree()
   elif choix == "0":  # Sortie de la boucle principale si l'utilisateur choisit de quitter
      print("Au revoir !")
      break
   else:  # Affichage d'un message d'erreur pour un choix invalide
      print("Choix invalide")
