# Calculatrice scientifique
# Auteurs : Abdoulaye SALL

import math

def addition():
    n = int(input("Entrez le nombre de termes (>=2) : "))
    if n < 2:
        print("Le nombre de termes doit être supérieur ou égal à 2.")
        return
    
    sum = 0
    for i in range(n):
        x = float(input("Terme {} : ".format(i+1)))
        print("Signe du terme (+, -) : ", end="")
        sign = input()
        if sign == "+":
            sum += x
        elif sign == "-":
            sum -= x
        else:
            print("Signe invalide")
            return
    
    print("Somme = {}".format(sum))

def modulo():
    a = int(input("Entrez le dividende : "))
    b = int(input("Entrez le diviseur : "))
    
    if b == 0:
        print("Erreur : division par 0")
        return
    
    r = a - (a // b) * b   
    print("Reste = {}".format(r))

def multiplication():
   n = int(input("Entrez le nombre de facteurs (>=2) : "))
   if n < 2:
      print("Le nombre de facteurs doit être supérieur ou égal à 2.")
      return
   
   prod = 1
   for i in range(n):
      x = float(input("Facteur {} : ".format(i+1)))
      print("Signe du facteur (+, -) : ", end="")
      sign = input()
      if sign == "+":
         prod *= x  
      elif sign == "-":
         prod *= -x
      else:
         print("Signe invalide")
         return
   
   print("Produit = {}".format(prod))

def division():
    a = float(input("Entrez le dividende : "))
    b = float(input("Entrez le diviseur : "))
    if b == 0:
        print("Erreur : division par 0") 
        return
    
    print("Résultat = {}".format(a / b))

def puissance():
    base = float(input("Entrez la base : "))
    exposant = int(input("Entrez l'exposant : "))
    
    if exposant >= 0:
        resultat = 1
        for _ in range(exposant):
            resultat *= base
    else:
        resultat = 1
        for _ in range(-exposant):
            resultat /= base
    
    print("Résultat = {}".format(resultat))

def factorielle():
   n = int(input("Entrez un entier positif : "))
   if n < 0:
      print("L'entier doit être positif")
      return
   
   facto = 1
   for i in range(1, n+1):
      facto *= i
      
   print("{}! = {}".format(n, facto))  

def logarithme():
    x = float(input("Entrez un nombre réel strictement positif : "))
    if x <= 0:
        print("Le nombre doit être strictement positif.")
        return
    
    if x <= 2:
        n = 10
        s = 0
        for k in range(1, n+1):
            s += (-1)**(k+1) * (x-1)**k / k
        print("ln({}) = {}".format(x, s))
        
    else:
        n = 0
        y = x
        while y > 2:
            y /= 2
            n += 1
            
        ln2 = (2-1) - (2-1)**2/2 + (2-1)**3/3 - (2-1)**4/4    
        ln_y = (y-1) - (y-1)**2/2 + (y-1)**3/3 - (y-1)**4/4
        
        print("ln({}) = {} + {}*ln(2) = {}".format(x, ln_y, n, ln_y + n*ln2))
    
def exponentielle():
    x = float(input("Entrez un nombre réel : "))
    
    n = 10
    s = 0
    for k in range(0, n+1):
        s += x**k / math.factorial(k)
        
    print("exp({}) = {}".format(x, s))
    
def racine_carree():
    K = float(input("Entrez un nombre réel positif ou nul : "))
    if K < 0:
        print("Le nombre doit être positif ou nul.")
        return
    
    x = K/2
    e = 0.00001
    while True:
        y = (x + K/x) / 2
        if abs(y-x) < e:
            break
        x = y
        
    print("sqrt({}) = {}".format(K, x))
      
while True:
   print("Vueillez choisir votre opération svp")
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
   
   choix = input("Votre choix : ")
   
   if choix == "1":
      addition()
   elif choix == "2":
      modulo()
   elif choix == "3":
      multiplication()
   elif choix == "4":
      division()
   elif choix == "5":
      puissance()
   elif choix == "6":
      factorielle()
   elif choix == "7":
      logarithme()
   elif choix == "8":
      exponentielle()
   elif choix == "9": 
      racine_carree()
   elif choix == "0":
      print("Au revoir !")
      break
   else:
      print("Choix invalide")
